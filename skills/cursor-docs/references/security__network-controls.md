---
title: "Network controls"
source: https://cursor.com/docs/security/network-controls
path: /docs/security/network-controls
---

# Network controls

Cursor has two kinds of network controls. The IP allowlist limits where your members can reach Cursor from. Network access settings limit what agents can reach. Both are on the **Security** page of the organization or team [dashboard](https://cursor.com/dashboard).

The IP allowlist and the team network access lists are available on Enterprise plans.

| Control                    | Direction | What it limits                                                      |
| :------------------------- | :-------- | :------------------------------------------------------------------ |
| **Ingress IP Allowlist**   | Inbound   | The addresses that can sign in to Cursor and call it for your team. |
| **Network access control** | Outbound  | The destinations that agents can connect to.                        |

These controls are separate from the firewall rules that let your network reach Cursor. For those, see [Network configuration](https://cursor.com/docs/enterprise/network-configuration.md).

## IP allowlist

The IP allowlist is a list of IP addresses and CIDR ranges. It doesn't take domain names. While it is enforced, Cursor refuses the requests listed below unless they come from one of those addresses.

### What it applies to

An enforced allowlist refuses these requests from addresses outside the list:

- **Sign-in.** Signing in from the desktop app, the web, the CLI, and mobile, and refreshing an existing session.
- **The dashboard.** Viewing and changing team settings.
- **API requests.** Calls to Cursor's APIs with a key or token that belongs to the team.
- **Cloud Agents.** Starting and managing Cloud Agents, and calling an automation's own webhook URL.

A person who belongs to more than one team is checked against each team's list.

A refused request returns `403` with a message that names the address and the team. If Cursor can't read a list, the request returns `503` and can be retried. A member who opens Cursor on the web from a blocked network sees a notice that their network is not on the team's IP allowlist.

### Set up the allowlist

### Add your addresses

Find **Ingress IP Allowlist**. Under **Allowed Addresses**, select **Add** or **New entry**. To add several together, use **Paste Addresses** or **Paste a list**. Enter one address or CIDR range per line, each optionally followed by a description.

### Check the list against your egress addresses

Compare the list with the egress addresses of your offices, VPN, CI, and integrations, and add any that are missing.

### Turn the list on

Turn on **Limit access by IP address**. A new list has **Shadow mode** on, which still allows requests from addresses outside the list. To enforce the list, turn off **Shadow mode** and confirm with **Enforce**. From then on, the requests listed under [What it applies to](https://cursor.com/docs/security/network-controls.md#what-it-applies-to) are refused from addresses outside the list, for every member of the team, including you.

Entries follow these rules:

- IPv4 and IPv6 addresses and CIDR ranges are accepted, for example `203.0.113.0/24`.
- A list holds up to 1,000 entries. Each can carry a description.
- A range that covers every address, such as `0.0.0.0/0` or `::/0`, isn't allowed. Turn the list off to allow every address.
- A list that is on but has no entries doesn't apply, and every address is allowed.

### Avoid locking yourself out

Cursor checks your own address when you save. If enforcing the list would block the address you're saving from, the save is refused. Add your address first.

That check covers only the admin who saves. Before you turn the list on, account for everyone else:

- **Remote and traveling members.** Include your VPN or secure web gateway egress addresses, and require members to connect through them.
- **Automation.** Include the addresses of CI runners, scripts, and servers that call Cursor with a team API key or service account.
- **A second admin on a second network.** Keep one who can change the list if your primary egress address changes.

If members are blocked after you turn the list on, an admin on an allowed address can edit the list or turn off **Limit access by IP address**.

### Organization IP allowlist

An organization can set one IP policy for every team linked to it. Organization admins manage it on the organization's **Security** page.

While the organization's policy is on and enforced, it replaces each team's own allowlist. Team admins then see it as a read-only **Organization IP Allowlist** and can't change it from the team.

### Origin inbound allowlist

Origin has its own inbound allowlist, which limits the addresses that can reach your repositories on Origin. See the [Origin API](https://cursor.com/docs/api/origin/reference/inbound-ip-allowlist.md).

## Agent network access

Agents run commands that make network requests. Network access settings decide which destinations those commands can reach. They apply in two places: the sandbox that runs agent commands in Cursor and the Cursor CLI, and the egress proxy in front of Cursor-hosted Cloud Agents.

### Team lists

Enterprise team admins manage these lists under **Network access control** on the team's **Security** page:

| List                                 | Applies to                                       | Effect                                                                                                             |
| :----------------------------------- | :----------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **Sandbox allowed destinations**     | Commands agents run in Cursor and the Cursor CLI | If you add any, agents can reach only these destinations, instead of Cursor's default list and members' own lists. |
| **Blocked domains and IPs**          | The sandbox                                      | Always blocked, even if allowed elsewhere. Cloud Agents don't use this list.                                       |
| **Cloud agent allowed destinations** | Cursor-hosted Cloud Agents                       | Applied at the Cloud Agent's egress proxy. An entry can allow a public IPv4 address or range on one port.          |

The lists may also be labeled **Sandbox Allowed Destinations**, **Cloud Agent Egress Allowed Destinations**, and **Blocked Domains/IPs**.

**Cloud agent egress uses the sandbox allowlist** makes Cloud Agents use the sandbox list. Turn it off to give Cloud Agents their own list.

A command that a member approves for full network access skips the team's lists. To stop members from approving that, restrict the available [run modes](https://cursor.com/docs/agent/security/run-modes.md#team-controls).

### Cloud Agent access modes and locking

Cloud Agents also have a network access mode. For the team, **Network access policy** offers **Allow all network access**, **Defaults + team allowlist**, and **Team allowlist only**. **Team allowlist only** is available on Enterprise plans. Members and saved environments get the same choices for their own allowlists.

**Lock network access policy** applies the team setting to every member, so members can't override it. On Enterprise teams the lock is on unless an admin turns it off. On other teams, a member's or environment's setting takes precedence over the team default unless an admin turns the lock on.

See [Cloud Agent network access](https://cursor.com/docs/cloud-agent/security-network.md#network-access) for each mode, the precedence rules, and locking.

### Organization network blocklist

Organization admins can keep one blocklist for every team in the organization. Grok Bot computers and Cursor-hosted Cloud Agents block the domains on the list. To block by address in the sandbox, use a team's **Blocked domains and IPs** list.

On the organization's **Security** page, import a `.txt` file with one domain per line under **Network blocklist**, then turn on **Enforce network blocklist**.

While **Enforce network blocklist** is on, the list applies to every team's Grok Bot computers and Cursor-hosted Cloud Agents. It applies in addition to each team's own blocked sites. Team admins see it as **Organization network blocklist** and can't remove its entries.

For Cloud Agents, keep these limits in mind:

- **New agents only.** New, forked, and recreated Cloud Agents apply the list. Running agents keep the policy they started with.
- **Hostname matching.** When a team allows all network access, Cloud Agents match blocked sites by hostname. Use **Team allowlist only** when you need a strict boundary.

#### File format and limits

The file is plain UTF-8 text with up to 50,000 domains, one per line. It can be up to 8 MB. The list applies to Grok Bot computers and Cursor-hosted Cloud Agents in every team linked to the organization.

- **Subdomains.** Each domain also blocks all of its subdomains. A leading `*.` is optional and means the same thing.
- **Plain domain names only.** Write `example.com`, not `https://example.com`. Schemes, URL paths, underscores, and private IP addresses are rejected.
- **Comments.** A line that starts with `#` is a comment. To add a note after a domain, put a space before the `#`.

```text
# Phishing domains
example.com
*.example.net # covers example.net too
```

One invalid line rejects the whole file. The error lists the problems by line.

To update the list, upload the full file again. Each upload replaces the previous list.

### Self-hosted machines

These settings apply to Cursor-hosted Cloud Agents. Agents on [Self-Hosted Machines](https://cursor.com/docs/cloud-agent/self-hosted.md) use the machine's own network, firewall, and proxy.

## Related

- [Cloud Agent network access](https://cursor.com/docs/cloud-agent/security-network.md#network-access)
- [Sandbox network access](https://cursor.com/docs/agent/security/run-modes.md#network-access)
- [Network configuration](https://cursor.com/docs/enterprise/network-configuration.md)
- [Private connectivity](https://cursor.com/docs/cloud-agent/private-connectivity.md)
- [Security overview](https://cursor.com/docs/security.md)
