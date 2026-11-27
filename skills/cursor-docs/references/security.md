---
title: "Security overview"
source: https://cursor.com/docs/security
path: /docs/security
---

# Security overview

Cursor's access controls answer four questions: who a person is, what a credential can do, where a request comes from, and what happened afterward. Team and organization admins manage these controls from the dashboard and the APIs that back them.

Most of these controls live on the **Security** and **API Keys** pages of the organization or team [dashboard](https://cursor.com/dashboard). You need the admin role on that team or organization to change them.

## How the controls fit together

| Layer                  | What it controls                                                                                       | Where to read more                                                                                                                                                                                                 |
| :--------------------- | :----------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Identity**           | Who can sign in, and how accounts are created and removed.                                             | [SSO](https://cursor.com/docs/account/teams/sso.md), [SCIM](https://cursor.com/docs/account/teams/scim.md), [Identity and access management](https://cursor.com/docs/enterprise/identity-and-access-management.md) |
| **Credentials**        | What a script, service, or integration can do without a person present.                                | [API keys and service tokens](https://cursor.com/docs/security/api-keys.md), [Service accounts](https://cursor.com/docs/account/enterprise/service-accounts.md)                                                    |
| **Sessions**           | Where each person is signed in, and how to end that access.                                            | [Session management](https://cursor.com/docs/security/sessions.md)                                                                                                                                                 |
| **Network**            | Which addresses can reach Cursor, and which destinations agents can reach.                             | [Network controls](https://cursor.com/docs/security/network-controls.md)                                                                                                                                           |
| **OAuth Applications** | Which third-party apps can act for your users, and which of your own servers can act for your members. | [OAuth Applications](https://cursor.com/docs/security/oauth-applications.md), [Trusted issuers](https://cursor.com/docs/security/trusted-issuers.md)                                                               |
| **Audit**              | A record of security events and admin changes.                                                         | [Audit logs](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs)                                                                                                                           |

## Identity

Identity is the base layer. Connect your identity provider with [SSO](https://cursor.com/docs/account/teams/sso.md) so people sign in with accounts you control, and provision them with [SCIM](https://cursor.com/docs/account/teams/scim.md) so access ends when someone leaves. Roles decide who can change security settings. See [Members and roles](https://cursor.com/docs/account/teams/members.md).

## Credentials

A credential acts without a person present, so each one should do one job. Cursor API keys carry a set of permissions and an expiry date that you choose when you create them. Service accounts give automation its own identity that isn't tied to an employee.

Start with [API keys and service tokens](https://cursor.com/docs/security/api-keys.md).

## Sessions

Every sign-in creates a session on one client: a browser, the desktop app, the CLI, or the mobile app. Members can review and revoke their own sessions. Admins can do the same for members of their team or organization.

See [Session management](https://cursor.com/docs/security/sessions.md).

## Network

Two kinds of controls apply to network traffic, and they point in opposite directions:

- **Inbound.** The IP allowlist limits the addresses your members can sign in and call Cursor from.
- **Outbound.** Network access settings limit the destinations that agents can reach.

See [Network controls](https://cursor.com/docs/security/network-controls.md).

## OAuth Applications and trusted issuers

Software outside Cursor can act for a user within the scopes you allow.

- **OAuth Applications.** A partner or internal app sends the user to a Cursor consent page and receives tokens for the access they approve. Use one when the app serves users outside your team or organization. See [OAuth Applications](https://cursor.com/docs/security/oauth-applications.md).
- **Trusted issuers.** A server you run signs a short assertion, and Cursor exchanges it for a short-lived access token for a member of your own team or organization. An admin chooses the scopes and token lifetime, and members don't approve anything. See [Trusted issuers](https://cursor.com/docs/security/trusted-issuers.md).

## Audit

Audit logs record sign-ins, credential changes, and changes to security settings. Review them in the dashboard, pull them through the Admin API, or stream them to your SIEM. See [Audit logs](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs).

## Related

- [Security and privacy hardening](https://cursor.com/docs/enterprise/security-hardening.md) for a recommended configuration across the whole product.
- [Privacy and data governance](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) for how Cursor handles your code and data.
- [Tenancy restriction](https://cursor.com/docs/enterprise/tenancy-restriction.md) for limiting your network to approved Cursor teams.
- [Agent security](https://cursor.com/docs/agent/security.md) and [Cloud Agent security](https://cursor.com/docs/cloud-agent/security.md) for how agents are sandboxed.
