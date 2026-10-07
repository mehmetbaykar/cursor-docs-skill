---
title: "Build an Origin App"
source: https://cursor.com/docs/origin/apps/build-app
path: /docs/origin/apps/build-app
---

# Build an Origin App

Origin is currently released in early beta. You can create repos, push and pull with git, mirror from GitHub, browse and search code, open and merge pull requests, and share with your Cursor team.

You must be a workspace admin to install the app.

## Register the app

### Generate an Ed25519 key pair

Only Ed25519 keys are accepted:

```bash
openssl genpkey -algorithm ED25519 -out origin-app-private.pem
openssl pkey -in origin-app-private.pem -pubout -out origin-app-public.pem
```

### Create the app and add the public key

In [Origin app settings](https://cursor.com/codebase/settings/apps), create the app and add the contents of `origin-app-public.pem` as a signing key. An app holds up to 10 active signing keys.

### Copy the App ID

The App ID is on the app's page. App IDs start with `app_`.

## Install the app

### Install the app on your owner

From the app's install page in the same settings, install the app on the owner that holds the repositories you clone, and select those repositories.

### Copy the installation id

The installation id is in the URL of the installation's page, `/codebase/settings/apps/installations/{installationId}`. Installation ids start with `i_`.

To read installation ids programmatically, call [List App Installations](https://cursor.com/docs/api/origin/reference/list-app-installations.md) with an app JWT as the bearer. The response includes each installation's `id`, `target.slug`, `scopes`, and `repoSelectionMode`.
