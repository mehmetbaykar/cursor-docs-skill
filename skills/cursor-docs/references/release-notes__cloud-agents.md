---
title: "Cloud Agents release notes"
source: https://cursor.com/docs/release-notes/cloud-agents
path: /docs/release-notes/cloud-agents
---

# Cloud Agents release notes

Weekly changes to [Cloud Agents](https://cursor.com/docs/cloud-agent.md). Each entry covers one week of changes and is labeled with the Monday that starts it.

## Week of Sep 28, 2026

### Environments

- **Environment builds are always on.** Environment builds can no longer be turned off. Every environment that isn't a draft now gets automatic builds, and Cloud Agents start from the latest build. Environments that previously had builds turned off now show their active build and recurring build failures, and the Trigger build dialog no longer warns that builds are off.
- **Fix Build works on builds whose snapshot expired.** Clicking Fix Build on a failed environment build whose snapshot has expired now starts the agent instead of failing. The agent boots the latest successful build and works from the failed build's logs. Launching an agent from a Dockerfile build failure also prefills the composer with a prompt to investigate and fix the build.
- **Fewer environment build failures from source control hiccups.** Automatic environment rebuilds keep running after a temporary source control access failure and stop only after three such failures in a row. Builds that fail because a self-hosted source control server is down are now reported as a source control outage.
- **See which environment changes came from the API.** In an environment's version history, saves made through the public API are now labeled "API".
- **Wildcard allowlist entries include the parent domain.** A network allowlist entry like `*.example.com` now also lets Cloud Agents reach `example.com` itself, not just its subdomains.

### Agents

- **Pinned agents follow you across devices.** Pinned agents on the web agents list are now saved to your account, so your pins follow you across browsers and devices. The agents sidebar now groups agents into Today, Last 7 days, and an Older section that starts collapsed.
- **Start an agent from a closed pull request.** You can now start an agent from a closed pull request whose head branch was deleted. The agent works on a new branch from the base branch, and the panel tells you so.
- **Clearer errors when an agent can't start.** If an agent fails to start because you lost access to one of its repositories, the error now names that repository. When only your Other Models usage has run out, the error reads "Out of Other Models usage" and suggests switching to a named model or raising on-demand usage. When an agent's machine runs out of memory, the error suggests running memory-heavy steps on fewer files or with lower parallelism.
- **Faster agent pages on the web.** Opening a Cloud Agent conversation on cursor.com no longer refetches changes that are already loading or up to date, and going back to the agents list is quicker because the list is loaded in the background.

### Slack

- **Slack model picker uses the web model catalog.** The Cloud Agents Slack settings model picker now builds its list from the same model catalog as the web picker and keeps your saved default selectable. The Slack model command now accepts any model you can use, instead of a fixed list.
- **Set a channel's Self-Hosted pool from Slack.** Any team member can now run `@Cursor pool set <name> channel` or `@Cursor pool unset channel` in Slack. Every change to a channel's default repository or Self-Hosted pool is announced in the channel.

### Fixes

- **Fixes to agent runs and follow-ups.** Sending a follow-up after stopping an agent early in its first step now works instead of failing with a VM not found error. Switching between Best-of-N tabs now loads the selected candidate's conversation. Agents started on a saved environment that changed after its last build no longer fail at startup with a build version mismatch.
- **Fixes to multi-repo environments.** Cloud Agents now start normally even when one of your multi-repo environments has colliding clone paths; before, that one environment made every start fail. Saving an environment whose generated name lists many repositories no longer fails.
- **Fixes to the Cloud Agents dashboard.** If the Cloud Agents settings page can't load privacy settings, it now shows an error with a Try again button. Failed loads on the runs pages also offer Try again, and the runs summary reads "1 run" instead of "1 runs".
- **Bitbucket file reads stay inside the repository.** Cloud Agents on Bitbucket Cloud repositories can no longer read files outside the repository through paths that use `..`, and paths like `./.cursor/environment.json` are read correctly.

## Week of Sep 21, 2026

### Environments

- **Activate a draft environment build while it's still running.** You can now click Activate on a draft build that is still in progress, and it becomes the active build for your environment as soon as it finishes. Activating a draft whose snapshot has already been deleted is still blocked, and no longer changes your saved environment settings.
- **Default-on environment builds work like turned-on builds.** Environments with no build setting of their own, where builds are on by default, now show their Active Build and the failing-builds warning, and are rebuilt when a build is triggered, so agents in them start from a fresher build.

### Agents

- **Long-running mode removed from the web.** The Long-running option in the web model picker, its time-limit pill, and the team Long-running agents setting are gone. Cloud Agents started from the web always run in standard mode.
- **Coordinators can switch a worker's model.** A Project coordinator can now move a worker to a different model when it sends the worker a message. The new model applies from the worker's next turn.

### Self-Hosted Machines

- **Shorter self-hosted options in Slack, GitHub, and Linear.** Add `sh=t` to a Slack, GitHub, or Linear request to run the agent on your self-hosted pool. `self_hosted` also accepts `t`/`f` and `1`/`0`, and all three surfaces now take the same options. Options written inside Slack code blocks no longer start or configure an agent.
- **Take control of desktops on Self-Hosted Machines.** Taking control of a Cloud Agent's desktop now reaches the machine you're viewing, including agents on Self-Hosted Machines. Older machines fall back to the previous takeover.
- **Agents on your own machines handle git and setup more carefully.** Cloud Agents on Self-Hosted Machines now check the machine's git name and email before committing, and set a repository-only fallback only if none is set. They ask for credentials on the machine instead of assuming Dashboard secrets or a signed-in GitHub CLI. On My Machine, agents prefer project-local setup over system-wide installs and global config changes.
- **Slack uses a channel's default Self-Hosted pool.** `@Cursor` launches in Slack now use the channel's default Self-Hosted pool when one is set, then the team default. If a launch is rejected, the reply names the channel default and how to change it with `@Cursor pool set <name> channel`.

### Models

- **Grok 4.7 on the Start plan.** Start plan users can now pick Grok 4.7 for Cloud Agents, fixed at medium effort and standard speed.

### Reliability

- **Clearer errors when image generation fails.** Image generation failures in a Cloud Agent now show a readable explanation instead of a raw status code.
- **Fixed moving some local chats to the cloud.** Moving a local chat to a Cloud Agent without typing a new message no longer fails with a "Missing required fields" error when the chat's saved state has no turns. The Cloud Agent now starts idle, keeps the chat's history, and runs your next follow-up.

### Fixes

- **Fixes to environments and agent starts.** Starting a cloud agent no longer overwrites the environment's saved repositories, and boots the default branch when no branch is given. Failed environment builds now report the specific cause (clone, source-control access, or pod start), and agents started with agent-scoped secrets now boot from the environment's build.
- **Fixes to Self-Hosted Machines.** Agents and subagents started on a self-hosted pool that accepts any repository now get picked up instead of waiting forever, and idle or deleted-run machines free up right away instead of showing as busy. Agents on Origin repositories that were detached from GitHub now receive their configured secrets.
- **Fixes to MCP connectors in Cloud Agents.** Connector tools that Cloud Agents list now accept the calls made to them, including for connector accounts with custom labels. Plugin-backed MCP servers that an admin granted now serve their tools, even when the dashboard label differs from the plugin name or the agent runs as a deployment service account. The environment info tool now shows every documented `environment.json` field, and for subagents it reports the network egress policy that is actually enforced.
- **Fixes to agent runs and follow-ups.** A follow-up sent while an agent's machine is being recreated is now saved to the queue immediately, so it no longer looks lost until the new machine is ready. An agent's link to its Origin pull request no longer disappears after a temporary lookup failure. Agents started or followed up with a specific model variant are now checked against your team's model policy using that variant, so they're no longer wrongly blocked. An agent left stuck behind a queued run that never started accepts follow-ups again after an hour instead of rejecting them.
- **Fixes to artifacts in agent pull requests.** Artifact links that an agent puts inside tables or other HTML in a pull request description now render as working links instead of raw text. Pull requests no longer get public artifact links for files that couldn't be confirmed to exist, and agents with many artifacts no longer re-announce the same artifacts as new on later turns.
- **Fixes to Slack message formatting.** Agent replies in Slack keep links whole, including URLs with parentheses or `&` and link text with brackets. Bold italic text, `~~~` code fences, task-list checkboxes, and images (now shown as links) render correctly, and text like `__init__` or `2*3*4` is no longer mis-styled.
- **Fixes to the Cloud Agents page and dashboard.** On cursor.com/agents, the first page of agents is now fetched on the server while the page renders, so it shows up faster on a full page load. In machine settings, the remote control toggle now explains why it is off and who can turn it on. Runs summary stat cards also reflow to fit the available width.

## Week of Sep 14, 2026

### Agents

- **Follow-ups to agents archived elsewhere now go through.** If you archive an agent on another client, such as the desktop app, and then send a follow-up from a tab you already had open on the web, Cloud Agents now unarchives the agent and delivers your message instead of failing. This works from the agent chat, resubmitted messages, side chats, and the review agents sidebar on pull request pages. Deleted agents stay closed.
- **Plan and limit dialogs appear where you start the agent.** When a Cloud Agent can't start because of your plan, usage pricing, model choice, or a protected scope, the dialog explaining why now opens on the page you started from, for pages within the agents area of cursor.com, instead of later on the agents page.
- **Draft pull requests stay in draft.** Fixed an issue where Cloud Agents marked their draft pull requests ready for review on their own, even when your repository rules said to keep them as drafts. Agents now follow your instructions and repository guidance, and still mark a PR ready when you ask.
- **Fixed agents reading the default branch when started on another branch or commit.** When you start a Cloud Agent on a specific branch or commit, it now waits until that ref is checked out before running any tools, so it no longer reads files from or describes the default branch first.
- **Cloud Agents keep their environment and files when it is moved to another machine.** Previously, if an agent's environment was moved while you sent a follow-up, the agent could report that the environment was unreachable and continue in a fresh one, losing your files. Now the agent shows "Reconnecting to your environment. This can take a few minutes.", retries on its own, and continues in the same environment with every file in place. If reconnecting takes too long, it asks you to send your message again instead of starting over.
- **Pin up to 75 agents.** The agents list on cursor.com now lets you pin up to 75 agents, up from 50.
- **Blocked models are now rejected as soon as you send a follow-up.** If you switch a Cloud Agent follow-up to a model your team admin has blocked, you now get a Model Blocked error right away. Before, the follow-up was queued and then failed mid-run or quietly ran on a different model.
- **Fixes to page layout on the Agents web app.** Opening a conversation, repo, or pull request no longer makes the page jump when the sidebar collapses, and the sidebar loads already collapsed if you keep it that way, or when you open a conversation in a narrow window. The agents list no longer shifts sideways when its scrollbar appears, or moves down when promotions, the Cursor Learn banner, or the connect source control prompt show up after the page loads.
- **Fixes to Cloud Agent runs and follow-ups.** Queued follow-ups, repo skills, and slash commands now load in side chats, and repo command pills from the composer pass their contents to the agent. PR creation failures from GitHub rate limits now say how long to wait.
- **Fewer failed starts and follow-ups.** When a Cloud Agent can't get a worker to start its session, it now retries on its own; if it still can't, it says "Cloud Agent could not get a worker to start your session; please retry in a few minutes." Follow-up turns no longer pick up another account's personal rules or skills from the workspace. The slash command menu of a failed or archived agent stops waiting for commands that will never load, and folders deleted from an agent's Context no longer reappear with leftover files.
- **Faster starts on a named branch.** Cloud Agents started on an explicitly named branch, whether the default branch or another one, can now use the faster startup path instead of falling back to the older start.

### Projects

- **Team admins' Projects setting now applies to Cloud Agents.** When a team admin turns off Projects, the team's Project agents no longer show up in Cloud Agent lists, and starting a new Project fails with "Projects are disabled for your team." Personal accounts, and teams that haven't changed the setting, keep Projects on.
- **Fixes to Projects coordinator and worker agents.** Coordinators can now start workers after a Project's repository is published under a new name, and PR label edits, environment drafts, and shared links use the published name too. Force-submitting a message to a worker no longer leaves the coordinator's call to it stuck as running. When a worker can't be created, the coordinator gets the real reason, such as hitting the nesting limit, instead of retrying a generic error.
- **Cloud workers share the Project's Context.** Cloud workers that a Project coordinator creates now use the coordinator's Context as their own, so files they save there are visible across the Project. Moving a worker out of the Project gives it its own Context again.

### Environments

- **Fixes to environment builds.** Builds stuck in progress no longer block scheduled builds, and stuck builds are marked failed after 9 hours instead of 24. The environments list also loads for large teams instead of timing out. Team environment builds that failed because the team's build account couldn't access a repository now rebuild with the access of the person who started the agent.

### Self-Hosted Machines

- **Self-hosted pools now respect repository access.** Starting a cloud agent on a team's Self-Hosted Machines pool now fails with an access error if you can't read the repository. Pool listings only show the repositories you have access to, and API keys limited to certain repositories can only use pools for those repositories.
- **Self-hosted agents without a repository can set one up.** Agents on Self-Hosted Machines that start without a repository now follow your worker's rules and credentials to find or clone the repository they need, instead of saying they have no repository access. If no rule explains how to get the repository, the agent says it isn't configured rather than guessing a clone URL.
- **Fixes to self-hosted and private workers.** Agents on pools whose machine is still booting wait for it instead of failing, dead worker connections reconnect or reassign instead of failing with a closed-transport error, and agents on Windows workers no longer break the clients that display them. Subagents sharing a parent's worker no longer orphan the parent's workspace.

### Integrations

- **More reliable self-hosted routing from Slack, GitHub, and Linear.** Mentioning the word `self_hosted` in a request no longer sends the agent to a Self-Hosted Machine by accident. Opt in explicitly with `self_hosted=true`, which now also works inside inline code and with trailing punctuation. In GitHub and Linear, options inside fenced code blocks are ignored. In Slack, `pool=<name>` for a self-hosted pool with no repository now starts the agent on that pool instead of failing to match the team's default repository.
- **Jira launches use the right repo host.** Cloud Agents launched from Jira with a default repo set as `owner/repo` now run against that repo on your connected GitLab or Azure DevOps host, instead of assuming github.com.

### MCP

- **Cloud agents with many MCP tools no longer fail on model tool limits.** When your MCP servers expose more tools than a model accepts, cloud agents now cap the MCP tools they send, keeping browser and custom tools first, instead of failing the request.
- **Clear error for empty Cursor-hosted repositories.** Starting a cloud agent or environment build on an empty repository hosted on Cursor now says the repository is empty and asks you to add an initial commit, instead of showing a generic failure.

### Dashboard

- **Fixes to Cloud Agents settings and machines pages.** The My machines list no longer shows the previous team's machines after you switch teams, and its page is kept in the URL so links and back navigation land on the right page. Closing the New environment dialog in any way, including browser back, now clears the draft instead of leaving stale repositories, name, and scope. Settings sections such as Preferences and Security have shareable anchor links, and counts show thousands separators.

## Week of Sep 7, 2026

### Agents

- **The agent steps back when you take control of its desktop.** When you take control of a Cloud Agent's desktop, the agent stops using the computer instead of competing with you, and the desktop is released as soon as a computer-use subagent finishes.
- **Faster starts when you name the default branch.** Cloud Agents started with the repository's default branch named explicitly, as the desktop app does, now reuse the prebuilt environment, the same as starts that name no branch, so they reach the first response sooner.

### Projects

- **Project coordinators and workers show the right state.** A Project coordinator is now marked unread only after a turn in which it actually sent you a message, and the messages it sends you now appear in the agent's conversation history. Workers and subagents that finished stay marked finished when a new message or a resubmitted message interrupts the turn that reports their completion.

### Pull requests

- **Pull requests from mirrored repositories open in the right place.** When a repository is mirrored between GitHub and Origin, Cloud Agents now open the pull request on whichever side is the source of truth and tell you which one they used. If the agent can't create the pull request, it reports the reason instead of working around it with another tool. Pull request links for mirrored repositories now point to the GitHub, GitHub Enterprise, or Origin host where the pull request actually lives, and agents no longer target a commit SHA as the base branch.
- **Merge approvals show the exact commit an agent will land.** When a Cloud Agent asks for approval to merge a pull request on an Origin repository, the request now shows the commit subject and message the agent chose, in both the mobile approval sheet and Slack. You approve the commit that actually lands in history, not just the pull request title.

### Subscriptions

- **CI subscriptions on your default branch no longer wake an agent on every merge.** When a cloud agent subscribes to CI on a repository's default branch, such as `main`, it now wakes once for the next finished CI result, and then the subscription closes. To have an agent keep watching a pull request's CI, have it subscribe to the PR's branch.

### Environments

- **Fixes to environment setup.** The environments list loads faster for teams with many environments. The numbered steps in the environment setup intro dialog now line up evenly.

### Self-Hosted Machines

- **Fixes for Cloud Agents on self-hosted workers.** Trying to attach to the workspace of an agent on a self-hosted worker now shows "Workspace runs on a self-hosted worker" right away, instead of waiting on a workspace that never becomes ready.
- **Fixes to self-hosted worker claims.** Self-hosted workers that reconnect no longer stay stuck on a stale claim, so they can be picked up for new agents again. Claim rejections no longer show up as "No self-hosted workers available", and claimed workers that never received a message are now released after the idle timeout.

### Slack

- **Set a team default Self-Hosted pool for Slack.** Team admins can run `@Cursor pool set <name>` so `@Cursor` mentions run on that Self-Hosted pool without adding `pool=` each time. If the pool serves any repository, mentions that name no repository can still launch an agent there. `@Cursor pool` and `@Cursor settings` show the current default, and `@Cursor pool unset` clears it.
- **Fixed Slack follow-ups that reached an agent without the thread.** When you mention Cursor in a Slack thread before its Cloud Agent has posted a reply, the agent now receives the whole thread, including forwarded messages and files, instead of only your latest message. Follow-ups sent from the follow-up dialog get the same full context.
- **Mentioning @Cursor in another team's agent thread now starts a new agent.** When you mention @Cursor in a Slack thread where the agent belongs to a different Cursor team, Cursor now starts a new Cloud Agent for you. Before, it refused and suggested Team Followups, which can't share agents across teams. If a follow-up is still denied, the message now says the agent belongs to another team.
- **Fixes to launching agents from Slack.** When a Slack launch fails, the reply now names the repository and the real cause, such as no access, repo not found, a disconnected source control provider, or GitHub being unreachable, and links to GitHub Status and a Try Again button for that last case. Mentioning Cursor several times in one thread no longer starts duplicate agents when an earlier launch is slow, and your saved default repo and branch now still apply after your Slack workspace is migrated.

### Jira

- **More reliable Cloud Agents from Jira.** Cloud Agents started from Jira keep working with the latest Jira agent protocol, and show as working instead of paused while they run. Each new request from Jira now starts its own conversation, follow-up messages on an active task no longer fail, and stopping an agent while it starts now pauses it once it launches.

### Fixes

- **Fixes to Cloud Agent reliability.** Stopping an agent no longer shows a spurious provider error, follow-ups no longer fail to restore the branch when untracked files are in the way, and unnamed terminals in environment.json now start. Plugin slash commands in follow-ups now wait briefly for a plugin that isn't ready yet instead of skipping it.

### Web app

- **Fixes to the agents web app.** Clicking an agent in the agents sidebar on cursor.com no longer bounces back to the previous agent, and back and forward restore the tab you had open. A new agent started from the web now shows its logs and conversation once it's created, instead of missing them.

## Week of Aug 31, 2026

### Agent runs

- **Fewer pointless wake-ups from subscriptions.** Cloud agents subscribed to GitHub CI or pull request events no longer wake for repeated passing CI results, their own pushes and PR edits, or label, title, and assignee changes. A failure, or the first green after one, still wakes the agent. When an event needs no action, the agent now ends its turn quietly instead of posting a filler reply in Slack or on the PR.
- **Plugin slash commands work in follow-ups.** You can now use a plugin slash command in a follow-up to a Cloud Agent, even if that plugin wasn't selected when the agent started: the agent installs the plugin before it runs the turn. If the plugin can't be installed, the agent says so and asks you to remove the command and send it again, or start a new agent.
- **Coordinator messages reach busy workers sooner.** In Projects, a message a coordinator sends to a worker that is in the middle of a turn is now delivered into that turn by default, instead of waiting for the turn to end. A worker that isn't running gets it as its next message.

### Environments

- **Clearer environment setup agents.** The first time you open an environment setup agent on the web, a short dialog with a video explains what the agent will do: install and verify your app, ask for secrets or network access, and prompt you to review and save the configuration. Setup agents are now named after the repository, like "Set up my-repo environment", and transcripts no longer show an environment line when the linked environment has no configuration.
- **Pin cloud roles to a single environment with OIDC tokens.** The identity token endpoint inside the agent's environment now accepts `sub_claim: "environment_id"`, which puts the agent's environment ID in the token's `sub` claim, so verifiers like AWS STS that only match `sub` can trust one environment. If the agent has no environment, the mint fails instead of falling back to the default subject.
- **Fixed Origin CLI commands failing in Cloud Agents with restricted network access.** Cloud Agents with restricted network egress working on repositories hosted on Cursor now automatically allow the Origin API hosts alongside the Git host, so `origin` CLI and API commands connect instead of failing. Other repositories and your custom allowlists are unchanged.

### Self-Hosted Machines

- **Fixed `pool` labels in Linear so runs go to your Self-Hosted Machines pool.** A Linear issue or project label whose parent label is `pool` now sends the Cloud Agent run to the pool with that name, as the docs describe. This also works when you assign or delegate an issue to Cursor, which has no comment to read. Before, those runs quietly used Cursor-hosted machines. Writing `pool=<name>` in the `@Cursor` comment still overrides the label.
- **Agents can find your Self-Hosted Machines.** When you ask a Cloud Agent to run work on a self-hosted machine, it can now list the connected machines you have access to and pick one. Before, the agent could fail with a tool-not-found error that made it look like your machine was gone.

### Integrations

- **Better Slack previews for Cursor-hosted pull request links.** Pull request links from Cursor-hosted repositories now unfurl in Slack with a formatted excerpt of the description, kept short so previews stay compact on Slack mobile. Links to a pull request's tabs, like its changes or commits, now unfurl too.

### Notifications

- **Fewer noisy push notifications from Cloud Agents.** Cloud Agents no longer push a turn-finished notification to your phone or browser. You still get push notifications when an agent asks a question or needs your approval.

### Performance

- **Faster environment loading.** MCP server configs now load in parallel for users with many servers. The environments list also loads faster and no longer times out for large teams with many repositories.

### Fixes

- **Fixes to environment and repository setup.** Saving an environment with a deleted environment's name now creates a new one, and starting an agent with an unknown environment name reuses the repo's existing environment. Multi-repo agents no longer fail on GitLab repos missing from the repo list. Repository checkout now retries on temporary proxy errors, and teams using Customer PrivateLink no longer see clone failures during environment builds or lose git access mid-run.
- **Fixes to self-hosted workers.** Cloud agents on self-hosted workers no longer fail to start or resume after an earlier failed attempt when idle workers are available, and they no longer fail with a screen recording error. Plugin slash commands and skills now show up when the plugins were already installed on the worker. Coordinator and worker notifications and PR actions also work again on workers with a repository set.
- **Fixes to MCP authentication and agents that manage other agents.** Cloud agents no longer pause to ask you to authenticate an MCP server that's already connected, and stopping an agent during MCP authentication now closes the Authenticate card instead of leaving it pending. When an agent starts or messages other agents, the start card now completes after the new agent's first turn, and a queued message that gets removed ends as canceled instead of waiting forever. When a subagent can't start because your included usage for its model has run out, the error now names the model. On the iOS app 1.9.0 and later, Cloud Agents that need MCP sign-in now show the sign-in card instead of a fallback message.
- **Fixes to cloud agent runs.** Cloud agents started from a registry model now run with the effort and parameters you pick in the model picker, not the model's defaults. Cloud agent runs and integration launches now use your account's current privacy mode instead of an outdated setting. Messages you send to a running agent now arrive in the order you sent them, even when an earlier message missed the agent's current step and waits for its next turn.

### Web app

- **Cleaner Cloud Agents layout on your phone.** On mobile, the agents pages on cursor.com use slightly larger text, a centered top navigation without the Dashboard tab, and a logo that takes you back to your agents. Search and the source filter now sit inline with the agents list, the composer has a taller input, and the menu button shows your profile photo.
