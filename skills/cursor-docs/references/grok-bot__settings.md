---
title: "Settings and notifications"
source: https://cursor.com/docs/grok-bot/settings
path: /docs/grok-bot/settings
---

# Settings and notifications

Grok Bot settings cover app-wide and desktop-local behavior. Each Bot's profile and notification preference live in its conversation details. Open settings from the account menu or with Cmd+,.

Settings sections depend on your account and rollout, so some options below
may not appear for you.

## General

- **Account.** Sign in or out of the Cursor account Grok Bot uses. The account menu also shows the installed version and a link to the iOS app.
- **Appearance.** Follow System, Light, or Dark.
- **Agent.** The time zone routines use for schedules and **Execution on Local Computer**. Cursor manages model selection, so there's no model picker.
- **Auto-review.** Your personal Auto Review rules.

Two of these settings deserve care. Execution on Local Computer controls whether Bots can run commands on the desktop in front of you; per-command approval is the default, and the setting applies to that desktop alone. Auto Review rules shape which actions stop for your approval, and they're stored on the current desktop and synced to its Grok Bot computer. Either way, don't assume another desktop installation carries the same configuration. Read [Approvals and Auto Review](https://cursor.com/docs/grok-bot/teams.md#approvals-and-auto-review) before changing either.

## Plugins

Use **Marketplace** to discover plugins and packaged skills, and **Yours** to review installed plugins and private skills. An installed plugin may still need browser authentication, and individual plugin tools can be enabled or disabled. On the Teams plan and the Enterprise plan, team-provided plugins may be required or restricted by an admin. See [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins.md).

## Usage and billing

**Usage & Billing** shows weekly included usage and on-demand usage for eligible accounts, and the account menu can show weekly usage at a glance. For how plans, weekly usage, and on-demand spend work, see [Plans and billing](https://cursor.com/help/grok-bot/plans.md).

## Team Setup

On the Teams plan and the Enterprise plan, **Team Setup** shows the managed setup your admin provides for team computers. You can review or reinstall the current setup. Admins configure it from the dashboard; see [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md#admin-controls).

## Updates

The update controls live in the **Beta** section of settings, and the Grok Bot app and the Agent Computer update separately:

- **Check for Updates** and **Restart to Update** update the desktop app.
- **Update Agent Computer** rebuilds the cloud computer on the latest image while preserving durable state.
- **Reset Agent Computer** is a last resort that returns the computer to its synced durable state; unsynced recent work doesn't come back.

See [Work with Grok Bot](https://cursor.com/docs/grok-bot/work.md#update-recover-or-reset) for the least destructive recovery order.

## Per-Bot settings

Open **View conversation details**, then **Agent settings**, to edit one Bot's name, title, description, avatar, and notifications preference. These belong to that Bot alone.

## Attention states and notifications

The sidebar distinguishes Bots that need attention (a question, approval, or handoff), unread activity (a new result), and working status. Opening a conversation marks its current activity as read, and the Bot menu can mark a conversation read or unread manually.

Turn on **Notifications** in a Bot's settings to get a system or mobile notification when that Bot finishes or needs input. Group chats don't have the same per-Bot notification switch. Notifications are suppressed while Grok Bot is focused; the sidebar and dock badge still show unread activity. On iPhone, both the device permission and the Bot's notification setting must allow the notification, and push delivery is rolling out gradually.

## In-app errors

Errors appear above the composer under **Notifications**. Some notices include **Copy request ID** for support; copy and share the complete ID with [support](https://cursor.com/help/grok-bot/get-help.md). Clearing a notice removes the notification, not the underlying action or history.

## Related pages

- [Work with Grok Bot](https://cursor.com/docs/grok-bot/work.md)
- [Plans and billing](https://cursor.com/help/grok-bot/plans.md)
- [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md)
- [Delete your Grok Bot account](https://cursor.com/help/grok-bot/delete-account.md)
