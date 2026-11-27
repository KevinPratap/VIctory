# VIctory Forge

VIctory has hundreds of open pull requests, and most of them can only be tried one at a time against `main`.
Many touch the same files, some fix the same problem twice, and nobody can test them together.

The Forge does that for everyone:

- **`forge/main`**: upstream `main` plus every open pull request that merges cleanly and still builds, one merge
  commit per pull request (`Forge: #N title`), oldest first. Check it out and test the combined state.
- **`forge/tested`**: the last candidate whose tests introduced no new failures against the same upstream
  baseline on the same worker. Incomplete runs and missing previously passing tests block promotion.
- **[STATUS.md](STATUS.md)**: what happened to each open pull request.
- **[forge.py](forge.py)**: the tool that builds both. Run it yourself; it needs only git, `gh` and cargo.

It runs by itself every 12 hours on GitHub Actions ([forge.yml](.github/workflows/forge.yml)), following fixed
rules: **[RULES.md](RULES.md)**. Nobody picks pull requests by hand; the rules decide, and anyone can check them.

**Claims:** who works on what is coordinated in [Marvisak/VIctory#1633](https://github.com/Marvisak/VIctory/issues/1633)
(`claiming: <ID>`, `done: <ID> -> #<PR>`, `finding: <one line>`), and a bot keeps **[CLAIMS.md](CLAIMS.md)** current
every 30 minutes. Claim before you write code, so nobody does the same work twice.

The Forge is not a fork of the project and does not replace review. Pull requests still go to
[Marvisak/VIctory](https://github.com/Marvisak/VIctory); the Forge only shows how they combine.

## What the status means

| Result | Meaning | What the author can do |
|---|---|---|
| in forge | Merged into `forge/main`, and the workspace builds with it. | Nothing. |
| conflicts with main | Does not merge with current `main` on its own. | Rebase onto `main`. |
| conflicts with pull requests | Merges with `main`, but not after the pull requests listed in *with*. These changed the same files first. | Look at those pull requests: often one of them already does the same, or the two need to agree. |
| breaks the build | Merges, but `cargo check --workspace --all-targets` or the repository's asset policy (`cargo xtask policy`) fails with it (first error shown). Often the pull request is older than an API change on `main`. | Rebase and build; remove files the policy refuses. |
| changes CI workflows | Changes `.github/workflows/`, which the Forge does not merge (the Actions token cannot push it, and other people's CI changes are not run unreviewed). | Nothing: it is reviewed upstream as usual. |
| held | Left out on purpose: known to break the title in testing, or adding files the asset policy refuses (reason given in [held.json](held.json)). | See the reason. |
| draft | Skipped until it is ready for review. | |

Pull requests are merged in number order, so an older pull request wins a conflict. Being listed under "conflicts
with pull requests" is not a judgement; it shows who else is working in the same place.

## How it is built

1. List the open pull requests and fetch every head.
2. Check each one against `main` with `git merge-tree` (no checkout).
3. Merge the ones that merge cleanly into a fresh branch from `main`, 20 at a time, and run
   `cargo check --workspace --all-targets` and `cargo xtask policy` after each batch. If a batch fails,
   recursively split it and leave out the pull requests that break the build.
4. Run the workspace tests on both the pinned upstream baseline and the candidate. Advance `forge/tested`
   only if both runs are complete, no new test fails, and every baseline passing test still passes.
5. For a rejected candidate, probe a bounded number of merge prefixes and report a suspect range. Earlier
   changes can interact with this range: it is a diagnostic lead, not proof of a single bad pull request.
6. Write `STATUS.md` and `status.json`, including what changed since the last run and the promotion verdict.

Only the build and asset policy gate inclusion in `forge/main`. Test regressions gate `forge/tested`, so a
rejected candidate leaves the last tested branch available. This is worker-specific automated coverage;
ignored tests and GPU paths skipped internally do not establish that the title runs correctly.

## Run it yourself

```
git worktree add --detach ../VIctory-forge origin/main
python -I forge.py --repo ../VIctory-forge --out <folder outside the repo>
python -I forge.py --repo ../VIctory-forge --out <folder outside the repo> --tests --tested-branch forge/tested
```

Use a worktree of its own: the tool resets it. With `--limit 25` it tries only the first 25 pull requests.

`--test-timeout 1800` bounds each baseline/candidate run. Regression investigation has both a run budget
(`--diagnostic-runs 6`) and a time budget (`--diagnostic-seconds 900`); set either diagnostic budget to zero
to disable probes. Full logs and `promotion.json` accompany the status report as workflow artifacts. An
existing tested ref is updated atomically, and publication uses a lease to avoid replacing a concurrent update.
CI executes candidate code in a job with read-only repository access and no persisted checkout credential.
A separate publisher imports the resulting Git bundle and reports without checking out or executing candidate
code with its write credential.

Run the source-only promotion tests with `python -I test_promotion.py -v`. They use synthetic test output
and disposable Git repositories, without Cargo, game data, a GPU, or network access.

## Game files

None. The Forge reads and writes only the repository's code and the pull requests' code. Nothing from any game
goes into the branch, the status page or the tool. Measurements made on a title (for example with
`victory translate` on your own copy) belong in the pull requests themselves, as counts only.

*Made with AI assistance (Claude Code), run by KevinPratap.*
