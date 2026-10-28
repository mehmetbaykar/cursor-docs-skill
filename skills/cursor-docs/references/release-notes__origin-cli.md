---
title: "Origin CLI release notes"
source: https://cursor.com/docs/release-notes/origin-cli
path: /docs/release-notes/origin-cli
---

# Origin CLI release notes

New features, improvements, and fixes in the [Origin CLI](https://cursor.com/docs/origin/cli.md). Each entry covers one release and is labeled with its release date. Changes to Origin on the web and in the API are in the [Origin release notes](https://cursor.com/docs/release-notes/origin.md).

## October 26, 2026 release

### Pull requests

- **`origin pr edit` no longer wipes a description by accident.** It refuses an empty, whitespace-only, or `null` `--body` or `--body-file`; use the new `--clear-body` flag to clear a description on purpose. `origin pr view` and `origin pr list` return each `--json` field under the name you asked for, so `--json body` prints `body`, not `description`. Update scripts that read `.description` after asking for `body`.
- **Merge-when-ready is now called auto-merge.** `origin pr view`, `status`, and `requirements` print an `Auto-merge` line, `origin pr merge --auto` and `--disable-auto` say auto-merge in their messages, and `origin pr watch` labels events `[auto-merge]`. Use `--json autoMerge` in scripts; `--json mergeWhenReady` still works but is deprecated. See [merge](https://cursor.com/docs/origin/cli/reference/pull-requests.md#merge).

### Repositories

- **Faster CloneKit downloads on more systems.** `origin repo clone-fast` uses its faster download engine with curl 7.75 or newer and GNU coreutils dd. When it can't, it prints a warning that says why and what to install, and the fallback engine uses bounded memory. See [CloneKit in CI](https://cursor.com/docs/origin/clonekit-ci.md).

## October 23, 2026 release

### Pull requests

- **`origin pr create` opens pull requests ready for review.** New pull requests open ready for review by default instead of as drafts; pass `--draft` or `--status draft` for a draft. If your 'Never open PRs as drafts' setting or the repository's setting turns a requested draft into a ready pull request, `origin pr create` says why. See [create](https://cursor.com/docs/origin/cli/reference/pull-requests.md#create).
- **Agentic code owner holds read like classic approval requirements.** When a ruleset uses Agentic code owner review, `origin pr requirements` lists its holds under "Approvals still needed" in the same shape as classic requirements, such as "1 approving review from anyone but the author (0 so far)".

### Stacks

- **`origin stack sync` cleans up merged branches it used to miss.** It deletes the local branches of merged and closed pull requests even after `origin stack get` stopped tracking them, unless that would lose a commit. A branch renamed with `git branch -m` is kept and reported with the command that lets sync delete it. Stack commands run on a merged or closed branch point you to [`origin stack sync`](https://cursor.com/docs/origin/cli/reference/stacks.md#view-get-and-sync).
- **Stack commands no longer throw away a rebase you're resolving.** `origin stack move`, `delete`, `restack`, and `sync` stop with an error when a rebase or merge they didn't start is in progress, instead of aborting it and discarding your resolved conflicts. When a stack rebase hits a conflict, the message names the branch, its new parent, the conflicting files, and the commit being applied, then lists the commands to run next.
- **Clearer `origin stack` messages.** `origin stack sync`, `get`, `push`, `restack`, and `delete-branch` say exactly what changed, for example `moved b's parent from main to a, as on Origin`. `origin pr create` and `origin pr edit` explain when a branch's stack parent couldn't be saved in your clone and point you to `origin stack get`.

### Scripting

- **Stack commands take `--json` field lists.** `origin stack` commands such as `get`, `restack`, and `push` take a comma-separated field list with `--json`, like `origin stack get --json members,checkedOut`, and a bare `--json` is a usage error that lists the fields. See [JSON and exit codes](https://cursor.com/docs/origin/cli/reference/stacks.md#json-and-exit-codes).

### Fixes

- **Fixes to `origin stack get` with restacked branches.** It fast-forwards branches that Origin restacked instead of reporting them as diverged, including in fresh clones, with `core.logAllRefUpdates=false`, and with `log.showSignature` enabled.

## October 21, 2026 release

### Stacks

- **Clean up merged stacks with `origin stack sync`.** It fast-forwards trunk, deletes your local branches whose pull requests were merged or closed, and restacks the branches that sat on them. Use `--dry-run` to preview or `--no-restack` to leave branches in place. `origin stack delete-branch` also moves stacked branches onto the deleted branch's parent and tells you when it checks out a different branch. See [view, get, and sync](https://cursor.com/docs/origin/cli/reference/stacks.md#view-get-and-sync).

### Pull requests

- **See every owner rule on a pull request and where it stands.** [`origin pr requirements`](https://cursor.com/docs/origin/cli/reference/pull-requests.md#requirements-and-watch) has an Owner rules section with one line per rule, including rules that already passed: who can approve, how many files it covers, and whether it still needs an approval. Rules waiting on approval are listed first, and `--json ownerRules` returns the same data.
- **Clearer message when a pull request has nothing to merge.** When a pull request's changes are already on its base branch, the merge blocker says so and suggests closing the pull request or pushing a commit with new changes.

### Scripting

- **Pick JSON fields for `origin ruleset` and access commands.** `origin ruleset` commands and the repository and namespace access commands take a field list with `--json`, for example `origin repo access remove --json repo,action,subject`. `origin ruleset list --json` includes bypass actors and returns an empty list when a repository has no rulesets.

## October 20, 2026 release

### Pull requests

- **See which bot owners can clear a Code Review Gate.** When a Code Review Gate policy still needs approval, [`origin pr requirements`](https://cursor.com/docs/origin/cli/reference/pull-requests.md#requirements-and-watch) lists any bot owner whose approval satisfies it, with the `origin pr reviewer request` command to ask for that bot's review. `--json` keeps the `nativeVerdict` field on gates and approvals, so scripts can tell which ones Agentic Owners decides.
- **See which stacked pull requests leave the merge queue with the one you remove.** `origin pr dequeue` names any pull requests queued behind the one you removed that left the merge queue with it, so you know what to queue again.
- **Clearer owner approval blockers in `origin pr requirements`.** Owner approval blockers name who must approve which paths. If the author is the only owner of the changed paths, the blocker says an approval from anyone but the author clears it. When a diff is too large for a full risk assessment, the blocker says so and suggests splitting the pull request.

### Rulesets

- &#x20;**Ruleset bypass actors use `group` instead of `team`.** In [`origin ruleset`](https://cursor.com/docs/origin/cli/reference/commands.md#rulesets) `create` and `update` specs and in ruleset output, a group bypass actor's `actorKind` is now `group`. Specs that still say `team` fail with an error telling you to use `group`, so update any saved specs.

### Fixes

- **Fixes to update hints.** The Origin CLI no longer prints its update hint or starts a background update check when git runs `origin credential-helper` or your shell requests completions, so git and shell output stay clean.

## October 19, 2026 release

### Pull requests

- **Clearer approval requirements.** Blockers for required reviewers name the files that need the approval, for example "1 approval from X required for a.ts, 0 so far." When Agentic Owners decides a pull request's review, [`origin pr requirements`](https://cursor.com/docs/origin/cli/reference/pull-requests.md#requirements-and-watch) labels it "Agentic Owners" instead of "Code Review Gate".

### Repositories

- **Map GitHub authors and dry-run pull request imports.** `origin repo import-prs` accepts `--user-map <file>` to map GitHub logins to Origin users (`user:<email>`), apps (`app:<app_id>`), or the import actor (`-`), with an optional `* -> target` catch-all. Add `--validate` to check every pull request's state, author mapping, and referenced commits without importing anything.

### Rulesets

- &#x20;**GitHub ruleset import no longer creates bypass actors that grant nothing.** Organization admin roles, repository roles, and `enforce_admins` are now reported as unsupported instead of becoming role bypass actors that never let anyone bypass. Ruleset commands accept only `user`, `team`, and `app` bypass actors, and `origin ruleset update` from a spec removes stored role actors. Add who may bypass with [`origin ruleset update`](https://cursor.com/docs/origin/cli/reference/commands.md#rulesets).

### Scripting

- **Pick `origin auth status` JSON fields, and catch broken git credential setup.** `origin auth status --json` takes a field list, such as `--json account,team,organization`, and `--json help` lists every field. `origin auth status` also warns when git uses the Origin credential helper for some Origin remotes but not `owner/repo` ones, and names the `origin auth setup-git` command that fixes it. See [authentication](https://cursor.com/docs/origin/cli/reference/commands.md#authentication).
- **Pick the label fields you want in JSON.** `origin label list`, `create`, `edit`, and `delete` take a comma-separated field list with `--json`, such as `--json name,color`, matching `gh`. Bare `--json` lists the fields. See [labels](https://cursor.com/docs/origin/cli/reference/commands.md#labels).

### Fixes

- &#x20;**Fixes to ruleset import and branch patterns.** `origin ruleset import` no longer adds a require-branch-up-to-date rule when a GitHub status-check rule lists no required checks. Saving a ruleset with an invalid branch or tag pattern fails with a plain explanation of the problem and how to fix it.
- **Fixed git remote detection and `origin push local` checks.** Commands that read your git remote recognize scp-style remotes without a user, like `host:org/repo`, and no longer mistake local paths containing a colon for remotes. `origin push local` rejects `--remote origin` or `--remote github` before any other checks run.
- **Fixes to the transcript private-key check.** The Origin CLI refuses to upload a transcript that hides a private key behind a BEGIN marker split across separate strings, including when a later string or plain-text line finishes the marker. Before, these transcripts could pass the secret check.

## October 15, 2026 release

### Pull requests

- **Safer transcript uploads in `origin pr gate report`.** `--transcript-file` refuses a transcript when a private key's BEGIN marker is split across lines, or when a line is nested too deeply to check for secrets. The help text and the "Stored transcript" message say that anyone who can read the repository can read the transcript until 30 days after the pull request closes or merges.

### Rulesets

- &#x20;**Clearer guidance when importing GitHub team reviewer rules.** `origin ruleset import --from-github` lists each required reviewer team with its approval count and tells you to add the requirement with `origin ruleset update` using `requiredReviewers`. It also notes when GitHub file patterns can't narrow the requirement, since Origin applies it to every pull request on the targeted branches. See [rulesets](https://cursor.com/docs/origin/cli/reference/commands.md#rulesets).
- &#x20;**GitHub file size limits carry over on ruleset import.** `origin ruleset import --from-github` converts a GitHub push ruleset's maximum file size rule into an Origin push ruleset instead of dropping it. Limits from 1 to 100 MB carry over; other values are still reported as unsupported.

### Authentication

- **Origin App installation tokens last their full lifetime.** When you export an Origin App installation token as `CURSOR_AUTH_TOKEN`, `origin` uses it until it expires instead of rejecting it five minutes early. Once it has expired, the CLI tells you to mint a new one.

### Scripting

- **Clearer errors for file and stdin flags.** Flags that take a file or `-` for stdin, such as `--input`, `--body-file`, `--signing-key`, and `--public-key`, require a value and fail with a usage error that names the flag and the problem, such as "does not exist" or "is not valid JSON". `origin pr create --body-file -` no longer competes with the push prompt for stdin.

## October 13, 2026 release

### Agents

- **Teach your coding agent to use the Origin CLI.** `origin agent prompt` prints a Markdown guide to `origin` for AI agents, matched to your installed version, with focused topics such as pull requests, review, and CI. `origin agent setup` installs a skill for Cursor, Claude Code, or Codex that points the agent to that guide, and mistyped commands suggest the closest match. See [agent commands](https://cursor.com/docs/origin/cli/reference/commands.md#agents).

### Pull requests

- **`origin pr merge` stops merges that would land on a closed pull request's branch.** If a pull request targets the head branch of a pull request that was closed without merging, `origin pr merge` refuses instead of landing your change on that branch. The message tells you how to fix it: retarget to trunk, reopen the parent and stack on it, or pass `--base-ok` to merge anyway.
- **Merge-conflict status no longer shows a pull request as clean too early.** `origin pr view --checks`, `origin pr watch`, and `origin pr status -c` now say when Origin is still checking for conflicts, is checking a conflicting pull request again, needs a restack, or has nothing to merge. Before, all of these showed as `no` or `MERGEABLE`.
- **Merge blockers say what to do next.** Blockers in [`origin pr requirements`](https://cursor.com/docs/origin/cli/reference/pull-requests.md#requirements-and-watch) now give the next step, such as "Restack the stack from #N to continue." or which branch to retarget onto when a stack's base branch was deleted. A blocker on a lower pull request in the stack names that pull request.
- **Shorter Gates section in `origin pr requirements`.** It shows only the gates your pull request requires, with their status at head, plus any errors in the head's `.origin/gates.ci`. When nothing is required, it prints `Gates: none required.`
- **`origin pr search` reports every invalid qualifier at once.** When a search has several unknown or malformed qualifiers, the error lists all of them instead of making you fix them one at a time.

### Stacks

- **Checking out a stack updates its trunk and protects teammates' branches.** `origin pr checkout --stack` and `origin stack get` fetch the stack's trunk branch and fast-forward it when it is behind. Branches for pull requests you didn't author are frozen, so stack commands won't rewrite them; run `origin stack unfreeze <branch>` to take one over. See [track and freeze](https://cursor.com/docs/origin/cli/reference/stacks.md#track-and-freeze).

### Repositories

- **Imported rulesets keep merge methods and merge queue exclusions.** `origin ruleset import --from-github` carries a GitHub ruleset's allowed merge and squash methods onto the imported pull request rule. Rebase is dropped with a warning. A ruleset that exempts GitHub merge queue branches also exempts Origin's merge queue branches, with a warning naming the added exclusion. See [rulesets](https://cursor.com/docs/origin/cli/reference/commands.md#rulesets).
- **Faster default-branch lookup in `origin repo clone-fast`.** It asks the server for the repository's default branch alone instead of downloading the full list of refs, and falls back to the old lookup if that request fails.

### Reliability

- **Git stops with a login hint instead of asking for a username.** When you aren't logged in to Origin, or your credentials expired and can't be refreshed, git operations through the Origin credential helper stop with a message to run `origin auth login`. Before, git fell back to a username prompt.
- **Fewer failed reads right after you create a pull request.** When Origin briefly reports that it is unavailable and asks the client to retry, `origin` commands that only read data try again, up to four attempts, instead of failing. That covers the moments after you create a pull request, before its first version is readable. Commands that change data are never retried.
- **Usage errors show what you can run next.** A mistyped command or missing argument prints the error with a short usage line, the commands and flags available at that level, and a pointer to `--help`. `-h` now works as `--help`, and `origin config get-channel` names the environment variable that set your channel.

### Fixes

- **Fixes to stack restack, checkout, and get.** `origin stack get` no longer fails on every run claiming `--take-remote` and `--keep-local` were both passed. `origin stack restack` rejects a branch with a `restack <branch> first` message instead of dropping commits. Stack checkout follows branches you renamed locally and reports when the stack's base branch is gone.
- **Fixes to `origin pr watch`.** It no longer reports a failure when the server hasn't read the pull request's merge rules yet; it waits up to two minutes instead. It also stops reprinting status that hasn't changed.

## October 6, 2026 release

- **Clearer messages when a write isn't approved.** When a command that needs approval is denied, expires, is cancelled, or can't be shown to anyone in Cursor, the CLI says nothing was applied and not to retry until someone can approve it. If `origin pr merge --auto --downstack` fails partway through a stack, the error names the pull requests that still have merge-when-ready on and how to turn it off with `--disable-auto`.

## October 6, 2026 release

- **`origin repo set-origin-remote` finds the right Origin repository.** It now asks Origin which repository mirrors your GitHub repo instead of guessing the URL from the owner and name, and `origin push local` uses the same lookup when it offers to run it. If the repo isn't mirrored or `gh` isn't signed in, it stops with an error and leaves your git remotes unchanged.

## October 6, 2026 release

### Pull requests

- **See what a pull request still needs to merge.** `origin pr requirements` lists required gates and their status at head, needed approvals, human-only paths, the Code Review Gate, and blockers in the stack. Add `--json` for scripts.
- **Safer merges and merge-when-ready status.** `origin pr merge --expect-head <number>=<sha>` refuses to merge if a listed pull request has moved, and `--auto --downstack` turns on merge-when-ready for every open pull request below this one. `origin pr view`, `status`, and `requirements` show a `Merge-when-ready` line, and `--json mergeWhenReady` returns it.
- **Manage reviewers and labels from the CLI.** `origin pr reviewer list`, `request`, and `remove` manage review requests for users, teams (`org/team`), and service accounts. `origin pr create` takes `--label` and `--reviewer`, and checks both before creating the pull request.
- **Wait on more than CI, and filter checks.** `origin pr watch --until` can wait for `merged`, `head:<sha>`, or `comment:<regex>`, and `--json` returns one result object. `origin pr checks --name <pattern>` limits output and the exit code to matching checks, and the output names the commit the checks ran on.
- **Edit and delete comments, and view one review thread.** `origin pr comment edit` and `origin pr comment delete` change or remove a comment you wrote, and `--edit-last` or `--delete-last` act on your newest one. `origin pr thread view <thread-id>` prints a single review thread, and comment JSON now includes a `url`.
- **Limit `origin pr diff` to specific paths.** List files, directories, or globs after `--`, as in `origin pr diff 123 -- src/ '*.md'`. In pathspecs and `--exclude`, `**` now matches any depth, including the top level.
- **See a pull request's cloud agents.** `origin pr view <number> --agents` lists the cloud agents attached to a pull request, and `--json agents` returns them for scripts.
- **More GitHub search syntax in `origin pr search`.** Negated qualifiers such as `-label:bug`, `has:` qualifiers, `OR` between scopes, and `mentions:` now work. `origin pr search --help` lists every supported qualifier.

### Stacks

- **Server-side restacks.** `origin stack restack --server` has Origin rebase your stack and move its branches in one atomic step, so your clone force-pushes nothing. Add `--dry-run` to preview first.

### Scripting

- **More `gh` JSON fields, and `--json help`.** `origin pr view` and `origin pr list` accept more `gh` field names, such as `body`, `state`, `headRefName`, and `isDraft`. Pass `--json help` to `origin pr view` or `origin pr list` to list the fields they accept.
- **Set a default repository with `ORIGIN_REPO`.** Commands that take `-R, --repo` fall back to the `ORIGIN_REPO` environment variable, then your clone's `origin` remote.
- **Find the Origin copy of a GitHub repository.** `origin repo from-github owner/repo` shows the Origin repository that mirrors a github.com repository, with its clone URL and source of truth, using your `gh` login.

### Reliability

- **Requests no longer hang.** Origin requests time out after 60 seconds by default; set `ORIGIN_TIMEOUT_MS` to change it, or `0` for no limit. `origin pr merge --match-head-commit <sha>` refuses the merge if the head has moved, and common server refusals print a suggested fix.
- **Shorter, clearer errors.** A mistyped command prints the error and a pointer to `--help` instead of the full help text. In a cloud agent VM, `origin api` stops with guidance instead of failing with a bare HTTP 401.
- **`origin auth login` shows who you signed in as.** After a successful login, including with `--api-key`, it prints the email of the account you signed in to.

### Fixes

- **Fixed stack navigation and restacking.** `origin stack up`, `down`, `top`, and `bottom` now work in single-branch and shallow clones when the target branch exists only on the remote. After a parent squash-lands, `origin stack restack` no longer replays trunk commits a child had merged in.
- **Fixed `--remote` handling.** Commands that take `--remote` now fail clearly when it is repeated or malformed, and a remote name starting with `-` is no longer read by git as an option.
- **Fixed pull request diffs and repo arguments.** `origin pr diff` shows real file modes and applies cleanly with `git apply`. Repo arguments ending in `.git` or `/` resolve correctly, and `origin pr list --mine` gives working steps in token sessions.

## October 1, 2026 release

### Pull requests

- **Request reviewers by email.** `origin pr edit --add-reviewer` takes one or more emails, fails if an email doesn't match exactly one reviewer candidate, and prints who was requested.
- **Links to new comments.** `origin pr comment` prints the new comment's id and a URL that opens it.
- **More `gh`-compatible JSON.** `origin pr view` and `origin pr list` accept `--json headRefOid`. Change output shows actions taken through an app or bot as "Name via app", and JSON output includes a `performedVia` field.
- **Gate checks no longer count as CI.** `origin pr checks` ignores Gate review checks when it sets its pending, failed, or no-checks exit code. `origin pr view` shows "unknown" instead of "no" for CI and approvals when the target's rules can't be read.
- **`origin pr stack` is removed, and so is `--branch` for picking a pull request.** Name a branch as the positional target instead. `origin pr checkout --branch` is unchanged.

### Reliability

- **Safer branch names.** `origin pr create --push` and `origin pr checkout` use fully qualified refs, so branch names that clash with tags work, and invalid names fail with `'<name>' is not a valid branch name`. `origin pr create --push` also pushes branches whose names start with `-`.
- **Automatic retries on rate limits.** When Origin rate-limits a request, the CLI waits and retries, printing "Origin rate limit reached; retrying in Ns."

## September 24, 2026 release

- **Find pull requests by commit.** `origin pr list --commit <sha>` lists the pull requests Origin records for a commit.
- **`reviewDecision` in JSON output.** `origin pr view --json reviewDecision` returns the review decision, matching `gh`.
- **Request bodies from stdin.** `origin api --input -` reads the request body from stdin instead of failing with "Unknown argument: -".
- **CloneKit fixes.** `origin repo clone-fast` no longer fails with spurious EPIPE errors during parallel range downloads, and it looks up the default branch while the kit downloads instead of before.

## September 17, 2026 release

- **Team details in `origin auth status`.** `origin auth status` prints your teams, role, and organization ids, and `--json` prints them as JSON for scripts.

## September 16, 2026 release

- **Clearer stack status.** `origin pr stack` shows how each pull request in a stack relates to its parent and the action that repairs it.

## September 15, 2026 release

### Repositories

- **Edit repository settings.** `origin repo edit` sets the default branch, visibility, allowed merge methods, and delete-branch-on-merge. `origin repo view` shows those settings, and `origin repo list --json <fields>` prints repositories as JSON with optional `--jq` filtering.
- **Manage access from the CLI.** `origin repo access` and `origin namespace access` list, grant, change, and remove access for teams, users, and organization groups, and list the roles you can assign. On repositories in your personal namespace, `origin repo access` also lists, grants, and removes external collaborators, with Read or Write access.
- **Manage GitHub mirrors.** `origin repo mirror` starts a mirror transition, watches its status, syncs a ref on demand, and detaches the mirror, with `--json` output.
- **Verify a migration.** `origin repo verify-migration` compares a GitHub repository's default branch, visibility, merge settings, labels, and rulesets against its Origin copy and exits 1 on a mismatch. Use `--namespace` to check every repository in a namespace.
- **Rulesets, labels, and apps.** `origin ruleset create`, `update`, and `delete` manage rulesets from flags or a JSON spec, and `origin ruleset import --from-github` converts GitHub rulesets or branch protection. `origin label` lists, creates, edits, deletes, and bulk-imports labels. `origin app` manages Origin apps, their signing keys, and webhook deliveries.
- **Stricter CloneKit downloads.** `origin repo clone-fast` checks every range response against the kit's size. If the server stops honoring byte ranges, it downloads the pack as one file, and a range that returns the wrong number of bytes fails the kit download with an error.

### Pull requests

- **Set the merge commit message.** `origin pr merge` accepts `--subject`, `--body`, and `--body-file` to set the commit message for a single pull request. When a stack lands as one commit, the flags are ignored instead of failing the merge.
- **Diffs for very large pull requests.** `origin pr diff` and `origin pr view` fetch the diff in pages, so very large changes no longer fail on an oversized response.
- **Request changes from the CLI.** `origin pr review --request-changes` (`-r`) submits a request-changes review instead of erroring. Pass exactly one of `--approve`, `--request-changes`, or `--comment`.

## September 8, 2026 release

- **Print your auth token.** Run `origin auth token` to print the access token the CLI is configured to use.
- **Git authenticates with `CURSOR_AUTH_TOKEN`.** When `CURSOR_AUTH_TOKEN` is set, git operations through the Origin credential helper use it before stored credentials, so headless jobs can export the token instead of running `origin auth login`.
- **Clear error for an expired token.** If `CURSOR_AUTH_TOKEN` has expired, the CLI stops with a message that the token must be refreshed instead of sending it and failing with a 401.
- **Control CloneKit fallback.** `origin repo clone-fast --fallback never` exits non-zero instead of falling back to `git clone`, and the command now reports which phase stopped.

## September 4, 2026 release

- **Faster CI clones with CloneKit.** For repositories with CloneKit turned on, `origin repo clone-fast` downloads a prebuilt clone kit, verifies it, fetches newer objects, checks out the default branch, and prints how long each phase took.
- **More reliable large clones.** `origin repo clone` raises git's HTTP post buffer, so large fetches no longer fail with "unable to rewind rpc post data" after a dropped connection.
