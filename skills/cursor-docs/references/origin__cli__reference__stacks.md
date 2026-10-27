---
title: "Stack commands"
source: https://cursor.com/docs/origin/cli/reference/stacks
path: /docs/origin/cli/reference/stacks
---

# Stack commands

Origin is currently released in early beta. You can create repos, push and pull with git, mirror from GitHub, browse and search code, open and merge pull requests, and share with your Cursor team.

A stack is a chain of pull requests where each one builds on the one below it. Origin records each pull request's parent, so basing one branch on another isn't enough. `origin stack` keeps the local branches of a stack in step with each other and with Origin. For single pull requests, see [Pull request commands](https://cursor.com/docs/origin/cli/reference/pull-requests.md).

## Open a stack

Open the bottom pull request first. Then create each child from a branch based on its parent's branch, and open it with `--stack-on`:

```bash
origin pr create --stack-on 122 --title "Add widget colors" --body-file body.md
origin pr edit 123 --stack-on 122
origin stack view
```

`origin pr edit --stack-on` changes a pull request's parent, and `origin pr edit --clear-stack` removes it. Before a branch has a pull request, `origin stack track --onto <parent>` records its parent locally.

## Subcommands

Commands that take a `[target]` accept a pull request number (`13` or `#13`), an Origin pull request URL, or a branch, and default to the current branch. `-R, --repo` picks the repository, as on [every command](https://cursor.com/docs/origin/cli/reference/commands.md#targeting-a-repository).

| Subcommand                | Description                                                                                                        | Usage                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| `view [target]`           | Show a stack as a tree, from the branch parents saved in this clone                                                | `origin stack view`                   |
| `get [target]`            | Fetch every member and create or fast-forward its local branch. Same as `origin pr checkout --stack`               | `origin stack get`                    |
| `sync`                    | Fast-forward trunk, delete local branches of merged and closed pull requests, and restack what was stacked on them | `origin stack sync`                   |
| `restack`                 | Rebase every member onto its parent's local tip, root to leaf                                                      | `origin stack restack`                |
| `restack-remote [target]` | Have Origin rebase the stack's open pull requests and move their branches                                          | `origin stack restack-remote`         |
| `push`                    | Push the current branch with a lease, or every member with `--all`                                                 | `origin stack push --all`             |
| `move [branch]`           | Move a branch onto a new parent, then restack                                                                      | `origin stack move --onto main`       |
| `delete [branch]`         | Remove a branch from its stack. Its children move to its parent and are restacked                                  | `origin stack delete add-sizes`       |
| `delete-branch [number]`  | Delete a merged or closed pull request's head branch on Origin and in this clone                                   | `origin stack delete-branch 122`      |
| `track [branch]`          | Record a branch's parent locally before it has a pull request                                                      | `origin stack track --onto add-sizes` |
| `untrack [branch]`        | Stop tracking a branch's parent when it has no pull request                                                        | `origin stack untrack`                |
| `freeze [branch]`         | Mark a branch frozen so stack commands never rewrite it                                                            | `origin stack freeze add-sizes`       |
| `unfreeze [branch]`       | Let stack commands rewrite a frozen branch again                                                                   | `origin stack unfreeze add-sizes`     |
| `up [member]`             | Check out the child of the current branch                                                                          | `origin stack up`                     |
| `down`                    | Check out the parent of the current branch                                                                         | `origin stack down`                   |
| `top [member]`            | Check out the top of the stack                                                                                     | `origin stack top`                    |
| `bottom`                  | Check out the member just above trunk                                                                              | `origin stack bottom`                 |

`track`, `untrack`, `freeze`, and `unfreeze` only change what this clone records. They make no network call.

## Keep a stack current

Origin never rebases a branch for you. Before you push to a branch in a stack, run:

```bash
origin stack get
origin stack restack
origin stack push --all
```

`get` fetches and fast-forwards every member. `restack` rebases each member onto its parent, root to leaf, and `push` pushes with a lease. When `push` rejects a member because its lease failed, someone else moved that branch, so start again from `get`.

`restack` rebases the bottom of the stack onto your local trunk branch, not the remote one. `origin stack get` fast-forwards local trunk when it's behind, and `origin stack sync` fetches and fast-forwards it, so run one of them first to restack onto the latest trunk.

A restack that conflicts stops on that member with git's conflict markers in the working tree. Resolve the files, run `git add` and `git rebase --continue`, then run `origin stack restack` again. `origin stack restack --dry-run` previews conflicts without moving anything.

When every member that needs to move has a pull request, `origin stack restack-remote` has Origin rebase them and move their branches instead, as the **Restack** button in Review does. Nothing in this clone changes, so run `origin stack get` afterward to pick up the new heads. On a conflict, Origin moves nothing and names the member. Restack locally to resolve it.

After a parent merges, leave its child's parent as it is: Origin moves the child's base to trunk and keeps the stack. Run `origin stack sync` or `origin stack restack`, then `origin stack push --all`. Don't run `origin pr edit --clear-stack` after a merge, because it splits the stack.

## View, get, and sync

| Command | Option              | Description                                                                                                                                     |
| ------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `view`  | `--refresh`         | Also show titles and states from Origin, and update this clone's branch parents to match. Use it after someone else changes the stack           |
| `get`   | `-f, --force`       | Reset diverged or ahead local branches to Origin's                                                                                              |
| `get`   | `--take-remote`     | Take Origin's parent wherever this clone's differs, dropping a local parent change that `push` hasn't published                                 |
| `get`   | `--keep-local`      | Where a parent changed both here and on Origin since the last `get`, keep yours for `push` to publish                                           |
| `get`   | `--remote <remote>` | Remote to fetch from (default: `origin`)                                                                                                        |
| `sync`  | `--remote <remote>` | Remote to fetch trunk from (default: `origin`)                                                                                                  |
| `sync`  | `--restack`         | Restack every local stack onto its parents and the updated trunk afterward (default: `true`). `--no-restack` leaves the branches where they are |
| `sync`  | `--dry-run`         | Report what `sync` would delete and move. Fetches, writes, and restacks nothing                                                                 |

## Restack

By default, `origin stack restack` rebases every member of the current branch's stack. These options narrow it or change how it moves branches:

| Option              | Description                                                                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--only`            | Restack the current branch alone                                                                                                                     |
| `--upstack`         | Restack the current branch and every member above it. Members below are left alone                                                                   |
| `--downstack`       | Restack the members below the current branch and the branch itself, root first. Members above are left alone                                         |
| `--dry-run`         | Report per member whether the rebase or merge would apply cleanly. Writes and pushes nothing                                                         |
| `--merge`           | Merge each parent into its child instead of rebasing, root to leaf, and push each moved member as a fast-forward. For clones that may not force-push |
| `--take-trunk`      | With `--merge`, also merge newer trunk into the root when nothing in the stack needs it yet                                                          |
| `--remote <remote>` | Remote a `--merge` restack reads trunk from and pushes to (default: `origin`)                                                                        |
| `--drop-change-ids` | Rewrite commits that carry a jj `change-id` header, which `git rebase` drops. Without it, `restack` refuses them                                     |

A `--merge` restack merges trunk into the root only once its parent merged, a member above it has newer trunk commits, or you pass `--take-trunk`. Never merge trunk straight into a child whose parent is still open, because its diff fills with trunk commits the parent lacks.

`origin stack restack-remote [target]` restacks through `target`, from the stack root (default: the open pull request at the top of the current branch's stack). `--dry-run` reports Origin's preview for each pull request and moves nothing.

## Push, move, and delete

| Command          | Option              | Description                                                                                                             |
| ---------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `push`           | `--all`             | Push every member of the stack that has a local branch, root to leaf                                                    |
| `push`           | `--remote <remote>` | Remote to push to (default: `origin`)                                                                                   |
| `move`           | `--onto <branch>`   | The new parent: another member, or trunk. Required                                                                      |
| `move`           | `--only`            | Move the branch alone. Its children stay on its old parent                                                              |
| `delete`         | `-c, --close`       | Also close its open pull request                                                                                        |
| `delete`         | `-f, --force`       | Delete even when work could be lost: an open pull request stays open, and unpushed commits are dropped                  |
| `delete-branch`  | `--merged`          | Delete every merged or closed member of the stack, not only one pull request                                            |
| `delete-branch`  | `--keep-local`      | Keep the local branches. Delete the branches on Origin and their remote-tracking refs, and stop tracking the local ones |
| `delete-branch`  | `--remote <remote>` | Remote whose tracking refs to remove (default: `origin`)                                                                |
| `move`, `delete` | `--drop-change-ids` | Rewrite commits that carry a jj `change-id` header                                                                      |

`origin stack move` restacks after the move. Run `origin stack push` to publish it.

## Track and freeze

| Command   | Option              | Description                                                                                            |
| --------- | ------------------- | ------------------------------------------------------------------------------------------------------ |
| `track`   | `--onto <branch>`   | Parent branch (default: the branch's upstream when that's another branch, else trunk when unambiguous) |
| `track`   | `--remote <remote>` | Remote whose branches and `HEAD` count as known (default: `origin`)                                    |
| `untrack` | `-f, --force`       | Also untrack every branch stacked on it                                                                |

`get` and `push` record a branch you didn't author as frozen, and no stack command rewrites a frozen branch. Run `origin stack unfreeze <branch>` only when its author asked you to take it over.

## Navigate

`up`, `down`, `top`, and `bottom` check out a neighbor in the current branch's stack. They take `--remote <remote>`, the remote to fetch from (default: `origin`).

When the stack forks above the current branch, `up` and `top` ask which member to land on. Pass the member as a branch or pull request number, either as the positional or with `--to`. `--non-interactive`, or `ORIGIN_NON_INTERACTIVE=1`, lists the options and exits `2` instead of asking.

## JSON and exit codes

Every subcommand except `up`, `down`, `top`, and `bottom` takes `--json <fields>`. `--verbose` on `get`, `restack`, `push`, `move`, and `delete` echoes git's own output to stderr.

Stack commands exit `2` when they refuse and change nothing, for example on a dirty working tree. With `--json`, a refusal prints `{"refused": "<reason>"}`.

## Merge a stack

Merging a pull request in a stack lands every open pull request from the stack root through it in one commit. `origin pr merge --auto --downstack` arms every open pull request below it too. See [Merge](https://cursor.com/docs/origin/cli/reference/pull-requests.md#merge).

## Next steps

- [Pull request commands](https://cursor.com/docs/origin/cli/reference/pull-requests.md)
- [Commands](https://cursor.com/docs/origin/cli/reference/commands.md)
- [Pull requests](https://cursor.com/docs/origin/pull-requests.md)
