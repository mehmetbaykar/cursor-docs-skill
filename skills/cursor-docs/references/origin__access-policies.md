---
title: "Custom access policies"
source: https://cursor.com/docs/origin/access-policies
path: /docs/origin/access-policies
---

# Custom access policies

Origin is currently released in early beta. You can create repos, push and pull with git, mirror from GitHub, browse and search code, open and merge pull requests, and share with your Cursor team.

### Preview

Custom access policies are in preview and can change before they're generally available.

A custom access policy is a named set of permissions you define for your team's codebase. Use one when the built-in policies, such as Read, Write, and Admin, give a person or group more or less access than they need.

## Kinds of policy

- **Codebase policies.** You grant a codebase policy on the codebase. It can include repository permissions and codebase permissions, such as creating repositories or installing apps.
- **Repository policies.** You grant a repository policy on a single repository. It includes repository permissions only.

## Who can use custom policies

Custom access policies are available on team codebases. Personal codebases don't have them.

Codebase admins create custom policies. A codebase admin is anyone with the built-in **Codebase Admin** policy.

## Where to find them

- **Codebase policies.** In the [Cursor dashboard](https://cursor.com/dashboard), select **Codebase**, then **Access**. Policies are listed under **Codebase Policies**, below **Who Has Access**.
- **Repository policies.** Open a repository at [cursor.com/codebase](https://cursor.com/codebase), select **Settings**, then **Access**. Policies are listed under **Access Policies**, below **Repo Access**.

Each list shows the built-in policies first, then your custom ones with a **Custom** badge. Select a policy to see its permissions.

## Create a policy

Codebase admins see a **New** button in both lists. Select it, name the policy, and choose its permissions.

Once the policy exists, it appears in the policy picker when you grant access, with **(Custom)** after its name.

## Related

- [Settings](https://cursor.com/docs/origin/settings.md) - repository and codebase settings, including access
- [Origin](https://cursor.com/docs/origin.md) - overview, access, and privacy
