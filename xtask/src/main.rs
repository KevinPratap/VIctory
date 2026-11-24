//! Repository maintenance. Run with `cargo xtask <command>`.

mod claims;
mod forge;
mod gh;
mod policy;

use std::path::{Path, PathBuf};
use std::process::Command;

use anyhow::{Context, Result};
use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(name = "xtask")]
struct Cli {
    #[command(subcommand)]
    command: Cmd,
}

#[derive(Subcommand)]
enum Cmd {
    /// Enforce the asset policy: the repository holds only small text files
    /// we wrote. Checks tracked and untracked-but-not-ignored files.
    Policy {
        /// Check only what is staged for commit (used by the pre-commit hook).
        #[arg(long)]
        staged: bool,
    },
    /// Point git at .githooks/ so every commit runs the policy check.
    InstallHooks,
    /// Build `forge/main`: `main` plus every open pull request that merges,
    /// builds and passes the asset policy; write STATUS.md (docs/forge.md).
    /// Resets the checkout it builds in: give it a worktree of its own.
    Forge {
        /// Where to write STATUS.md.
        #[arg(long)]
        out: PathBuf,
        /// The checkout to build in (default: this one).
        #[arg(long)]
        repo: Option<PathBuf>,
        /// `owner/name` whose pull requests are taken (default: this repository).
        #[arg(long)]
        slug: Option<String>,
        /// The remote of that repository.
        #[arg(long, default_value = "origin")]
        remote: String,
        #[arg(long, default_value = "forge/main")]
        branch: String,
        /// Pull requests merged before each build.
        #[arg(long, default_value_t = 25)]
        batch: usize,
        /// Only the first N pull requests (to try it out).
        #[arg(long, default_value_t = 0)]
        limit: usize,
        /// Run the workspace tests on the result and report them.
        #[arg(long)]
        tests: bool,
        /// The last run's STATUS.md, to report what changed.
        #[arg(long)]
        previous: Option<PathBuf>,
    },
    /// Read the coordination issue's claims and write CLAIMS.md (docs/forge.md).
    Claims {
        #[arg(long)]
        out: PathBuf,
        /// `owner/name` of the repository with the issue (default: this one).
        #[arg(long)]
        slug: Option<String>,
        /// Also keep the bot's comment in the issue current.
        #[arg(long)]
        comment: bool,
    },
}

fn main() -> Result<()> {
    let root = workspace_root();
    match Cli::parse().command {
        Cmd::Policy { staged } => policy::run(&root, staged),
        Cmd::InstallHooks => {
            let status = Command::new("git")
                .args(["config", "core.hooksPath", ".githooks"])
                .current_dir(&root)
                .status()
                .context("running git")?;
            anyhow::ensure!(
                status.success(),
                "git config failed (is this a git repository?)"
            );
            println!("hooks installed: commits now run `cargo xtask policy --staged`");
            Ok(())
        }
        Cmd::Forge {
            out,
            repo,
            slug,
            remote,
            branch,
            batch,
            limit,
            tests,
            previous,
        } => {
            let repo = repo.unwrap_or_else(|| root.clone());
            let slug = match slug {
                Some(s) => s,
                None => this_repository(&root)?,
            };
            let cfg = forge::config(&root)?;
            let opts = forge::Opts {
                repo,
                out,
                slug,
                remote,
                branch,
                batch: batch.max(1),
                limit,
                tests,
                previous,
            };
            forge::run(&opts, &cfg)
        }
        Cmd::Claims { out, slug, comment } => {
            let slug = match slug {
                Some(s) => s,
                None => this_repository(&root)?,
            };
            claims::run(&root, &slug, &forge::config(&root)?, &out, comment)
        }
    }
}

/// `owner/name` of this checkout's GitHub repository (`GITHUB_REPOSITORY` in
/// Actions, else gh's answer for `origin`).
fn this_repository(root: &Path) -> Result<String> {
    if let Ok(s) = std::env::var("GITHUB_REPOSITORY") {
        return Ok(s);
    }
    Ok(gh::ok(
        "gh",
        &[
            "repo",
            "view",
            "--json",
            "nameWithOwner",
            "--jq",
            ".nameWithOwner",
        ],
        root,
    )?
    .trim()
    .to_owned())
}

fn workspace_root() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("xtask lives in the workspace")
        .into()
}
