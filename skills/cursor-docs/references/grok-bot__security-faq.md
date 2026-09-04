---
title: "Grok Bot security FAQ"
source: https://cursor.com/docs/grok-bot/security-faq
path: /docs/grok-bot/security-faq
---

# Grok Bot security FAQ

These are the questions security reviews ask most often. The controls behind each answer are on [Grok Bot security](https://cursor.com/docs/grok-bot/security.md). Dashboard settings and rollout steps are on [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md).

## Isolation and access

### How are users isolated from each other?

Each user gets a dedicated Firecracker microVM with its own kernel,
memory, and virtual devices. One user cannot reach another user's
computer. Within one user, every Bot shares that computer. Treat a login
or file on the computer as available to every Bot that user runs. When a
workload needs its own computer and credential set, give it its own
Cursor user.

### What can a Bot access?

Only accounts and plugins the member or team grants. A Bot has no
identity of its own and cannot hold more access than the signed-in
member. Connector tokens stay on Cursor's backend. Login, two-factor,
and payment steps are handed to the member. See
[identity and sign-ins](https://cursor.com/docs/grok-bot/security.md#identity-and-sign-ins).

### If we block a plugin, can a Bot still reach that service in the browser?

Yes. Blocking a plugin doesn't block that service's website. The
connector policy and the [network policy](https://cursor.com/docs/grok-bot/security.md#network-policy)
are separate layers. Closing the website path takes **Network Controls**,
which is Enterprise only.

### Can admins push connectors to members?

No. The connector policy allows or blocks servers. Provisioning
connectors to members, whether mandatory or default-on, is not available.

## Network and egress

### Can we restrict which destinations computers can reach?

**Network Controls is Enterprise only.** Admins set a Grok Bot network
policy from that panel on the Grok Bot page of the dashboard. Self-serve
Teams do not see it and cannot set a destination allowlist. Teams without
a policy default to allow-all. See
[network policy](https://cursor.com/docs/grok-bot/security.md#network-policy).

### Do admin controls apply per group, or only org-wide?

Directory-group scope is part of **Network Controls**, which is Enterprise
only. Groups can set their own policy, and a lock makes the team policy
effective for everyone. The organization-wide enable switch is also
Enterprise only and applies to the whole organization. Cloud Agents, Team
Rules, and public template sharing apply to the whole team on Teams and
Enterprise.

### Why do some websites block Bots?

Some services flag datacenter IP addresses. The egress ranges are shared
static ranges, available from your account team; allowlist them on your
own services where appropriate.

### Are dedicated egress IPs available?

No. Computers use shared static egress IP addresses. Dedicated
per-customer IPs are not available. Current ranges are available from
your account team.

### Can traffic run through our own network?

Cursor doesn't operate a VPN, tunnel, or private link into your network
for Grok Bot. The supported paths are shared static egress with the
destination allowlist, and installing your own networking client through
**Team Setup**, which is Enterprise only. See
[Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md).

## Approvals, logging, and data

### What does Auto Review check?

With enforcement on, Auto Review evaluates shell commands, plugin calls,
computer use, automation writes, and delegation such as Cloud Agent and
subagent launches. It can let an action proceed, require approval, or
deny it. It doesn't review every side effect, such as memory writes and
most settings changes. Each member's own setting remains the off switch;
an organization-level lock is not available.

### Can I see what Bots did on behalf of my team?

Spend and usage are on the dashboard usage page, broken down by product.
**Audit logs are Enterprise only.** They cover admin, security, and
authentication events,     plus Grok Bot control-plane events like Bot
creation, access changes, Team Setup, and routines, filterable by application, and
can stream to your SIEM. **Action Recording is Enterprise only** and is a
separate setting, off by default. When enabled, it records Bot actions
internally. **OpenTelemetry Export is Enterprise only.** Configure it to
receive those events in your own collector, tagged
`cursor.surface=grok_bot`. They don't appear on the Audit Log page.

### Can I restrict which models Grok Bot uses?

The team model allowlist is Enterprise only, and enforcement is not
guaranteed. Onboarding presents an acknowledgement that Grok Bot may not
follow the list. Cursor manages model selection, and there is no
customer-facing model picker. If your contract restricts subprocessors,
contact your account team.

### Where do Grok Bot computers run?

In the United States today. That is not the same as Cursor's
[US-only data residency](https://cursor.com/docs/enterprise/privacy-and-data-governance.md#data-residency)
program, which does not apply to Grok Bot by default. If your review
needs a written residency commitment, contact your account team. See
[data residency](https://cursor.com/docs/grok-bot/security.md#data-residency).

### Can we run Grok Bot on-premises or from our own image?

No. Grok Bot runs only on Cursor-hosted cloud computers. On-premises
deployment, deployment inside your own perimeter, and bring-your-own-image
deployment are not supported today.

### Can we install our own security tooling on team computers?

**Team Setup is Enterprise only.** Those admins can install their own
tooling on every team computer. Grok Bot doesn't ship a built-in
customer-facing EDR feed.

### Why do members have to sign in to company tools again?

Sign-in sessions inside the computer can drop when the computer is
recreated, for example after an image update or a policy change. Sessions
ride your identity provider, so your session policies also apply.

### What happens to data when an admin terminates a computer?

Computer management is Enterprise only, and only organization admins can
terminate a member's computer. The durable disk is kept, and the member's
next session starts a fresh computer on that disk. Terminating a computer
is separate from the Enterprise only enable switch.

### What certifications apply to Grok Bot?

Anysphere holds ISO/IEC 27001 and ISO/IEC 42001 certifications, issued by
Schellman, and Grok Bot is included in the current ISO scope. Certificates
and reports are available at [trust.cursor.com](https://trust.cursor.com).

## Related pages

- [Grok Bot security](https://cursor.com/docs/grok-bot/security.md)
- [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md)
- [Configure identity and access](https://cursor.com/docs/grok-bot/identity.md)
- [Connect to private networks](https://cursor.com/docs/grok-bot/private-networks.md)
- [Privacy and Data Governance](https://cursor.com/docs/enterprise/privacy-and-data-governance.md)
