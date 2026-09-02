---
title: "Grok Bot for Teams and Enterprise"
source: https://cursor.com/docs/grok-bot/teams
path: /docs/grok-bot/teams
---

# Grok Bot for Teams and Enterprise

Grok Bot gives each person on your team standing Bots for everyday work: research, operations, documents, browsing, and automations. This page is for team and organization admins, for the security reviewers deciding whether Grok Bot is allowed in, and for members who want to understand the approval model they work inside. It consolidates how Grok Bot is built, what Bots can reach, the controls you can set, and the configuration Cursor recommends.

## Availability

| Plan        | Access                                                                        |
| ----------- | ----------------------------------------------------------------------------- |
| Individuals | Included with every paid Cursor plan, or through an individual SuperGrok link |
| Teams       | Included; every member has access, and usage follows the seat's allowance     |
| Enterprise  | Contact your account team to enable Grok Bot for your organization            |

[Plans and billing](https://cursor.com/help/grok-bot/plans.md) is the canonical plan and usage matrix.

## Architecture

### How Grok Bot is built

Grok Bot is a computer-use agent that operates applications, browsers, and development environments. It runs in Cursor's cloud, and each user's work executes on a dedicated cloud computer. The desktop and mobile apps are thin clients for chat, review, and approvals.

The security model rests on four principles:

- **Per-user isolation.** Each user's work runs in a dedicated Firecracker microVM, a micro virtual machine with hardware-level separation from other users.
- **No access by default.** A Bot can use only the accounts and plugins the user or team grants it.
- **Human approval gates.** Sensitive actions require user approval, evaluated by an independent review model called Auto Review.
- **Administrative control.** Team-level policies govern plugins, network egress, and delegation.

The pieces fit together like this:

1. **Local machine.** Chat, review, and approvals happen on the member's device. Work runs in the hosted computer. Optional [local execution](https://cursor.com/docs/grok-bot/teams.md#local-execution) requires per-command approval by default and can be turned off.
2. **Environment.** One persistent Firecracker microVM per user. Every Bot that user runs shares that computer. Admins manage Grok Bot from the Grok Bot page of the [Cursor dashboard](https://cursor.com/dashboard/bot): a network policy, team rules, setup scripts, an organization-wide off switch, and termination of any member's computer.
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
- **Plan for shared egress addresses.** If your company restricts services by source IP, see [static egress IPs](https://cursor.com/docs/grok-bot/teams.md#static-egress-ips).
- **Decide how members sign in to company tools** from the computer. See [identity and sign-ins](https://cursor.com/docs/grok-bot/teams.md#identity-and-sign-ins).
- **Review the policies Grok Bot inherits**: your MCP configuration, Team Rules, and Auto Review team instructions.

### Set up your team

### Enable Grok Bot for your team

Open [Grok Bot in the Cursor dashboard](https://cursor.com/dashboard/bot).
Before you enable it, a wizard walks you through privacy mode, pricing, and
model availability.

### Configure the network policy

Teams without a policy default to allow-all. See
[network policy](https://cursor.com/docs/grok-bot/teams.md#network-policy) for the modes.

### Audit your MCP allowlist

Any permitted connector is available to every Bot a member runs; see the
[connector policy](https://cursor.com/docs/grok-bot/teams.md#admin-controls) entry.

### Review the delegation and sharing defaults

Check the **Cloud Agents** and **Public template sharing** entries under
[admin controls](https://cursor.com/docs/grok-bot/teams.md#admin-controls); both ship with permissive defaults.

### Admin controls

Nearly everything sits on the Grok Bot page of the [Cursor dashboard](https://cursor.com/dashboard/bot); entries note when a control lives elsewhere.

- **Enable Grok Bot.** An organization-wide switch that enables or disables Grok Bot. Disabling blocks members; it doesn't delete member computers.
- **Network policy.** Four modes, group scope, and a lock. See [network policy](https://cursor.com/docs/grok-bot/teams.md#network-policy).
- **Cloud Agents.** Allow or block delegation to Cursor Cloud Agents. The default is on.
- **Public template sharing.** Off keeps Bot template sharing within your team, and the policy is enforced on Cursor's servers, including for existing public templates. Teams on the Enterprise plan start with public sharing off.
- **Team Rules.** Rules applied for every member's Bots. Rules are always required and can't be made optional, and you scope each rule to Cursor, Grok Bot, or both. Keep them short and few, like "never move company data to personal accounts"; for enforcement, use Auto Review instructions instead.
- **Team Setup.** Manifests of admin install scripts that run on every team computer, so your standard tooling is in place everywhere. Don't put secret values in setup scripts. To install your own networking client and reach private services, see [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md).
- **Computer management.** Organization admins can look up any member's computer, see when it was created and last active, and terminate it; team admin rights aren't enough, because a computer spans every team the member belongs to. The durable disk is kept, and the member's next session starts a fresh computer.
- **Auto Review team instructions.** Team-wide allow and block instructions that feed the reviewer's decisions for every member. These live in team settings under Security and Automation.
- **Local execution.** The policy for Bots acting on a member's own machine. See [local execution](https://cursor.com/docs/grok-bot/teams.md#local-execution).
- **Action Recording.** An Enterprise plan setting that records Bot actions and is off by default. To receive the events in your own collector, configure [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md). See [logging and audit](https://cursor.com/docs/grok-bot/teams.md#logging-and-audit).
- **Connector policy.** Grok Bot inherits your team's Cursor MCP allow and block policy in full; there is no separate Grok Bot connector list, and connectors appear as plugins in the app. Configure the policy under [MCP server trust management](https://cursor.com/docs/enterprise/model-and-integration-management.md#mcp-server-trust-management). When policy blocks a server, members see the plugin as **Disabled by team admin**. Provisioning connectors to members, whether mandatory or default-on, is not available.

## Security

Use these controls and deployment details to evaluate and limit what Bots can access, change, and retain.

### Network policy

Admins set a Grok Bot network policy for the team from the dashboard. It controls which destinations team computers can reach.

| Mode                         | Effect                                                             |
| ---------------------------- | ------------------------------------------------------------------ |
| No policy                    | Allow all (the default for teams without a policy)                 |
| Allow all network access     | Explicitly allow all destinations                                  |
| Defaults plus team allowlist | Cursor's default destinations plus your list                       |
| Team allowlist only          | Only your list, plus the destinations a computer needs to function |

- **Destinations** cover web domains as well as IP ranges with ports for raw connections, with no cap on the number of entries.
- **Groups** can set their own network policy, which replaces the team's for their members, and a lock makes the team policy effective for everyone.
- **The policy is separate from Cloud Agent network settings**, and it's applied when a computer is created or recreated. Recreate or restart a running computer to pick up a new policy.
- **Restricting egress limits where data can be sent.** Dedicated data loss prevention hooks are not available.

Blocking a plugin doesn't block that service's website. The connector policy and the network policy are separate layers, and closing both paths takes both controls.

### Static egress IPs

Hosted computers reach the internet through shared static egress IP addresses. The ranges are shared across Grok Bot customers, and dedicated per-customer IPs are not available, so treat the ranges as identifying Grok Bot traffic rather than your team alone. Current ranges are available from your account team, and the product control is the destination allowlist rather than a source IP editor.

If your company inspects TLS traffic, allow Cursor's published hostnames and bypass inspection for them; your account team can provide the current list.

### Approvals and Auto Review

Approvals keep consequential actions under the member's control. The strongest boundary is the one in the request itself, so have members state what a Bot may change and where it must stop:

> Reconcile the campaign data and draft a recommended budget change. Don't
> change the campaign or message the agency. Ask for approval after showing
> the current value, proposed value, and expected impact.

When an action needs approval, the conversation shows the proposed operation and its inputs. **Allow once** lets the Bot continue with that action, **Always allow** can save a matching rule, and **Deny** blocks it (on iPhone, the controls are **Approve once** and **Deny**). An approval controls the proposed action, not work already completed, and nobody should approve an action whose target or effect they can't identify.

Auto Review is the review layer behind those prompts: an independent review model that evaluates risky Bot actions before they run, covering shell commands, plugin calls, computer use, automation writes (changes to routines and event triggers), and delegation such as Cloud Agent and subagent launches. It can let an action proceed, require approval, or deny it.

- **Enforcement is enabled by Cursor and is currently active for all users.** Each member's own Auto Review setting remains the off switch; for security-sensitive deployments, ask members to leave it on.
- **Team instructions shape it for everyone.** Admins add team-wide block instructions for actions that are never acceptable and allow instructions for routine safe work, in team settings under Security and Automation.
- **Members can add personal rules** under **Settings** > **General** > **Auto-review**: Require Approval rules always stop matching actions, Always Allow rules let matching actions proceed only when the review finds no other reason to stop, and Require Approval wins when both match. Narrow rules around a known action and scope work best, like "require approval before sending any external email" or "always allow running `git status` in `/workspace/reports`"; avoid broad rules like "allow everything in the browser". Personal rules are stored on the current desktop and synced to its Grok Bot computer, so another desktop installation needs its own.
- **It doesn't review every side effect.** Memory writes and most settings changes are examples. Treat it as a complement to explicit boundaries and least privilege, working alongside controls that don't depend on a model's judgment: per-action approvals, the network policy, and per-user isolation.

### Identity and sign-ins

Members sign in to Grok Bot with their Cursor account, so your existing Cursor SSO configuration applies. SAML 2.0 single sign-on works with Okta, Microsoft Entra, Google Workspace, and OneLogin, SSO can be required for all members (which blocks password login), and SCIM 2.0 provisioning is available on the Enterprise plan. For step-by-step Okta and Entra ID configuration, including app assignment and sign-in rules for the computer browser, see [Configure identity and access](https://cursor.com/docs/grok-bot/identity.md).

Inside the hosted computer, members sign in to applications through your own identity provider in the browser, comparable to enrolling a new laptop. Your session policies govern those sessions, and revoking the user in your identity provider ends them.

A Bot has no identity or credentials of its own:

- **Bots act as the signed-in member.** A Bot can never hold more access than the person it belongs to, every action stays attributable to a named member, and there's no separate machine identity outside your identity provider to provision, rotate, or audit. Team-managed connectors are the one exception: they may use team or service-account credentials.
- **Connector tokens stay on Cursor's backend.** Bots invoke tools without receiving OAuth tokens, and tokens are never stored on the computer.
- **Credentials stay with the member.** For login, two-factor, and payment steps, the Bot hands the computer to the member rather than typing credentials. For supported connections, a secure secret request masks the entered value and keeps it out of the transcript and away from the model; passwords and one-time codes never belong in ordinary chat. See [Store secrets securely](https://cursor.com/help/grok-bot/secrets.md).

To revoke access quickly, terminate the member's computer from the dashboard (the durable disk is kept, and the next session starts a fresh computer) and revoke sessions in your identity provider. Application sessions persist only on the member's computer.

When a project or login should no longer be available, members clean up directly: pause or delete related routines, sign out of websites on the computer, uninstall plugins and revoke their authorization in the source service, and remove sensitive files from `/workspace`. Deleting a Bot doesn't remove computer files or browser sessions.

### Logging and audit

Audit Logs and Action Recording use separate pipelines. Audit Logs cover administrative and security events. Action Recording captures Bot actions internally, and OpenTelemetry Export sends those events to your collector when configured.

- **Audit logs on the Enterprise plan** cover admin, security, and authentication events. View them in the dashboard or stream them to your SIEM.
- **Action Recording** is an Enterprise plan setting that is off by default. When a team enables it, Cursor records Bot actions, including scrubbed shell commands, in an internal store with a 90 day retention. To receive the sanitized events in your own collector, configure [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md). Action Recording events don't appear on the Audit Log page.

### Endpoint tooling

Grok Bot doesn't ship a built-in customer-facing telemetry or EDR feed. The computers are Cursor-operated infrastructure that Cursor monitors for operational health and abuse, and that telemetry deliberately excludes customer data. Team Setup manifests let admins install their own tooling on every team computer.

### Data retention and deletion

Each member's computer keeps local files, browser sessions, and anything saved in the browser on a durable disk across sessions.

- **Idle computers hibernate automatically.** Hibernation is not deletion.
- **Image updates preserve files.** Computers on a stale system image are recreated on the fresh image with member files preserved.
- **Member resets keep synced data.** Members can reset their own computer from the desktop app. Reset keeps the synced durable data, and recent unsynced work can be lost. See [Recover Grok Bot computer data](https://cursor.com/help/grok-bot/computer-recovery.md).
- **Deletion follows the DPA.** Under the [Data Processing Agreement](https://cursor.com/terms/dpa), data is deleted or returned within 30 days of written direction after the service ends.
- **Backups run daily.** Cursor's production control plane is covered by daily encrypted backups, replicated to a separate recovery facility.

A per-organization retention policy and customer-managed point-in-time restore of an individual computer are not available.

### Data residency

Grok Bot computers run in the United States today. If your review needs a written residency commitment, contact your account team.

### Models and data

Cursor manages model selection. There is no customer-facing model picker, and the serving mix can change over time with no fixed vendor set guaranteed. Usage analytics show the model that actually served each request, including failovers, and billing follows the actual serving model.

- **The team model allowlist is honored by default, and enforcement is not guaranteed.** Onboarding presents an acknowledgement that Grok Bot may not follow the list, so treat enforcement as configuration dependent. See [model access control](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control).
- **Privacy Mode applies.** While a member is on your team, the team's privacy mode governs them, and with Privacy Mode enabled, customer data is not used for training.
- **Zero Data Retention follows Cursor's existing provider agreements.** Model providers don't keep prompts or outputs, and Grok Bot adds no separate control. Providers may run abuse and safety classifiers, and flagged data may be stored for investigation.

### Local execution

Bots can act on a member's own machine through the desktop app: run commands, read files, and move files between the cloud computer and the local machine. This is separate from work in the hosted computer, with its own control, and it's distinct from Auto Review, which governs work inside the hosted computer.

Per-command approval is the default, and the approval card shows the exact command. Members choose the policy under **Settings** > **General** > **Agent** > **Execution on Local Computer**: ask every time, always allow, or never. Recommend **Never** unless a Bot has a specific reason to work on local files. Local execution can be disabled entirely, and a team-level ceiling is enforced through settings; a dashboard control for the ceiling is not available today.

### Hosting

Grok Bot runs only on Cursor-hosted cloud computers. On-premises deployment, deployment inside your own perimeter, and bring-your-own-image deployment are not supported today, and Cursor doesn't operate a VPN, tunnel, or private link into your network for Grok Bot. The supported model is shared static egress combined with the destination allowlist. Teams on the Enterprise plan can install their own networking client on every team computer through Team Setup to reach private services; see [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md).

### Prompt injection

Content a Bot reads from the outside world, like web pages, plugin results, and command output, can try to steer it. Grok Bot layers defenses: Auto Review checks Bot actions against the member's actual request when enforcement is on, and beneath it sit controls that don't depend on any model's judgment, including the network policy, per-action approvals, and per-user isolation. Outside content is marked as untrusted data when presented to the model. These controls reduce, but don't eliminate, risk from malicious content, which is another reason to keep consequential actions behind approval.

### Certifications

Anysphere, the company behind Cursor, holds ISO/IEC 27001 and ISO/IEC 42001 certifications, issued by Schellman, and Grok Bot is included in the current ISO scope. ISO/IEC 27001 certifies the information security management system, the security program of the whole organization. ISO/IEC 42001 certifies the AI management system, how Cursor governs the AI it builds and operates. Certificates and reports are available at [trust.cursor.com](https://trust.cursor.com).

## Recommended configuration

For security-sensitive deployments, this is the recommended baseline.

For administrators:

1. **Configure the network policy.** Teams without a policy default to allow-all.
2. **Audit the team MCP allowlist before enabling Grok Bot.** Any permitted connector is available to every Bot a member runs.
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

Yes. The organization-wide switch is on the Grok Bot page of the Cursor
dashboard. Disabling blocks members without deleting their computers.

### Can I see what Bots did on behalf of my team?

Spend and usage are on the dashboard usage page, broken down by product.
Audit logs on the Enterprise plan cover admin, security, and authentication
events and can stream to your SIEM today. Action Recording is a separate
Enterprise plan setting. When enabled, it records Bot actions internally.
Configure [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md) to
receive those events in your own collector. They don't appear on the Audit
Log page.

### Can I set a Grok Bot spend cap?

A separate Grok Bot spend cap is not available today. Account-level
on-demand controls apply, and the per-product split is on the dashboard
usage page.

### Can I restrict which models Grok Bot uses?

Partially. The team model allowlist is honored by default, and enforcement
is not guaranteed; onboarding presents an acknowledgement that Grok Bot
may not follow the list. Cursor manages model selection, and there is no
customer-facing model picker. If your contract restricts subprocessors,
contact your account team.

### Why does a member see a plugin as Disabled by team admin?

Your team's MCP policy blocks that server. Enable the plugin on the team
plugins page, add its server URL to your MCP allowlist if you use one, and
have the member restart the app. If a permitted plugin still fails for
regular members with a vendor-side permission error, check the provider's
requirements; some vendors restrict their MCP endpoints to their own
administrators. See [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins.md).

### How do members request access?

Members can send a request from the app.

### Do admin controls apply per group, or only org-wide?

The network policy is group-aware: groups can set their own policy, and a
lock makes the team policy effective for everyone. The enable switch
applies to the whole organization.

### Why do some websites block Bots?

Some services flag datacenter IP addresses. The egress ranges are shared
static ranges, available from your account team; allowlist them on your
own services where appropriate.

### Why do members have to sign in to company tools again?

Sign-in sessions inside the computer can drop when the computer is
recreated, for example after an image update or a policy change. Sessions
ride your identity provider, so your session policies also apply.

## Related pages

- [Configure identity and access](https://cursor.com/docs/grok-bot/identity.md)
- [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md)
- [Work with Grok Bot](https://cursor.com/docs/grok-bot/work.md)
- [Plans and billing](https://cursor.com/help/grok-bot/plans.md)
- [Privacy and Data Governance](https://cursor.com/docs/enterprise/privacy-and-data-governance.md)

### Roll out Grok Bot with your account team

Contact our team about Enterprise plan enablement, egress ranges, residency commitments, and security review support.
