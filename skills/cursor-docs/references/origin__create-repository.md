---
title: "Create an Origin repository"
source: https://cursor.com/docs/origin/create-repository
path: /docs/origin/create-repository
---

# Create an Origin repository

Origin is currently released in early beta. You can create repos, push and pull with git, mirror from GitHub, browse and search code, open and merge pull requests, and share with your Cursor team.

Please submit any and all feedback to [hi@cursor.com](mailto:hi@cursor.com) to help us make the product better.

Create an empty Origin repository from the web UI, or ask a Cursor agent to create one for you. Then clone it and push with git. If the code already lives on GitHub, [mirror the repository](https://cursor.com/docs/origin/mirror-github.md) instead.

## Create in the UI

From [cursor.com/codebase](https://cursor.com/codebase):

1. Select **New**
2. In the **New repo** dialog, enter a **Repo Name**. If the repo will be owned by a team codebase, also choose **Internal** or **Private** visibility. Repos owned by a personal account are always created as private, so the visibility chooser is not shown.
3. Select **Create Repo**

After creation, open the repo to copy the clone URL from the green **Code** button and push from your machine.

## Sync from GitHub

To copy an existing GitHub repository into Origin, select **Sync from GitHub** on the codebase home instead of **New**. You choose the GitHub organization and repository, then confirm the sync. See [Mirror a GitHub repository](https://cursor.com/docs/origin/mirror-github.md) for prerequisites, what syncs, and how to detach from GitHub.

## Create with a Cursor agent

Cursor agents can create Origin repositories as part of a task. Ask the agent in Cursor to create a repo on Origin; it can install the [Origin CLI](https://cursor.com/docs/origin/cli.md), sign in, create the repo, set the remote, and push.

Agents use the same permissions as your Cursor account. You need access to Origin code storage for the create to succeed. [Cloud agents](https://cursor.com/docs/origin/integrations.md) can work against existing Origin repositories: clone, branch, commit, and push. On a repo created on Origin they can open Origin pull requests; on a [mirrored GitHub repo](https://cursor.com/docs/origin/mirror-github.md) they open GitHub pull requests.

## Name, visibility, and sharing

Enter a **Repo Name** in the **New repo** dialog. What comes next depends on whether the repo is owned by a team codebase or by your personal account.

### Team-owned repos

- Choose visibility in the **New repo** dialog:
  - **Internal**, visible to anyone on your team with access to the codebase
  - **Private**, visible only to members granted access directly or through codebase permissions
- Team access follows your Cursor team and codebase access
- After creation, manage visibility and per-repo access from the repository **Settings** tab. See [Settings](https://cursor.com/docs/origin/settings.md).

### Personal repos

- Repos created under a personal account are always **Private** and visible only to you by default. The **New repo** dialog does not show a visibility chooser for personal repos.
- To share a personal repo, open the repo, go to **Settings**, then **Collaborators**, and invite the people you want to give access.

## Push your first commit

After you create an empty repo in the UI, initialize a local project and push:

```bash
git clone https://origin.cursor.com/{owner}/{repo}.git
cd {repo}
# add your files
git add .
git commit -m "Initial commit"
git push -u origin main
```

If you already have a local project:

```bash
cd your-project
git remote add origin https://origin.cursor.com/{owner}/{repo}.git
git push -u origin main
```
