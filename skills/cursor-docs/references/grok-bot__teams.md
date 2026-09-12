---
title: "Grok Bot for Teams and Enterprise"
source: https://cursor.com/docs/grok-bot/teams
path: /docs/grok-bot/teams
---

# Grok Bot for Teams and Enterprise

Grok Bot gives each person on your team standing Bots for everyday work: research, operations, documents, browsing, and automations. This page is for team and organization admins rolling Grok Bot out. Security reviewers should start with [Grok Bot security](https://cursor.com/docs/grok-bot/security.md) and the [Grok Bot security FAQ](https://cursor.com/docs/grok-bot/security-faq.md). Members who want the approval model should start there too.

## Availability

| Plan        | Access                                                                                |
| ----------- | ------------------------------------------------------------------------------------- |
| Individuals | Included with every paid Cursor plan, or through an individual SuperGrok link         |
| Teams       | Included; every member has access, and usage follows the seat's allowance             |
| Enterprise  | Enable Grok Bot for your team from [your dashboard](https://cursor.com/dashboard/bot) |

That table is product access, not the admin control list. Grok Bot is included on Teams. Several settings are **Enterprise only** and do not appear for self-serve Teams. [Admin controls](https://cursor.com/docs/grok-bot/teams.md#admin-controls) marks each one.

[Plans and billing](https://cursor.com/help/grok-bot/plans.md) is the canonical plan and usage matrix.

## Enabling Grok Bot for your team

On the Teams plan, Grok Bot is enabled by default, and every member has access without any admin action. It stays off for teams on [Privacy Mode (Legacy)](https://cursor.com/docs/grok-bot/teams.md#before-you-roll-out) or on a [legacy request-based plan](https://cursor.com/docs/models-and-pricing.md#legacy-request-based-pricing). There is no switch to turn it off.

On the Enterprise plan, an admin turns it on from [Grok Bot in the Cursor dashboard](https://cursor.com/dashboard/bot). Once enabled, you can give access to all team members or limit it to specific [groups](https://cursor.com/dashboard/members?subtab=groups) with "Manage Group Access". Turning Grok Bot off blocks every member without deleting their computers.

Admins on either plan can bring members in with "Invite Team" on the Grok Bot page. Existing Cursor users on your team get an email with a download link. New users get an invitation to your Cursor team, by email or invite link, that also points them to Grok Bot. Teams that manage membership through SCIM see only the existing-users option.

## Before you roll out

- **Move off Privacy Mode (Legacy).** That setting blocks Grok Bot entirely, and you're prompted to change it before enabling. Check the privacy setting in Team Settings.
- **Plan for shared egress addresses.** If your company restricts services by source IP, see [static egress IPs](https://cursor.com/docs/grok-bot/security.md#static-egress-ips).
- **Clear your gateway.** If member devices sit behind Zscaler or another TLS-inspecting proxy, allow Cursor's domains, including the nested `*.*.cursorvm.com` pattern, and exempt them from inspection before members connect. See [Configure TLS-inspecting proxies](https://cursor.com/docs/grok-bot/proxies.md).
- **Decide how members sign in to company tools** from the computer. See [identity and sign-ins](https://cursor.com/docs/grok-bot/security.md#identity-and-sign-ins).
- **Review the policies Grok Bot inherits**: Team Rules and the connector policy on every plan, plus team Auto-review rules and the MCP allowlist on Enterprise.

## Architecture

### How Grok Bot is built

Grok Bot is a computer-use agent that operates applications, browsers, and development environments. It runs in Cursor's cloud, and each user's work executes on a dedicated cloud computer. The desktop and mobile apps are thin clients for chat, review, and approvals.

The security model rests on four principles:

- **Per-user isolation.** Each user's work runs in a dedicated Firecracker microVM, a micro virtual machine with hardware-level separation from other users.
- **No access by default.** A Bot can use only the accounts and plugins the user or team grants it.
- **Human approval gates.** Sensitive actions require user approval, evaluated by an independent review model called Auto Review.
- **Administrative control.** Team admins can set Team Rules, Cloud Agent delegation, template sharing, and the local execution ceiling. Network Controls, Team Setup, Action Recording, Enforce Auto-review, Auto-review rules, and the organization-wide enable switch are Enterprise only.

The pieces fit together like this:

1. **Local machine.** Chat, review, and approvals happen on the member's device. Work runs in the hosted computer. Optional [local execution](https://cursor.com/docs/grok-bot/security.md#local-execution) requires per-command approval by default and can be turned off.
2. **Environment.** One persistent Firecracker microVM per user. Every Bot that user runs shares that computer. Admins manage Grok Bot from the Grok Bot page of the [Cursor dashboard](https://cursor.com/dashboard/bot). Team Rules, Cloud Agent delegation, public template sharing, and Execution on Local Computer are available to team admins. **Enterprise only** on that page: the organization-wide enable switch, Network Controls, Team Setup, Action Recording, Enforce Auto-review, Auto-review rules, and computer management for organization admins. Members never see this page.
3. **The Bot.** Shell, browser, and computer use inside the hosted computer. A Bot has no access by default and acts only with accounts the member signs it into. It hands login, two-factor authentication, and payment steps to the member.
4. **Plugins.** Your team's Cursor MCP (Model Context Protocol) policy applies in full, allowing or blocking each connector. OAuth tokens stay on Cursor's connector backend, and Bots invoke tools without receiving them.
5. **Cloud Agents.** Grok Bot can delegate coding tasks to separate computers under your existing [Cloud Agent](https://cursor.com/docs/cloud-agent.md) controls. Admins can disable spawning.
6. **Models and data.** Cursor manages model selection. With Privacy Mode enabled, customer data is not used for training; Cursor enforces this on its servers, and when the setting can't be verified, the system defaults to not training.

### How users are isolated

Each user gets a dedicated computer with hardware-level separation, and one user cannot reach another user's computer. Every computer is a Firecracker microVM with its own kernel, memory, and virtual devices.

Within one user, the boundary is different: all of that user's Bots share one computer, and Bots isolate personalities and workspaces, not compute. Treat a login or file on the computer as available to every Bot that user runs, sign the browser out of accounts a Bot no longer needs, and remove sensitive temporary files when work completes. When a workload needs its own computer and credential set, give it its own Cursor user.

## Admin controls

Most Grok Bot settings sit on the Grok Bot page of the [Cursor dashboard](https://cursor.com/dashboard/bot), which only admins see. A few live in Team Settings, your Team Marketplace, or your identity provider. Several controls are available only on the [Enterprise plan](https://cursor.com/docs/enterprise.md); the rest are available on Teams and Enterprise.

### Access and identity

Who can use Grok Bot, and how members are provisioned.

#### Enable Grok Bot

The organization-wide switch on the Grok Bot page, with **Manage Group Access** beside it. Turning it on opens a setup modal that covers privacy mode, pricing, and model availability. Turning it off blocks every member without deleting their computers. See [Enabling Grok Bot for your team](https://cursor.com/docs/grok-bot/teams.md#enabling-grok-bot-for-your-team).

*Available on the [Enterprise plan](https://cursor.com/docs/enterprise.md).*

#### SCIM

SCIM 2.0 provisioning and deprovisioning through your identity provider. Members sign in to Grok Bot with their Cursor account, so your existing [SCIM](https://cursor.com/docs/account/teams/scim.md) and SSO setup carries over. For Okta and Entra ID steps, including app assignment and sign-in rules for the computer browser, see [Configure identity and access](https://cursor.com/docs/grok-bot/identity.md).

*Available on the [Enterprise plan](https://cursor.com/docs/enterprise.md).*

### Agent capabilities

What Bots may do on behalf of members. Each control applies to every member's Bots.

#### Cloud Agents

Allows or blocks Bots delegating coding tasks to Cursor [Cloud Agents](https://cursor.com/docs/cloud-agent.md). The switch is on the Grok Bot page, applies to the whole team, and is on by default. Delegated work runs on separate computers under your existing Cloud Agent controls. Turn it off when your team doesn't need delegation.

#### Public template sharing

Controls whether members can publish Bot templates outside your team. Off keeps sharing team-only, and Cursor enforces the policy on its servers, including for templates that are already public. Enterprise teams start with public sharing off; other teams start with it allowed. For what a shared template contains, see [Share a Bot](https://cursor.com/docs/grok-bot/work.md#share-a-bot).

#### Connector policy

Grok Bot inherits your team's Cursor connector policy. There is no separate Grok Bot connector list, and connectors appear as plugins in the app. Set which servers members can use from your Team Marketplace on the dashboard's [Plugins page](https://cursor.com/dashboard/plugins), not on the Grok Bot page. The MCP allowlist is Enterprise only; see [MCP server trust management](https://cursor.com/docs/enterprise/model-and-integration-management.md#mcp-server-trust-management). Any permitted connector is available to every Bot a member runs, and a blocked one shows as **Disabled by team admin**. Pushing connectors to members, whether mandatory or default-on, is not available.

#### Execution on Local Computer

Caps what Bots may do on a member's own machine through the desktop app: open files and run tasks. Pick **Always allow**, **Ask every time**, or **Never allow** on the Grok Bot page. **Always allow**, the default, leaves the choice to each member, whose own setting defaults to asking before every task. **Ask every time** makes every local task ask for approval, and **Never allow** turns local execution off for the whole team. A member's own setting still applies when it is stricter than the team's. Pick **Never allow** unless Bots have a specific reason to work on member machines. See [local execution](https://cursor.com/docs/grok-bot/security.md#local-execution).

### Rules and approvals

Guidance Bots follow, and the review layer that stops actions.

#### Team Rules

Rules that every member's Bots follow. Add them from the Grok Bot page and scope each rule to Cursor, Grok Bot, or both. Rules applied to Grok Bot are always required, so members can't turn them off. Keep them short and few, like "never move company data to personal accounts." Rules guide a Bot; for approval behavior, use [Auto-review rules](https://cursor.com/docs/grok-bot/teams.md#auto-review-rules).

#### Enforce Auto-review

Prevents members from turning Auto-review off. The switch is on the Grok Bot page and is off by default. When it is on, Bots always check risky actions before running them and ask for approval when needed. Turn it on before you rely on team Auto-review rules.

*Available on the [Enterprise plan](https://cursor.com/docs/enterprise.md).*

#### Auto-review rules

Team-wide "Ask first" and "Allow automatically" rules that apply to every member's Bots on top of their own rules. Add them with "Configure Rules" on the Grok Bot page; changes save automatically. Members see the team rules under "Settings" > "General" > "Auto-review" but can't edit or delete them, and "Ask first" wins when rules conflict. Turning enforcement off stops applying the team rules. See [approvals and Auto Review](https://cursor.com/docs/grok-bot/security.md#approvals-and-auto-review).

*Available on the [Enterprise plan](https://cursor.com/docs/enterprise.md).*

### Computers and network

How team computers are set up, what they can reach, and how you recreate or terminate them.

#### Network Controls

Restricts which destinations team computers can reach. Pick one of four modes, from allow-all to a team allowlist of domains and IP ranges. Directory groups can carry their own policy, and a lock makes the team policy apply to everyone. Teams without a policy default to allow-all. See [network policy](https://cursor.com/docs/grok-bot/security.md#network-policy) for the modes and how a new policy reaches running computers.

*Available on the [Enterprise plan](https://cursor.com/docs/enterprise.md).*

#### Team Setup

Manifests of install scripts that run on every team computer, so the same tooling is present everywhere. Keep secret values out of setup scripts. Members see the managed setup under **Team Setup** in the app, where they can review or reinstall it. For how manifests run, and to install a networking client that reaches private services, see [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md).

*Available on the [Enterprise plan](https://cursor.com/docs/enterprise.md).*

#### Grok Bot Computers

Lets organization admins recreate or terminate the computers of many members at once, with a result for each member. Team admin rights aren't enough, because one computer spans every team the member belongs to. Recreate moves members to the latest image and Team Setup while keeping their Bots, files, and logins. Terminate ends the member's current work and keeps the durable disk; the member's next session starts a fresh computer on it. Neither action removes access: to do that, remove the member from the team or turn off Grok Bot for their group, and revoke their sessions in your identity provider. See [Manage Grok Bot computers](https://cursor.com/docs/grok-bot/computers.md).

*Available on the [Enterprise plan](https://cursor.com/docs/enterprise.md).*

### Logging and audit

What gets recorded, and where it goes.

#### Action Recording

Records Bot actions, including scrubbed shell commands. The switch is on the Grok Bot page and is off by default. Recorded events don't appear on the Audit Log page. To receive them in your own collector, configure [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md), which delivers each event tagged `cursor.surface=grok_bot`. Retention details are on [logging and audit](https://cursor.com/docs/grok-bot/security.md#logging-and-audit).

*Available on the [Enterprise plan](https://cursor.com/docs/enterprise.md).*

#### Audit logs

Admin, security, and authentication events, plus Grok Bot control-plane events: Bot creation, member access changes, Team Setup manifests, MCP authentication, Slack account links, and routines. Each row names the application that acted, so you can filter the log to Grok Bot. View them on the [Audit Log page](https://cursor.com/dashboard/audit-log) or stream them to your SIEM; see [audit logs](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs). For the actions Bots took, use [Action Recording](https://cursor.com/docs/grok-bot/teams.md#action-recording).

*Available on the [Enterprise plan](https://cursor.com/docs/enterprise.md).*

#### OpenTelemetry Export

Streams Cursor usage metrics and logs, including recorded Grok Bot actions, to a collector you run. It's the customer path for Action Recording events. Configure it under **Team Settings** > **OpenTelemetry Export**. Endpoint requirements and the event schema are on [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md).

*Available on the [Enterprise plan](https://cursor.com/docs/enterprise.md).*

## Security

The security model, network policy, approvals and Auto Review, identity, logging, data handling, and certifications live on [Grok Bot security](https://cursor.com/docs/grok-bot/security.md). Common review questions are on [Grok Bot security FAQ](https://cursor.com/docs/grok-bot/security-faq.md).

## Recommended configuration

For security-sensitive deployments, this is the recommended baseline.

For administrators:

1. **Configure Network Controls. Enterprise only.** Teams without a policy default to allow-all. Self-serve Teams cannot set this. See [Grok Bot security](https://cursor.com/docs/grok-bot/security.md#network-policy).
2. **Audit connector policy in Teams Marketplace before enabling Grok Bot.** Any permitted connector is available to every Bot a member runs.
3. **Turn on Enforce Auto-review before you rely on team rules. Enterprise only.** Members can add stricter personal rules on top, and "Ask first" wins when rules conflict.
4. **Set Execution on Local Computer to Never allow** unless Bots need to act on member machines. The default leaves the choice to each member.
5. **Disable Cloud Agent spawning** if you don't need delegation.
6. **Keep public template sharing off** unless members should publish Bot templates outside the team.
7. **Add team Auto-review rules. Enterprise only.** Cover actions that should always ask first or can proceed automatically. Production deployments, external email, payments, and accepting legal terms are good "Ask first" examples. Keep automatic rules narrow.
8. **Gate sign-in to managed devices through your identity provider.** Grok Bot sign-in uses your SSO, so a device-aware sign-in policy applies to it. This gates sign-in, not the hosted computer itself.

For members:

1. **Never paste credentials into chat.** The masked secret request is the supported path.
2. **Prefer Allow once over Always allow** for actions that touch accounts, money, or shared resources.
3. **Sign the Bot's browser into accounts sized to the task**, and sign it out of accounts it no longer needs. Use scoped service accounts where the source system supports them.
4. **Start new roles with read-only tasks and draft outputs**, and keep sending, publishing, purchasing, deletion, and production changes behind approval.
5. **Review installed plugins and active routines regularly**, and pause a routine when its source system changes.

## FAQ

### Can I turn Grok Bot on or off for my team?

The organization-wide **Enable Grok Bot** switch is Enterprise only. It
lives on the Grok Bot page of the Cursor dashboard. Self-serve Teams do
not get this switch. Disabling blocks members without deleting their
computers.

### Can I set a Grok Bot spend cap?

A separate Grok Bot spend cap is not available today. Account-level
on-demand controls apply, and the per-product split is on the dashboard
usage page.

### Why does a member see a plugin as Disabled by team admin?

Your team's connector policy blocks that server. Enable it in **Teams
Marketplace**, add its server URL to your MCP allowlist if you use one,
and have the member restart the app. If a permitted plugin still fails
for regular members with a vendor-side permission error, check the
provider's requirements; some vendors restrict their MCP endpoints to
their own administrators. See [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins.md).

### How do members request access?

Members can send a request from the app. On a pooled Enterprise team
whose admin has not finished setup, members see a team-setup message
instead. The next step is for an admin to use the Enterprise only enable
switch. Self-serve Teams do not use that switch.

### Can I see what kind of work my team does with Grok Bot?

Yes, on Enterprise teams where it has rolled out. The Conversation
Insights page of the Analytics dashboard has a **Grok Bot** source that
groups Bot conversations by Type of Work and Level of Automation. See
[Grok Bot Conversation Insights](https://cursor.com/docs/account/teams/analytics.md#grok-bot-conversation-insights).

Isolation, egress, approvals, logging, and data-handling questions are on [Grok Bot security FAQ](https://cursor.com/docs/grok-bot/security-faq.md).

## Related pages

- [Grok Bot security](https://cursor.com/docs/grok-bot/security.md)
- [Grok Bot security FAQ](https://cursor.com/docs/grok-bot/security-faq.md)
- [Configure identity and access](https://cursor.com/docs/grok-bot/identity.md)
- [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md)
- [Configure TLS-inspecting proxies](https://cursor.com/docs/grok-bot/proxies.md)
- [Manage Grok Bot computers](https://cursor.com/docs/grok-bot/computers.md)
- [Work with Grok Bot](https://cursor.com/docs/grok-bot/work.md)
- [Grok Bot Conversation Insights](https://cursor.com/docs/account/teams/analytics.md#grok-bot-conversation-insights)
- [Plans and billing](https://cursor.com/help/grok-bot/plans.md)
- [Privacy and Data Governance](https://cursor.com/docs/enterprise/privacy-and-data-governance.md)

### Roll out Grok Bot with your account team

Contact our team about Enterprise plan enablement, egress ranges, residency commitments, and security review support.
