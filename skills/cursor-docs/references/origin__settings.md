---
title: "Settings"
source: https://cursor.com/docs/origin/settings
path: /docs/origin/settings
---

# Settings

Origin is currently released in early beta. You can create repos, push and pull with git, mirror from GitHub, browse and search code, open and merge pull requests, and share with your Cursor team.

Please submit any and all feedback to [hi@cursor.com](mailto:hi@cursor.com) to help us make the product better.

Open a repository at [cursor.com/codebase](https://cursor.com/codebase) and select the **Settings** tab. These settings apply to one repository. For team-wide Origin settings, see [Codebase settings](https://cursor.com/docs/origin/codebase-settings.md).

The tabs under **Settings** depend on who owns the repository. Repo visibility and the **Access** tab only appear on team-owned repos; personal repos manage sharing under **Collaborators** instead.

- Team-owned repos: **General**, **Access**, **Rules and Protections**, and **Apps**
- Personal repos: **General**, **Collaborators**, **Apps**, **Rules and Protections**, and **Advanced**

The Access, Collaborators, and Rules and Protections UIs are being redesigned; labels and layout may change during early beta.

## General

### Sync status

For a repository [mirrored from GitHub](https://cursor.com/docs/origin/mirror-github.md), **Sync Status** shows Origin as the mirror and GitHub as the source, with a link to the source repo. Repositories created on Origin do not show sync status.

### Detach from GitHub

Under **Danger Zone**, **Detach from GitHub** stops syncing with GitHub and makes the Origin copy a standalone Origin-hosted repository: Origin becomes the source of truth, and pushes to the Origin remote no longer flow to GitHub. Your GitHub repository is not affected.

## Access

**Access** is only available on team-owned repositories. For repos owned by a personal account, see [Collaborators](https://cursor.com/docs/origin/settings.md#collaborators).

Use **Access** to review who can access this repository.

Visibility is chosen when you [create the repository](https://cursor.com/docs/origin/create-repository.md). An **Internal** repo is visible to anyone on your Cursor team with access to the codebase. A **Private** repo is visible only to members granted access directly or through codebase permissions; when a repo is switched to Private, the person making the change automatically keeps admin access.

Team-wide Origin access (who can enable Origin, create repositories, or disable the feature) is managed in [Codebase settings](https://cursor.com/docs/origin/codebase-settings.md#permissions).

![Origin repository Settings Access tab](https://cursor.com/docs-static/images/origin/settings-permissions.png)

## Collaborators

**Collaborators** is only available on repos owned by a personal account. Team-owned repos manage access under [Access](https://cursor.com/docs/origin/settings.md#access).

Repos created under a personal account are always **Private** and visible only to you by default. Use **Collaborators** to invite specific users and give them access to this repository.

Personal repos do not have a per-repo visibility control; if you need Internal-style team-wide access, create the repo under a team codebase instead.

## Rules and Protections

**Rules and Protections** is where you configure branch rules and merge protections for the repository. Available controls may expand during early beta.

## Apps

Use **Apps** to connect third-party tools to this repository.

In early beta you can connect:

- **Vercel** — link your Vercel account; pushes can trigger deploys and pull requests can get preview environments
- **Depot** — run CI on Origin-hosted repositories
- **Buildkite** — run CI on Origin-hosted repositories

The repository **Apps** tab shows apps installed for this repository. To install or manage apps, select **Manage Apps**, which opens the codebase-level [Apps settings](https://cursor.com/docs/origin/codebase-settings.md#apps).

**Depot** and **Buildkite** work on **Origin-hosted repositories only**, not on repos [mirrored from GitHub](https://cursor.com/docs/origin/mirror-github.md). Mirrored repos keep CI on GitHub.

For internal Origin API apps, see [Codebase settings → Apps](https://cursor.com/docs/origin/codebase-settings.md#apps).
