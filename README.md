# VIctory Forge

VIctory has hundreds of open pull requests, and most of them can only be tried one at a time against `main`.
Many touch the same files, some fix the same problem twice, and nobody can test them together.

The Forge does that for everyone:

- **`forge/main`**: upstream `main` plus every open pull request that merges cleanly and still builds, one merge
  commit per pull request (`Forge: #N title`), oldest first. Check it out and test the combined state.
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
| already in main | Merging the proposed head leaves the tree identical to `main`. | Confirm there is no remaining work, then close the PR. |
| head changed | The author's branch changed while the report was being prepared. | Use the next report for the new head. |
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
3. Merge the ones that merge cleanly into a fresh branch from `main`, 25 at a time, and run
   `cargo check --workspace --all-targets` and `cargo xtask policy` after each batch. If a batch fails, its pull requests are redone one
   at a time and the ones that break the build are left out.
4. Run the workspace tests on the result, then write `STATUS.md` and `status.json`, including what changed since
   the last run.

Only the build and the asset policy gate a merge: the GPU tests need a GPU, and running them per pull request would
take days. The tests of the final branch are run once and reported in `STATUS.md`.

## Run it yourself

```
git worktree add --detach ../VIctory-forge origin/main
python -I forge.py --repo ../VIctory-forge --out <folder outside the repo>
```

Use a worktree of its own: the tool resets it. With `--limit 25` it tries only the first 25 pull requests.

## Triage and conflicts

Use `--triage-only` with the same command to write the report without checking out a branch or running builds. Reruns refresh `main` and fetch only PR heads that changed. The report lists PRs already incorporated in `main` and potential overlaps based on the merge result, linked issues, or titles and changed files. The JSON includes the reported PR head and both sides of each conflict.

To work on a reported conflict, fetch the PR branch and the reported merge target into your clone. A conflict with `main` uses the report's `base` commit. For a conflict with other PRs, fetch `forge/main` from the Forge fork. Use that worktree to test integration and apply the relevant fix separately on the PR branch. If Forge discarded the target during a failed build, use the listed PRs and files to reproduce the conflict locally.

```
python -I triage.py resolve --repo ../VIctory --status /path/to/status.json --pr 123 --worktree ../resolve-123
```

Git reuses any resolution already recorded in that clone. Review the staged result and resolve any remaining conflicts. Run the relevant checks before committing. Running `git rerere` after resolving a conflict records the resolution for another run in the same clone.

After a maintainer checks the diffs, preserves any distinct tests, and labels the redundant PR `duplicate`, this command previews the closure. The head SHA must be the one the maintainer reviewed.

```
python -I triage.py close --pr 123 --canonical 456 --head <full-reviewed-head-sha>
```

Pass `--apply` from an account with upstream write access to link the canonical PR and close the duplicate. Scheduled Forge runs only report overlaps.

## Game files

None. The Forge reads and writes only the repository's code and the pull requests' code. Nothing from any game
goes into the branch, the status page or the tool. Measurements made on a title (for example with
`victory translate` on your own copy) belong in the pull requests themselves, as counts only.

*Made with AI assistance (Claude Code), run by KevinPratap.*
