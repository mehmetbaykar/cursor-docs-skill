---
title: "Origin CLI release notes"
source: https://cursor.com/docs/release-notes/origin-cli
path: /docs/release-notes/origin-cli
---

# Origin CLI release notes

New features, improvements, and fixes in the [Origin CLI](https://cursor.com/docs/origin/cli.md). Each entry covers one release and is labeled with its release date. Changes to Origin on the web and in the API are in the [Origin release notes](https://cursor.com/docs/release-notes/origin.md).

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
