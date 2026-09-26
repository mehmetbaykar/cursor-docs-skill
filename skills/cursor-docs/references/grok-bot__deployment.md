---
title: "Deploy Grok Bot to your organization"
source: https://cursor.com/docs/grok-bot/deployment
path: /docs/grok-bot/deployment
---

# Deploy Grok Bot to your organization

Your IT team installs the Grok Bot desktop app on member devices with the tools it already uses for other software: download a versioned installer, push it, and decide when devices move to a new release. Dashboard controls for turning Grok Bot on and scoping access are on [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md), and deploying the Cursor editor is covered in [Deployment patterns](https://cursor.com/docs/enterprise/deployment-patterns.md).

## What you deploy

| Component       | Runs on                                                                         | Updated by                                                            |
| --------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Desktop app     | macOS (Apple silicon and Intel), Windows (x64 and Arm64), Linux (x64 and Arm64) | The app, or your package manager for Linux `.deb` and `.rpm` installs |
| iPhone app      | iOS 18 or later                                                                 | The App Store                                                         |
| Android app     | Android 9 or later                                                              | Google Play                                                           |
| Hosted computer | Cursor's cloud, one per member                                                  | Cursor                                                                |

The apps are clients for chat, review, and approvals. Bots do their work on the member's hosted computer. Your device management tool reaches the apps on member devices and stops there: the hosted computer runs Linux in Cursor's cloud and isn't enrolled in MDM. To put your own tooling on hosted computers, Enterprise teams use [Team Setup](https://cursor.com/docs/grok-bot/private-networks.md#install-a-networking-client-with-team-setup).

## Get the installers

- **Cursor dashboard.** The **Download Grok Bot** setup row on the [Grok Bot page](https://cursor.com/dashboard/bot) installs the app or copies a link you can share with members.
- **Download page.** [cursor.com/download/bot](https://cursor.com/download/bot) lists the current installer for every platform and format.
- **Release feed.** For scripted packaging, read the current release from the feed below and download the file it names.

| Platform | Architectures        | Formats                  |
| -------- | -------------------- | ------------------------ |
| macOS    | Apple silicon, Intel | `.dmg`                   |
| Windows  | x64, Arm64           | Setup `.exe`             |
| Linux    | x64, Arm64           | `.deb`, `.rpm`, AppImage |

### Read the current release from the feed

Each platform has a JSON feed at `https://api2.cursor.sh/updates/api/download/stable/{platform}/sand`:

| `{platform}`       | Installer            |
| ------------------ | -------------------- |
| `darwin-arm64`     | macOS, Apple silicon |
| `darwin-x64`       | macOS, Intel         |
| `win32-x64-user`   | Windows x64          |
| `win32-arm64-user` | Windows Arm64        |
| `linux-x64`        | Linux x64            |
| `linux-arm64`      | Linux Arm64          |

```bash
curl -s https://api2.cursor.sh/updates/api/download/stable/darwin-arm64/sand
```

The fields you need:

| Field              | Value                                                                      |
| ------------------ | -------------------------------------------------------------------------- |
| `version`          | The current release                                                        |
| `commitSha`        | The build the release comes from. Linux download URLs include it.          |
| `downloadUrl`      | The installer: `.dmg` on macOS, Setup `.exe` on Windows, AppImage on Linux |
| `debUrl`, `rpmUrl` | Linux only. The `.deb` and `.rpm` packages.                                |

The response can carry other fields. Installing the desktop app doesn't need them.

### Build a versioned URL

macOS and Windows installers keep a versioned URL for each release. Replace `{version}` with the release you want:

| Installer            | URL                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------ |
| macOS, Apple silicon | `https://downloads.cursor.com/grokbot/stable/darwin-arm64/{version}/Grok_Bot_{version}.dmg`      |
| macOS, Intel         | `https://downloads.cursor.com/grokbot/stable/darwin-x64/{version}/Grok_Bot_{version}_x64.dmg`    |
| Windows x64          | `https://downloads.cursor.com/grokbot/stable/win32-x64/{version}/Grok_Bot_{version}_Setup.exe`   |
| Windows Arm64        | `https://downloads.cursor.com/grokbot/stable/win32-arm64/{version}/Grok_Bot_{version}_Setup.exe` |

Linux packages sit under the release's `commitSha`, in `https://downloads.cursor.com/grokbot/stable/{commitSha}/linux/x64/` or `.../linux/arm64/`. Copy the exact file URLs from `downloadUrl`, `debUrl`, and `rpmUrl` in the Linux feed.

## Push the desktop app with your device management tool

- **macOS.** Deploy the `.dmg` with the Mac management tool you run today, such as Jamf Pro, Kandji, or Microsoft Intune.
- **Windows.** Deploy the Setup `.exe` with Intune, Configuration Manager, or another software distribution tool. Install silently with `Grok_Bot_{version}_Setup.exe /S`. The installer installs per user, into the member's profile under `%LOCALAPPDATA%\Programs`, so deploy it in user context, not as SYSTEM. Test the install on a pilot device before you push it.
- **Linux.** Install the `.deb` or `.rpm` with your configuration management tool, such as Ansible, Puppet, or Chef. Prefer these packages for managed fleets: package installs update through your package manager on your schedule. See [Linux package updates](https://cursor.com/docs/grok-bot/deployment.md#linux-package-updates).
- **iPhone.** Members install Grok Bot from the [App Store](https://apps.apple.com/app/grok-bot/id6794501026) on iOS 18 or later.
- **Android.** Members install Grok Bot from [Google Play](https://play.google.com/store/apps/details?id=ai.x.grok.bot) on Android 9 or later. To push it to managed devices, approve it in managed Google Play from Intune or another Android device management tool.

Members sign in with their Cursor account through your normal SSO flow. Grok Bot has no separate login. To assign the Cursor app in Okta or Entra ID, see [Configure identity and access](https://cursor.com/docs/grok-bot/identity.md#assign-the-cursor-app).

## Choose a version

- **Pin the version you tested.** Download that release's installer and keep it in your own software repository or MDM package store. Deploy from your copy so every new device gets the same build. Cursor doesn't publish how long older installers stay available for download, and a pinned build works only until Cursor stops supporting it. See [How desktop updates work](https://cursor.com/docs/grok-bot/deployment.md#how-desktop-updates-work).
- **Save the full Linux URL.** Linux package URLs include the release's `commitSha`, so record the URL along with the version.
- **Check what a device runs.** In the app, open the account menu and choose **About**. The dialog shows **Version**, and **Copy version info** copies the version, release track, and operating system.

### How desktop updates work

| Install                                            | How updates arrive                                                                                                                                                                                                      |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| macOS `.dmg`, Windows Setup `.exe`, Linux AppImage | The app checks for updates automatically and offers each new version to the member. **Restart to Update**, in the **Updates** section of [settings](https://cursor.com/docs/grok-bot/settings.md#updates), installs it. |
| Linux `.deb` or `.rpm`                             | The app doesn't install updates. New versions arrive through your package manager.                                                                                                                                      |

For macOS, Windows, and AppImage installs, no device policy, installer option, or dashboard setting turns off desktop app updates. Pinning decides which version you install; the app still offers newer ones afterward.

Old builds stop working. When Cursor stops supporting a build, the app covers its whole window with **Update required** until the member updates. A build loses support when it falls below Cursor's minimum version, or when it passes a maximum age and a newer release is available. This applies to every install, including Linux `.deb` and `.rpm` packages. Cursor sets both limits remotely and doesn't publish them, so plan a regular cadence for moving devices to the current release.

### Linux package updates

Installing the `.deb` adds Cursor's signed apt repository at `/etc/apt/sources.list.d/grok-bot.sources`. Installing the `.rpm` adds a signed repository at `/etc/yum.repos.d/grok-bot.repo`. Devices then pick up new Grok Bot versions whenever they run package upgrades.

To control when Linux devices move:

- **Hold the package.** Use your package manager's hold, such as `apt-mark hold grok-bot`, and release it when you're ready to upgrade.
- **Turn the repository off.** Set `Enabled: no` in `grok-bot.sources`, or `enabled=0` in `grok-bot.repo`. The package rewrites these files on every install and upgrade and keeps your choice. Then ship new versions yourself from package files you've tested.

Either way, upgrade before the installed version loses support. A held package still gets the **Update required** screen.

## Update the hosted computers

Cursor maintains the hosted computer's image, so there is no image for you to pin or supply. A computer moves to a newer image in one of three ways:

| Trigger                        | What happens                                                                                                                                                                                                       | Who starts it                                                                                               |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| New image                      | Cursor recreates idle computers on the new image in the background, gradually and without a fixed schedule. Until then, a computer stays on its current image. Member files carry over, and Team Setup runs again. | Cursor, in the background                                                                                   |
| **Update Grok Bot's Computer** | Rebuilds the member's computer on the latest image. Scheduling it for a later time isn't available to every account yet.                                                                                           | The member, from the **Updates** section of the desktop app's settings                                      |
| **Recreate VMs**               | Rebuilds the selected members' computers on the latest image and Team Setup                                                                                                                                        | Organization admins on Enterprise, from [Grok Bot Computers](https://cursor.com/docs/grok-bot/computers.md) |

Running computers pick up Team Setup manifest changes roughly once a day. To apply a change sooner, recreate the computers. On Enterprise, [audit logs](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs) record computer updates, resets, recreates, and terminations as `grok_bot_vm` events, and operations across many members as `grok_bot_vm_bulk`.

## Open the network path

Devices download installers and desktop updates from `cursor.com` and `downloads.cursor.com`, and the app connects to Cursor's API and the member's hosted computer on the domains in [Allow these domain patterns](https://cursor.com/docs/grok-bot/proxies.md#allow-these-domain-patterns). Allow all of them, including the nested `*.*.cursorvm.com` pattern, and exempt them from TLS inspection before you push the app.

## Rollout checklist

### Move off Privacy Mode (Legacy)

Privacy Mode (Legacy) blocks Grok Bot entirely. See [Before you roll
out](https://cursor.com/docs/grok-bot/teams.md#before-you-roll-out).

### Clear your network

Allow Cursor's domains on your gateway and exempt them from TLS inspection.
See [Configure TLS-inspecting proxies](https://cursor.com/docs/grok-bot/proxies.md).

### Assign the Cursor app in your identity provider

Grok Bot sign-in uses your Cursor SSO. See [Assign the Cursor
app](https://cursor.com/docs/grok-bot/identity.md#assign-the-cursor-app).

### Turn on Grok Bot and choose who gets it

On Enterprise, an admin turns Grok Bot on from the dashboard and scopes it
with **Manage Group Access**. On Teams, every member already has access.
See [Enabling Grok Bot for your
team](https://cursor.com/docs/grok-bot/teams.md#enabling-grok-bot-for-your-team).

### Apply the recommended configuration

Set the admin controls in [Recommended
configuration](https://cursor.com/docs/grok-bot/teams.md#recommended-configuration) before
members start.

### Pilot the installer

Install your chosen version on a few devices for each platform, sign in,
and confirm the app connects to the hosted computer.

### Push to your fleet

Deploy the tested installer to every device whose owner has access.

### Plan updates

Pick a cadence for moving devices to new releases. For Linux, decide
whether devices upgrade from Cursor's repository or from packages you
ship.

## FAQ

### Can I turn off automatic updates for the desktop app?

On macOS, Windows, and AppImage installs, no. The app checks for updates
and offers them to members. Linux `.deb` and `.rpm` installs don't update
themselves, so you control them with your package manager. See [How
desktop updates work](https://cursor.com/docs/grok-bot/deployment.md#how-desktop-updates-work).

### Is there an MSI or PKG installer?

The published installers are a `.dmg` for macOS, a Setup `.exe` for
Windows, and a `.deb`, `.rpm`, or AppImage for Linux. Wrap the `.dmg` or
`.exe` in your management tool's package format if it requires one.

### Does my device management tool reach the hosted computer?

No. The hosted computer runs Linux in Cursor's cloud and isn't enrolled in
MDM. Enterprise teams install their own tooling on it with [Team
Setup](https://cursor.com/docs/grok-bot/private-networks.md). If your identity provider
requires a managed device, see [Allow sign-in to IdP apps from the
computer](https://cursor.com/docs/grok-bot/identity.md#allow-sign-in-to-idp-apps-from-the-computer).

### Can I pin the hosted computer's image?

No. Cursor maintains the image and moves computers to new images in the
background. Enterprise organization admins can recreate computers at a
time they choose from [Grok Bot Computers](https://cursor.com/docs/grok-bot/computers.md).

### Can members install Grok Bot without IT?

Yes, unless your device policies block it. Members can download the app
from the dashboard link an admin shares or from
[cursor.com/download/bot](https://cursor.com/download/bot). Access still
depends on your plan and, on Enterprise, on **Manage Group Access**.

## Related pages

- [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md)
- [Configure identity and access](https://cursor.com/docs/grok-bot/identity.md)
- [Configure TLS-inspecting proxies](https://cursor.com/docs/grok-bot/proxies.md)
- [Manage Grok Bot computers](https://cursor.com/docs/grok-bot/computers.md)
- [Settings and notifications](https://cursor.com/docs/grok-bot/settings.md#updates)
- [Deployment patterns](https://cursor.com/docs/enterprise/deployment-patterns.md)

### Plan your Grok Bot rollout

Contact our team about Enterprise enablement, deployment planning, and security review support.
