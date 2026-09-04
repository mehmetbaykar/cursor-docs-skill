---
title: "Grok Bot security"
source: https://cursor.com/docs/grok-bot/security
path: /docs/grok-bot/security
---

# Grok Bot security

Use these controls and deployment details to decide whether Grok Bot is allowed in, and to limit what Bots can access, change, and retain. Rollout steps and the dashboard settings list live on [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md). Common review questions are on [Grok Bot security FAQ](https://cursor.com/docs/grok-bot/security-faq.md).

**Enterprise only** on the Grok Bot dashboard: the organization-wide enable
switch, **Network Controls**, **Team Setup**, **Action Recording**, and
computer management for organization admins. Audit logs, OpenTelemetry
Export, the MCP allowlist, and SCIM are also Enterprise only. Self-serve
Teams do not see those settings. The full list is on
[admin controls](https://cursor.com/docs/grok-bot/teams.md#admin-controls).

## Network policy

**Network Controls is Enterprise only.** Admins set a Grok Bot network policy from the [Grok Bot page](https://cursor.com/dashboard/bot) of the Cursor dashboard. It controls which destinations team computers can reach. Self-serve Teams do not see this panel and cannot set a destination allowlist. Teams without a policy default to allow-all.

| Mode                         | Effect                                                             |
| ---------------------------- | ------------------------------------------------------------------ |
| No policy                    | Allow all (the default for teams without a policy)                 |
| Allow all network access     | Explicitly allow all destinations                                  |
| Defaults plus team allowlist | Cursor's default destinations plus your list                       |
| Team allowlist only          | Only your list, plus the destinations a computer needs to function |

- **Destinations** cover web domains as well as IP ranges with ports for raw connections, with no cap on the number of entries.
- **Directory groups. Enterprise only, inside Network Controls.** Groups can set their own network policy, which replaces the team's for their members, and a lock makes the team policy effective for everyone.
- **The policy is separate from Cloud Agent network settings**, and it's applied when a computer is created or recreated. Recreate or restart a running computer to pick up a new policy.
- **Restricting egress limits where data can be sent.** Dedicated data loss prevention hooks are not available.

Blocking a plugin doesn't block that service's website. The connector policy and the network policy are separate layers, and closing both paths takes both controls.

## Static egress IPs

Hosted computers reach the internet through shared static egress IP addresses. The ranges are shared across Grok Bot customers, and dedicated per-customer IPs are not available, so treat the ranges as identifying Grok Bot traffic rather than your team alone. Current ranges are available from your account team, and the product control is the destination allowlist rather than a source IP editor.

If your company inspects TLS traffic, allow Cursor's published hostnames and bypass inspection for them; your account team can provide the current list.

**Team Setup is Enterprise only.** Those teams can install their own networking client on every team computer to reach private services. That path is separate from these shared egress ranges. See [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md).

## Approvals and Auto Review

Approvals keep consequential actions under the member's control. The strongest boundary is the one in the request itself, so have members state what a Bot may change and where it must stop:

> Reconcile the campaign data and draft a recommended budget change. Don't
> change the campaign or message the agency. Ask for approval after showing
> the current value, proposed value, and expected impact.

When an action needs approval, the conversation shows the proposed operation and its inputs. **Allow once** lets the Bot continue with that action, **Always allow** can save a matching rule, and **Deny** blocks it (on iPhone, the controls are **Approve once** and **Deny**). An approval controls the proposed action, not work already completed, and nobody should approve an action whose target or effect they can't identify.

Auto Review is the review layer behind those prompts: an independent review model that evaluates risky Bot actions before they run, covering shell commands, plugin calls, computer use, automation writes (changes to routines and event triggers), and delegation such as Cloud Agent and subagent launches. It can let an action proceed, require approval, or deny it.

- **Enforcement is enabled by Cursor and is currently active for all users.** Each member's own Auto Review setting remains the off switch; for security-sensitive deployments, ask members to leave it on. An organization-level lock is not available.
- **Team instructions shape it for everyone.** Admins add team-wide block instructions for actions that are never acceptable and allow instructions for routine safe work, in team settings under Security and Automation. Those instructions are not on the Grok Bot page.
- **Members can add personal rules** under **Settings** > **General** > **Auto-review**: Require Approval rules always stop matching actions, Always Allow rules let matching actions proceed only when the review finds no other reason to stop, and Require Approval wins when both match. Narrow rules around a known action and scope work best, like "require approval before sending any external email" or "always allow running `git status` in `/workspace/reports`"; avoid broad rules like "allow everything in the browser". Personal rules are stored on the current desktop and synced to its Grok Bot computer, so another desktop installation needs its own.
- **It doesn't review every side effect.** Memory writes and most settings changes are examples. Treat it as a complement to explicit boundaries and least privilege, working alongside controls that don't depend on a model's judgment: per-action approvals, the network policy, and per-user isolation.

## Identity and sign-ins

Members sign in to Grok Bot with their Cursor account, so your existing Cursor SSO configuration applies. SAML 2.0 single sign-on works with Okta, Microsoft Entra, Google Workspace, and OneLogin, and SSO can be required for all members (which blocks password login). **SCIM is Enterprise only:** SCIM 2.0 provisioning and deprovisioning. For step-by-step Okta and Entra ID configuration, including app assignment and sign-in rules for the computer browser, see [Configure identity and access](https://cursor.com/docs/grok-bot/identity.md).

Inside the hosted computer, members sign in to applications through your own identity provider in the browser, comparable to enrolling a new laptop. Your session policies govern those sessions, and revoking the user in your identity provider ends them.

A Bot has no identity or credentials of its own:

- **Bots act as the signed-in member.** A Bot can never hold more access than the person it belongs to, every action stays attributable to a named member, and there's no separate machine identity outside your identity provider to provision, rotate, or audit. Team-managed connectors are the one exception: they may use team or service-account credentials.
- **Connector tokens stay on Cursor's backend.** Bots invoke tools without receiving OAuth tokens, and tokens are never stored on the computer.
- **Credentials stay with the member.** For login, two-factor, and payment steps, the Bot hands the computer to the member rather than typing credentials. For supported connections, a secure secret request masks the entered value and keeps it out of the transcript and away from the model; passwords and one-time codes never belong in ordinary chat. See [Store secrets securely](https://cursor.com/help/grok-bot/secrets.md).

To revoke access quickly, an organization admin terminates the member's computer from the dashboard. That computer management control is Enterprise only. The durable disk is kept, and the next session starts a fresh computer. You also revoke sessions in your identity provider. Application sessions persist only on the member's computer.

When a project or login should no longer be available, members clean up directly: pause or delete related routines, sign out of websites on the computer, uninstall plugins and revoke their authorization in the source service, and remove sensitive files from `/workspace`. Deleting a Bot doesn't remove computer files or browser sessions.

## Logging and audit

Audit Logs and Action Recording use separate pipelines. Audit Logs cover administrative and security events, including Grok Bot control-plane actions. Action Recording captures Bot actions, and OpenTelemetry Export sends those events to your collector when configured, tagged `cursor.surface=grok_bot`.

- **Audit logs. Enterprise only.** They cover admin, security, and authentication events, plus Grok Bot control-plane events: Bot creation, member access changes, Team Setup manifests, MCP authentication, Slack account links, and routines. Filter them by application in the dashboard, or stream them to your SIEM. Self-serve Teams do not get this log.
- **Action Recording. Enterprise only.** It is a setting on the Grok Bot page, off by default. When a team enables it, Cursor records Bot actions, including scrubbed shell commands, in an internal store with a 90 day retention. Action Recording events don't appear on the Audit Log page. To receive the sanitized events in your own collector, configure [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md), which is also Enterprise only. Privacy Mode (Legacy) forces recording off.

## Endpoint tooling

Grok Bot doesn't ship a built-in customer-facing telemetry or EDR feed. The computers are Cursor-operated infrastructure that Cursor monitors for operational health and abuse, and that telemetry deliberately excludes customer data. **Team Setup is Enterprise only.** Those admins can install their own tooling on every team computer.

## Data retention and deletion

Each member's computer keeps local files, browser sessions, and anything saved in the browser on a durable disk across sessions. Connector tokens are never stored on the computer.

- **Idle computers hibernate automatically.** Hibernation is not deletion.
- **Image updates preserve files.** Computers on a stale system image are recreated on the fresh image with member files preserved.
- **Member resets keep synced data.** Members can reset their own computer from the desktop app. Reset keeps the synced durable data, and recent unsynced work can be lost. See [Recover Grok Bot computer data](https://cursor.com/help/grok-bot/computer-recovery.md).
- **Deletion follows the DPA.** Under the [Data Processing Agreement](https://cursor.com/terms/dpa), data is deleted or returned within 30 days of written direction after the service ends.
- **Backups run daily.** Cursor's production control plane is covered by daily encrypted backups, replicated to a separate recovery facility.

A per-organization retention policy and customer-managed point-in-time restore of an individual computer are not available.

## Data residency

Grok Bot computers run in the United States today. That is not the same as Cursor's [US-only data residency](https://cursor.com/docs/enterprise/privacy-and-data-governance.md#data-residency) program, which does not apply to Grok Bot by default. If your review needs a written residency commitment, contact your account team.

## Models and data

Cursor manages model selection. There is no customer-facing model picker, and the serving mix can change over time with no fixed vendor set guaranteed. Usage analytics show the model that served each request, including failovers, and billing follows the serving model.

- **The team model allowlist is Enterprise only, and enforcement is not guaranteed.** The list is honored by default. Onboarding presents an acknowledgement that Grok Bot may not follow it, so treat enforcement as configuration dependent. See [model access control](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control).
- **Privacy Mode applies.** While a member is on your team, the team's privacy mode governs them, and with Privacy Mode enabled, customer data is not used for training.
- **Zero Data Retention follows Cursor's existing provider agreements.** Model providers don't keep prompts or outputs, and Grok Bot adds no separate control. Providers may run abuse and safety classifiers, and flagged data may be stored for investigation.

## Local execution

Bots can act on a member's own machine through the desktop app: run commands, read files, and move files between the cloud computer and the local machine. This is separate from work in the hosted computer, with its own control, and it's distinct from Auto Review, which governs work inside the hosted computer.

Per-command approval is the default, and the approval card shows the exact command. Members choose the policy under **Settings** > **General** > **Agent** > **Execution on Local Computer**: ask every time, always allow, or never. Recommend **Never** unless a Bot has a specific reason to work on local files. Local execution can be disabled entirely, and a team-level ceiling is enforced through settings; a dashboard control for the ceiling is not available today.

## Hosting

Grok Bot runs only on Cursor-hosted cloud computers. On-premises deployment, deployment inside your own perimeter, and bring-your-own-image deployment are not supported today, and Cursor doesn't operate a VPN, tunnel, or private link into your network for Grok Bot. The supported model is shared static egress combined with the destination allowlist. **Team Setup is Enterprise only.** Those teams can install their own networking client on every team computer to reach private services; see [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md).

## Prompt injection

Content a Bot reads from the outside world, like web pages, plugin results, and command output, can try to steer it. Grok Bot layers defenses: Auto Review checks Bot actions against the member's request when enforcement is on, and beneath it sit controls that don't depend on any model's judgment, including the network policy, per-action approvals, and per-user isolation. Outside content is marked as untrusted data when presented to the model. These controls reduce, but don't eliminate, risk from malicious content, which is another reason to keep consequential actions behind approval.

## Certifications

Anysphere, the company behind Cursor, holds ISO/IEC 27001 and ISO/IEC 42001 certifications, issued by Schellman, and Grok Bot is included in the current ISO scope. ISO/IEC 27001 certifies the information security management system, the security program of the whole organization. ISO/IEC 42001 certifies the AI management system, how Cursor governs the AI it builds and operates. Certificates and reports are available at [trust.cursor.com](https://trust.cursor.com).

## Related pages

- [Grok Bot security FAQ](https://cursor.com/docs/grok-bot/security-faq.md)
- [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md)
- [Configure identity and access](https://cursor.com/docs/grok-bot/identity.md)
- [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md)
- [Privacy and Data Governance](https://cursor.com/docs/enterprise/privacy-and-data-governance.md)

### Review Grok Bot with your account team

Contact our team about egress ranges, residency commitments, and security review support.
