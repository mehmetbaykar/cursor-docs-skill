---
title: "Grok Bot for Teams and Enterprise"
source: https://cursor.com/docs/grok-bot/teams
path: /docs/grok-bot/teams
---

# Grok Bot for Teams and Enterprise

Grok Bot gives each person on your team standing Bots for everyday work: research, operations, documents, browsing, and automations. This page is for team and organization admins rolling Grok Bot out. Security reviewers should start with [Grok Bot security](https://cursor.com/docs/grok-bot/security.md) and the [Grok Bot security FAQ](https://cursor.com/docs/grok-bot/security-faq.md). Members who want the approval model should start there too.

## Availability

| Plan        | Access                                                                        |
| ----------- | ----------------------------------------------------------------------------- |
| Individuals | Included with every paid Cursor plan, or through an individual SuperGrok link |
| Teams       | Included; every member has access, and usage follows the seat's allowance     |
| Enterprise  | Contact your account team to enable Grok Bot for your organization            |

That table is product access, not the admin control list. Grok Bot is included on Teams. Several settings are **Enterprise only** and do not appear for self-serve Teams. The [admin controls](https://cursor.com/docs/grok-bot/teams.md#admin-controls) table names each one.

[Plans and billing](https://cursor.com/help/grok-bot/plans.md) is the canonical plan and usage matrix.

## Architecture

### How Grok Bot is built

Grok Bot is a computer-use agent that operates applications, browsers, and development environments. It runs in Cursor's cloud, and each user's work executes on a dedicated cloud computer. The desktop and mobile apps are thin clients for chat, review, and approvals.

The security model rests on four principles:

- **Per-user isolation.** Each user's work runs in a dedicated Firecracker microVM, a micro virtual machine with hardware-level separation from other users.
- **No access by default.** A Bot can use only the accounts and plugins the user or team grants it.
- **Human approval gates.** Sensitive actions require user approval, evaluated by an independent review model called Auto Review.
- **Administrative control.** Team admins can set Team Rules, Cloud Agent delegation, and template sharing. Network Controls, Team Setup, Action Recording, and the organization-wide enable switch are Enterprise only.

The pieces fit together like this:

1. **Local machine.** Chat, review, and approvals happen on the member's device. Work runs in the hosted computer. Optional [local execution](https://cursor.com/docs/grok-bot/security.md#local-execution) requires per-command approval by default and can be turned off.
2. **Environment.** One persistent Firecracker microVM per user. Every Bot that user runs shares that computer. Admins manage Grok Bot from the Grok Bot page of the [Cursor dashboard](https://cursor.com/dashboard/bot). Team Rules, Cloud Agent delegation, and public template sharing are available to team admins. **Enterprise only** on that page: the organization-wide enable switch, Network Controls, Team Setup, Action Recording, and computer management for organization admins. Members never see this page.
3. **The Bot.** Shell, browser, and computer use inside the hosted computer. A Bot has no access by default and acts only with accounts the member signs it into. It hands login, two-factor authentication, and payment steps to the member.
4. **Plugins.** Your team's Cursor MCP (Model Context Protocol) policy applies in full, allowing or blocking each connector. OAuth tokens stay on Cursor's connector backend, and Bots invoke tools without receiving them.
5. **Cloud Agents.** Grok Bot can delegate coding tasks to separate computers under your existing [Cloud Agent](https://cursor.com/docs/cloud-agent.md) controls. Admins can disable spawning.
6. **Models and data.** Cursor manages model selection. With Privacy Mode enabled, customer data is not used for training; Cursor enforces this on its servers, and when the setting can't be verified, the system defaults to not training.

### How users are isolated

Each user gets a dedicated computer with hardware-level separation, and one user cannot reach another user's computer. Every computer is a Firecracker microVM with its own kernel, memory, and virtual devices.

Within one user, the boundary is different: all of that user's Bots share one computer, and Bots isolate personalities and workspaces, not compute. Treat a login or file on the computer as available to every Bot that user runs, sign the browser out of accounts a Bot no longer needs, and remove sensitive temporary files when work completes. When a workload needs its own computer and credential set, give it its own Cursor user.

## Roll out Grok Bot

### Before you roll out

- **Move off Privacy Mode (Legacy).** That setting blocks Grok Bot entirely, and you're prompted to change it before enabling. Check the privacy setting in Team Settings.
- **Plan for shared egress addresses.** If your company restricts services by source IP, see [static egress IPs](https://cursor.com/docs/grok-bot/security.md#static-egress-ips).
- **Decide how members sign in to company tools** from the computer. See [identity and sign-ins](https://cursor.com/docs/grok-bot/security.md#identity-and-sign-ins).
- **Review the policies Grok Bot inherits**: Team Rules and Auto Review team instructions, which are on Teams and Enterprise. The MCP allowlist is Enterprise only.

### Set up your team

### Open Grok Bot in the Cursor dashboard

Open [Grok Bot in the Cursor dashboard](https://cursor.com/dashboard/bot).
**Enable Grok Bot is Enterprise only.** **Enable** opens a setup modal
that covers privacy mode, pricing, and model availability. Self-serve
Teams see **Learn more** and an onboarding path, not an organization-wide
switch.

### Configure Network Controls, Enterprise only

**Network Controls** is Enterprise only. Teams without a policy default to
allow-all. See [network policy](https://cursor.com/docs/grok-bot/security.md#network-policy) for
the modes. Self-serve Teams do not see this panel.

### Audit your connector policy

Any permitted connector is available to every Bot a member runs; see the
[connector policy](https://cursor.com/docs/grok-bot/teams.md#admin-controls) entry.

### Review the delegation and sharing defaults

Check the **Cloud Agents** and **Public template sharing** entries under
[admin controls](https://cursor.com/docs/grok-bot/teams.md#admin-controls); both ship with permissive defaults.

### Admin controls

Most Grok Bot settings sit on the Grok Bot page of the [Cursor dashboard](https://cursor.com/dashboard/bot). That page is admin-only. **Enterprise only** means the control is hidden on self-serve Teams. It is not a default you can turn on later.

| Control                       | Availability                                            | Where                                                       |
| ----------------------------- | ------------------------------------------------------- | ----------------------------------------------------------- |
| Enable Grok Bot               | Enterprise only                                         | Grok Bot page                                               |
| Network Controls              | Enterprise only                                         | Grok Bot page                                               |
| Team Setup                    | Enterprise only                                         | Grok Bot page                                               |
| Action Recording              | Enterprise only                                         | Grok Bot page                                               |
| Computer management           | Enterprise only. Organization admins.                   | Grok Bot page                                               |
| Cloud Agents                  | Teams and Enterprise                                    | Grok Bot page                                               |
| Public template sharing       | Teams and Enterprise                                    | Grok Bot page                                               |
| Team Rules                    | Teams and Enterprise                                    | Grok Bot page                                               |
| Connector policy              | Teams and Enterprise. MCP allowlist is Enterprise only. | Teams Marketplace                                           |
| Auto Review team instructions | Teams and Enterprise                                    | Team Settings, Security and Automation                      |
| Audit logs                    | Enterprise only                                         | Dashboard audit log (filter by application), or SIEM stream |
| OpenTelemetry Export          | Enterprise only                                         | Team Settings                                               |
| SCIM                          | Enterprise only                                         | Identity provider                                           |

- **Enable Grok Bot. Enterprise only.** An organization-wide switch. Incomplete setup shows **Disabled** and **Enable**; after setup, the page shows **Enabled** and **Disable**. Disabling blocks members and doesn't delete member computers. Self-serve Teams do not get this switch. Their dashboard shows **Learn more**, and a first admin visit can open onboarding at `/bot/onboarding`.
- **Network Controls. Enterprise only.** Four modes, directory-group scope, and a lock. The dashboard label is **Network Controls**. Self-serve Teams have no destination allowlist. See [network policy](https://cursor.com/docs/grok-bot/security.md#network-policy).
- **Team Setup. Enterprise only.** Manifests of admin install scripts that run on every team computer, so your standard tooling is in place everywhere. Don't put secret values in setup scripts. To install your own networking client and reach private services, see [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md).
- **Action Recording. Enterprise only.** Records Bot actions and is off by default. Events do not appear on the Audit Log page; control-plane changes do, and Bot actions go to Action Recording and [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md), tagged `cursor.surface=grok_bot`. See [logging and audit](https://cursor.com/docs/grok-bot/security.md#logging-and-audit).
- **Computer management. Enterprise only.** Organization admins can look up any member's computer, see when it was created and last active, and terminate it. Team admin rights aren't enough, because a computer spans every team the member belongs to. The durable disk is kept, and the member's next session starts a fresh computer.
- **Cloud Agents. Teams and Enterprise.** Allow or block delegation to Cursor Cloud Agents. The default is on. The toggle applies to the whole team.
- **Public template sharing. Teams and Enterprise.** Off keeps Bot template sharing within your team, and the policy is enforced on Cursor's servers, including for existing public templates. Enterprise teams start with public sharing off. Other teams start with public sharing allowed. The control itself is on both plans.
- **Team Rules. Teams and Enterprise.** Rules applied for every member's Bots. Rules are always required and can't be made optional, and you scope each rule to Cursor, Grok Bot, or both. Keep them short and few, like "never move company data to personal accounts"; for enforcement, use Auto Review instructions instead.
- **Auto Review team instructions. Teams and Enterprise.** Team-wide allow and block instructions that feed the reviewer's decisions for every member. These live in team settings under Security and Automation, not on the Grok Bot page.
- **Local execution.** The policy for Bots acting on a member's own machine. See [local execution](https://cursor.com/docs/grok-bot/security.md#local-execution). A dashboard control for the team ceiling is not available on any plan.
- **Connector policy.** Grok Bot inherits your team's Cursor connector policy. There is no separate Grok Bot connector list, and connectors appear as plugins in the app. Configure marketplace require and restrict in **Teams Marketplace** (Integrations), not on the Grok Bot page. The MCP allowlist is Enterprise only. See [MCP server trust management](https://cursor.com/docs/enterprise/model-and-integration-management.md#mcp-server-trust-management). When policy blocks a server, members see the plugin as **Disabled by team admin**. Provisioning connectors to members, whether mandatory or default-on, is not available.
- **Audit logs. Enterprise only.** Admin, security, and authentication events, plus Grok Bot control-plane events: Bot creation, member access changes, Team Setup manifests, MCP authentication, Slack account links, and routines. Rows carry the application that acted and can be filtered by it. View them in the dashboard or stream them to your SIEM. Self-serve Teams do not get this log.
- **OpenTelemetry Export. Enterprise only.** The customer path for Action Recording events. Configure it under Team Settings. See [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md).
- **SCIM. Enterprise only.** SCIM 2.0 provisioning and deprovisioning. See [Configure identity and access](https://cursor.com/docs/grok-bot/identity.md).

## Security

The security model, network policy, approvals and Auto Review, identity, logging, data handling, and certifications live on [Grok Bot security](https://cursor.com/docs/grok-bot/security.md). Common review questions are on [Grok Bot security FAQ](https://cursor.com/docs/grok-bot/security-faq.md).

## Recommended configuration

For security-sensitive deployments, this is the recommended baseline.

For administrators:

1. **Configure Network Controls. Enterprise only.** Teams without a policy default to allow-all. Self-serve Teams cannot set this. See [Grok Bot security](https://cursor.com/docs/grok-bot/security.md#network-policy).
2. **Audit connector policy in Teams Marketplace before enabling Grok Bot.** Any permitted connector is available to every Bot a member runs.
3. **Ask members to keep Auto Review enforcement on.** Enforcement is enabled by Cursor and currently active for all users, and each member's own setting remains the off switch.
4. **Set an explicit local execution policy**, and decide whether Bots may act on member machines at all.
5. **Disable Cloud Agent spawning** if you don't need delegation.
6. **Keep public template sharing off** unless members should publish Bot templates outside the team.
7. **Add team block instructions** for actions that are never acceptable in your environment, and allow instructions for routine safe work. Production deployments, external email, payments, and accepting legal terms are common block examples.
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

Isolation, egress, approvals, logging, and data-handling questions are on [Grok Bot security FAQ](https://cursor.com/docs/grok-bot/security-faq.md).

## Related pages

- [Grok Bot security](https://cursor.com/docs/grok-bot/security.md)
- [Grok Bot security FAQ](https://cursor.com/docs/grok-bot/security-faq.md)
- [Configure identity and access](https://cursor.com/docs/grok-bot/identity.md)
- [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md)
- [Work with Grok Bot](https://cursor.com/docs/grok-bot/work.md)
- [Plans and billing](https://cursor.com/help/grok-bot/plans.md)
- [Privacy and Data Governance](https://cursor.com/docs/enterprise/privacy-and-data-governance.md)

### Roll out Grok Bot with your account team

Contact our team about Enterprise plan enablement, egress ranges, residency commitments, and security review support.
