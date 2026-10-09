---
title: "Settings"
source: https://cursor.com/docs/origin/settings
path: /docs/origin/settings
---

# Settings

Origin is currently released in early beta. You can create repos, push and pull with git, mirror from GitHub, browse and search code, open and merge pull requests, and share with your Cursor team.

## Repository settings

Open a repository at [cursor.com/codebase](https://cursor.com/codebase) and select the **Settings** tab. These settings apply to one repository. For team-wide Origin settings, see [Codebase settings](https://cursor.com/docs/origin/settings.md#codebase-settings).

The tabs under **Settings** depend on who owns the repository. Repo visibility and the **Access** tab only appear on team-owned repos; personal repos manage sharing under **Collaborators** instead.

- Team-owned repos: **General**, **Access**, **Rules and Protections**, and **Apps**
- Personal repos: **General**, **Collaborators**, **Apps**, **Rules and Protections**, and **Advanced**

The Access, Collaborators, and Rules and Protections UIs are being redesigned; labels and layout may change during early beta.

### General

#### Sync status

For a repository [mirrored from GitHub](https://cursor.com/docs/origin/mirror-github.md), **Sync Status** shows Origin as the mirror and GitHub as the source, with a link to the source repo. Repositories created on Origin do not show sync status.

#### Detach from GitHub

Under **Danger Zone**, **Detach from GitHub** stops syncing with GitHub and makes the Origin copy a standalone Origin-hosted repository: Origin becomes the source of truth, and pushes to the Origin remote no longer flow to GitHub. Your GitHub repository is not affected.

### Access

**Access** is only available on team-owned repositories. For repos owned by a personal account, see [Collaborators](https://cursor.com/docs/origin/settings.md#collaborators).

Use **Access** to review who can access this repository.

Visibility is chosen when you [create the repository](https://cursor.com/docs/origin/create-repository.md). An **Internal** repo is visible to anyone on your Cursor team with access to the codebase. A **Private** repo is visible only to members granted access directly or through codebase permissions; when a repo is switched to Private, the person making the change automatically keeps admin access.

Team-wide Origin access (who can enable Origin, create repositories, or disable the feature) is managed in [Codebase settings](https://cursor.com/docs/origin/settings.md#permissions).

![Origin repository Settings Access tab](https://cursor.com/docs-static/images/origin/settings-permissions.png)

### Collaborators

**Collaborators** is only available on repos owned by a personal account. Team-owned repos manage access under [Access](https://cursor.com/docs/origin/settings.md#access).

Repos created under a personal account are always **Private** and visible only to you by default. Use **Collaborators** to invite specific users and give them access to this repository.

Personal repos do not have a per-repo visibility control; if you need Internal-style team-wide access, create the repo under a team codebase instead.

### Rules and Protections

**Rules and Protections** is where you configure branch rules and merge protections for the repository. Available controls may expand during early beta.

### Apps

The repository **Apps** tab shows apps installed for this repository. To install or manage apps, select **Manage Apps**, which opens the codebase-level [Apps settings](https://cursor.com/docs/origin/apps.md).

## Codebase settings

Codebase settings apply across your team's Origin repos at [cursor.com/codebase](https://cursor.com/codebase), not to a single repository. Open codebase settings from the codebase home (separate from a repo's **Settings** tab).

### Permissions

Team-level permissions control who can use Origin for your codebase: who can access repos under your claimed codebase name, and how Origin relates to your Cursor team membership.

- A team admin [claims the codebase name](https://cursor.com/docs/origin.md#enable-origin) and enables Origin; non-admins can request access from the same page
- Once Origin is enabled, admins can create repositories and use Permissions to grant access, including repository creation, to other members
- Admins can disable Origin for the team at any time from the dashboard; teams on legacy privacy mode cannot enable Origin, so switch to [Privacy Mode](https://cursor.com/help/security-and-privacy/privacy.md#how-do-i-enable-privacy-mode) first if you want access

Exact controls in the Permissions UI may change during early beta.

### Notifications

Use **Notifications** in codebase settings to choose which pull request events in the codebase's repos send you a Slack DM from `@Cursor`. If your [Slack](https://cursor.com/docs/integrations/slack.md) account isn't linked yet, connect it on the **Slack** row. Then turn on the events you want: **Review requested**, **Pull request merged**, **Review submitted**, and **Comment**. **Apps and bots** includes activity from apps and bots, and **Ignore drafts** skips draft pull requests. Each switch saves as soon as you change it.

To open these settings from Slack, select **Manage notifications** in a DM's menu.

**Scheduled personal reminders** send you a Slack DM digest of open review requests on a recurring schedule. Select **Add reminder**, then choose the **Days** (**Weekdays**, **Every day**, or **Custom**), **Times**, **Time zone**, and **Repositories**. Turn on **All open pull requests** to list every open pull request in those repos instead of only your review requests. **Ignore drafts**, **Ignore approved pull requests**, and **Labels** narrow the digest. Use a reminder's switch to pause it.

**Channel subscriptions** post pull request activity from the codebase's repos in a Slack channel. Invite `@Cursor` to the channel first. Only members of a channel can manage its subscriptions. Select **Add subscription**, choose the channel and a repository, then pick the events to post: **Pull requests**, **Reviews**, or **Comments**. Add **Labels** to post only when a pull request has every label. For a private or internal repo, anyone in the channel, including people added later, sees its activity.
