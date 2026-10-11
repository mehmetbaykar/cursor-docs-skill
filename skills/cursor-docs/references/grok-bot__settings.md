---
title: "Settings and notifications"
source: https://cursor.com/docs/grok-bot/settings
path: /docs/grok-bot/settings
---

# Settings and notifications

Grok Bot settings cover app-wide and desktop-local behavior. The panes are **General**, **Computer**, **Usage & Billing**, and **Updates**. Each Bot's name, picture, and label live in its conversation details. Open settings from the account menu or with Cmd+,.

Settings sections depend on your account and rollout, so some options below
may not appear for you.

## General

- **Account.** Sign in or out of the Cursor account Grok Bot uses. The account menu also has **Get Grok Bot for mobile**, and **Support** > **About** shows the installed version.
- **Appearance.** Follow System, Light, or Dark.
- **Bot.** The time zone [routines](https://cursor.com/help/grok-bot/routines.md#how-do-schedules-and-time-zones-work) use for schedules, and your Auto-review switch and **Custom Rules**, plus any team rules your admin requires. Grok Bot manages model selection, so there's no model picker.

Auto-review rules shape which actions stop for your approval. When your admin enforces Auto-review for the team, the same table also shows locked team rules with `Required by your admin. You can't edit or delete this rule.` Members can add their own rules on top, but they only make behavior stricter; **Ask first** wins when rules conflict. If your admin turns enforcement off, you only see and use your own rules. Your personal rules are saved to your account, so the same rules apply on every desktop and on iPhone. Read [Approvals and Auto Review](https://cursor.com/docs/grok-bot/security.md#approvals-and-auto-review) before changing them.

## Computer

**Computer** has two sections. **Your computer** holds settings for the desktops signed in to your account. **Bot's computer** holds the update and reset controls for the cloud computer your Bots share; see [Updates](https://cursor.com/docs/grok-bot/settings.md#updates).

### Run commands on your desktop

**Execution on this computer** controls whether Bots can run commands on a desktop. Each listed desktop under **Your computer** has its own setting. Until a desktop is listed, the page shows **Execution on Local Computer** instead. Per-command approval is the default, and the setting applies to that desktop alone. Read [Approvals and Auto Review](https://cursor.com/docs/grok-bot/security.md#approvals-and-auto-review) before changing it.

### Route traffic through your desktop

Under **Your computer**, turn on **Route traffic through this computer** to send your Grok Bot computer's web traffic through the current desktop. The route applies to new connections. Destinations see your desktop's IP address, and the Bot can reach networks available from that device.

The setting applies to one desktop. If your Enterprise admin turns off **Allow Local Egress Routing**, the toggle turns off and locks with `Disabled by your admin. You can't turn this on.` Any active route stops within five minutes. Your choice is preserved and takes effect again if the admin re-allows local egress.

For private network options and their tradeoffs, see [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md).

## Plugins

Plugins aren't in settings. Open **Connect apps** in the sidebar to find plugins and packaged skills. Select the connected count next to the title to manage installed plugins and private skills. An installed plugin may still need browser authentication, and individual plugin tools can be enabled or disabled. On the Teams plan and the Enterprise plan, team-provided plugins may be required or restricted by an admin. See [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins.md).

## Usage and billing

**Usage & Billing** shows weekly included usage and on-demand usage for eligible accounts, and the account menu can show weekly usage at a glance. For how plans, weekly usage, and on-demand spend work, see [Plans and billing](https://cursor.com/help/grok-bot/plans.md).

## Team Setup Scripts

**Team Setup Scripts** is Enterprise only. Admins manage these scripts on the Grok Bot page of the dashboard, and they run on every member's computer. Members don't see them in settings. See [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md#admin-controls).

## Updates

The Grok Bot app and Grok Bot's computer update separately:

- **Check for Updates** and **Restart to Update**, in the **Updates** pane, update the desktop app.
- **Update Bot's Computer**, in **Settings** > **Computer** under **Bot's computer**, moves the cloud computer to the latest version. A software update only refreshes Grok Bot's software and keeps installed apps. A computer update rebuilds the computer, keeping files and logins but removing installed apps and packages. The text under **Update Bot's Computer** says which kind is waiting.
- **Reset Bot's Computer**, in the same section, is a last resort that rebuilds the computer from your last saved data, the same as Recover; if the computer can't be reached to save first, very recent changes don't come back.

See [Work with Grok Bot](https://cursor.com/docs/grok-bot/work.md#update-recover-or-reset) for the least destructive recovery order.

## Per-Bot settings

Click the Bot's name at the top of the chat (**View conversation details**) to open its details. Click the name or the label to edit it, and click the Bot's picture to change its avatar. These belong to that Bot alone. Personal Bots don't have a description; to change what a Bot does, tell it in chat. See [Change a Bot's name, picture, and what it does](https://cursor.com/help/grok-bot/edit-bot.md).

## Attention states and notifications

The sidebar distinguishes Bots that need attention (a question, approval, or handoff), unread activity (a new result), and working status. Opening a conversation marks its current activity as read, and the Bot menu can mark a conversation read or unread manually.

Turn on **Notifications** for a Bot to get a system or mobile notification when that Bot finishes or is waiting for you. On the phone, the switch is in the Bot's profile. On desktop, ask the Bot to turn its notifications on or off. Group chats don't have the same per-Bot notification switch. Notifications are suppressed while Grok Bot is focused; the sidebar and dock badge still show unread activity. On iPhone, both the device permission and the Bot's notification setting must allow the notification, and push delivery is rolling out gradually.

## In-app errors

Errors appear above the composer under **Notifications**. Some notices include **Copy request ID** for support; copy and share the complete ID with [support](https://cursor.com/help/grok-bot/get-help.md). Clearing a notice removes the notification, not the underlying action or history.

## Related pages

- [Work with Grok Bot](https://cursor.com/docs/grok-bot/work.md)
- [Plans and billing](https://cursor.com/help/grok-bot/plans.md)
- [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md)
- [Grok Bot security](https://cursor.com/docs/grok-bot/security.md)
- [Delete your Grok Bot account](https://cursor.com/help/grok-bot/delete-account.md)
