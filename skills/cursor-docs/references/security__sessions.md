---
title: "Session management"
source: https://cursor.com/docs/security/sessions
path: /docs/security/sessions
---

# Session management

A session is one sign-in to Cursor on one client: a browser, the desktop app, the CLI, or the mobile app. You can see every session on your account and end any of them. Team and organization admins can do the same for their members.

Revoking a session signs that client out. The client has to sign in again to start a new session.

## View your sessions

Open your settings in the [dashboard](https://cursor.com/dashboard) and find **Active Sessions** or **Sessions**. The list shows each active session on your account.

## Revoke a session

Revoke a session when you no longer use a device, or when you don't recognize a sign-in.

### Find the session

In the list of sessions, find the row for the client you want to sign out.

### Revoke it

Select **Revoke** on that row. If a dialog asks you to confirm, select **Revoke session**.

Revoking a session signs that client out. Your other sessions stay signed in.

## Sign out everywhere

**Sign out everywhere** ends every session on your account in one step. It signs you out of the desktop app, the CLI, the mobile app, and other browsers.

Two options change what it covers:

- **Keep this browser signed in.** Leaves your current browser session active so you can keep working in the dashboard.
- **Also revoke my personal API keys.** Revokes the API keys you created. Scripts that use a revoked key stop working.

Keys held by authorized applications and service accounts stay active. Revoke those from their own pages. See [Revoke an application's access](https://cursor.com/docs/security/oauth-applications.md#revoke-access) and [Revoke a key](https://cursor.com/docs/security/api-keys.md#revoke-a-key).

If you think your account is compromised, sign out everywhere and revoke your personal API keys in the same step. Then secure the account you sign in with. See [Compromised account](https://cursor.com/help/security-and-privacy/account-compromised.md).

## Manage member sessions

Team admins can view and revoke the sessions of team members, and organization admins can do the same for members of every team in the organization.

Member sessions appear on the **Security** page.

### View a member's sessions

### Open member sessions

On the team's **Security** page, find **Member sessions**. Organization admins find the same section on the organization's **Security** page, where they can also filter by team.

### Find the member

Search by name or email, then open the member's sessions.

Each session shows these fields:

| Field             | Meaning                                                                                                                 |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------- |
| **Client**        | The client that last used the session, such as Web, Desktop IDE, Desktop app, CLI, Mobile app, or Grok Bot.             |
| **Created**       | When the member signed in.                                                                                              |
| **Last active**   | When the session was last used. A session that started before Cursor recorded activity shows **Not tracked** or a dash. |
| **IP / location** | The address and country the session was last used from.                                                                 |
| **Expires**       | When the session ends if nothing revokes it first. Shown in its own column or when you hover **Created**.               |

### Revoke a member's session

To end one session, select **Revoke** on its row. This signs the member out of that session and leaves their other sessions in place.

To end all of a member's sessions, select **Sign out everywhere**.

A member's sessions belong to their account, not to your team, so the list and **Sign out everywhere** cover every team, every organization, and personal use.

Revoking a session doesn't remove the member or change their role. They can sign in again unless you also block the sign-in. To end access for good, deactivate the user in your identity provider so [SCIM](https://cursor.com/docs/account/teams/scim.md) removes them, or [remove them from the team](https://cursor.com/docs/account/teams/members.md).

Removing a member from a team also ends every session on their account, unless they still belong to another team in your organization. The audit log records the result in the `credentials_revoked` event. See [Authentication and membership](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#authentication-and-membership).

### Automate member sign-out

Team and organization API keys can carry two permissions for member sessions:

- **View member sign-ins.** Lists the sessions of members. See List Member Sessions in the [Admin API](https://cursor.com/docs/account/teams/admin-api.md#list-member-sessions) and the [Organization API](https://cursor.com/docs/account/organizations/organization-admin-api.md#list-member-sessions).
- **Sign members out.** Ends a member's session on one client or everywhere. See Revoke Member Sessions in the [Admin API](https://cursor.com/docs/account/teams/admin-api.md#revoke-member-sessions) and the [Organization API](https://cursor.com/docs/account/organizations/organization-admin-api.md#revoke-member-sessions).

Grant them only to keys that run offboarding or incident response. See [API keys and service tokens](https://cursor.com/docs/security/api-keys.md#permissions).

## What revoking a session doesn't do

- **It doesn't revoke API keys.** Keys keep working until they expire or someone revokes them. A member can revoke their own keys when they sign out everywhere. Admins can [revoke a member's keys](https://cursor.com/docs/security/api-keys.md#revoke-a-key) separately.
- **It doesn't end an application's access.** OAuth applications the member approved keep their access. See [Revoke an application's access](https://cursor.com/docs/security/oauth-applications.md#revoke-access).
- **It doesn't block the next sign-in.** Use your identity provider or team membership for that.

## Audit

Sign-outs and credential revocations appear in the audit log. See [Audit logs](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs).

## Related

- [API keys and service tokens](https://cursor.com/docs/security/api-keys.md)
- [SSO](https://cursor.com/docs/account/teams/sso.md) and [SCIM](https://cursor.com/docs/account/teams/scim.md)
- [Network controls](https://cursor.com/docs/security/network-controls.md)
- [Security overview](https://cursor.com/docs/security.md)
