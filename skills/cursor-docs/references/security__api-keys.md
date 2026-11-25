---
title: "API keys and service tokens"
source: https://cursor.com/docs/security/api-keys
path: /docs/security/api-keys
---

# API keys and service tokens

A Cursor API key authenticates a script, service, or integration to Cursor's APIs. Each key has an owner, a set of permissions, and an expiry date. A key can do only what its permissions allow, and never more than its owner can.

For endpoints, authentication headers, and rate limits, see the [Cursor APIs overview](https://cursor.com/docs/api.md).

## Key owners

The owner decides whose access a key uses and who can manage it.

| Owner               | Who creates it             | Acts as                                                                             | Use it for                                                             |
| :------------------ | :------------------------- | :---------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **Personal**        | Any member, for themselves | The member                                                                          | Your own scripts, the Cursor CLI, and the SDK                          |
| **Team**            | Team admins                | The team                                                                            | Admin API automation, reporting, and team-owned Cloud Agents           |
| **Organization**    | Organization admins        | The organization                                                                    | Automation that spans every team in the organization                   |
| **Service account** | Team admins, on Enterprise | A [service account](https://cursor.com/docs/account/enterprise/service-accounts.md) | CI pipelines and shared automation that shouldn't depend on one person |

A team key belongs to the team, not to the admin who created it. It keeps working after that person leaves, until it expires or an admin revokes it.

## Permissions

You choose a key's permissions when you create it. The permissions offered depend on the owner.

| Owner               | Permission areas                                                                                                                                                      |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Personal**        | Run agents. Sign in to the Cursor CLI and SDK.                                                                                                                        |
| **Team**            | Members, member sign-ins, usage and spend, groups, analytics, audit logs, settings, repositories, Bugbot, security findings, automations, Cloud Agents, and Grok Bot. |
| **Organization**    | Members, member sign-ins, groups, usage, audit logs, and models.                                                                                                      |
| **Service account** | Team permission areas, except automations. **Run Cloud Agents** is selected by default. You can also limit the repositories the key can reach.                        |

A key with permissions you select is a fine-grained key. See [Fine-grained and legacy keys](https://cursor.com/docs/security/api-keys.md#fine-grained-and-legacy-keys).

Most areas split into a view permission and a manage permission. A manage permission doesn't include its view permission. Select both when a key needs to list and change the same things.

A few permissions grant more than one route:

- **Run Cloud Agents.** Launches and manages Cloud Agents as the team. Usage is billed to the team.
- **Sign in to the Cursor CLI and SDK.** Lets the CLI and SDK sign in as you with the key. They get the same access as a CLI login.
- **Sign members out.** Ends a member's session on one client or everywhere. See [Session management](https://cursor.com/docs/security/sessions.md#automate-member-sign-out).

API reference pages name the scope each route requires. See the [Admin API](https://cursor.com/docs/account/teams/admin-api.md) and the [Organization API](https://cursor.com/docs/account/organizations/organization-admin-api.md#scopes).

## Fine-grained and legacy keys

Cursor has two types of API key.

A fine-grained key carries only the permissions you select when you create it. Use fine-grained keys for new work.

A legacy key is an older key without custom permissions. It keeps working until it expires or someone revokes it.

|            | Fine-grained key                          | Legacy key                                                                                                                            |
| :--------- | :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| **Access** | Only the permissions selected for the key | A personal key isn't limited to selected permissions. A team or organization key carries a broad scope, such as `read:*` or `admin:*` |
| **Rotate** | **Rotate key** replaces the secret        | Can't be rotated. Create a new key                                                                                                    |
| **Revoke** | **Delete key**                            | **Delete API Key** or **Revoke key**                                                                                                  |

The dashboard labels each type:

- On the **Team** tab, team keys with selected permissions are listed under **Fine-grained API Keys**. Older team keys are listed under **Legacy API Keys**.
- Under **Type**, a legacy key shows **Cursor (legacy)**.
- On the **Members** tab, a legacy personal key shows **Full access**.

Where to create a fine-grained key:

- **Personal and team keys.** Use **New API Key** on the **User** or **Team** tab, or **Create API key**. A personal or team key made with **Create API key** is always fine-grained.
- **Organization keys.** Create them on the organization's API keys page. The **Org** tab creates legacy organization keys with one scope.

To replace a legacy key, create a fine-grained key with the permissions the integration needs. Update the integration, then revoke the legacy key.

## Create a key

Keys are created in the dashboard. There is no API for creating a team or personal key.

### Open the API Keys page

Go to the **API Keys** page of the [dashboard](https://cursor.com/dashboard).

### Choose the owner and start a key

Pick the **User**, **Team**, or **Org** tab, then select **New API Key**. Or select **Create API key**, then turn on **Team key** for a key the team owns and its admins can revoke. Leave it off for a personal key.

### Set the name, expiry, and permissions

Give the key a name that says what uses it. Pick an expiry under **Expires**, then select its **Permissions**.

### Store the secret

The secret is shown once after the key is created. Copy it into your secret manager before you close the dialog.

Cursor asks you to sign in again if your sign-in is too old to create or change a key.

To create a key for a service account, see [Service accounts](https://cursor.com/docs/account/enterprise/service-accounts.md#creating-a-service-account).

## Expiry

Choose an expiry when you create a key: 30 days, 90 days, 180 days, 1 year, or never. The dashboard recommends 180 days.

An expired key fails authentication. It stays in the list so you can see what it was used for. Create a new key to replace it.

Choose **Never expires** only for a key that you rotate on your own schedule.

## Rotate a key

Rotating a key replaces its secret and keeps its name and permissions.

To rotate a key, open its menu on the API Keys page and select **Rotate key**. The new secret is shown once.

The old secret stops working, so have the new secret ready to deploy before you rotate. To run old and new side by side, create a second key, move your systems to it, then revoke the first.

OAuth application client secrets can rotate with a 24-hour overlap. See [Manage an application](https://cursor.com/docs/security/oauth-applications.md#manage-an-application).

Older keys without custom permissions can't be rotated. Create a new key to replace one.

A service account key rotates from the service account's row, with **Rotate API key**. See [Rotating an API key](https://cursor.com/docs/account/enterprise/service-accounts.md#rotating-an-api-key).

## Revoke a key

To revoke a key, open its menu on the API Keys page and select **Delete key**. Requests that use a deleted key fail. On older keys without custom permissions, the action is **Delete API Key** or **Revoke key**.

Admins can also act on keys they didn't create:

- **Members' personal keys.** On Enterprise teams, admins can list the personal keys of members on the team's verified domains and revoke any of them. See [Review members' API keys](https://cursor.com/docs/account/teams/members.md#review-members-api-keys).
- **Keys from former members.** The API Keys page lists keys and service accounts created by people who have left the team. Review or revoke them there.
- **All of your own keys.** When you [sign out everywhere](https://cursor.com/docs/security/sessions.md#sign-out-everywhere), you can also revoke every personal key you created.

Team admins can turn off **Allow personal API key creation** for the team. While it's off, members can't create or rotate personal keys. Existing keys keep working until they're revoked. See [Review members' API keys](https://cursor.com/docs/account/teams/members.md#review-members-api-keys).

## Review key activity

### Last used

The API Keys page shows when each key was last used, under **Last used**. It appears in three places:

- The list of your keys and team keys.
- The **Members** list of members' personal keys.
- The service accounts table.

A dash or an empty cell means no use has been recorded for the key.

**Last used** is available on every plan. Reviewing members' personal keys requires an Enterprise plan. See [Review members' API keys](https://cursor.com/docs/account/teams/members.md#review-members-api-keys).

### View audit logs

To see what one key did, open the menu on its row and select **View audit logs**. The audit log opens filtered to that key. Remove the filter to see every event again.

The action is on key rows and on service account rows. A service account with more than one key has one **View audit logs** action for each key.

**View audit logs** appears for admins who can view the audit log, which requires an Enterprise plan. The link is for API keys only. Sessions don't have one.

For the events keys produce, see [API keys and service accounts](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#api-keys-and-service-accounts).

## Service tokens

A service token is the same kind of credential as an API key. It has an owner and a set of permissions, and it can do only what those permissions allow, never more than its owner can. You don't create a service token yourself. Cursor issues it automatically in exchange for another credential, and it expires much sooner than a key.

Cursor issues service tokens in two ways:

| Issued through                                                               | Acts as                                                                                                                                                                                                          | Lifetime                                                            |
| :--------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| [OAuth Applications](https://cursor.com/docs/security/oauth-applications.md) | The user who approved the application, with the scopes they approved                                                                                                                                             | 1 hour. The application gets the next token with its refresh token. |
| Delegated tokens                                                             | One active team member, when a service account key calls `POST /v1/sub-tokens`. See [Create a user-scoped worker token](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-a-user-scoped-worker-token). | 1 hour                                                              |

Service tokens follow the same rules as API keys:

- **Permissions.** Tokens use the same permissions as keys. A token from an OAuth application holds only the scopes the user approved. A delegated token holds only what its service account key allows.
- **Team policy.** An enforced [IP allowlist](https://cursor.com/docs/security/network-controls.md#ip-allowlist) covers API requests made with a token, as it covers requests made with a key. While a team has **Allow personal API key creation** turned off, OAuth applications can't get tokens for that team.

Two things work differently, because Cursor issues the token and you don't:

- **Tokens aren't listed.** The API Keys page lists keys, not service tokens. A token has no row there, so it has no **Last used** date and no **View audit logs** action.
- **You revoke a token where it was issued.** You can't delete a single token from the dashboard. Revoke what issued it instead:
  - **OAuth Applications.** The application revokes its own tokens. To end every token an application holds, select **Disable application** or **Delete application**. See [Manage an application](https://cursor.com/docs/security/oauth-applications.md#manage-an-application).
  - **Delegated tokens.** A delegated token stops working when its service account key is deleted or expires, when the service account is archived, or when the member leaves the team.

Revoking your personal keys when you [sign out everywhere](https://cursor.com/docs/security/sessions.md#sign-out-everywhere) doesn't revoke service tokens.

Prefer a service token when a system acts for a specific user, or when you don't want to store a long-lived secret.

## Use a key

Send the key as the username in Basic authentication, with an empty password:

```bash
curl https://api.cursor.com/teams/members \
  -u YOUR_API_KEY:
```

The Cloud Agents API also accepts the key as a Bearer token:

```bash
curl https://api.cursor.com/v1/me \
  -H "Authorization: Bearer YOUR_API_KEY"
```

A missing, expired, or revoked key returns `401`. A valid key without the permission a route needs returns `401` on the Admin API and the Organization API, and `403` on the Cloud Agents API. See [Common error responses](https://cursor.com/docs/api.md#common-error-responses).

## Keep keys least-privilege

- **One key per job.** Give each integration its own key so you can revoke one without breaking the others.
- **Only the permissions the job needs.** Start with view permissions. Add a manage permission when the integration must change something.
- **Set an expiry.** A key that expires limits how long a leaked secret is useful.
- **Use a service account for shared automation.** A personal key ends with its owner's access. A service account doesn't.
- **Store secrets in a secret manager.** Don't commit keys to a repository or paste them into chat.
- **Review keys on a schedule.** Check **Last used** for each key and remove keys that nothing uses. See [Review key activity](https://cursor.com/docs/security/api-keys.md#review-key-activity).
- **Watch the audit log.** Key creation, rotation, and revocation are recorded. Use **View audit logs** on a key's row to see what that key did. See [Audit logs](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs).

## Related

- [Cursor APIs overview](https://cursor.com/docs/api.md)
- [Service accounts](https://cursor.com/docs/account/enterprise/service-accounts.md)
- [Admin API](https://cursor.com/docs/account/teams/admin-api.md)
- [Security overview](https://cursor.com/docs/security.md)
