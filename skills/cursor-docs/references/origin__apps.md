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

The [Origin App Marketplace](https://cursor.com/codebase/apps) lists these apps. Sign in to Cursor to browse it, or open an app's listing page directly from the links below to install it on your codebase.

| Category           | Apps                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deployments        | [Cloudflare](https://cursor.com/codebase/apps/public/cloudflare), [Netlify](https://cursor.com/codebase/apps/public/netlify), [Render](https://cursor.com/codebase/apps/public/render), [Spacelift](https://cursor.com/codebase/apps/public/spacelift-deploy-us), [Vercel](https://cursor.com/codebase/apps/public/vercel)                                                                                                                                             |
| CI                 | [Buildkite](https://cursor.com/codebase/apps/public/buildkite), [CircleCI](https://cursor.com/codebase/apps/public/circleci), [CloudBees](https://www.cloudbees.com/blog/enterprise-jenkins-now-builds-from-cursor-origin), [Depot](https://cursor.com/codebase/apps/public/depot), [EngFlow](https://cursor.com/codebase/apps/public/engflow), [Namespace](https://cursor.com/codebase/apps/public/namespacelabs), [RWX](https://cursor.com/codebase/apps/public/rwx) |
| Code review        | [CodeRabbit](https://cursor.com/codebase/apps/public/coderabbitai), [Greptile](https://cursor.com/codebase/apps/public/greptile), [Tenki](https://cursor.com/codebase/apps/public/tenki)                                                                                                                                                                                                                                                                               |
| Security           | [Artemis Security](https://cursor.com/codebase/apps/public/artemis-security), [Semgrep](https://cursor.com/codebase/apps/public/semgrep), [Socket Security](https://cursor.com/codebase/apps/public/socket-security), [Upwind](https://cursor.com/codebase/apps/public/upwind-security)                                                                                                                                                                                |
| Monitoring         | [Sentry](https://cursor.com/codebase/apps/public/sentry)                                                                                                                                                                                                                                                                                                                                                                                                               |
| Project management | [Linear](https://cursor.com/codebase/apps/public/linear)                                                                                                                                                                                                                                                                                                                                                                                                               |

The marketplace is open to submissions, so this list grows as partners [publish apps](https://cursor.com/docs/origin/apps/publish.md).

Origin apps work on **Origin-hosted repositories only**, not on repos [mirrored from GitHub](https://cursor.com/docs/origin/mirror-github.md). Mirrored repos keep their CI and integrations on GitHub.
