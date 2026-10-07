---
title: "Publish to the App Marketplace"
source: https://cursor.com/docs/origin/apps/publish
path: /docs/origin/apps/publish
---

# Publish to the App Marketplace

The [Origin API reference](https://cursor.com/docs/api/origin.md) covers authentication, installation, scopes, and webhooks. Send feedback to [hi@cursor.com](mailto:hi@cursor.com).

Partners build an Origin app in their own namespace, make it public, and submit it for review. Once Cursor approves it, the app is listed in the marketplace for every Origin team.

## Overview

1. Create a private Origin app in your own namespace at [cursor.com/codebase/settings/apps](https://cursor.com/codebase/settings/apps).
2. Build and test it there. Install it and walk through the [flows](https://cursor.com/docs/origin/apps/publish.md#flows) below.
3. Make the app **Public**. On your app's settings page, click **Edit App** and set the **Visibility** row to Public. Any Origin team can now install it from a direct link, but it isn't in the marketplace yet. Test that install with the same URL the marketplace uses once the app is listed:

   ```text
   https://cursor.com/codebase/apps/install?client_id=<APP_ID>&source=app-metadata&returnTo=/codebase/settings/apps
   ```

   `client_id` is the app ID (`app_01…`), not the slug.
4. Record a demo video of the [flows](https://cursor.com/docs/origin/apps/publish.md#flows) below, about 5 to 10 minutes long. Then click **Submit to marketplace** next to **Edit App** on your app's settings page.
5. After Cursor approves the app, it's **Listed** in the marketplace and you get an email.

## App visibility

Apps have three visibility settings: Private, Public, and Listed.

- **Private**: new apps start here. Only your namespace can view and install the app.
- **Public**: any Origin team can install the app from a direct link. It isn't listed in the marketplace until Cursor approves it. Public apps need at least one default scope.
- **Listed**: the public app appears in the marketplace.

Namespace admins switch an app between Private and Public in the **Visibility** row of the **Edit App** page. Set your app to Public to test it outside your namespace.

The marketplace install URL is:

```text
https://cursor.com/codebase/apps/install?client_id=<APP_ID>&source=app-metadata&returnTo=/codebase/settings/apps
```

`client_id` is the app ID (`app_01…`), not the slug. Don't add `scope` or `redirect_uri`. Those start the [partner-initiated install](https://cursor.com/docs/api/origin/reference/installation.md), not the marketplace flow. The public listing page (`/codebase/settings/apps/public/<slug>`) works only after the app is listed.

Unlisting an app or making it Private hides it from the marketplace. Existing installs keep working. Making a previously listed Private app Public again doesn't relist it. Submit it again to get it back in the marketplace.

## Submit to the marketplace

Once your app is Public, a namespace admin clicks **Submit to marketplace** next to **Edit App** on the app's settings page and provides:

- **Demo video** (required): a link to a demo video, about 5 to 10 minutes long, that covers the [flows](https://cursor.com/docs/origin/apps/publish.md#flows) below. The link must be viewable without signing in, for example an unlisted YouTube video or a public Google Drive link.
- **App description** (required): a detailed description of your app and its main flows.
- **Suggested slug** (optional): a unique identifier for your app, for example the one in its marketplace URL.
- **Suggested tags** (optional): comma-separated.

The slug and tags are suggestions. Cursor may not use them.

You get a confirmation email when you submit and another email when your app is listed. Cursor reviews every submission. Questions? Email [hi@cursor.com](mailto:hi@cursor.com).

## Approval checklist

- The app is Public and installs from the direct link.
- A demo video, about 5 to 10 minutes long, covers the required [flows](https://cursor.com/docs/origin/apps/publish.md#flows) and is viewable without signing in.
- The app description covers your app and its main flows.
- The app follows the [Origin brand guidelines](https://app.notion.com/p/3c2da74ef045815e904aece09e477803).

## Flows

Walk through these flows in your demo video, aiming for about 5 to 10 minutes. Here, a "user" means a user of your product.

### Required in every demo

**Product flows**

- Your app's main product flows, for example a CI app posting check runs or a code review app posting review comments.

**Install from Origin**

Someone installs your app from Origin and consents to your default scopes.

- Origin redirects to your first redirect URI.
- Origin and your product both show Installed.
- The install works on a personal namespace and on a team.
- The install works with all repositories and with selected repositories.

**Uninstall**

Tear the install down from either side.

- Uninstall from Origin Apps: your product shows disconnected and stops receiving webhooks. Show your product's logs or event history if this isn't visible in the UI.
- Disconnect from your product: the installation no longer appears in Origin Apps.

### Show if your app supports it

**Install from your site**

The user starts on your site, goes through Origin to pick an owner and repositories, and returns to your product.

- Your product shows Installed.

**New and existing users of your product**

During install, someone who already has an account in your product logs in, and someone new creates one.

- Existing user: they're prompted to log in, the install completes, and both sides show Installed and linked.
- New user: they land on your account creation flow, create an account, then complete the install.

**Link a repository**

Once the app is installed, the user connects Origin as the source for a project.

- Connect an existing project to an Origin repository.
- Create a new project from an Origin repository.

**Update scopes**

The app is already installed and asks for more scopes. See [Update scopes](https://cursor.com/docs/origin/apps/publish.md#update-scopes) below.

- The consent screen shows **New Permissions** and **Granted Permissions**, and the button reads **Reinstall**.
- Both sides show Installed with the new scopes.
- If the user cancels, the old scopes stay.

## Integration reference

### Update scopes

Send the workspace admin back to `https://cursor.com/codebase/apps/install` with the extra `scope`. Origin doesn't prompt them on its own. The button reads **Reinstall**. It updates the same install, and the same page can also switch between all and selected repositories.

Pass `include_granted_scopes=true` to keep what the admin already granted and ask only for the new scopes, shown as **New Permissions** and **Granted Permissions**. Without that flag, `scope=` replaces the grant. See [Installation](https://cursor.com/docs/api/origin/reference/installation.md) for every install parameter.

If nothing changed, Origin shows *No changes were made to the existing install. Redirecting to the App website.* and doesn't send `installation.updated`.

### Change repositories

**Manage** in Origin Apps changes repositories only, not scopes.

### The `installation.updated` webhook

When scopes or repositories change, Origin sends `installation.updated` to your app's webhook. You don't need to subscribe to it.

## Related

- [Origin API](https://cursor.com/docs/api/origin.md)
- [Integrations](https://cursor.com/docs/origin/integrations.md)
