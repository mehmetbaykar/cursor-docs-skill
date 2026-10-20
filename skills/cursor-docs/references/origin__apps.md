---
title: "Origin Apps"
source: https://cursor.com/docs/origin/apps
path: /docs/origin/apps
---

# Origin Apps

Origin is currently released in early beta. You can create repos, push and pull with git, mirror from GitHub, browse and search code, open and merge pull requests, and share with your Cursor team.

Add third-party apps to your codebase from the [Origin App Marketplace](https://cursor.com/codebase/apps), or build a private app that calls the [Origin API](https://cursor.com/docs/api/origin.md).

You install and manage apps on the **Apps** page in [codebase settings](https://cursor.com/docs/origin/settings.md#codebase-settings), at [cursor.com/codebase/settings/apps](https://cursor.com/codebase/settings/apps). To see which apps are installed on a repository, open the **Apps** tab in its [repository settings](https://cursor.com/docs/origin/settings.md#apps).

## Third-party apps

The [Origin App Marketplace](https://cursor.com/codebase/apps) includes these apps. To install one on your codebase, sign in to Cursor and open the app's listing page.

| Category           | Apps                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Deployments        | [Cloudflare](https://cursor.com/codebase/apps/public/cloudflare), [Netlify](https://cursor.com/codebase/apps/public/netlify), [Render](https://cursor.com/codebase/apps/public/render), [Spacelift](https://cursor.com/codebase/apps/public/spacelift-deploy-us), [Vercel](https://cursor.com/codebase/apps/public/vercel)                                               |
| CI                 | [Buildkite](https://cursor.com/codebase/apps/public/buildkite), [CircleCI](https://cursor.com/codebase/apps/public/circleci), [Depot](https://cursor.com/codebase/apps/public/depot), [EngFlow](https://cursor.com/codebase/apps/public/engflow), [Namespace](https://cursor.com/codebase/apps/public/namespacelabs), [RWX](https://cursor.com/codebase/apps/public/rwx) |
| Code review        | [CodeRabbit](https://cursor.com/codebase/apps/public/coderabbitai), [Greptile](https://cursor.com/codebase/apps/public/greptile), [Tenki](https://cursor.com/codebase/apps/public/tenki)                                                                                                                                                                                 |
| Security           | [Artemis Security](https://cursor.com/codebase/apps/public/artemis-security), [Semgrep](https://cursor.com/codebase/apps/public/semgrep), [Socket Security](https://cursor.com/codebase/apps/public/socket-security), [Upwind](https://cursor.com/codebase/apps/public/upwind-security)                                                                                  |
| Monitoring         | [Sentry](https://cursor.com/codebase/apps/public/sentry)                                                                                                                                                                                                                                                                                                                 |
| Project management | [Linear](https://cursor.com/codebase/apps/public/linear)                                                                                                                                                                                                                                                                                                                 |

Origin apps work only on Origin-hosted repositories, not on repositories [mirrored from GitHub](https://cursor.com/docs/origin/mirror-github.md). Mirrored repositories keep their CI and integrations on GitHub.

## Build your own app

To call the Origin API, [build a private app](https://cursor.com/docs/origin/apps/build-app.md) for your team. Apps authenticate with app JWTs and installation access tokens. The [Origin API reference](https://cursor.com/docs/api/origin.md) covers the base URL, authentication, scopes, webhooks, and endpoints.

The marketplace is open to submissions. To list your app for every Origin team, make it public and [submit it for review](https://cursor.com/docs/origin/apps/publish.md).
