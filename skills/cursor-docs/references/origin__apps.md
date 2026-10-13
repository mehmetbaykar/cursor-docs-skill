---
title: "Origin Apps"
source: https://cursor.com/docs/origin/apps
path: /docs/origin/apps
---

# Origin Apps

Origin is currently released in early beta. You can create repos, push and pull with git, mirror from GitHub, browse and search code, open and merge pull requests, and share with your Cursor team.

**Apps** under [codebase settings](https://cursor.com/docs/origin/settings.md#codebase-settings) (also at [cursor.com/codebase/settings/apps](https://cursor.com/codebase/settings/apps)) is where you install and manage apps for your codebase:

- **Third-party apps** from the [Origin App Marketplace](https://cursor.com/codebase/apps): install them here, then see which apps are active on a given repository from that repository's **Apps** tab in [Repository settings](https://cursor.com/docs/origin/settings.md#apps)
- **Private apps** for API access: [create an app](https://cursor.com/docs/origin/apps/build-app.md) for your team, then use the app credentials and installation flow to call the Origin API
- **Marketplace apps**: make your app public and submit it for review to list it in the Origin App Marketplace for every Origin team. See [Publish to the Marketplace](https://cursor.com/docs/origin/apps/publish.md).

Apps authenticate with app JWTs and installation access tokens. For base URL, authentication, scopes, webhooks, and endpoint reference, see the [Origin API](https://cursor.com/docs/api/origin.md).

## Third-party apps

In early beta you can connect the third-party apps listed in the [Origin App Marketplace](https://cursor.com/codebase/apps). Sign in to Cursor to browse it.

[Depot](https://cursor.com/codebase/apps/public/depot) and [Buildkite](https://cursor.com/codebase/apps/public/buildkite) work on **Origin-hosted repositories only**, not on repos [mirrored from GitHub](https://cursor.com/docs/origin/mirror-github.md). Mirrored repos keep CI on GitHub.
