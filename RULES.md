# Forge rules

The Forge runs by itself. These rules decide everything it does, so that nobody has to make a call by hand, and
anyone can predict and check the result.

## 1. When it runs

- Every 12 hours (00:00 and 12:00 UTC), and whenever someone with write access starts the workflow by hand.
- Each run starts from scratch: upstream `main` as it is at that moment, and the pull requests as they are.
  Nothing from a previous run is kept except the list of what changed.

## 2. What gets into `forge/main`

A pull request is merged when **all** of these hold:

1. It is open and not a draft.
2. It merges with upstream `main` without conflicts.
3. It merges after the pull requests already taken in this run, without conflicts.
4. With it, `cargo check --workspace --all-targets` passes.
5. With it, the repository's asset policy (`cargo xtask policy`) passes: nothing from the game, no archives,
   no binaries the policy refuses.
6. It does not change `.github/workflows/`. The Actions token cannot push workflow changes, and the Forge does
   not run other people's CI changes unreviewed. Such pull requests are listed as "changes CI workflows".
7. It is not held (rule 4).
8. It targets `main`, still has the head the run listed, and adds changes to `main`.

Pull requests are tried **oldest first** (by number). An older one wins a conflict with a newer one. That is a
fixed order, not a judgement of quality.

## 3. What the status page says

Every open pull request gets one result:

| Result | Meaning |
|---|---|
| in forge | merged (rule 2) |
| already in main | merging this head leaves the `main` tree unchanged |
| head changed | the fetched head differs from the listed head |
| alternate base | the PR targets a branch other than `main` |
| conflicts with main | fails rule 2.2: rebase onto `main` |
| conflicts with pull requests | fails rule 2.3: the pull requests named under *with* changed the same files first |
| breaks the build | fails rule 2.4 or 2.5: the first error is shown |
| changes CI workflows | rule 2.6 |
| held | rule 4 |
| draft | skipped until ready |

"Since the last run" lists which pull requests joined the branch and which left it.

The overlaps section records matching patch IDs and merge trees, or shows related PRs based on changed files and linked issues or titles. A match is evidence for a reviewer. The status JSON pins the PR head and merge target so a reviewer can recreate a conflict and reuse their clone's recorded Git resolutions.

## 4. Holds

A hold keeps out a pull request that builds but is known to break the title. Holds are in
[held.json](held.json) and follow these rules:

- Each hold gives a **reason**: what broke, on what hardware, and when.
- Each hold names the **commit** it was observed on. **When the author pushes a new commit, the hold lifts by
  itself**, and the pull request is tried again.
- A hold is never used for style, opinion, or a competing approach. Only for observed breakage.
- Problems the checks already catch (build, asset policy) need no hold: rule 2 keeps those out on its own,
  and they come back in as soon as they are fixed.

## 5. Tests

After merging, the Forge runs `cargo test --workspace --no-fail-fast` on the branch and lists failing tests on the
status page. A failing test does not keep a pull request out. GPU tests need a GPU, and the automatic runs have
none, so most GPU tests skip there.

## 6. What the Forge never does

- It never pushes to, comments on, labels, approves, or closes anything in the upstream repository.
  It only reads upstream (pull requests, and the coordination issue for claims).
- It never edits a pull request's code. Each one is merged as its author wrote it, one merge commit each.
- It never adds anything from the game, or anything the asset policy refuses.
- It never changes these rules by itself. Changes to the rules or holds are commits to this branch, with a reason.

The local `triage.py close` command is separate from the Forge run. A maintainer can use it after labeling a reviewed PR `duplicate` and choosing a canonical PR. It checks the reviewed head again before closing.

## 7. Claims

Who works on what is coordinated in one issue upstream, the **coordination issue** (linked from
[CLAIMS.md](CLAIMS.md)), so that two people (or two agents) do not write the same thing twice. A bot reads it every
30 minutes and publishes [CLAIMS.md](CLAIMS.md). It only reads the issue; it never posts there.

Commands, each on its own line in a comment:

| Command | Meaning |
|---|---|
| `claiming: <ID>` | You take the task. Several IDs: `claiming: A-1, B-2`. Words after an ID explain it. |
| `claiming: <one line>` | You take something not listed yet; it gets a `NEW-n` ID. |
| `done: <ID> -> #<PR>` | Your pull request for the task is open. Putting the ID in the pull request's title or body counts the same. |
| `release: <ID>` | You give the task back; the next person who claimed it gets it. |
| `finding: <one line>` | Something needs doing that you will not do yourself: say where, why, and what it needs (game files, a GPU). It becomes a `FIND-n` task. |

Tasks come from the table in the coordination issue's body (kept by its author and the maintainers), from
`finding:` comments, and from [work.json](work.json).

The rules:

1. **Claim before you write code.** Read CLAIMS.md and the open pull requests first. If someone has the task,
   pick another, or review theirs.
2. **The first valid claim wins.** Later claims on the same task wait in line and get it if it is released or expires.
3. **A claim expires after 14 days without a pull request.** Comment `claiming: <ID>` again to renew it.
4. **An edited comment does not count.** Claims are first come, first served, so a claim cannot be changed
   afterwards: post a new comment instead.
5. **Only the holder** can mark a task done or release it.
6. A pull request closed without merging frees its task again. A merged one closes it.
7. Claims coordinate work; they do not decide merges. Two pull requests can still overlap. The Forge status page
   shows it, and the one that lands upstream first stands.

## 8. Changing the rules

Open an issue or a pull request against the `forge-status` branch of this repository. Anyone can propose a change.
The change takes effect at the next run.
