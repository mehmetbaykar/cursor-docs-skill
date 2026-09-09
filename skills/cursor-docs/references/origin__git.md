---
title: "Clone, Push & Pull"
source: https://cursor.com/docs/origin/git
path: /docs/origin/git
---

# Clone, Push & Pull

Origin is currently released in early beta. You can create repos, push and pull with git, mirror from GitHub, browse and search code, open and merge pull requests, and share with your Cursor team.

Please submit any and all feedback to [hi@cursor.com](mailto:hi@cursor.com) to help us make the product better.

Origin works with standard git. Open a repo at [cursor.com/codebase](https://cursor.com/codebase), select the green **Code** dropdown, and copy the clone URL.

## Clone with HTTPS

The **Code** menu includes an **HTTPS** tab:

```text
https://origin.cursor.com/{owner}/{repo}.git
```

Example:

```bash
git clone https://origin.cursor.com/acme/checkout.git
```

## Clone with the Origin CLI

The same menu has an **Origin CLI** tab with CLI-oriented setup. Install and sign in first:

```bash
curl -fsSL https://downloads.cursor.com/origin/install.sh | sh
origin auth login
```

See [Install the Origin CLI](https://cursor.com/docs/origin/cli.md).

## Authenticate

Sign in with the Origin CLI before the first git operation if you have not already:

```bash
origin auth login
```

Then clone, fetch, pull, or push with git.

## Add a remote to an existing repo

```bash
git remote add origin https://origin.cursor.com/{owner}/{repo}.git
git push -u origin main
```

To keep GitHub and Origin in parallel while you evaluate:

```bash
git remote set-url --add --push origin https://github.com/acme/checkout.git
git remote set-url --add --push origin https://origin.cursor.com/acme/checkout.git
```

For a full history copy from GitHub into Origin, prefer [mirroring](https://cursor.com/docs/origin/mirror-github.md).

## Mirrored GitHub repositories

A repo [mirrored from GitHub](https://cursor.com/docs/origin/mirror-github.md) uses the same HTTPS clone URL:

```text
https://origin.cursor.com/{owner}/{repo}.git
```

GitHub stays the source of truth. `git push` to this remote goes to GitHub. Origin updates after GitHub accepts the push.

When GitHub is unavailable, keep working on the Origin copy with `origin/*` branches and `origin push local`. Reads of an already-synced repo may still work over the same HTTPS clone URL. Git LFS batch does not fail over. `/local` is the supported write path while GitHub is down.

## Forge-local branches on mirrored repos

On a mirrored repo, `origin/*` branches are your workspace on the Origin copy. Use them to keep working when GitHub is unavailable, or for any other git state you want only on Origin. Those refs stay on Origin. They never sync from GitHub and never sync to GitHub.

Origin does not sync GitHub branches named `origin` or `origin/...`. That is deliberate, so a GitHub branch with that name cannot overwrite what you pushed with `origin push local`. Feature branches that should become GitHub pull requests still use a normal `git push origin`.

### `origin push local`

`origin push local` writes those Origin-only branches. It is not a substitute for `git push origin`.

`git push origin <branch>` uses the clone URL and, on an inbound mirror, lands on GitHub. `origin push local` does this instead:

1. Confirms the checkout's `origin` remote is an inbound-mirrored Origin repo
2. Creates or updates a git remote named `origin-local` at `https://origin.cursor.com/{owner}/{repo}.git/local`
3. Scopes that remote's fetch and push refspecs to `refs/heads/origin/*`
4. Pushes every local `origin/*` branch to `/local`

Origin does not rewrite the name. `origin/my-state` is stored as `refs/heads/origin/my-state`.

```bash
git branch origin/my-state HEAD
origin push local
```

After the first run, `git remote -v` includes:

```text
origin-local    https://origin.cursor.com/{owner}/{repo}.git/local (fetch)
origin-local    https://origin.cursor.com/{owner}/{repo}.git/local (push)
```

`git push origin-local` and `git fetch origin-local` use the same scoped refspec. `origin push local --dry-run` prints the push without sending it. `--remote <name>` picks a different remote name. Do not pass `--remote origin` or `--remote github`; those remotes stay the GitHub-backed upstream.

The `origin` remote must already point at Origin:

```text
https://origin.cursor.com/{owner}/{repo}.git
```

`/local` exists only on inbound mirrors. On a repo created directly on Origin, push any branch to `origin`.

`/local` is enabled per repository. If git reports the repository as not found, the endpoint is not enabled for that repo yet. Per-ref `remote rejected` messages mean the server refused a ref outside `origin/`.

### Branch names that start with `origin/`

Matching is a path segment after `origin/`. A branch named exactly `origin` is reserved and is not pushable to `/local`. A name such as `original/backup` is also outside the namespace.

On inbound mirrors:

- **Push to `/local`.** Only `origin/<name>` refs are accepted. Everything else is rejected with a message to push that ref to the upstream remote.
- **Fetch from GitHub.** Inbound sync skips `origin` and `origin/*`. That is deliberate: a GitHub branch with that name cannot overwrite what you pushed with `origin push local`.
- **Push to the clone URL.** `git push origin origin/my-state` still sends `origin/my-state` to GitHub. Origin will not import that GitHub branch on the next sync.
- **Pull requests.** Cloud agents on a mirrored repo open [GitHub pull requests](https://cursor.com/docs/origin/pull-requests.md#mirrored-github-repositories) from ordinary branches you push to GitHub. An `origin/*` branch is not on GitHub, so it cannot be the head of a GitHub pull request.

Git also uses `origin/` for remote-tracking refs: `origin/main` means branch `main` on the `origin` remote. Create the local branch with an explicit name (`git branch origin/my-state HEAD` or `git switch -c origin/my-state`) so you do not check out the remote-tracking branch by mistake.

### When should I use origin push local?

When GitHub is unavailable, or whenever you want git state only on the Origin copy. Create an `origin/...` branch and run `origin push local`. For work you want on GitHub, including pull requests, run `git push origin`.

### Does Origin rename origin/ branches?

No. The branch name on Origin is the same local name. `git fetch origin-local` tracks them as `origin-local/origin/<name>` because that is how git names remote-tracking refs, not because Origin strips or rewrites the prefix.

### What if GitHub already has a branch named origin/something?

Origin does not import it. Sync skips GitHub branches named `origin` or `origin/...` so they cannot overwrite what you pushed with `origin push local`.

## Pull latest

```bash
git pull origin main
```

## Troubleshooting

If clone or push fails, confirm you are signed in with `origin auth login`. See [Install the Origin CLI](https://cursor.com/docs/origin/cli.md).

If your shell says `command not found: origin` after install, add `~/.local/bin` to your `PATH` (for zsh: append `export PATH="$HOME/.local/bin:$PATH"` to `~/.zshrc`, then `source ~/.zshrc`). Details are on the CLI page.
