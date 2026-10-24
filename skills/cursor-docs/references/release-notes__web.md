---
title: "Cursor web release notes"
source: https://cursor.com/docs/release-notes/web
path: /docs/release-notes/web
---

# Cursor web release notes

Weekly changes to Cursor on the web, from integrations and admin settings to automations, the APIs, security and approval agents, and models. Each entry covers one week and is labeled with the Monday that starts it. [Cloud Agents](https://cursor.com/docs/release-notes/cloud-agents.md) and [Bugbot](https://cursor.com/docs/release-notes/bugbot.md) have their own pages.

## Week of Oct 12, 2026

### Integrations

#### GitHub

- &#x20;**Bugbot reviews pull requests in shared GitHub installations.** When another team in your organization shares its GitHub installation with your team, Bugbot runs on pull requests in the shared repositories using your team's Bugbot settings.
- &#x20;**Connecting GitHub no longer turns on Bugbot for every repository on Enterprise teams.** When an Enterprise team or a GitHub Enterprise Server installation connects GitHub, existing repositories stay off until an admin turns Bugbot on for them. New repositories also stay off unless you change the installation's auto-enable setting, and these changes appear in your team's audit log.
- &#x20;**Clearer GitHub access errors.** When an agent can't reach a GitHub repository, the error says why. A repository not granted to the Cursor GitHub App comes with a link to grant access, an organization that requires SAML SSO comes with a link to authorize, and [IP allow list](https://cursor.com/docs/integrations/github.md#ip-allow-list-configuration) blocks are explained. Changing settings for an installation linked to a different Cursor account explains how to uninstall and reinstall it from your team's dashboard.
- &#x20;**Fixes to the GitHub integration.** Admins of merged teams can manage GitHub and Bugbot installations again instead of seeing "Team is not active". Agents with access to more than 500 repositories get a GitHub token instead of failing, and GitHub requests no longer fail when HTTP/2 isn't available. When GitHub rate limits token refreshes, you see a "try again later" message.

#### Bitbucket

- &#x20;**Bitbucket Data Center explains a missing permission.** If Cursor's application link grants less than Repositories Read, connecting [Bitbucket Data Center](https://cursor.com/docs/integrations/bitbucket.md) shows a page asking your Bitbucket admin to raise it before you reconnect, and the setup instructions list that permission.
- &#x20;**Fixes to Bugbot for Bitbucket.** Bitbucket Cloud admins who get admin access through a group or workspace role can turn Bugbot on or off for a repository. Reconnecting a repository no longer fails with 405 errors when Bugbot updates its existing webhook.
- **Fixes to Bitbucket.** Repository lists in large Bitbucket workspaces load partially instead of failing, and reading pull request diffs and repositories no longer fails when Bitbucket Cloud redirects. Creating a pull request reuses the open one even when the repository name differs in letter case, and empty secondary repositories are skipped.

#### GitLab

- &#x20;**GitLab credentials stay on your GitLab host.** When a [GitLab](https://cursor.com/docs/integrations/gitlab.md) instance redirects a request to a different host, Cursor refuses the redirect with an error instead of sending your token or OAuth client secret there. Same-host redirects, such as a moved project or renamed namespace, are still followed.
- **Fixes to the GitLab integration.** Empty GitLab repositories added as secondary repositories are skipped instead of making the agent fail. Webhooks with a missing token or unknown registration return an error, so GitLab shows the failure instead of reporting success.

### Dashboard and admin

#### Plugins and MCP

- &#x20;**See which servers Team list enforcement would block before you turn it on.** Team list settings on the Plugins page, and the new Turn On Team List Enforcement dialog, now list the plugins and MCP servers members use that aren't on the Team list, with how many members use each. You can add a plugin to the Team list or allow a remote MCP server in one click, and the dialog warns you when enforcement would block every MCP server. See [MCP server trust management](https://cursor.com/docs/enterprise/model-and-integration-management.md#mcp-server-trust-management).

#### Integrations

#### SSO and SCIM

- &#x20;**Control who can join through SSO.** Organization admins can turn off SSO auto-enrollment in organization settings. When it is off, only invited or SCIM-provisioned users can join, while existing members keep signing in with SSO as before. Anyone else who signs in through your SSO connection is told to ask an admin for an invite. See [SSO settings](https://cursor.com/docs/account/teams/sso.md#additional-settings).

#### Members and groups

- &#x20;**Create team groups that the whole team can see.** The New group dialog on the Members Groups tab now has a Visibility switch, so admins can make a group and its members visible to the whole team when they create it instead of editing it afterward. Groups stay visible only to admins unless you turn the switch on.
- &#x20;**Choose how many members to show per page.** The Members page now has a Rows per page control at the bottom of the list, so admins of large teams can show 50, 100, or 250 members at a time. Your choice is kept in the page URL, and changing it takes you back to the first page.

#### Agent settings

- &#x20;**Project agents now ask before using a new machine, on every plan.** The **Automatically allow Projects to place their work** switch in Cloud Agents security settings now starts off for every team, not only Enterprise teams, so a person approves each new machine, environment, or repository a Project's agents use. Teams that turned the switch on keep auto-allow, and approvals already granted stay in place. See [Cloud Agents security settings](https://cursor.com/docs/cloud-agent/settings.md#security-settings).
- &#x20;**Clearer warnings for network allowlist entries that won't match.** In the team Network access settings, admins now see which sandbox allowlist entries cloud agent egress ignores, along with explanations for unsupported characters and wildcard patterns. Catch-all entries such as `*.` and URL paths are no longer accepted for cloud agent egress, so a mistyped entry can't open access to every host. See [network access settings](https://cursor.com/docs/cloud-agent/settings.md#network-access-settings).
- &#x20;**Choose a mode for Approval Agents.** Approval Agent settings now include a Mode option under Configuration. Default is the faster choice and fits most teams. Low costs less and runs slower. You need edit access to change it. See [PR Routing & Approval](https://cursor.com/docs/approval-agents.md).

#### Rollouts

- &#x20;**Send Rollouts notices to Slack channels by repository, service, or environment.** In Rollouts settings, team admins can subscribe Slack channels to change notices that match a repository, service, or environment, and add an optional message, including @mentions, that's posted in the thread after each new issue. Members can add their own personal subscriptions, and both team and personal subscriptions can be edited later. See [Rollouts notifications](https://cursor.com/docs/rollouts.md#notifications).
- &#x20;**Send deployment events to Rollouts from your GitHub deployments.** When you set up deployment events in Rollouts, you can choose **Use my GitHub deployments** to record deployments from your watched repositories, with no CI reporter needed. The manual setup now shows numbered, collapsible steps, and its copyable snippets report a missing or rejected Cursor API key in your CI log without failing the deploy. Deployments from gitlab.com projects now appear on a deployment's page, with **Version** and **Previous version** linking to the GitLab commit. See [sending deployment events](https://cursor.com/docs/rollouts.md#send-deployment-events).

#### Cloud agent environments

- **Find, filter, and rename Cloud Agent environments.** The Environments list now marks environments defined by a committed `.cursor/environment.json` with a **Config as code** badge, and a **Config as code** switch shows only those environments. You can rename an environment by clicking its name on the environment's edit page, and the **Repo** filter has a search box. In the default environment picker, unnamed environments show their repositories, such as "web-app +3", instead of an ID, and you can search for them by repository name. See [environment management](https://cursor.com/docs/cloud-agent/settings.md#environment-management).
- **Clearer messages when a Cloud Agent environment build can't use its environment.json.** When an environment build fails because its tracked `environment.json` is missing, empty, or can't be read, the build page now says so and tells you to restore or check the file, then rebuild. Agents keep using the last successful build in the meantime. Builds that fail because the GitHub App can't access a repository now list the affected repositories with an **Open installation settings** button, and teams that require self-hosted workers see a note in place of the **Trigger build** action. See [Cloud Agent Builds](https://cursor.com/docs/cloud-agent/builds.md#manage-builds).

#### Usage and analytics

- &#x20;**Export usage events for your whole organization.** Organizations with pooled usage now get a Usage events section on the organization Usage page, with an Export button that downloads event-level usage across the organization's teams for the selected date range and filters. If an export isn't possible, for example when the organization has both merged and unmerged teams, the button is disabled and the page explains why.
- **Reorder usage event columns and read usage labels more easily.** On the Usage page, you can drag the usage events table's column headers, or move them with the keyboard, into the order you want. Your browser remembers the order, and Date and User stay in place. Usage types now read "Additional usage" and "Credit grants", Auto requests show as Auto or as the routed model with its Auto option in the chart and model filter, and usage owned by a team rather than a person or API key shows as Team in the table and CSV export.

#### Security and audit logs

- &#x20;**More team changes in the audit log.** The audit log now records changes to cloud agent network egress and sandbox networking settings, and to your team's repository allowlist and blocklist, including repo patterns. It also records Remote Control events, such as a computer being registered or a device being paired, unpaired, or revoked, with a new Remote Control filter. Merge queue bypass attempts and pull request takeovers are now logged too, and takeovers show the previous author. See [audit logs](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs).

#### Workspace settings

- &#x20;**Add an icon to your team or organization.** Admins can upload, change, or remove a team icon (PNG, JPEG, or WebP up to 2MB) in the Team profile settings. The icon appears in the workspace switcher, command palette, team selector, and the organization's teams table. Organization owners can also set an organization icon from the organization Overview page.

#### Automations

- &#x20;**See more flagged vulnerabilities per page.** The flagged vulnerabilities table on the Vulnerability Scanner page now has a rows-per-page selector with 10, 25, 50, or 100 rows. It shows 25 by default instead of 5. Long titles wrap to two lines, and the Prev and Next buttons no longer move when you change pages. See [Security Agents](https://cursor.com/docs/security-agents.md).

#### Account and navigation

- **See what you lose before deleting your account.** The delete account dialog in Profile settings now lists what will be deleted, starting with your Cursor account's name, email, and member-since date. If your account is merged with a Grok account, it also shows that account under Deleted and your linked X account under Unlinked, since X accounts are unlinked, not deleted. The dialog also notes that payments already made are not eligible for a refund.
- **Reset a saved color palette from Appearance settings.** If you saved a colorblind or high-contrast color palette, Settings > Appearance now shows it in a Color palette row with a Reset button. Resetting shows a toast with Undo, so you can restore the palette.

#### Fixes

- &#x20;**Fixes to Rollouts setup and issue pages.** Rollouts setup now pre-selects your team's existing observability connections, and Rollouts only shows as Enabled once setup is finished. If Rollouts is already on, setup still shows that step, with a link to its settings. Clicking Fix on an issue opened from a direct link now starts from the right rollout, and links to pull requests open on the portal you're using.
- **Fixes to cloud agent environments.** Restoring an older team environment version no longer removes your personal override, and the Secrets row now says it includes team and personal secrets, with Manage opening the secrets that match the environment's scope. If the environments list fails to load, the Environments pages, Slack repo routing rules, and the agent environment picker now show the error or fall back instead of loading forever. The Environments section also recognizes any connected source control provider, so it loads faster and no longer shows the Connect Source Control card by mistake.
- &#x20;**Fixes to usage and analytics.** Team usage event tables now load long date ranges, such as 30 days, without timing out on large teams. The usage card shows a member's own spending limit, including a $0 limit, instead of the team limit. The Usage Leaderboard no longer lists service accounts, team API keys, or unauthenticated usage, and no longer merges members who share an email or have none.
- &#x20;**Fixes to team invites and team selection.** Copy invite link now uses the role you pick in the invite form on teams without seat tiers, so an admin link no longer adds people as members. When you belong to several teams, paid teams now come before free ones, so you no longer land on a free team by default.
- **Fixes to integrations and shared pages.** Teammates who haven't connected Slack now see a deployed agent's existing Slack apps as read-only rows with a Connect Slack button, not an empty state. Shared canvases now print on white paper without the browser's header and footer, and the disabled Team sharing option explains when your team's admin turned it off.
- **Fixes to dashboard navigation and phone layouts.** On phones, tab strips scroll to the screen edges, tap targets are larger, and the members search and setup checklist no longer crowd the layout. The Cmd+K command palette now opens above other dialogs, and closing it leaves the dialog underneath open. Each dashboard tab sets its own browser title, a failed background refresh no longer replaces a loaded workspace with an error screen, and profile settings show your saved first and last name.

### Automations

#### Triggers

- **Label triggers for Origin pull requests.** Automations on Origin repositories can now use the Label change trigger, which runs when a label is added to or removed from a pull request, as it does for GitHub.
- **Inline review comments on Origin pull requests now trigger automations.** Automations with a pull request review comment trigger now run when someone leaves an inline review comment on an Origin pull request. Before, those comments only reached automations that trigger on top-level pull request comments.

#### Security agents

- &#x20;**Vulnerability Scanner caps hourly scans per team.** [Vulnerability Scanner](https://cursor.com/docs/security-agents.md) automations run at most 500 repository scans per team per hour. Scans over the cap are skipped and show in run history as rate limited.
- **Subagents in managed security runs no longer message on their own.** Fixed an issue where helper subagents in managed security review, vulnerability scanner, and PR approval runs could send Slack and Teams messages or resolve review threads on their own. Those actions are now refused for subagents in these runs.

#### Integrations

- **Automations load the MCP servers you named.** Automations that pick an [MCP server](https://cursor.com/docs/cloud-agent/automations.md#mcp-server) by name, like `slack` or `google-drive`, now find it even when the capitalization or spacing doesn't match. Before, these runs could start without the server's tools. If Cursor still can't find a server, the run shows a warning telling you to check the name or reconnect the server under Integrations.
- **Clearer status when GitLab has MCP turned off.** When a GitLab MCP server in an MCP action is blocked because GitLab has MCP turned off for your groups, the automation editor now explains that an Owner of your top-level GitLab group must turn on MCP client access, instead of showing a sign-in prompt that can't succeed.
- &#x20;**Only team admins can connect a team's PagerDuty integration.** Connecting, replacing, or moving a team's [PagerDuty integration](https://cursor.com/docs/cloud-agent/automations.md#pagerduty-triggers) now requires a team admin, the same as disconnecting it. A PagerDuty account connected to one team can't move to another team until an admin disconnects it. The connection page now tells you why a connection failed: your session ended, you aren't a team admin, or the account belongs to another team.

#### Automation runs

- &#x20;**Managed automations no longer run on models your team blocks.** When your team's model settings block every model a managed automation can use, such as the security reviewer or vulnerability scanner, the run now fails with a "Model blocked" error asking a team admin to allow a model. Before, the automation could fall back to a blocked model.

#### Automations page

- **The Model column shows the variant your automation actually runs.** The Automations list, overview table, and run history now label each automation's [model](https://cursor.com/docs/cloud-agent/automations.md#model) with the effort and Fast settings you saved, instead of the model's default variant. If a saved selection doesn't match a single variant, the column shows the plain model name.

#### Fixes

- **Fixes to which branch and repository automations launch on.** Automations tied to a single-repo environment, including repos saved as SSH URLs, now run on the branch you saved instead of the environment's default branch. Automations that target a specific self-hosted machine fall back to `main` instead of failing when Cursor can't reach the git host. Runs that fail because the GitHub App was installed under another account now say the repository isn't connected to this team and explain how to reinstall the app.
- **Fixes to the automation editor and integrations.** MCP actions now show when a server needs sign-in even if no sign-in link came back, and clicking sign in gets a fresh link. PagerDuty services load faster on accounts with many services, and descriptions over 1,024 characters now show a clear error. Turning off Change Monitor reports a failure instead of looking successful while it keeps running, and the Bugbot MCP tools and installation pages under From Cursor now load.
- **Automations list rows work with the keyboard.** You can now reach and open rows in the Automations list with the keyboard. Tab moves focus from row to row.
- **Fixes to long automation runs.** Runs that take a very large number of actions no longer fail to save their action history. The oldest entries are compacted so the run keeps recording.

### APIs

- &#x20;**Make directory groups visible to your whole team.** [Team directory groups](https://cursor.com/docs/account/teams/admin-api.md#team-directory-groups) in the Admin API now have a `visibility` field. Set it to `team` when you create or update a group so every team member can see the group and its members, or `team_admin` to keep it visible only to admins. If you leave it out on create, the group is visible only to admins.
- &#x20;**Fixed missing member spend in the team spend endpoint.** [`POST /teams/spend`](https://cursor.com/docs/account/teams/admin-api.md#get-spending-data) now counts each member's billed usage in full for teams on combined billing, so reported spend no longer comes up short. If spend data can't be read, the endpoint returns a 503 error instead of reporting zero spend.

### Security and approval agents

#### Security agents

- **Vulnerability Scanner findings show in Flagged Vulnerabilities.** Fixed an issue where findings from a Vulnerability Scanner didn't appear in the [Flagged Vulnerabilities](https://cursor.com/docs/security-agents.md#flagged-vulnerabilities) list.
- **Show more flagged vulnerabilities per page.** The Flagged Vulnerabilities list now has a **Rows per page** selector (10, 25, 50, or 100) and shows 25 rows by default instead of 5. Long titles wrap to two lines, and the **Prev** and **Next** buttons stay in place as you page.
- **Fixed multi-file findings close when you push a fix.** When a finding names more than one file, Security Reviewer re-checks each of those files on every push, so a fix in any of them closes the finding. You no longer need to resolve it by hand. Open findings in files you haven't changed now count toward the security check, so the check status matches the open threads.
- **Saving large Security Reviewer configurations works.** Saving a Security Reviewer with many selected repositories, exclusions, or Slack channels no longer fails.

#### Approval agents

- **Approval comments show everyone who can approve.** When a [PR Routing & Approval](https://cursor.com/docs/approval-agents.md) policy is waiting on review and more owners can approve than were requested, its comment reads like "Needs 1 approval from any of: @alice, @bob (+2 more)". On [Origin](https://cursor.com/docs/origin.md) repositories, a pending policy that lists bot owners names them and shows how to request their review from the **Reviewers** list or with `origin pr reviewer request`.

### Models and Cursor Router

- **New model: Gemini 4 Argon.** [Gemini 4 Argon](https://cursor.com/docs/models/gemini-4-argon.md) is now available in Cursor.

## Week of Oct 5, 2026

### Integrations

#### GitHub

- &#x20;**Pull request details stay limited to people with GitHub access.** Cursor shows pull request details only to people whose GitHub account can read the repository, even when a teammate already loaded them. Everyone else gets an access error.
- **Clearer errors when GitHub blocks a merge method.** Merging a [GitHub](https://cursor.com/docs/integrations/github.md) pull request from Cursor with a merge method the repository doesn't allow now fails right away with GitHub's own reason, such as "Squash merges are not allowed on this repository." Before, Cursor retried and then showed a generic can't-merge-yet message.
- **Fixes to GitHub status and setup.** Pending commit-status checks now show as running instead of queued, Actions log excerpts no longer hang on redirects, and `@cursor` commands from people whose GitHub username contains "cursor" are no longer ignored. GitHub Enterprise Server app installs now land on the team that started setup.

#### GitLab

- **GitLab repository lists and merge request lookups load reliably.** The Bugbot repository list for large [GitLab](https://cursor.com/docs/integrations/gitlab.md) groups loads with the projects fetched so far instead of failing on a timeout, and finding the merge request for a branch now works for GitLab instances reached through AWS PrivateLink or an egress proxy.

#### Linear

- **Full Linear team names on hover.** Hover a truncated team name in the teams list on the [Linear integration page](https://cursor.com/docs/integrations/linear.md) to see the full name.

#### Source control

- **Steadier self-hosted source control connections.** Cursor retries a read request once when a connection to GitLab self-managed or Azure DevOps drops briefly. Over AWS PrivateLink, GitHub, GitLab, and Bitbucket requests also retry once when the server closes the connection.

### Dashboard and admin

#### Plugins and MCP

- &#x20;**Control which MCP and plugin tools your team can use.** Admins can turn Team list enforcement on or off from the Plugins page and limit a URL MCP server's or plugin's tools from its detail dialog, picking allowed tools from a live preview. The MCPs tab has an Allowlist rules editor that marks rules that apply only while Team list is on, and each server shows its access status, such as Read-only or Cloud only, with a tooltip that explains why the IDE and CLI block it. See [MCP server trust management](https://cursor.com/docs/enterprise/model-and-integration-management.md#mcp-server-trust-management).
- &#x20;**Browse and add plugins and MCP servers from one list.** The Plugins & MCPs page shows installed plugins and MCP servers together in one searchable table, with an Add button for the selected scope. Clicking a plugin opens its details in a dialog instead of a separate page.

#### Members and groups

- &#x20;**Set soft or hard spend limits for a group's members.** In organization group settings, admins can set a member's monthly spending limit to No limit, Soft limit, or Hard limit. A soft limit doesn't block members and can be paired with pace alerts. A hard limit blocks members once their monthly spend reaches the amount. See [group spend limits](https://cursor.com/docs/enterprise/organization-groups.md#spend-limits).
- &#x20;**Groups show their slugs, label synced groups correctly, and all appear on large teams.** Team and organization group lists and group pages show each group's slug under its name. On the team Groups tab, groups synced from your identity provider are labeled Synced instead of Manual, and Move member no longer offers synced groups as destinations. Teams with more than 200 groups now see all of them on the Groups tab, in the Move member list, and in the invite group picker.
- &#x20;**Pending invites close when someone joins your team.** When someone joins your team in any way, such as SSO, domain join, SCIM, or a direct add, their other pending email invites to it close automatically, and an old invite link still takes them to the team. When someone joins through a copied invite link, the audit log records the member who copied the link as the inviter.

#### SSO and SCIM

- &#x20;**Turn on SSO auto-enrollment from either SSO page.** The SSO auto-enrollment switch now also appears on the older team SSO settings page, and both SSO pages show a newly finished SSO setup as soon as you return to the tab. When your identity provider marks a SCIM user inactive, Cursor removes their team seat but keeps their SSO membership, so reactivating them doesn't require adding them again. See [SCIM user management](https://cursor.com/docs/account/teams/scim.md#user-management).

#### Agent settings

- &#x20;**Control where Project agents can run.** The new **Automatically allow Projects to place their work** switch in Cloud Agents security settings decides whether a Project's agents can start work on any machine, environment, or repository the Project owner can reach without asking first. When it's off, agents ask for approval before they use a new one. It starts off for Enterprise teams and on for other teams. See [Cloud Agents security settings](https://cursor.com/docs/cloud-agent/settings.md#security-settings).
- **Choose which team your Slack agents run under.** If you belong to more than one paid team, the **Team for Slack agents** setting in Cloud Agents settings picks the team that agents you start from Slack run, bill, and use settings under. The setting is locked when your Slack workspace is restricted to one team. See [Team for Slack Agents](https://cursor.com/docs/integrations/slack.md#team-for-slack-agents).

#### Automations

- **Mine, Team, and Explore tabs on the Automations page.** Mine lists the automations you own, Team shows your team's automations alongside agents from Cursor, and Explore holds the template gallery. Team admins open on Team by default, and everyone else opens on Mine.
- &#x20;**Security Reviewer and Vulnerability Scanner have their own pages.** The From Cursor automations list shows separate Security Reviewer and Vulnerability Scanner cards in place of the single Security card. Each page lists only its own agents and recent runs, its New button creates that type directly, and flagged vulnerabilities appear on the Vulnerability Scanner page. Old Security links redirect to Security Reviewer. See [Security Agents](https://cursor.com/docs/security-agents.md).
- **Start Rollouts checks yourself when a deploy isn't recorded.** If a merged change goes live without a recorded deployment, select **Run checks** on the change's page in Rollouts, pick the environment and services, and Rollouts starts checking it. Deferred checks show as **Deferred** with the reason, and closing an issue now asks for a reason, such as **Fixed** or **Duplicate**. See [Rollouts](https://cursor.com/docs/rollouts.md#deploy-tracking).

#### Usage and integrations

- &#x20;**Filter usage by SDK.** The Usage pages for teams and organizations have an SDK option in the client filter, so you can see spend and requests from agents run through the Cursor SDK on their own. Now available to everyone.
- &#x20;**Connect SharePoint for your whole team.** Admins can connect SharePoint from the Integrations page: choose delegated or application permissions, enter your Microsoft tenant, grant admin consent, and optionally allow write access. If setup stops partway, members who add the SharePoint plugin are told to ask an admin, and admins get a link back to Integrations to finish.

#### Security and privacy

- &#x20;**Bitbucket connection changes in the audit log.** The audit log records when a Bitbucket Cloud or Bitbucket Server connection is connected, disconnected, registered, or deleted, and when its token is set or cleared, with the provider and host. Filter for them with the new Source Control Connection event type. See [audit logs](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs).
- &#x20;**Clearer privacy mode names.** Privacy settings now read "Privacy Mode (no training)" and "Legacy (no storage)". When you invite teammates from a personal plan, a new "Share Cursor Analytics" checkbox sets the new team's privacy setting, and Privacy Mode stays on unless you check it.
- &#x20;**Control Grok dictation and private chats.** Team admins can turn dictation on or off for their members from the Grok tab. Organization admins also get a Features section there with switches that turn off dictation or private (temporary) chats for every team in the organization, so all chats are kept for compliance exports.

#### Fixes

- **Fixes to dashboard layout and display.** Team settings opens on the first click, and plan reset and billing cycle dates show in your local time zone instead of UTC. The Usage page shows how far you are over your monthly limit instead of $0 remaining, and the Overview setup checklist shows the steps that loaded instead of failing the whole card. Long names and emails truncate with the full text on hover, and pages no longer flash stale content or jump while loading.
- **Fixes to the dashboard on phones.** The navigation drawer can be swiped left to close, the Members table and Usage filters fit the screen, and the Usage date picker no longer widens the page. The team name editor wraps and stops at 200 characters, and the invite email field no longer autocapitalizes or autocorrects.
- **Fixes to the Automations page layout.** The Automations list no longer leaves a gap between each automation's title and author, the "Showing N" count is the right size with proper spacing, the filter tabs line up with the page title, and shared GitHub and GitLab triggers use a generic git icon.
- **Fixes to Rollouts settings.** Clicking Authenticate on an MCP tool no longer wipes an existing shared connection, and already-connected servers refresh instead of opening a sign-in window. The data sources list shows every row instead of a small scrolling box, and notification help text wraps on mobile.
- **Fixes to environments and secrets.** An environment's page shows history for that environment only. Double-clicking Duplicate creates one copy instead of two, and choosing All repositories in the Edit Secret dialog saves the secret for every repository.
- &#x20;**Fixes to integrations and MCP authentication.** Registering a GitHub Enterprise Server app attaches it to the team you selected, and the existing-apps list shows that team's apps. Authenticating an MCP server for a service account returns you to the settings page you started from, and the private inference assignee picker loads groups from every linked team. Paging through the Origin repositories card no longer hides the card or shows the wrong page when a page change fails.
- &#x20;**Fixes to account sessions and deletion.** When an account's email changes to a different address through your identity provider, SSO, or directory sync, existing Cursor sessions on that account are signed out. Deleting an account that was previously merged with another account no longer fails.

### Automations

#### Automations page

- **Mine, Team, and Explore tabs on the Automations page.** The Automations page now opens on Mine, which lists the automations you own across your personal account and teams, alongside popular templates. Team shows your team's automations, and Explore holds the full template gallery. Now available to everyone. Team admins land on Team, and users without a team see Mine and Explore.
- **See each automation's tools at a glance.** The Tools column on the Automations page shows each tool as a pill with its icon and name. When a row has more tools than fit, a +N pill shows how many more there are.

#### Triggers

- **Microsoft Teams automations now fire on every channel post.** Automations that listen to a Microsoft Teams channel now run on regular posts in that channel, not only on posts that @mention Cursor.
- **Failed Slack-triggered runs are marked on the trigger message.** When an automation started from a [Slack message](https://cursor.com/docs/cloud-agent/automations.md#slack-triggers) fails, that message now gets a red X reaction in place of the hourglass. Before, the hourglass disappeared and nothing showed that the run had failed. The channel still gets no failure post.

#### Security agents

- **Vulnerability Scanner follows your custom instructions and files follow-ups.** Team Vulnerability Scanner automations now use your [custom instructions](https://cursor.com/docs/security-agents.md#custom-instructions) to shape what they scan. After a scan, they carry out the follow-up actions those instructions ask for, like filing a ticket for each new finding, through the automation's MCP servers, and link what they filed in the finding's Slack report.

#### Automation runs

- **Clearer reasons when a run fails.** Run history now tells you whether to retry or contact your admin when your organization's policy check blocks a model request or is unavailable. Runs that fail because no self-hosted worker matches their labels now name those labels.

#### Fixes

- **Fixes to the Vulnerability Scanner.** Findings recorded by the [Vulnerability Scanner](https://cursor.com/docs/security-agents.md) show up again instead of appearing empty. Repositories listed as host/owner/name without https\:// now scan instead of failing. Teams that turn Security off in their managed automation settings no longer get scheduled scanner runs.
- **Fixes to Change Monitor setup.** Turning off Change Monitor now stops its agents, and asks you to try again if they don't stop. Saving repositories the installation can't see, or that are missing a webhook, now shows the specific setup error instead of a generic one. Nested GitLab paths now ask for the full `gitlab.com/<group>/<project>` form, and fully qualified GitLab projects are watched correctly.
- &#x20;**Fixes to the automation editor and integrations.** Your GitHub or GitLab connection no longer shows as disconnected when you belong to several teams or use self-hosted GitHub Enterprise or GitLab. The editor's MCP server options now list the selected team's servers. Disconnecting a team's PagerDuty integration now removes the team's connection, and "Configure here" links in Security Reviewer comments and Slack messages open that agent's page under From Cursor.
- **Fixes to the Automations page layout on web and mobile.** On narrow screens, the Automations list now scrolls sideways instead of cutting off columns, and the row actions stay pinned on the right. Spacing and alignment across the page header, tabs, toolbar, and list rows are fixed.

### APIs

- &#x20;**Clearer error for Azure DevOps repos in the Bugbot repo update endpoint.** [`POST /bugbot/repo/update`](https://cursor.com/docs/bugbot.md#enabling-or-disabling-repositories) now returns a 400 for `dev.azure.com` and `visualstudio.com` repo URLs, explaining that Azure DevOps repo settings are managed from the Cursor dashboard, instead of telling you to install the Cursor GitHub or GitLab app.

### Security and approval agents

#### Security agents

- &#x20;**Separate Security Reviewer and Vulnerability Scanner pages.** Under From Cursor in the dashboard, the Security card is now two cards, Security Reviewer and Vulnerability Scanner. Each opens a page that lists only that type of [security agent](https://cursor.com/docs/security-agents.md) and its recent runs, with a New button that creates that type and an icon that shows whether it's enabled. Old Security links redirect to Security Reviewer.
- **Incomplete reviews no longer auto-approve.** When part of a security review fails, Security Reviewer no longer treats the result as clean, so it doesn't auto-approve the PR. If no reviewer finishes, it posts no findings and leaves existing threads alone. Earlier findings stay open when their follow-up check times out or fails.
- **Accepted findings aren't posted again on every push.** If you resolve a finding without fixing it, for example to accept the risk, a later push that finds the same issue no longer opens a new comment. A different issue on the same lines still gets its own comment, and a fixed issue that comes back is reported again.
- **Failed large reviews finish sooner.** When every reviewer on a very large security review fails, the review now stops early instead of retrying until its budget runs out.

#### Approval agents

- **Clearer approval requirements on pull requests.** [PR Routing & Approval](https://cursor.com/docs/approval-agents.md) checks, comments, and the reviewer hovercard now say exactly what clears review, such as "Needs 1 approval from any human reviewer" with suggested reviewers, one approval from any of a set of owners, or approvals from all named owners. Auto-approved low-risk pull requests no longer show a leftover approval requirement.

### Models and Cursor Router

- **New model: Claude Haiku 5.5.** [Claude Haiku 5.5](https://cursor.com/docs/models/claude-haiku-5-5.md) is now available in Cursor as an opt-in model. Turn it on in Cursor Settings > Models.
- **Fixes for Mistral models.** Mistral requests that failed with a validation error now complete, and the model's reasoning shows up as thinking, separate from its answer.
- **Vendor names for Alibaba and Mistral models.** The model list now labels these models with their vendor.

## Week of Sep 28, 2026

### Integrations

#### GitHub

- **All your GitHub installations and accounts load.** If you have many GitHub App installations, connecting GitHub and picking repositories now shows all of them instead of missing the ones past the first page. If one of several connected GitHub accounts has an expired token, the others still load instead of failing with "GitHub access token is no longer valid".
- **Newly created repositories.** Cursor no longer denies access to a GitHub repository you can write to when GitHub briefly fails to return the repository's details, such as right after it is created.
- **Cloud Agent follow-ups on GitHub Enterprise Server.** Cloud Agents started through a GitHub Enterprise Server app now receive pull request and CI updates for the team that owns the app, instead of having those webhook events rejected.
- **GitHub stays connected through GitHub incidents.** When GitHub briefly rejects valid refresh tokens, Cursor keeps your GitHub connection instead of deleting it, and removes the token only if it keeps failing, so you don't have to reconnect GitHub.

#### GitLab

- **Clearer GitLab access errors.** Starting work on a GitLab project where you lack Maintainer or Owner access now consistently says GitLab Maintainer access is required instead of asking you to reconnect, and the token cooldown error states the remaining wait in minutes or hours.
- **Connecting GitLab clears token cooldowns.** After you connect GitLab, your personal and team repositories are usable right away instead of waiting out a cooldown left by earlier token errors.
- **Organization admins can manage team GitLab and Bitbucket connections.** Organization admins who aren't members of a team can now load and manage that team's GitLab and Bitbucket integrations instead of getting an error.

#### Bitbucket

- **Replies when a comment command can't run.** When @cursor can't run a command from a Bitbucket pull request comment, Cursor now replies on the pull request with the reason, such as needing a linked Bitbucket account or write access, instead of ignoring the comment.

### Dashboard and admin

#### Cloud agents

- **Fix failed Cloud Agent environment builds in one click.** When an environment build fails during install or on its Dockerfile, the environment and build pages show a **Fix Build** button that starts an agent to debug it, including for builds whose snapshot has expired. Builds with a deleted snapshot show a **Snapshot expired** chip and can't be activated, and deactivating the active build warns you when no other build can take over. Builds that fail because your self-hosted source control server is unreachable now say so. See [Cloud Agent Builds](https://cursor.com/docs/cloud-agent/builds.md#debug-a-build).

#### Automations

- &#x20;**More control over label triggers in Approver Agents.** A label-change trigger can now fire when a label is added, removed, or either, and you can limit it to one label name. These settings are now saved when you edit the agent.
- &#x20;**Vulnerability Scanner runs in Security Agents run history.** Recent Runs on the Security Agents page now lists Vulnerability Scanner runs next to security reviewer runs.

#### SSO and SCIM

- &#x20;**More reliable SCIM directory sync.** For organizations that own their SCIM directory, groups your identity provider pushes for teams linked to that organization now become synced groups instead of legacy directory groups. In directories with at least 10 users, if your identity provider briefly reports every user with no groups, directory sync no longer removes all directory group memberships.

#### Fixes

- **Fixes to Cloud Agent environment builds.** Build logs open at the newest line and keep following new output until you scroll up. When a page of the builds table comes back empty but older builds exist, it now tells you to use **Next** instead of leaving you stuck, and the **Trigger build** dialog no longer warns that builds are off.
- **Fixes to Cloud Agents settings and runs.** The Run history chart on the Cloud Agents Runs page no longer pushes the page down while it loads. Cloud agent settings refresh while the page is open, and network access entries like `*.example.com` now also match `example.com`.
- &#x20;**Fixes to groups and teams.** On a group's Members tab, the row actions menu stays on screen on wide tables. When you create a team in an organization, the team admin list puts you first and selects you by default.
- **Fixes to the dashboard on mobile.** On mobile, the navigation menu button now sits at the left of the top bar, and long GitHub Enterprise instance names truncate in settings.
- **Fixes to GitLab and Bitbucket integrations.** GitLab and Bitbucket connections on the Integrations page no longer fail to load when the team selected in the dashboard is one you aren't a member of, such as a canceled team. They show as read-only instead.
- **Fixes to Bugbot settings.** Old Bugbot license links open Bugbot settings in Automations.

### Automations

- **GitLab support in pull request triggers and comments.** The Comment on PR action accepts GitLab merge request URLs, including self-hosted GitLab. Git pull request triggers can be saved with a nested GitLab group (group/subgroup) or an organization URL as the org scope, and invalid entries show an error.
- **Clearer run failures.** When a run fails because of a configuration problem, such as a missing branch, an inaccessible repository, a model blocked by your team's region, an API key rate limit, or a missing Slack channel, run history shows the specific reason and what to do. Runs whose agent ran out of memory or whose machine stopped responding say so, and a run that later succeeds shows as succeeded.
- **Fixes to automation runs.** Automations with more than one schedule now run on every schedule instead of only the first. The open pull request step now opens the PR for runs owned by service accounts and for older team automations. Security Reviewer automations triggered by pull request comments or labels run again instead of being skipped, and automations with Slack access no longer stall on each step while re-listing Slack channels.
- **Fixes to team selection and PR Approver.** On cursor.com, automation actions run under the team you have selected instead of your default team. PR Approver reviews no longer say reviewers were assigned when assignment was turned off or failed; they say human review is needed instead.

### APIs

- **Skip the no-issues comment.** [`POST /bugbot/review`](https://cursor.com/docs/bugbot.md#trigger-a-review) accepts an optional `postSuccessComment` boolean. Set it to `false` and a review with no new findings doesn't post the "found no new issues" comment. It defaults to `true`.
- **Cost for free Bugbot reviews.** [`GET /analytics/team/bugbot-reviews`](https://cursor.com/docs/bugbot.md#review-analytics) now returns `cost_cents` for seat-based and free-trial reviews, showing their undiscounted model cost, and adds a `billed` field. `billed` is `false` when your team wasn't charged for the review.

### Security and approval agents

- **Admin Only label.** If you can't make changes to Security Agents, its pages now show an Admin Only label next to the page title.
- **Save without linking Slack.** You can now save edits to a security agent without connecting your own Slack account, as long as its Send to Slack channels are unchanged.
- **More reliable security reviews.** Security reviews keep results that finish right at the deadline, retry transient connection errors, and fall back to another model when the selected model is unavailable.

### Models and Cursor Router

- **New model: Claude Sonnet 5.5.** [Claude Sonnet 5.5](https://cursor.com/docs/models/claude-sonnet-5-5.md) is now available in Cursor.
- **New models: GLM 5.3 and GLM 5.3 Flash.** [GLM 5.3](https://cursor.com/docs/models/glm-5-3.md) and [GLM 5.3 Flash](https://cursor.com/docs/models/glm-5-3-flash.md) from Z.ai are now available in Cursor. They're off by default; turn them on in Cursor Settings > Models.

## Week of Sep 21, 2026

### Integrations

#### GitHub

- **Repository access updates right away.** After you connect, reconnect, or disconnect GitHub, changes to which repositories you can access apply immediately instead of after a cache expires.

#### GitLab

- **Renamed and moved projects.** After a GitLab project is renamed or moved, Cursor resolves the current project instead of a stale copy.
- **Disconnecting self-hosted GitLab keeps your GitHub connection.** Disconnecting a self-hosted GitLab instance on the Integrations page now disconnects that instance even when your current team can't see it, instead of disconnecting your GitHub account.

#### Azure DevOps

- **Bugbot repository status.** The Azure DevOps Bugbot dashboard no longer shows enabled repositories as disabled.

### Dashboard and admin

#### Cloud agents

- **Clearer Cloud Agent environment build failures.** Failed environment builds now explain what went wrong, such as "Git provider isn't connected", "No access to a repository", or "GitHub IP allow list blocked access", instead of a generic error. You can activate a draft build while it is still running, and build logs now include an **Ask Agent** link. See [Cloud Agent Builds](https://cursor.com/docs/cloud-agent/builds.md#debug-a-build).
- &#x20;**Limit Cloud Agents to selected groups.** Enterprise admins can now set Restrict By to Groups in the Cloud Agents access settings and pick which groups can use Cloud Agents, instead of listing members by name.
- &#x20;**Set spend limits for service accounts.** The service accounts list in the dashboard now shows each account's spend limit and current spend. Admins can edit an account's limit per billing period or set it to No limit.

#### Fixes

- &#x20;**Fixed the team Groups tab.** The Groups tab no longer fails to load with an "invalid int 32" error for some groups.
- &#x20;**Fixed members and invites.** The invite screen now rejects spreadsheets, PDFs, and addresses longer than 255 characters instead of creating broken invites. A newly created invite link now shows up right away instead of appearing missing, and revoking your current session from Active Sessions now signs you out instead of showing an error.
- &#x20;**Model access settings apply more consistently.** Saving a section of the Models page no longer turns a new Cursor model in its 7-day review window on or off by accident. Only an explicit Enable now or Keep disabled choice is saved. Model blocks and release-delay settings for your team now also apply when Auto routes to that model.
- &#x20;**Clearer Network Access Control settings.** The settings now say that the blocklist applies only to the local sandbox, list the patterns each list supports, and warn when an entry, such as an IP address with a port or a path, won't behave as expected in a sandbox list.
- &#x20;**Fixed GitLab for team-owned instances.** On the Integrations page, GitLab repository sync and your personal connection status for a team's GitLab instance now use the team you have selected, so they load and sync correctly.

### Automations

- **Fixes to Slack triggers and channel pickers.** Slack-triggered automations in private channels shared across workspaces now fire for owners who are members of the channel. Slack channel pickers on large workspaces no longer miss channels after a slow load, and Refresh reloads the full channel list.
- **Fixes to automation runs.** Security Reviewer automations triggered by pull request comments or CI completion run again instead of being skipped, and runs whose parent agent is no longer active fail with a clear message instead of retrying.
- **Fixes to the automation editor.** Adding or editing a custom MCP server from an automation's actions no longer drops auth settings such as OAuth scopes.
- **Faster branch picker for Origin repositories.** When you set a branch for an automation trigger on an Origin repository, the default branch now appears right away instead of after the full branch list loads.

### APIs

- **Organization audit logs.** Organization API keys can call [`GET /organizations/audit-logs`](https://cursor.com/docs/account/organizations/organization-admin-api.md#get-audit-logs) to read audit events across the organization. Filter by time range, event type, search text, users, or a single linked team, with pagination.
- **Organization API key expiration.** When you create an Organization API key, you can now set it to expire after 30, 90, or 180 days, or one year. Once a key expires, it no longer authenticates against organization APIs.
- **Look up many commits at once.** The [commit lookup endpoint](https://cursor.com/docs/account/teams/ai-code-tracking-api.md#get-commit-details) accepts a comma-separated list of up to 100 full commit hashes. Lists with three or more hashes used to return 404; more than 100 now returns 400.

### Security and approval agents

- **Smarter follow-ups on findings.** Partly fixed findings are treated as addressed, and a failed follow-up check leaves the existing thread as is.
- **Overlapping findings stay visible.** A new finding overlapping an acknowledged one is posted as its own comment.
- **Model fallback.** Security reviews fall back to the next model when the preferred model is out of capacity.
- **Every run opens.** Every run in the Security Agents run history is now clickable. A run opens its session transcript, or a run summary when no transcript is available.

### Models and Cursor Router

- **New model: Grok 4.7.** [Grok 4.7](https://cursor.com/docs/models/grok-4-7.md) is now available in Cursor.
- **New model: Claude Opus 5.5.** [Claude Opus 5.5](https://cursor.com/docs/models/claude-opus-5-5.md) is now available in Cursor.
- **Shorter Grok model names.** [Grok 4.5](https://cursor.com/docs/models/grok-4-5.md) and [Grok 4.6](https://cursor.com/docs/models/grok-4-6.md) now appear by those names in the model picker and its tooltips, without the "Cursor" prefix.
- **Auto follows team model settings.** When a team admin blocks a Cursor-served model such as [Grok 4.7](https://cursor.com/docs/models/grok-4-7.md), or the team's release delay for new models hasn't passed yet, Auto no longer routes that team's requests to it.

## Week of Sep 14, 2026

### Integrations

#### Slack

- **Full bot alerts in automations.** Automations triggered from Slack now read the full content of bot alerts that use attachment blocks, instead of only their one-line fallback text.

#### GitLab

- **Large GitLab groups and repositories.** The GitLab repository picker no longer times out on large organizations, and resolving a branch or tag works on repositories with thousands of branches.

#### Azure DevOps

- **Reconnect prompt for expired Azure DevOps access.** When Microsoft Entra rejects your Azure DevOps refresh token, Cursor stops retrying and the dashboard shows the connect card so you can reconnect.
- **Large Azure DevOps access tokens.** The dashboard and Cloud Agent starts no longer fail with a server error when your Azure DevOps access token is larger than 4 KB.
- **Per-organization errors in the Azure DevOps repository picker.** When one Azure DevOps organization refuses to list its projects, the repository picker shows an access error on that organization instead of failing the whole picker.

### Dashboard and admin

#### Members and groups

- &#x20;**Groups pushed from your identity provider now appear as team groups.** When your identity provider pushes a directory group through [SCIM](https://cursor.com/docs/account/teams/scim.md#directory-groups), Cursor creates a matching team group in the dashboard and keeps its members in sync. Removing a user from the group in your identity provider removes them from the team group, and deleting the group retires it. Groups that synced before this change keep working as they did.
- &#x20;**Removed members are now signed out everywhere.** When you remove a member from a team that isn't connected to SSO, Cursor ends all of their active sessions so they lose access right away. Sessions stay active only if the member still belongs to another team in the same organization. Your audit log stream also gets a new credentials revoked event that records what happened to the member's sessions, repository access, and cloud agent git tokens.
- **Choose your home team in an organization.** If you're a direct member of two or more teams in your organization that have billing set up, at least one seat, and a subscription that isn't canceled, pick a home team under My Settings > More while a team in that organization is selected in the dashboard. Cursor uses that team for your account when no team is specified, or you can set it to None.
- &#x20;**See a group's Codebase access on a new Access tab.** Team and organization group pages have an Access tab that shows the group's access to your team's Codebase and any repository-specific access, with Manage links to change it.
- &#x20;**Organization admins appear in team member lists.** Team member lists now include admins of the linked organization, labeled Org Admin.

#### Workspace settings

- &#x20;**Turn Projects on or off for your team.** Admins can use the Enable Projects switch in Team Settings, under Chat, to control whether team members can use Projects in Cursor. When it's off, Projects is hidden for everyone on the team.
- &#x20;**Data exports for every team.** The Data Exports tab is no longer limited to Enterprise teams. Any team member with permission to read exports can open it and download archives Cursor has prepared and released for the team, including teams whose subscription has ended. Export links open straight to the right team.
- &#x20;**Team MCP servers on members' machines (since removed from the dashboard).** This week added a Run team MCP servers on members' machines switch to the Team MCP Servers section of the Plugins & MCPs tab. The Plugins & MCPs tab no longer shows that switch. Teams and members can also configure up to 1,000 MCP servers each.
- &#x20;**Connect more than one Jira site to a team.** Admins with a connected Jira site now see a Connect another site action on the Jira page in the dashboard. It opens the Atlassian Marketplace to install Cursor on the new site, and the site list refreshes when you come back.
- **Clearer way back to Agents from settings.** The settings sidebar header now shows a Back to Agents link next to the Cursor mark.

#### Usage and cloud agents

- &#x20;**Security Reviewer spend is easier to track on the Usage page.** Security Reviewer usage is now attributed to Security Reviewer, and you can filter usage events by it. When you filter by Security Reviewer, each review run shows as one row, including the reviewer agents it spawns, instead of being split across many rows.
- **See exactly what a cloud agent environment build used.** Environment [build](https://cursor.com/docs/cloud-agent/builds.md) pages now have a Configuration section that shows the build's source, install and start scripts, terminals, and environment.json. Build logs sit in a collapsible Build output panel with an Ask an agent about these logs button, and they keep streaming past one minute without disconnecting or repeating lines.

#### Fixes

- **Dashboard pages no longer jump while they load.** Overview, Usage, Billing, Cloud Agents, and Integrations pages reserve space for banners, usage tables, and invoices, and the dashboard no longer shifts sideways on first load.
- &#x20;**Fixed MCP server and secrets settings.** The Choose Tools dialog stays on screen with its header and Use Selected Tools button visible, scrolls long tool lists, and trims long tool descriptions to three lines with the full text on hover or click. Editing an MCP server no longer drops extra auth settings such as scopes. The update warning for a new secret now appears only when a secret with that name exists in the same scope.
- &#x20;**MCP restrictions on team groups now apply.** MCP settings saved on a team group are now enforced for the group's members. Editing MCP settings on a SCIM directory group linked to a team group saves them to that team group without dropping its existing restrictions.

### Automations

- **Enable Cursor-built agents from a card grid.** The From Cursor section of the Automations page shows each agent as a card with an enabled or disabled badge and an Enable or Manage button.
- **Clearer delete confirmation.** Deleting an automation from the list or its settings page opens a dialog that names the automation and warns that deletion can't be undone, replacing the browser's confirm popup.
- **Fixes for Security Reviewer.** Security Reviewer keeps syncing when a trigger repository is deleted or removed from the GitHub App, covers the repositories in an organization-wide trigger, and retries Origin, GitLab, and Bitbucket repositories that failed to connect.
- **Automations on Origin repositories.** Security Reviewer now triggers on pull requests in team Origin repositories. Origin check runs from automations are grouped under the product name, such as Cursor Automation, and each run is named after its automation.

### APIs

- **Find groups by ID or name.** [Organization group](https://cursor.com/docs/account/organizations/organization-admin-api.md#organization-groups) objects now include a `publicId`, and [List Organization Groups](https://cursor.com/docs/account/organizations/organization-admin-api.md#list-organization-groups) accepts a `name` query parameter that returns the group with that exact name.
- **Filter organization members.** [`GET /organizations/members`](https://cursor.com/docs/account/organizations/organization-admin-api.md#list-organization-members) now accepts `email`, `userId`, `search`, `organizationRole`, and `teamId` query filters. `email` and `userId` each take up to 100 comma-separated values.
- **Team directory groups.** The [Admin API](https://cursor.com/docs/account/teams/admin-api.md#team-directory-groups) adds `/teams/directory-groups` endpoints to list, create, read, update, and delete a team's directory groups, including each group's name and monthly spending limit, and to add or remove members by user ID.

### Security and approval agents

- **MCP actions after a review.** When a review finishes, Security Reviewer carries out the actions your custom instructions ask for, using the agent's configured MCP servers.
- **Redesigned run transcripts.** Opening a Security Reviewer run that ran on Cursor-managed hosting shows a transcript styled like Cloud Agents.

### Models and Cursor Router

- **1M context kept on Cloud Agent follow-ups.** A Cloud Agent started on the 1M-context variant of [GPT-5.6 Terra](https://cursor.com/docs/models/gpt-5-6-terra.md) now shows 1M in the web follow-up model picker, and follow-ups run at 1M instead of 272K.

## Week of Sep 7, 2026

### Integrations

#### GitHub

- **Accurate GitHub connect errors.** If connecting GitHub fails, the callback page now says whether you were rate limited, hit an authorization problem, or are missing an installation, and shows an error code and request ID instead of a generic rate-limit message.
- **Clear error past the repository limit.** When a request needs access to more repositories than GitHub allows in one installation token, Cursor now explains the limit instead of asking you to reinstall the GitHub App.
- **Team marketplaces refresh from private repositories.** Plugin marketplace refresh can now authenticate through a GitHub App installation owned by another team in the same organization, so marketplaces on child teams pick up updates from private repositories.

#### GitLab

- **Connect self-hosted GitLab to the right team.** Connecting a self-hosted GitLab instance from the Integrations page now links the selected team, and its repositories populate there, instead of your default team.
- **Reliable host removal.** Deleting a GitLab host now removes all of its repositories, even when webhook cleanup fails for some of them.

#### Bitbucket

- **Complete Bitbucket Cloud pull request lists.** Listing closed or all Bitbucket Cloud pull requests now includes merged, declined, and superseded ones.
- **Faster Data Center registration errors.** Registering a Bitbucket Data Center instance now fails within seconds when the host is unreachable instead of hanging through retries.
- **Bitbucket Cloud pull request diffs.** Pull request diffs from Bitbucket Cloud now load when Bitbucket redirects the request.

### Dashboard and admin

#### Admin

- &#x20;**Download team data exports from the dashboard.** Enterprise admins now have a Data exports tab that lists the exports prepared for their team, with a download link for each archive. The tab stays available after a subscription ends, so you can still retrieve your team's data. Available on Enterprise plans.
- &#x20;**Confirm before turning off Security Agents or Approval Agents.** Turning off Security Agents or Approval Agents in team settings now opens a confirmation dialog, where you can optionally share why you're turning it off.
- &#x20;**Build the MCP allowlist from your configured servers.** In team MCP Configuration, the MCP Allowlist's Add Rule menu lets you enter a custom rule or pick one of your team's configured MCP servers, each marked Allowed by default, Already allowed, or Blocked by allowlist. For a URL MCP server, Choose Tools lists the server's tools, after you sign in if needed, so you can pick the tools the policy allows instead of typing their names.
- &#x20;**Confirm decisions on new Cursor models.** On the Models page, choosing Enable now or Keep disabled (previously Block) for a new Cursor model in its 7-day review window now asks you to confirm. Pending rows show the date the model will be enabled automatically and no longer carry a New model label.

#### Analytics

- &#x20;**Redesigned team Analytics charts.** The Active Users chart on the [Analytics page](https://cursor.com/docs/account/teams/analytics.md) now stacks CLI, Cloud Agents, and Bugbot activity with an All line. Every chart shares one color palette with a clickable legend below it. Hover a chart to download its data or copy the matching API curl command.

#### Members

- &#x20;**Team Admin and Org Admin are now labeled separately.** Member lists, role pickers, CSV exports, and the organization member detail page now show team admins as Team Admin and organization admins as Org Admin.
- &#x20;**Members > Set Cap now warns when a higher limit still applies.** If you set a member's spend cap below a higher group or team limit, the dashboard tells you to lower that limit instead. Before, the save went through with no message and the member's limit stayed the same.

#### SSO and SCIM

- &#x20;**SCIM keeps team-owned groups and organization access in sync with your identity provider.** When a directory group maps to a group owned by a team, [SCIM](https://cursor.com/docs/account/teams/scim.md) now adds its members to that team, including existing members who were missing from it.

#### Fixes

- **Fixed several issues in the Automations editor.** User MCP servers are now dimmed in the tool picker, with a tooltip, when an automation runs as a service account. The model picker no longer shows raw model IDs while models load, and the remove button on MCP server rows is always visible.
- &#x20;**Fixed SCIM group mappings that changed the wrong memberships.** Mappings no longer add users to extra teams or refill the root team when a directory group already maps elsewhere, and no longer remove members still covered by another mapped group. Full syncs now defer removals when directory data is incomplete.
- **Fixed issues with cloud agent environments.** Members who can't create team environments can no longer save a new environment with Team scope. When an environment build fails because the repository's GitHub App belongs to another team, the builds page now shows a warning saying so.

### Automations

- **Auto tier now saves in automations.** Choosing Cost, Balance, or Intelligence for Auto in an automation's model picker now saves correctly, and cloud runs launch with the tier you picked. Before, every tier reopened and ran as Balance.
- **Model pickers no longer flash raw model IDs.** The model pickers in the automation prompt editor wait for the model list to load instead of briefly showing internal model IDs.
- **Fixes to automation saves.** Saving an automation on a self-hosted GitLab repository whose host uses a host-level service account no longer fails while setting up webhooks.

### Security and approval agents

- **GitLab and Bitbucket reviews.** Security Reviewer now reviews GitLab merge requests and Bitbucket pull requests, posting a summary comment and a status check on the change.
- **More runs in run history.** The Security Agents run history now includes Security Reviewer runs that ran on Cursor-managed hosting. Click one to open its session view.
- **Confirm before turning off.** Turning off Security Agents or PR Routing & Approval for your team now asks you to confirm, and you can optionally say why.

### Models and Cursor Router

- **New model: Muse Spark 1.3.** [Muse Spark 1.3](https://cursor.com/docs/models/muse-spark-1-3.md) from Meta is now available in Cursor.
- **Cursor Grok 4.6 sees images directly.** [Cursor Grok 4.6](https://cursor.com/docs/models/grok-4-6.md) now receives images you attach and images returned by tools as images, instead of working from text descriptions of them.

## Week of Aug 31, 2026

### Integrations

#### GitHub

- **Clearer error for suspended GitHub App installations.** When the Cursor GitHub App installation is suspended, Cursor now says so and points you to the app status in your GitHub organization settings.
- **Stale Bugbot comments are cleared.** When Bugbot clears reviews from a previous run on a GitHub pull request, their bodies are replaced with a short "Stale Bugbot comment from a previous run." note. Comments from anyone else are left alone.
- **Correct GitHub Enterprise installation.** When installation IDs from different GitHub Enterprise Server instances collide, Cursor now picks the installation of the GitHub Enterprise app your team or account owns.

#### Azure DevOps

- **Bugbot works with spaces in names.** Bugbot no longer fails silently on Azure DevOps repositories whose organization, project, or repository name contains spaces.

### Dashboard and admin

#### Cloud agents

- &#x20;**Manage Self-hosted Machines pools from the Cloud Agents dashboard.** Team Pools is now called Self-hosted Machines. The All Self-hosted Machines page lists each pool with its repository, active and idle machines, total machines, and a Sessions column. Admins can set a pool's Reconnect Window or delete a pool without taking its connected machines offline. See [Self-hosted pools](https://cursor.com/docs/cloud-agent/self-hosted/pool.md).
- &#x20;**See Cloud Agent activity at a glance, with full run history on a new Runs page.** The Cloud Agents page now opens with Total runs, Success rate, and Recent runs cards for the date range you pick. Select All Runs to open the Runs page, with a run history chart, a runs table, and filters for trigger, status, and creator. Team admins see runs across the team, and personal users see their own.

#### Members, groups, and SSO

- &#x20;**Remove members from your organization.** Organization admins can now choose Remove from Organization from a member's row menu on the organization Members page. After you confirm, the person loses access to every team in the organization and can move to an individual Cursor plan. You can't remove yourself this way.
- &#x20;**Copy settings from an existing team when you create an organization team.** A new step when you create a team in an organization lets you pick a source team and choose which settings to copy: models, security, rules and commands, hooks, MCP and plugin policy, spending limits, and team access defaults. A preview shows what each category will copy and lists connections, such as the GitHub App or MCP servers, that you'll need to set up again.
- &#x20;**Directory groups move into groups without losing spend limits.** SCIM directory groups that have moved into [organization groups](https://cursor.com/docs/enterprise/organization-groups.md) no longer appear twice on the Groups page or in directory settings, and ones not yet moved show a Legacy badge. Filtering analytics or members by a moved directory group includes its new group's members. Members with a lower individual spend limit keep it instead of getting the group's higher limit.
- &#x20;**Sort group members by usage and spending limit.** On the Members tab of a group synced from your identity provider, click the Username, usage, On-Demand Spend, or Limit column header to sort, and click again to reverse the order. When you sort by limit, members with no limit appear last.
- &#x20;**Warning before SCIM sync removes team members.** When you switch a team or group to Synced, or change which directory groups it syncs from, the dashboard now asks you to confirm before saving. The warning explains that members outside the selected groups are removed, and that switching back to Manual doesn't restore them. Read more about [SCIM provisioning](https://cursor.com/docs/account/teams/scim.md).

#### Analytics

- &#x20;**Refreshed Analytics charts.** Charts on the Analytics page and the dashboard overview share one color palette, a more compact layout, and a two-column tile grid on mobile and tablet. The AI commits chart labels the editor series Desktop and replaces Primary Branch Only with a Primary Branch checkbox. See [team analytics](https://cursor.com/docs/account/teams/analytics.md).

#### Settings and navigation

- &#x20;**More models in admin model settings, and simpler Fable data-retention consent.** Newer models now appear in admin model settings, so admins can enable, disable, or restrict them, and Muse Spark models appear under Meta on the Models page. Teams that accepted the data-retention consent for Claude Fable 5 don't need to accept it again for Fable 5.1. In organization and group settings, the exemption section is now called "Anthropic: Claude Fable Data Retention Exemption" and links to Organization Groups for organizations that include contractors or other third parties.
- &#x20;**Clearer Origin switch in team settings.** The Origin section of team settings now has an Enable Origin switch: on means your team can create Origin repositories. It replaces the old "Disable creating Origin repositories" switch, and your current setting is unchanged. The description explains that turning Origin off makes existing repositories read-only and hides the Codebase tab.
- **Shared organization links open your own organization.** Links to cursor.com/organization now open the same page in your organization's dashboard, keeping the rest of the path and any query string. If your account isn't part of an organization, you see a not-found page.
- **Easier navigation on mobile and clearer page titles.** On a phone, tap a dashboard page title to jump to another section from a dropdown, and open your account from the avatar in the header. The Overview, Analytics, and Usage pages now show a title at the top.

#### Fixes

- &#x20;**Fixed SCIM group sync.** Members provisioned through SCIM are now added to organization groups and passed on to mapped teams instead of being skipped, and synced groups no longer get stuck in an errored state. Adding a group-to-team mapping no longer removes existing team members. Creating a group with a duplicate name, or deleting a group that still has SCIM mappings, now explains what went wrong.
- &#x20;**Fixed the Integrations page for multi-team organizations.** Disconnecting GitLab now disconnects the team you have selected, and GitHub Enterprise, GitLab Self-Hosted, and Bitbucket Data Center rows load installations for that team. Self-hosted GitLab connections no longer fail when another team in the organization already registered the same host. Long instance names now end with an ellipsis, and integration rows lay out correctly on mobile.
- &#x20;**Cloud Agent secrets no longer show another team's secrets.** When you switch teams, the secrets list now shows the selected team's secrets, and creating, editing, and deleting secrets applies to that team instead of your default team.
- **Cloud Agents settings pages keep their header while you scroll.** Environment detail pages, Repository Routing, Team Secrets, and My Secrets now have a sticky breadcrumb header in place of the old back links. The Environments list has a compact Repo filter, and Edit is now the primary action on an environment's page.
- **Fixed tooltip and diff glitches in settings and admin pages.** The Billable Seats tooltip on the Members page now opens below its label instead of hiding behind the header, and Audit Log value diffs no longer show stray "No newline at end of file" markers. The API Keys and Protected Git Scopes sections also have more consistent layouts.

### Automations

- **Search remote machines when picking an environment.** The Remote Machines menu in an automation's environment picker is now searchable by machine name, path, repo, or pool, and groups your own machines under My Machines. Pools show how many workers are active and whether they are busy.
- **Approval Agents only offer supported repositories.** When you set up an Approval Agent, the trigger menu and the org and repository pickers only offer repositories Approval Agents support, so you can no longer pick a GitLab or Bitbucket repository. If an unsupported repository is still selected, saving shows an error asking you to remove it.
- **Fixes to automation launches and runs.** Automations on GitLab repos no longer fail to launch when a repo needs re-linking, and automations owned by removed team members are reliably disabled.
- **Teammates can manage team automations.** Deleting a team automation now works from the team you have selected instead of failing access checks, and teammates other than the creator can save Slack channels on managed review agents such as Security Reviewer.

### APIs

- **Manage organization groups from the API.** The [Organization API](https://cursor.com/docs/account/organizations/organization-admin-api.md#organization-groups) can now create, rename, and delete groups, and set or clear a group's monthly spending limit. Group responses include `memberCount` and `monthlySpendingLimitDollars`.
- **Model access covers every configurable model.** The [model access](https://cursor.com/docs/account/organizations/organization-admin-api.md#model-access) routes now list and accept every model you can configure, including hidden models and all of their parameters. Models that are unavailable, end-of-life, or internal no longer appear and are rejected.
- **Set spend limits in bulk.** The [Admin API](https://cursor.com/docs/account/teams/admin-api.md#set-user-spend-limits-in-bulk-preview) adds `POST /teams/user-spend-limits`, in preview, to set or clear spend limits for up to 100 team members in one request. The response reports each member as `updated`, `unchanged`, or `failed`.

### Security and approval agents

- **Search your security agents.** The Security Agents list has a search box that filters agents by name.

### Models and Cursor Router

- **New model: Claude Fable 5.1.** [Claude Fable 5.1](https://cursor.com/docs/models/claude-fable-5-1.md) is now available in Cursor. With Privacy Mode on, or on an Enterprise plan, Anthropic's data retention terms must be accepted before it can be used.
- **New model: Gemini 3.8 Flash.** [Gemini 3.8 Flash](https://cursor.com/docs/models/gemini-3-8-flash.md) is now available in Cursor.
- **Fast mode in Max Mode for GPT-5.6.** You can now turn on Fast for [GPT-5.6 Sol](https://cursor.com/docs/models/gpt-5-6-sol.md), [GPT-5.6 Terra](https://cursor.com/docs/models/gpt-5-6-terra.md), and [GPT-5.6 Luna](https://cursor.com/docs/models/gpt-5-6-luna.md) in Max Mode. Previously, turning on Fast switched these models out of Max Mode's long context.
