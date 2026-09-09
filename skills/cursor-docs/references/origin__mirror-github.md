---
title: "Mirror a GitHub repository"
source: https://cursor.com/docs/origin/mirror-github
path: /docs/origin/mirror-github
---

# Mirror a GitHub repository

Origin is currently released in early beta. You can create repos, push and pull with git, mirror from GitHub, browse and search code, open and merge pull requests, and share with your Cursor team.

Please submit any and all feedback to [hi@cursor.com](mailto:hi@cursor.com) to help us make the product better.

Mirroring copies a GitHub repository into Origin and keeps Origin updated as the GitHub repo changes. GitHub stays the source of truth. Use this when the code already lives on GitHub and you want Origin browse, search, and agent workflows on that history.

## Prerequisites

- A Cursor account with Origin access on a Pro, Teams, or Enterprise plan
- The [Cursor GitHub app](https://cursor.com/docs/integrations/github.md) connected to the org or account that owns the repo
- GitHub admin access on the repository you want to sync (required to enable the mirror)

## Sync a repo

1. Open [cursor.com/codebase](https://cursor.com/codebase)
2. Select **Sync from GitHub**
3. Choose the GitHub organization and repository
4. Confirm the sync

When the sync finishes, open the Origin copy to browse files and commit history.

You can confirm sync status later under the repository **Settings → General** tab. Synced repos show Origin as the mirror and GitHub as the source.

## What syncs

| Included                                      | Not included                         |
| --------------------------------------------- | ------------------------------------ |
| Git history, branches, and tags               | GitHub Issues                        |
| Code you can browse and search on Origin      | GitHub Actions workflows and secrets |
| GitHub pull requests you can review in Cursor |                                      |
| Ongoing updates so Origin stays current       |                                      |

Issues and CI configuration stay on GitHub. Origin also does not sync GitHub branches named `origin` or `origin/...`, so they cannot overwrite your Origin-only workspace.

## Clone URL

The green **Code** button copies the same HTTPS remote used for every Origin repo:

```text
https://origin.cursor.com/{owner}/{repo}.git
```

Pushes to this remote go to GitHub. Origin updates after GitHub accepts the push. See [Clone, Push & Pull](https://cursor.com/docs/origin/git.md).

## Forge-local `origin/` branches

`origin/` branches are your workspace on the Origin copy. Use them to keep working when GitHub is unavailable, or for any other git state you want only on Origin. Push them with `origin push local`, not `git push origin`.

Origin does not sync GitHub branches named `origin` or `origin/...`. That is deliberate, so a GitHub branch with that name cannot overwrite what you pushed with `origin push local`.

See [forge-local branches](https://cursor.com/docs/origin/git.md#forge-local-branches-on-mirrored-repos).

## After you mirror

- Browse and search at [cursor.com/codebase](https://cursor.com/codebase)
- Clone the Origin remote from the green **Code** button when you want a local checkout from Origin
- Attach [cloud agents](https://cursor.com/docs/origin/integrations.md) to the Origin repo. On a mirrored repo, those agents open GitHub pull requests
- Review [GitHub pull requests](https://cursor.com/docs/origin/pull-requests.md#mirrored-github-repositories) in Cursor

## If GitHub is unreachable

Keep working on the Origin copy with `origin/` branches and `origin push local`. `/local` is the supported write path while GitHub is down.

Reads of an already-synced repo may still work over the same HTTPS clone URL. Origin serves the copy it already has. Git LFS batch does not fail over. A repo that has not finished its first sync still needs GitHub.

## Detach from GitHub

To stop syncing, open **Settings → General** and select **Detach from GitHub** under **Danger Zone**. This stops the sync and converts the Origin copy into a standalone Origin-hosted repository: Origin becomes the source of truth, and pushes to the Origin remote no longer flow to GitHub. Your GitHub repository is not affected.

## Sync lag

If browse looks stale:

- Confirm the GitHub app still has access ([GitHub integration](https://cursor.com/docs/integrations/github.md))
- Confirm you are a GitHub admin on the source repo
- Re-run **Sync from GitHub** from [cursor.com/codebase](https://cursor.com/codebase), or check **Settings → General** for sync status

## When not to mirror

If you only want automated review comments on GitHub PRs, [Bugbot](https://cursor.com/docs/bugbot.md) does that without moving storage. Mirror when you want Origin browse, search, and cloud agents on that GitHub history.
