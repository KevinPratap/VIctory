# The Forge and claims

With hundreds of open pull requests, most can only be tried one at a time against `main`, many touch the same
files, and some fix the same thing twice. Two automatic helpers keep that manageable without anyone deciding by
hand: the **Forge** combines the pull requests that fit together, and **claims** say who works on what. Both run
by the rules below, so anyone can predict and check what they do.

## The Forge

Every 12 hours (00:00 and 12:00 UTC), and by hand from the Actions tab, `.github/workflows/forge.yml` runs
`cargo xtask forge`. It writes:

- **`forge/main`**: `main` plus every open pull request that fits (rule 2), one merge commit each
  (`Forge: #N title`). Check it out to test everything together.
- **`STATUS.md` on `forge/status`**: one result for every open pull request, the tests on `forge/main`, and what
  joined or left the branch since the last run.

Each run starts from scratch from `main` as it is then. It never merges anything into `main`: that stays with
review.

### Rule 1: what gets into `forge/main`

A pull request is merged when all of these hold:

1. It is open and not a draft.
2. It merges with `main` without conflicts.
3. It merges after the pull requests already taken in this run.
4. With it, `cargo check --workspace --all-targets` passes.
5. With it, the asset policy (`cargo xtask policy`) passes.
6. It does not change `.github/workflows/`. The Actions token cannot push workflow changes, and the Forge does
   not run other people's CI changes unreviewed.
7. It is not held (rule 3).

Pull requests are tried **oldest first** (by number), so an older one wins a conflict with a newer one. Pull
requests are merged in batches of 25. A batch that fails is halved until the pull request that breaks it is
found.

### Rule 2: the results

| Result | Meaning | What the author can do |
|---|---|---|
| in forge | merged | nothing |
| conflicts with main | fails 1.2 | rebase onto `main` |
| conflicts with pull requests | fails 1.3: the pull requests named under *with* changed the same files first | check whether one of them already does the same, or agree with its author |
| breaks the build | fails 1.4 or 1.5: the first error is shown | rebase and build; remove what the policy refuses |
| changes CI workflows | fails 1.6 | nothing: it is reviewed as usual |
| held | rule 3 | see the reason |
| draft | skipped until ready | |

A failing test does not keep a pull request out. The tests of `forge/main` are listed so that authors can see
what their change breaks in combination with others. The runner has no GPU, so GPU tests skip there.

### Rule 3: holds

A hold keeps out a pull request that builds but is known to break the title. Holds are in `.github/forge.toml`:

- Each gives a **reason**: what broke, on what hardware, and when.
- Each names the **commit** it was seen on. A new commit lifts the hold by itself, and the pull request is tried
  again.
- Holds are only for observed breakage, never for style, opinion or a competing approach.
- What the build or the asset policy already catches needs no hold.

## Claims

Work is claimed in the **coordination issue**, titled "Coordinating who works on what" (its number is in
`.github/forge.toml`), so two people (or two agents) do not write the same thing twice.
`.github/workflows/claims.yml` runs `cargo xtask claims` on every comment there and every 30 minutes. It keeps
`CLAIMS.md` on `forge/status` and one bot comment in the issue current. That comment is the only thing it writes in
the issue.

Put each command on its own line in a comment:

| Command | Meaning |
|---|---|
| `claiming: <ID>` | You take the task, before you write code. Several: `claiming: A-1, B-2`. Words after an ID explain it. |
| `claiming: <one line>` | You take something not listed yet; it gets a `NEW-n` ID. |
| `done: <ID> -> #<PR>` | Your pull request is open. Putting the ID in the pull request's title or body counts the same. |
| `release: <ID>` | You give the task back. |
| `finding: <one line>` | Something needs doing that you will not do yourself: where, why, and what it needs (game files, a GPU). It becomes a `FIND-n` task. |

Tasks come from the table in the issue's body (`` | `ID` | what | where | needs | ``), from `finding:` comments, and
from `[[task]]` entries in `.github/forge.toml`.

1. **Claim before you write code.** Read the claims and the open pull requests first. If someone has the task,
   pick another or review theirs.
2. **The first valid claim wins.** Later claims wait in line, and get the task if it is released or expires.
3. **A claim expires after 14 days without a pull request** (`claim_expiry_days`). Claim it again to renew it.
4. **An edited comment does not count**, so claims stay first come, first served. Post a new comment instead.
5. **Only the holder** can mark a task done or release it.
6. A pull request closed without merging frees its task. A merged one closes it.
7. Claims coordinate work. They do not decide merges.
8. Nothing from the game goes in comments: no files, no dumps, no shader names or hashes from the title.

## What the automation never does

- It never pushes to `main`, and it never merges, approves, labels or closes anything.
- It never edits a pull request's code. Each one is merged as its author wrote it.
- In the coordination issue it edits only its own comment.
- It never adds anything the asset policy refuses.

## Running it yourself

```
git worktree add --detach ../VIctory-forge origin/main
cargo xtask forge --repo ../VIctory-forge --out <folder outside the repository> --limit 25
cargo xtask claims --out <folder outside the repository>
```

`--repo` needs a worktree of its own, because the Forge resets it. Both need `gh`, signed in or with `GH_TOKEN`.

## Changing the rules

These rules, the holds and the open tasks change by pull request to `main`, like any other code. The next run
uses them.
