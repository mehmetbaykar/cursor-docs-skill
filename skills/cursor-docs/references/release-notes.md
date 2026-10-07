---
title: "Release notes"
source: https://cursor.com/docs/release-notes
path: /docs/release-notes
---

# Release notes

Every Cursor product in one timeline, newest first, with up to 10 recent releases each. Filter by product, open a product's page for its full history, or follow along with the [RSS feed](https://cursor.com/docs/release-notes/rss.xml).

## 3.23

### Chat and composer

- **Cmd+F reliably searches the chat.** Cmd+F now opens find in the chat transcript whenever the chat or prompt has focus, or focus is anywhere outside the editor panel and Customize. File, diff, terminal, and browser find open only when you're working in that panel, and the fullscreen conversation tray now has its own find bar. Chat find also matches only text you can see, no longer flashes "0 of 0" while it searches, and uses the same yellow highlights as diff and browser find.
- **Move through long conversations from the keyboard.** Press Cmd/Ctrl+Up or Cmd/Ctrl+Down to jump between your messages, and Cmd/Ctrl+Shift+Up or Cmd/Ctrl+Shift+Down to jump to the top or bottom of the conversation. The shortcuts also work while the prompt has focus, as long as it's empty.
- **Reference pull requests with `#`.** Type `#` in the prompt box to pick from your pull requests, including the ones the current agent opened, and add one to your message as context. This also works in follow-up question inputs and when you edit a sent message.
- **Minimize or remove the plan above the prompt.** The plan card above the prompt now has a Minimize button that collapses it to a Plan pill, so it stays out of the way while you keep chatting. Right-click the Plan or Canvas pill and choose Remove to clear it. The plan card also takes priority over follow-up suggestions and opens once another card closes.
- **Approval prompts explain why they appear.** When an agent asks to edit or read a file outside your workspace, or to edit a protected config file, the approval card now says why, for example "This edits a file outside your workspace." Read approval cards show the full file path with an Allow button.
- **Queued messages no longer get lost.** Messages you queue while an agent is working are no longer dropped when a turn ends.

### Cloud agents

- **Drop local files into prompts for SSH, WSL, and dev container agents.** When you drop, paste, or attach a file or folder from your computer into the prompt of an agent running on a remote machine, the Agents Window copies it to that machine and mentions the copy, so the agent can read it. Copies go to a separate uploads folder outside your workspace, so they never show up as workspace changes, and slow copies show a progress notification.
- **Drop a folder onto a cloud agent prompt to attach its files.** Dragging a folder onto the prompt of a cloud agent now attaches the files inside it, skipping hidden files. Up to 20 files are attached per drop, and a notice tells you when a folder had more and only the first 20 were added.
- **Slack mentions are readable in cloud agent prompts.** When a cloud agent starts from Slack, people mentioned in the prompt now show as @Name instead of raw Slack user IDs. Clicking a mention opens that person in the Slack app if it's installed, or in Slack on the web otherwise, and Find matches the names as shown.
- **New cloud agents use your repo's default environment.** When you pick Cloud for a new agent, by clicking it or cycling with Cmd+;, the agent now runs on the repo and Cursor picks its environment. Before, it could preselect another teammate's saved environment. If an agent starts with a warning, such as falling back to the default image without your environment's setup, the environment status row in the chat shows the warning, counts it, and opens on its own.
- **Continue on Cloud shows saved environment names.** Continue on Cloud options now show each saved environment's name, so you can tell apart two environments on the same repo.

### Files, changes, and pull requests

- **Copy an agent's pull request link from the Copy menu.** When an agent has opened a pull request, the agent's Copy menu in the panel and sidebar now includes Copy PR Link. It copies the link for your preferred review destination, such as GitHub or Graphite, and confirms with a toast.
- **Clearer pull request status and faster PR actions.** Pull requests whose checks are only waiting on someone's approval now show under a yellow Action Required group instead of CI Failing, and mergeable PRs read Ready. In the PRs tray, merged PRs in a stack fold into an "N merged" row you can click to expand, and middle-clicking a PR row in the tray or apps rail opens it in your browser. In a PR tab, press Cmd+Enter (Ctrl+Enter on Windows and Linux) to submit a reply in a discussion thread.

### Navigation and layout

- **Switch command palette filters with the arrow keys.** When the search box in the command palette is empty, press Left or Right to move between the filter pills, such as All, Agents, Files, and Actions. The footer shows the arrow-key hint when this works.
- **Drag subagents and chat links into a split.** You can drag a subagent from the subagent tray, or a chat link in a conversation, onto a conversation tile to open it in a split pane. Top, bottom, left, and right drop zones now work more reliably on wide or narrow panes.
- **Clearer syntax colors in the Cursor Light themes.** Cursor Light and Cursor Light Colorblind now give each kind of code its own consistent color, so code is easier to scan. Types are underlined in blue, properties are blue, decorators and macros are orange, and parameters are italic.
- **Press Escape to show or hide the Apps panel.** When focus isn't in a text field and no dialog or menu is open, Escape toggles the Apps panel, and exits it first if it's fullscreen. Escape in the prompt also dismisses informational trays above the composer, and closing a dialog, menu, or fullscreen video with Escape no longer toggles the Apps panel too.

### Customization and settings

- **Buy credits and manage your plan from Plan & Usage.** On plans with a weekly usage allowance, hitting the weekly limit now shows a notice with Buy Credits and Upgrade Plan. Buy Credits opens an in-app purchase dialog, and the block lifts once the purchase goes through. Plan & Usage settings also show a Credits section with your prepaid balance, pending top-ups, and automatic top-up, plus a line showing when your weekly usage resets.
- **MCP tools that require confirmation always ask in Auto-review.** Fixed an issue where the Auto-review classifier could approve MCP tool calls that the server marks as requiring confirmation, such as merges, without showing you an approval prompt. These calls now show the approval card unless you use Run Everything or have allowlisted the tool.
- **Fixed Windows hooks that point to extensionless scripts.** On Windows, a hook command that names a script without an extension, such as a plugin's `scripts/run`, now runs the matching `.ps1`, `.exe`, `.bat`, or `.cmd` file next to it. Before this fix, these hooks opened a new console window, never received their input, and reported success without doing anything.
- **Fixed repository access rules for people on more than one team.** Admin repository allowlists and blocklists now come only from your active team, so another team's allowlist no longer blocks repositories you should be able to open. Switching teams applies the new team's rules right away.
- **Turn Cursor Tab on or off from any file tab.** The "..." menu on a code file's tab now always includes a Cursor Tab switch, so you can turn Tab completions on or off without leaving the editor. Your keybinding style, such as Vim or Emacs, also stays selected in that menu instead of resetting to Default after an update.
- **Settings now explain a missing menu bar icon on macOS.** If macOS has Cursor turned off under System Settings > Menu Bar > Allow in the Menu Bar, the Menu Bar Icon setting now says so and offers an Open Settings button to turn it back on. Cursor also restores the icon automatically when an older hidden-icon preference was keeping it out of view.

### Fixes

- **Fixes to the Agents tray and subagents.** Back and Forward now step into and out of subagent previews opened from the Agents tray, including previews opened from a side chat. The collapsed Agents pill no longer shows a stopped subagent as needing attention, and local subagents that failed no longer stay stuck in the tray (you can still open them from their Task block). Cloud subagent Task cards now show the subagent's name and progress even when the subagent starts after the card appears.
- **Fixes to cloud agent creation and follow-ups.** A prompt that fails to start a cloud agent comes back so you can retry, and back-to-back follow-ups arrive in the order you sent them.
- The last messages in a chat no longer hide behind the pending question panel.
- Unsent drafts longer than 100,000 characters now survive a reload instead of coming back empty.
- An image dropped into the follow-up composer now attaches once, not twice.
- Typing a follow-up no longer crashes the agent panel.
- Answered agent questions no longer reopen.
- With text selected in a conversation, Cmd+L adds it to that conversation, including side chats.
- **Fixes to trays and pills above the prompt.** Pills above the prompt no longer jump or flicker when a tray or banner opens or closes, and swapping one tray for another now crossfades in place without shifting the layout. The plugin install confirmation now sits above other suggestions with View Details beside the confirm button, and the plugin-added notice can be dismissed with Escape.
- **Fixes to agent turn reliability.** Provider decode errors are now retried automatically.
- **Fixes to MCP server sign-in.** Connecting to Microsoft Entra-backed MCP servers such as Azure DevOps no longer asks for consent on every sign-in, so tenants where an admin has already granted consent stop landing on "Approval required."
- **Fixes for Windows, git, and non-QWERTY keyboards.** Plugins now load with git 2.26 and 2.27, and on Windows the minimize, maximize, and close buttons no longer disappear after you close a modal. On layouts like AZERTY and Dvorak, shortcuts on the physical Z and Y keys, such as Cmd+W, no longer trigger undo or redo.
- **Fixes to branches and git actions.** The automation branch picker shows the default branch right away, and pull requests the local agent opens from its shell are now detected.
- **Fixes to cloud agent git actions.** Fix Merge Conflicts stays in its loading state while the cloud agent works, and Checkout Branch and Fast Forward Branch no longer appear for cloud agents whose checkout can't be changed.
- **Fixes to the sidebar and project picker.** Choosing Rename from an agent's right-click menu now reliably opens the rename field, and the sidebar footer shows your account name and avatar right away at startup. When every agent is pinned or in a project, a Chats header keeps the sidebar customize menu reachable, and the No Repo section no longer offers a Remove from Sidebar action that did nothing. In the project picker, long folder paths are shortened in the middle so the folder name stays visible, and row controls appear when you highlight a row with the keyboard.
- **Unread badge matches the sidebar.** While the Agents Window is open, the Dock badge and menu bar unread count no longer count cloud agents that aren't in the sidebar.
- **Accessibility fixes.** Screen readers now announce the highlighted item and its position in composer menus like slash commands, name agent tiles "Panel 1", "Panel 2" with a "Panel actions" menu, and treat collapsible sidebar section headers as expandable buttons. Buttons in the chat transcript show a focus ring when you reach them by keyboard, and dialogs focus the primary button more reliably when they open, so Enter confirms.
- **Fixes to sign-in, screenshots, and terminal links.** Enterprise members behind flaky corporate proxies are no longer signed out after a single failed team membership check. Agent screenshots of a hidden or minimized window time out after 5 seconds instead of hanging, and finished terminal commands no longer auto-open a browser for a server started in a different terminal.

## 3.23

### Plans and billing

- &#x20;**Plan & Usage shows your plan and prepaid credits.** On Premium, Plus, Super, and Ultra plans, Cursor Settings > Plan & Usage shows your plan by name, your usage reset date, and, below Ultra, an upgrade button for the next tier. Individual accounts on these plans also get a Credits section with the prepaid balance, pending top-ups, and the auto top-up rule, plus buttons to add credits or change the rule.

### Agent and chat

- **Approval prompts now tell you why the agent is asking.** When the agent asks to read or edit a file outside your workspace, or edit a protected config file, the approval card shows the reason.
- **Clearer errors when image generation fails.** When the agent can't generate an image, it now tells you why instead of showing a raw request error. A content-policy block suggests describing the subject in your own words, and a rate limit or provider outage asks you to try again.

### Cloud agents

- **Slack mentions in cloud agent prompts show as readable names.** When you open a cloud agent started from Slack, people mentioned in its prompts appear as `@Name` instead of raw Slack user IDs, and find in the conversation matches the names you see. Clicking a mention opens that person in Slack.

### Editor

- **AI features recover on their own when the extension host hangs.** If the extension host that powers Cursor's AI features stops responding for about a minute, Cursor restarts it automatically, so you no longer need to reload the window. It also keeps restarting a crashing host with increasing delays, and skips the automatic restart while you debug extensions.

### Fixes

- **Fixed Windows hooks that point to extensionless scripts.** On Windows, a [hook](https://cursor.com/docs/hooks.md) command that points to a script without a file extension now runs the matching `.ps1`, `.exe`, `.bat`, or `.cmd` file next to it. Before, these hooks opened a stray terminal window and reported success without running.
- **Fixed transparent images turning black when attached to chat.** When Cursor shrinks a large image you attach, transparent areas now stay transparent.
- **Fixed Investigate Error in Chat taking over its shortcut.** Cmd+Shift+D now runs Investigate Error in Chat only when the cursor is on an error, warning, or AI lint. Elsewhere, the shortcut goes to its other binding.
- **Fixed Apply writing blank files for very large cloud agent diffs.** When a cloud agent changes more files than can be shown, Review Changes now warns that file contents are not available instead of saying there are no changes, and Apply is blocked instead of writing empty files.
- **Fixes to agent reliability.** Follow-up messages you queue while the agent works are no longer lost, and `/summarize` shows an error when it fails. Agent turns no longer hang when `.cursorignore` rules fail to load. MCP tools that require confirmation still ask for approval when Auto-review allows the call.
- **Fixes to cloud agents.** Cloud agent chats reconnect after sleep or network drops and load older turns one page at a time without stalling. Follow-ups are processed in send order and keep the model variant you picked.
- **Fixes to the agent chat transcript.** Questions the agent asked in chat no longer reopen after you answer them, and large unsent drafts are no longer lost when the chat reloads.
- **Fixes to MCP sign-in.** MCP servers that sign in with Microsoft Entra no longer ask for consent every time when an admin has approved the app.
- **Fixes to Git.** On macOS, Cursor no longer hangs when the git on your PATH can't run, and falls back to the system or Homebrew git. Plugins load with git 2.26 and 2.27.
- **Accessibility fixes.** Screen readers now announce the highlighted item and its position in the agent input's `/` and `@` menus. Buttons in the agent chat show a focus ring when you reach them with the keyboard.
- &#x20;**Fixes to team and enterprise policies.** Repository access rules now come only from your active team, so another team's allowlist no longer blocks your repos. Team privacy mode no longer falls back to the restrictive default during brief network errors, and Enterprise members behind unreliable proxies are no longer signed out after a temporary membership check failure.
- **Fixes to the editor.** Extension hosts no longer deadlock at startup, and searches started while Cursor loads no longer fail. Ctrl+I and Ctrl+L no longer land on a chat stuck on "Loading Chat", and undo/redo no longer catches other shortcuts on AZERTY or Dvorak layouts.

## October 1, 2026 release

### Pull requests

- **Request reviewers by email.** `origin pr edit --add-reviewer` takes one or more emails, fails if an email doesn't match exactly one reviewer candidate, and prints who was requested.
- **Links to new comments.** `origin pr comment` prints the new comment's id and a URL that opens it.
- **More `gh`-compatible JSON.** `origin pr view` and `origin pr list` accept `--json headRefOid`. Change output shows actions taken through an app or bot as "Name via app", and JSON output includes a `performedVia` field.
- **Gate checks no longer count as CI.** `origin pr checks` ignores Gate review checks when it sets its pending, failed, or no-checks exit code. `origin pr view` shows "unknown" instead of "no" for CI and approvals when the target's rules can't be read.
- **`origin pr stack` is removed, and so is `--branch` for picking a pull request.** Name a branch as the positional target instead. `origin pr checkout --branch` is unchanged.

### Reliability

- **Safer branch names.** `origin pr create --push` and `origin pr checkout` use fully qualified refs, so branch names that clash with tags work, and invalid names fail with `'<name>' is not a valid branch name`. `origin pr create --push` also pushes branches whose names start with `-`.
- **Automatic retries on rate limits.** When Origin rate-limits a request, the CLI waits and retries, printing "Origin rate limit reached; retrying in Ns."

## 1.12.0

### Projects

- **Project chats focus on the conversation.** A Project's coordinator chat shows your messages, its replies, questions, and approvals without Worked or thinking sections, and messages you send in a row are grouped together.
- **Live status while a Project works.** While a Project's coordinator is running, its chat shows a status line such as the step it reported, Running commands, Messaging an agent, or Writing a reply.

### Agents

- **Agent links open in the app.** Tapping a cursor.com/agents link in an agent chat, including a link to a subagent, opens that agent in Cursor for iOS, and shared agent links open straight to the agent's chat instead of the inbox.
- **Earlier messages load as you scroll.** Scrolling up in an agent chat loads earlier messages automatically and keeps the messages you're reading in place while they load.
- **Voice call messages are labeled.** Messages sent from a voice call show a Voice call label with a waveform icon.
- **Scrub through long chats.** Hold and drag the scroll indicator to move through a long conversation.

### Review

- **Large diffs in Review.** For very large diffs, the Review screen lists every changed file with line counts and explains when the contents exceed the viewing limit, and pull request review now loads commits past the first 50, up to 250.

### Fixes

- **Projects.** A Project's inbox row shows its loader while the coordinator is running, worker rows update when a worker finishes, errors, or restarts, images and media from Project workers load with a Retry option if loading gives up, and finished Projects on the Live Activity show how long the whole Project ran instead of 0m.
- **Model picker.** Choosing Auto for a cloud agent follow-up switches the agent to Auto instead of keeping the previous model.
- **Large files and code blocks.** Opening a very large edited file shows File too large to preview with a Copy option instead of hanging, chats with edits to large files stay responsive, and a crash while scrolling code blocks with line numbers is fixed.
- **Sending and pickers.** Backgrounding the app right after sending no longer shows a false Couldn't start agent or Couldn't send message error, and the Workspace picker's Recents no longer lists repositories or environments that are no longer available.
- **Visual polish.** Dragging sideways on a bottom sheet no longer moves it off-axis, large pull request numbers show without thousands separators, and overlapping avatars fully cover the ones behind them.
- **MCP sign-in failures.** When signing in to a cloud MCP server fails, the sign-in card in the chat shows it as failed instead of skipped.

## 1.0.35

- **Custom tools know which session called them.** The `execute` callback of a `local.customTools` entry now receives `context.sessionId`, the local session that invoked the tool. Subagents started with `Task` pass their own id, so a host can keep separate state for each child agent. TypeScript only; unset when the runtime has no session id.
- **Fixes to local agents and TypeScript types.** Local agents now work on FIPS-enabled hosts, and existing local agent stores move to the new location automatically. Agents restored from the same process or VM snapshot no longer reuse request and session IDs, so concurrent runs don't collide or get stuck. The `LocalSubagentInherit` type declarations now resolve without an unpublished internal package, using the newly exported `LocalSubagentResourceProviderFields` and `LocalToolExecutor` types.

## 1.0.34

- **Subagents can inherit the parent's executors and tool limits.** Set `local.subagentInherit` so that agents started by the `Task` tool, including nested ones, use the same custom read, write, and shell executors and reported workspace path as the parent, and the same allowed and excluded tools. Pass it on `Agent.create()` or override it for one `send`. TypeScript local agents only. If you leave it unset, subagents behave as they did before.
- **Fixed requests stalling on dropped connections in long-running agents.** When an agent sits idle between runs, the SDK now closes unused HTTP/2 connections after 29 seconds. It also checks a connection that has been quiet for about a minute before reusing it. Requests no longer get written into a connection the server has already closed, where they used to hang until the stall timeout aborted them.
- **Stalled connections are retryable and bounded.** When a connection stalls, the run fails with a retryable `NetworkError` carrying the code `connection_stalled`, and a streak of stall retries stops after 3 minutes instead of retrying indefinitely.
- **Fewer dependencies installed with the SDK.** Installing `@cursor/sdk` no longer adds `@connectrpc/connect-node` or `undici` 5.x to your project's dependency tree, so installs are smaller and you no longer get version conflicts or audit warnings from those packages.

## v2026.09.28

### Fixes

- **Grok turns no longer end on a rejected output.** When the provider rejects a Grok model's output before any tool in the step has run, the agent now retries that step once instead of ending the turn with an error.
- **No extra turn after an empty reply.** After you resume a session or a background task finishes, an empty model reply no longer triggers an unwanted retry or continuation turn.
- **Self-hosted workers recover from a silent connection.** A worker whose connection to Cursor goes silent for 90 seconds now reconnects on its own instead of appearing connected while receiving no work. If your account uses Privacy Mode (Legacy), the worker now exits at startup with a message explaining how to switch to Privacy Mode instead of reconnecting endlessly.
- **Self-hosted workers keep an agent's state open between turns.** On shared and pool self-hosted workers, an agent's follow-up step reuses its open state instead of reopening it from scratch, and a claim from a different agent no longer fails on state the previous agent has already released.
- **Image generation errors say what to do next.** When the image provider declines a request, the agent now shows a message you can act on instead of "Request failed with status code 400." For content-policy blocks, the message suggests describing the subject without naming trademarked characters, brands, or real people. For rate limits and provider outages, it says to try again in a moment.
- **Timed-out shell commands keep their output.** When a long-running command writes its output to a file and then times out, the agent now gets the file's path, size, and line count instead of an empty result, so it can read the output and keep working.
- **The CLI runs the exact model you pick.** `--model` and `/model` now run the model you choose even when its ID starts with another model's ID. Previously the CLI could silently run the shorter base model instead.
- **macOS workers report memory the way Activity Monitor does.** A self-hosted worker on macOS no longer counts file cache as used memory, so an idle Mac no longer looks nearly out of memory.

## Week of Sep 28, 2026

### Web

- **Find merged pull requests.** A repository's pull requests list has a new Merged tab with a count, and `is:merged` in the search box now filters to merged pull requests.
- **Request Changes reviews now block merging.** A Request Changes review from someone with write access blocks the pull request from merging until it's resolved, and dismissing someone else's Request Changes review requires write access. Pending reviews you haven't submitted no longer count as approvals or blockers, and reviews on the pull request page are ordered by when they were submitted.
- **Choose repositories when requesting an app, and cancel pending requests.** When you request an app install, you can pick all repositories or specific ones, with the repository from the install link preselected. A pending request shows its status, and you can cancel it from that status button. Namespace owners or team admins get an email when someone requests an install, and you get an email when your request is approved or denied. The install page also shows the app's publisher, verification, and website, a View Listing button, and the account you're signed in as.
- **IP allowlists apply to people, not your apps.** When your team has an inbound IP allowlist, it now applies only to user credentials, so apps, service accounts, and agents are no longer blocked. The allowlist is also checked on Origin web pages and repository downloads, and it can hold up to 1,000 entries. Owners can read and replace the allowlist through the Origin API; see the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).
- **Clearer Git errors and safer pushes.** When Git is denied access to an Origin repository, it now explains why, including which Cursor account was used and how to switch. Pushing a file larger than 100 MB is rejected with an error naming the file and its size. Pushes to `HEAD` or to ref names outside `refs/` are refused instead of moving the default branch, and a malformed ref name is rejected on its own while the rest of the push lands.
- **Blame follows renames.** Blame now follows file renames the way `git blame` does, so lines in a renamed file keep the commit that wrote them instead of pointing at the rename. Branch and tag names that look like commit hashes now resolve to the branch or tag, and commit lists and comparisons use the same merge base and ordering as Git.
- **CODEOWNERS matches GitHub more closely.** CODEOWNERS patterns now follow gitignore rules, so directory and anchored patterns resolve owners the way GitHub does, and logins with underscores are accepted. Email entries resolve only to people who can review the repository. When code owners can't be determined, for example because the file is too large or too many files changed, the code owner requirement is blocked with an explanation instead of passing or failing silently.
- **Rulesets are enforced more strictly.** Pull requests into a branch frozen by an active ruleset that blocks merges now show "Merging is blocked by a ruleset." unless you can bypass it. An active ruleset with a rule type Origin doesn't recognize now blocks merging instead of being skipped, and saving a rule that can't run in that kind of ruleset fails with an error. Merge when ready now waits for ruleset rules to pass even if you could bypass them.
- **Fixes to merge when ready.** Merge when ready no longer merges a commit pushed after checks ran, waits for a newly linked parent pull request to merge first, and turning it off reliably stops a pending merge. A merged pull request now records the commit that actually landed it.
- **Fewer false merge conflicts.** Pull requests with an edit next to a line inserted on the base branch now show as mergeable when Git would merge them cleanly, instead of reporting a conflict. When a pull request's head commit is missing, it asks you to push the branch again instead of showing an error.
- **Fixes to stacked pull requests.** After a stacked pull request's base lands and it's retargeted, its diff and restack include only its own commits. Restacking keeps conflict resolutions from merges with trunk, including onto a squash-landed parent. A pull request drafted or closed at the moment its stack merged now shows as merged.
- **Fixes to diffs on large and renamed changes.** Renamed files are paired the way Git pairs them, line counts match Git for final-newline and line-ending changes, and diffs for deeply nested changes now load instead of failing. On very large pull requests, Load more now fetches the next batch of files.
- **Fixes to pull request pages.** Reopening a pull request whose head or base branch was deleted now tells you to restore the branch first. Permalinks now open the right file when its path has spaces or non-ASCII characters. Authors and reviewers who acted through an app show that app next to their name.

### API

- **Prepare and inspect merges through the Origin API.** A new call rebuilds a pull request's test merge ref against the current base and reports whether it's mergeable, conflicted, or pending, with the merge, base, and head commits. Mergeability responses also include the head commit they were computed against. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).
- **Scope check runs to a base commit.** Apps can pass a base commit when posting check runs so a check counts only for pull requests with that base, and the base commit appears in check responses, the Origin SDK, and check run webhooks. Check runs posted with a failing status keep that status. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).
- **More of Origin is available through the Origin API.** You can read, add, and remove reactions on pull request comments, check a user's permission on a repository, and list commits within a time range. Responses for repositories, commits, and pull requests, and pull request webhooks, now link to the page on Cursor. Ruleset bypass users now use public user IDs, which is a breaking change. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.

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

## Week of Sep 28, 2026

### Repository settings

- **Configure Bugbot per repository.** On GitHub pull requests, Bugbot reads a `.cursor/config/bugbot.yaml` file to set its triggers, review effort, incremental review, PR summary, and risk score for that repository. Values in the file override team settings, and the file can lower Autofix but never turn it on. The Bugbot Settings section in the dashboard links to the docs for config files.

### Autofix

- **Autofix stays off your branch in New Branch mode.** When Autofix is set to New Branch, it now keeps its fixes on a separate branch and never commits to the pull request's own branch.

### Reviews and checks

- **Bugbot checks no longer get stuck.** A Bugbot run that is cancelled or times out now completes its check as neutral instead of leaving it in progress. When the base branch gets new commits that don't change the pull request's merge base, Bugbot still posts its review, and a cancelled run's check says why it was cancelled.
- **Clearer results for oversized and rate-limited reviews.** When no file in a pull request fits Bugbot's review budget, Bugbot posts its "too large to review" comment and a neutral check instead of an error. A manual Bugbot command that hits a temporary GitHub rate limit now gets a reply asking you to retry in a few minutes. Bugbot also no longer reviews symlink targets as if they were source files.

### Bitbucket

- **Better Bugbot on Bitbucket.** Bugbot can now review Bitbucket Cloud pull requests from forks. When Bugbot refuses a comment command on Bitbucket, it replies with the reason. Failure comments render as markdown instead of escaped HTML, and Bugbot retries a review when Bitbucket's sign-in service is briefly unavailable instead of skipping it. The team allowlist accepts Bitbucket nicknames that contain spaces.

### Dashboard

- **Clearer installation permissions in the dashboard.** On your personal Bugbot dashboard, GitHub organization installations owned by a team are shown read-only, and changes are rejected with a message to switch to that team's dashboard. Personal installations you can't change without a paid plan are also read-only and say a paid subscription is required.
- **Dashboard fixes.** Repository pickers and lists in Bugbot rules and learning settings show repositories as owner/name, and search matches the owner. The Set License Cap toggle reflects the saved cap after a refresh. If a Bugbot dashboard view fails to render, it shows a message with a Try again button instead of a blank page.

### Billing

- **Team limits apply to token-billed Bugbot runs.** On teams with token-based Bugbot billing, runs are no longer blocked by the installing user's personal spend limits; only the team's limit applies. Bugbot no longer runs as a member with the Unpaid Admin role and posts a comment explaining how to fix it. Changing Bugbot licenses on a team without Stripe billing now shows a clear error.

### API

- **Skip the no-issues comment on API-triggered reviews.** The Bugbot review trigger API accepts `postSuccessComment`. Set it to `false` to skip the "found no new issues" comment on that review.

## 3.22

### Agents

- **Failed agents now show a clear Error status.** Agents that fail now get a red Error status in the sidebar, with their own Error group and an Error option under Show > Status, on by default.
- **Usage ring in the chat status bar.** When your monthly usage passes the display threshold, the chat status bar shows a usage ring with a "Usage N%" tooltip. Click it to open usage details, which now float over the conversation and close with Escape.
- **Fewer unnecessary Auto-review blocks.** Auto-review no longer blocks preparatory steps such as drafting an email, staging changes, or previewing a deploy just because a block instruction forbids the later send or apply; the final committing step is still checked. Reviews also fail less often when the classifier returns an incomplete decision.
- **Pin up to 75 agents.** The pinned agents limit is now 75, up from 50, so you can keep more agents at the top of the sidebar.
- **Grok 4.7 now names itself correctly.** When you ask Grok 4.7 who it is, it now says it is Grok 4.7, a model trained by SpaceXAI. Before, it could call itself Composer or an earlier Grok version.
- **Voice Submit Keywords work in any language.** Submit keywords in non-Latin scripts, such as Cyrillic or Chinese, now trigger auto-submit while you dictate. Accented keywords like "envíalo" also match correctly instead of being mangled.
- **Agents recover when their reasoning gets stuck in a loop.** When an agent's reasoning starts repeating the same line, Cursor now stops that step and retries it once with a nudge to move on, so the run keeps going instead of stalling.
- **See where unread replies start in any agent chat.** Cloud and local agent chats now mark where replies you haven't seen begin and show a New Messages pill that jumps to them, like Project chats already did.

### Projects

- **Create Project keeps your work and picks the right repository.** Choosing Add Models in the Create Project dialog now opens Settings without losing your project name, appearance, or model picks, and reopening the dialog restores them. The dialog no longer waits on the repository list before you can create, keeps the repository you pick from Repos or Recents instead of switching to a saved environment for the same repo, and defaults to the same environment as your New Chat draft.

### Cloud agents

- **Clearer cloud agent errors with one-click recovery.** Cloud agent errors now show in the tray above the input, including while a run is retrying automatically or after its session expires. When a run fails, the error offers a single next step where one applies, such as Retry, Manage Usage, or Manage Environments. Opening a terminal for a cloud agent whose machine is offline now opens a Terminal tab that explains why, and it connects automatically once the machine is reachable again.
- **Starting a Cloud Agent from a link no longer picks a random repository.** Opening a Cloud Agent from an in-app prompt or a deeplink used to preselect the first repository in your list when you had no local or recent repo. Now it uses your current repo or most recent Cloud repo if you have one, and otherwise opens a new Cloud Agent with the repository picker one click away.
- **Find Bitbucket repositories beyond the first 5,000 in the project picker.** In Bitbucket workspaces with more than 5,000 repositories, typing in the project picker now also searches Bitbucket, so repositories past the first 5,000 show up in the results. Browsing without a search still lists the first 5,000.

### Files, changes, and pull requests

- **Review only what the agent just changed.** The Changes tab now has a Last Agent Turn scope that shows only the edits from the agent's latest turn. Clicking Review or a file in the end-of-turn summary opens the Changes tab in that scope, so you can check the newest edits without digging through earlier changes.
- **Markdown previews keep your place and show agent store images.** Switching away from a Markdown preview and back now restores your scroll position and cursor instead of jumping to the top. Markdown documents from an agent store also render their store images instead of broken image links.

### Navigation and layout

- **More relevant command palette search results.** Searching agents in the command palette now ranks chats whose transcript matches your query above chats that only loosely match the name or PR link, and typing a PR number (with or without #) still finds its chat. Searches with no matches now show "No results found" instead of suggesting a new agent, and results you can already see are selectable while other sections finish loading.
- **Screen readers can tell prompt boxes apart.** Each prompt box now has its own name for screen readers, such as "Prompt", "Side chat prompt", "Subagent prompt", "Fullscreen prompt", or "Design mode prompt". In split layouts the name includes the tile number, for example "Prompt, tile 2". Menu options in the prompt box are also read as part of their list.
- **Update notifications for Linux .deb and .rpm installs.** Cursor installed through apt or dnf now tells you when a new version is available instead of leaving updates turned off. Choosing Update shows the exact upgrade command with a Copy Command button, and Later snoozes that version.
- **Opening a Rust project no longer pegs the CPU.** With language servers on, the Agents Window no longer starts rust-analyzer and a full cargo check just because a folder contains Rust. The server now starts when you open a Rust file, and language extensions you disabled stay off.
- **The Agents Window recovers on its own when its extension host hangs or keeps crashing.** Previously, a frozen extension host could leave agent requests stuck with no error until you reloaded the window. If that extension host stops responding for 60 seconds, it is now restarted automatically and requests resume. If it keeps crashing, it keeps restarting with increasing delays instead of giving up after three crashes. The automatic restart after a hang is skipped while a debugger may be attached to the extension host.
- **Find side chats in the command palette.** Searching in the command palette now finds side chats. Each one is labeled Side chat, shows its parent agent's name, and opens on its parent agent.

### Customization and settings

- **MCP servers show every page of tools.** MCP servers that paginate their tools, prompts, or resources now show every page, not just the first one.
- **Hooks can tie a subagent back to its conversation.** The `subagentStop` hook now receives `child_conversation_id`, the ID of the subagent's own conversation, so audit and policy scripts can tie subagent activity back to its parent.
- **`/subscribe` cleans up after merged pull requests.** A subscription to one pull request now closes on its own when that pull request merges or closes. The CI subscription on its branch closes too, unless another open pull request still uses the branch.

### Fixes

- **Fixes to Projects.** The project picker shows a named cloud environment's name instead of "No Repo" when its repositories are unpublished drafts. Switching between agents in a Project keeps recent conversations loaded, so going back to one no longer reloads its transcript, and with split panes the conversation in the unfocused pane stays on screen.
- **Fixes to the subagent tray.** The Agents pill stays visible and shows as selected while the subagent tray is open.
- **Fixes to the composer and queued follow-ups.** Queued follow-ups no longer vanish when a turn ends, and large unsent drafts are no longer cleared on reload. Typing follow-ups with keyword suggestions no longer crashes the agent panel, and scrolling while editing a previous message behaves correctly again.
- **Fixes to the chat transcript.** The last messages are no longer hidden behind a pending question panel, answered questions no longer reappear, and visualization cards show an error instead of spinning forever.
- **Fixes to context summarization.** After a long chat is summarized, the agent keeps your latest request instead of losing it behind an automatic reminder, and a failed summary no longer replaces your conversation history with a placeholder. Stopping an agent mid-summary now cancels promptly instead of showing a server error.
- **Fixes to cloud agents and Move to Cloud.** New cloud agents keep the model you picked, cloud agents outside the current workspace no longer send false "Done" notifications, and chats that wake up in the background move up in the sidebar. Move to Cloud works for chats whose saved state lost its turns.
- **Fixes to the built-in browser.** Web pages can no longer fake element picks into agent context; only real clicks select elements. Hidden browser tabs no longer keep rendering in the background, and DevTools starts only when you first open the console, so browser tabs use less CPU and memory. Browser pages and DevTools show up with their own labeled rows in Process Explorer.
- **Fixes to agent context reads.** Agent context reads no longer stall when the startup .cursorignore scan fails.

## 3.22

### Agent

- **Auto-review no longer blocks drafts and previews.** When you add a block instruction like "don't send emails" or "don't deploy", [Auto-review](https://cursor.com/docs/agent/security/run-modes.md) now applies it only to the call that sends or deploys. Calls that draft, stage, preview, plan, or read run instead of stopping for approval.
- **Clearer agent tool calls in chat.** When the agent reads its to-do list, the chat shows the list itself. Pull request actions show their result or the error instead of being hidden, and agents blocked on approval say "Approval required" or "Approval denied" instead of "Couldn't start".
- **Agents retry when their reasoning loops.** If an agent's reasoning repeats the same line over and over, Cursor stops that step and retries it once with a nudge to move on.
- **Voice submit keywords work in any language.** Voice submit keywords, the spoken words that send your prompt, now save in Settings and trigger submit in non-Latin scripts like Cyrillic or Chinese. Accented letters are kept, so `envíalo` no longer saves as `envalo`.

### MCP

- **More reliable MCP server sign-in and tool loading.** Signing in to OAuth-protected [MCP servers](https://cursor.com/docs/mcp.md#static-oauth-for-remote-servers) works with more servers, including ones that reject Cursor's redirect URLs at registration or ask you to sign in again later. Servers that paginate their tools, prompts, or resources now expose all of them instead of only the first page, and agents with many MCP tools no longer fail by going over the model's tool limit.

### Hooks

- **Hooks can tell which subagent a tool call came from.** When a tool runs inside a subagent, `preToolUse`, `postToolUse`, and `postToolUseFailure` [hooks](https://cursor.com/docs/hooks.md) now receive `parent_tool_call_id`, the ID of the Task tool call that started that subagent. `subagentStop` hooks receive `child_conversation_id`, so audit scripts can link a finished subagent to its own conversation.

### Browser

- **See and undo the agent's device emulation in the built-in browser.** When the agent resizes a tab to a phone-sized viewport, the [browser](https://cursor.com/docs/agent/tools/browser.md) tab shows a "Device emulation · W×H" badge with a Reset button, and the emulation clears when the agent's turn ends. The browser also uses less memory because DevTools starts only when you first open the console, and web pages can no longer fake element selections or area screenshots sent to chat.

### Source control

- **Git hooks run again for Source Control operations.** Fixed a regression where commits, pushes, pulls, checkouts, branch creation, and clones from the Source Control view skipped repository hooks such as `pre-commit`, `commit-msg`, `pre-push`, `post-checkout`, Husky, and Git LFS. Commands that run hooks are marked `(hooks)` in the Git output channel. Background activity like status refreshes and autofetch still skips them.

### Updates

- **Update notifications for apt and dnf installs on Linux.** If you installed Cursor from a `.deb` or `.rpm` package, Cursor now tells you when a new version is available. Click **Update** to see the `apt-get` or `dnf` upgrade command and copy it with **Copy Command**, or click **Later** to skip that version.

### Fixes

- **Fixes to agent chat and the follow-up queue.** Queued follow-ups no longer vanish when a turn ends or disappear when a steer falls back to the queue. The "Worked for" duration includes tools that ran after the final reply.
- **Agent context reads no longer hang after a failed startup scan.** If the first `.cursorignore` scan fails at startup, Cursor retries it instead of leaving agent context reads stuck for the rest of the session.
- **Fixes to cloud agents.** Slash menus no longer show the previous team's managed skills after you switch accounts or teams, and cloud agents outside the current workspace no longer send false "Done" notifications.
- **Fixes to the editor and workbench.** Cmd/Ctrl+Shift+B runs Run Build Task again, and unsaved backups of deleted files no longer reopen every time a window opens. Worktree fetches work on git versions older than 2.29. If the local extension host that connects Cursor to its servers hangs, Cursor restarts it so the window reconnects, unless a debugger may be attached, and it keeps restarting that host if it crashes repeatedly. Cancelled symbol and call hierarchy requests no longer leak memory.
- **Fixes to usage banners, the model picker, and chat visualizations.** Models you enabled in the model picker no longer disappear when the model list refreshes. The usage-limit banner no longer stacks under a usage-limit error in the composer or shows a Request Credit button when your organization hides credit requests. Visualization cards in chat show an error instead of loading forever when their content never arrives, and chart tooltips no longer shift the surrounding chat.

## September 24, 2026 release

- **Find pull requests by commit.** `origin pr list --commit <sha>` lists the pull requests Origin records for a commit.
- **`reviewDecision` in JSON output.** `origin pr view --json reviewDecision` returns the review decision, matching `gh`.
- **Request bodies from stdin.** `origin api --input -` reads the request body from stdin instead of failing with "Unknown argument: -".
- **CloneKit fixes.** `origin repo clone-fast` no longer fails with spurious EPIPE errors during parallel range downloads, and it looks up the default branch while the kit downloads instead of before.

## v2026.09.22

### Auto-review

- **Auto-review weighs block instructions against what a call does.** Under an instruction like "Send comms that include external people," it now leans toward allowing MCP calls that only draft, preview, plan, or read, and toward blocking calls that send, post, publish, apply, or delete. Add instructions to `permissions.json` as shown in [Configuring Auto-review](https://cursor.com/docs/agent/security/run-modes.md#configuring-auto-review).

### Self-hosted workers

- **Any-repo pool workers reuse checkouts you already cloned.** With [`--clone-git-repos`](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools), a worker reuses a clean checkout of the claimed repo in its worker directory. It fetches the requested branch, tag, or commit and keeps the checkout when the claim ends, so a large repo no longer re-clones on every claim. The worker log says why it reused or skipped each checkout. The worker also refuses to start from a directory it can't write to, and prints git's error in the terminal when a clone fails.
- **Warm pools wake hibernated workers for follow-ups.** When a follow-up arrives for an agent whose worker is hibernated, `agent worker controller --warm-idle` now runs your `--spawn` hook with `CURSOR_WAKE=1` and that worker's ID, matching claim-then-spawn mode. If the hook restores the machine, the follow-up picks up in its original workspace instead of landing on an idle spare with an empty disk. This applies to pools with a [reconnect window](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#hibernation).

### Fixes

- **Fixed agents getting stuck repeating the same line of reasoning.** When the agent's reasoning keeps repeating a single line, the step now stops and retries once with a reminder to stop deliberating and move on, instead of looping.
- **Fixed summarization losing your latest request or your conversation.** After summarizing a long conversation, the agent now keeps your most recent message word for word instead of a reminder, so it stays on task. If summarization fails, or you press Stop while it runs, the agent keeps the earlier conversation instead of replacing it with an empty or interrupted summary.
- **Fixed authentication errors and the wrong rules on self-hosted workers.** Workers started with an API key no longer fail with an authentication error when they open a desktop session after their first hour. An agent's first turn now loads rules, skills, and plugins from its own workspace instead of a cached set another workspace left on the machine.
- **Fixed model instructions for Grok 4.7 and Opus 5.5.** Grok 4.7 now identifies itself as Grok 4.7 when asked, instead of claiming to be Composer. Opus 5.5 now gets the same communication instructions as Opus 5, which ask for a one-line note on what it's about to do before its first tool call and a short closing summary that leads with the outcome.

## 1.0.32

- **Steer an agent while it waits on background subagents.** `run.steer(text)` used to resolve `revert_to_followup` when the agent had ended its turn to wait on background subagents, so your message waited until that work finished. Now the steer runs right away as the next turn, and background results still arrive afterward. TypeScript local runs only.
- **Know when a step has finished requesting tools.** `onDelta` now receives a `tool-requests-listed` update with a `callCount` once the model finishes listing its tool calls for a step, while those tools may still be running. Use it to tell when every tool call in a step has started, for example to group or batch a step's tool calls in your UI.
- **Fixes to cloud agent creation.** For cloud agents, the first `send()`, which creates the agent on the server, no longer fails with an id conflict when the SDK generated the agent id: it retries with a fresh id, or continues with the agent if its own earlier create already succeeded. SDK-generated agent and run ids also no longer repeat when a process is restored from the same snapshot more than once. Ids you pin yourself still report the conflict.
- **The bridge ignores your project's `.env` and `bunfig.toml`.** The standalone `cursor-sdk-bridge` executables no longer load `.env` or `bunfig.toml` from the working directory, which is usually your project when the SDK starts the bridge. Files in a checkout can no longer change the bridge's endpoints, tokens, or preloaded code.

## 1.10.0

### Projects

- **Projects.** Cursor for iOS now supports Projects. Your Projects appear in their own section of the inbox; tap one to open its chat. On iPhone, the New Project row starts a Project from a name, with an optional repository, branch, and model. If a team admin turns off Projects for the team, the Projects section and New Project are hidden.

### Fixes

- **iPad chat.** On iPad, the chat stays readable while the keyboard is up instead of being blurred at the bottom.

## Week of Sep 21, 2026

### Web

- **Sign in to repositories with SSH certificates from your team's certificate authority.** Team admins can add trusted SSH certificate authorities from the SSH certificate authorities section of the API Keys page, so members can clone, fetch, push, and use LFS with short-lived OpenSSH certificates instead of registering individual keys. Admins can also require certificates, which blocks registered SSH keys and API keys over HTTPS while certificates and the Origin CLI keep working. The same controls are available in the Origin API; see the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).
- **Build stacked pull request workflows on the Origin API.** Pull requests returned by the Origin API and carried in pull request webhooks now include their stack and parent pull request, and you can set or clear a stack parent when you create or update a pull request. You can also list every pull request in a stack. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for field details and the breaking change to the old parent field.
- **Squash merges keep credit for everyone who contributed.** When you squash-merge a pull request, the merge commit now adds a Co-authored-by trailer for each author of the squashed commits and for anyone those commits already listed as a co-author. Cursor's agent and bot addresses are skipped, and no one is listed twice. When a bot's pull request is squash-merged, the person who merged it and the people who approved its latest version are credited as co-authors.
- **Choose exactly where an app gets installed, and review permission reductions one by one.** App install links now open a consent page for a specific namespace. If you can install the app in more than one, you pick from a "Choose where to install" list first, and the install button names the namespace you picked. When an installed app asks for fewer permissions, its page shows a "Permissions can be reduced" notice, and on the review page you can keep or remove each permission it would drop.
- **The audit log now records repository clones and fetches, and shows who edited or deleted a comment.** When a person clones or fetches an Origin repository, your team's audit log now records it, along with their email and whether they used HTTPS or SSH. Background autofetches and machine actors are left out. Audit entries for pull request comment edits and deletes now name the person who made the change, not the comment's original author.
- **Fixes to merging and stacked pull requests.** Pull requests with nothing left to merge are now blocked instead of landing an empty commit. Stacks with already-merged lower changes now land on the correct base, restacks list conflicted files when they stop, and a cancelled rerun no longer turns a passing check red or blocks merge when ready. Reopened pull requests also pick up commits pushed while they were closed.
- **Fixes to pull request diffs and the Files changed view.** Expand all on huge files no longer freezes the tab, pull requests over the file limit let you load more files, code owner shields are back, and your pending review comments show as drafts right away.
- **Fixes to pull request pages and repository settings.** Searching a repository's pull requests with an unsupported filter like `is:merged` now shows an empty state that explains the filter and offers Clear search, instead of silently showing the default list. Repository and namespace permission settings only list Admins and Members when they have access, and committing a suggested edit without a name and email on your profile now explains what's missing.
- **Fixes to code tours.** Code tours created before a tour update now regenerate with the latest version instead of showing outdated content, while tours prepared ahead of time still appear right away. Tours no longer include stray planning notes from the model, and custom tours are left unchanged.
- **Fixes to Git operations.** Rejected pushes now show the real reason next to each ref instead of a generic unpack error. Blame and file history are correct for paths with non-ASCII characters, and repositories with consecutive dots in their names now work in clone and push URLs.
- **Fixes to cancelled Bugbot checks.** When a Bugbot review is cancelled on a pull request, its check now shows as cancelled instead of neutral, so a check that later becomes required can no longer pass without a finished review. Checks left on a commit the pull request has moved past still show as neutral, unless the check is required.

### API

- **Apps can act on behalf of namespace members.** Origin apps can now request short-lived installation user tokens that act as a member of the namespace, named by user ID or email, for API calls and HTTPS git clone, fetch, and push. Work done this way is attributed to the member "via" the app across API responses, webhooks, audit logs, and the PR page. Installations need the new User Delegation permission; see the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **More of your pull request workflow is available through the Origin API and webhooks.** You can now delete pull request comments, filter pull requests by head commit, see what each check run write did, and read a version's potential merge commit through the Origin API and Origin SDK. Webhooks now cover comment reactions and name who removed a label, and expired app installation tokens return a clear error. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.

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

## Week of Sep 21, 2026

- **More accurate Bugbot checks on Origin.** On Origin pull requests, a Bugbot run that errors or can't post its review now fails the Bugbot check instead of reporting neutral. A run cancelled by a new push is marked cancelled, so it no longer satisfies a required Bugbot check.
- **Bitbucket-only teams can finish Bugbot setup.** Teams connected only through Bitbucket no longer see a prompt to connect GitHub or GitLab during Bugbot setup. The setup steps now show the Bitbucket connection as connected.
- **Reviews continue past oversized files.** When one changed file is too large for Bugbot to review, Bugbot skips that file and still reviews the others. Before, an oversized file could make Bugbot skip every file after it.

## 3.21

*Enterprise teams get Projects from 3.21.9 unless opted in.*

### Agents

- **Team rules with file patterns now apply only to matching files.** Fixed team rules scoped to a file pattern, such as `*.py`, being added to every agent conversation. They now apply when the agent reads a matching file or you add one to context, so unrelated chats no longer spend tokens on them. Team rules without a file pattern still apply to every conversation.
- **Fixed getting stuck when a usage limit offers Switch to Auto.** When a usage limit offers a model switch, the limit banner now shows **Switch to Auto** next to the upgrade button, and the prompt stays editable. Choosing Switch to Auto clears the banner and resends your message with Auto so the conversation can continue.
- **Cloud subagents waiting on you now stand out.** When a cloud subagent stops to ask you a question or needs you to sign in to an MCP server, the Agents pill shows a yellow status dot and the subagent's row in the tray is marked as needing attention, so you can unblock it instead of waiting on a stalled run.
- **Video review subagents no longer review videos they weren't given.** When the agent asks a subagent to review a video, the video file now has to be attached. A file path that only appears in the prompt no longer counts. If no video is attached, the subagent says so in plain text instead of making up a review.

### Chat and composer

- **A Save check mark while editing a queued message or goal.** When you edit a queued message or a goal, the send button becomes a Save check mark.
- **Smoother scrolling while an agent streams.** While the chat follows a streaming reply, it now glides to new text and tool cards instead of jumping.
- **The steering prompt opens Settings.** The Steer New Messages? banner above the queue now opens Settings at New Messages instead of changing the setting for you. The first time a message steers a running agent, a one-time notice says so and links to the setting.

### Projects

- **Create Project picks a smarter default and explains failures.** The Create Project dialog now preselects the cloud repo or environment of the agent you're viewing, or of your New Chat draft, including multi-repo environments. When creating a project fails, the dialog shows the reason instead of a generic retry message, and if your plan blocks it, the notification includes an Upgrade button.
- **Project workers get renamed when reassigned.** When a Project's coordinator gives a worker a very different task, it can now rename that worker so its name in the sidebar matches the new work.

### Cloud agents

- **See which self-hosted worker runs your agent.** Agents running on a self-hosted pool show the worker's name and its pool in the chat status bar.
- **Find any cloud environment by name from the project picker.** Typing in the project picker searches all of your cloud environments, including ones beyond the first page, and highlights the matching text. The Run on menu shows Cloud with a loading spinner while access is still being checked instead of hiding it.
- **Attach PDFs, code, archives, and other files to cloud agents.** Cloud agent prompts now accept any non-image file up to 10 MB, from drag and drop or the + menu, so the agent can read it in its environment. Videos and empty files are not supported yet, and you'll see a message when a file can't be attached.

### Files, changes, and pull requests

- **Pull requests for Origin repositories open in the Agents Window.** Clicking a github.com pull request link for a repository tracked on Origin now opens the PR tab in the Agents Window instead of your browser, when PR Link Destination is set to open inside Cursor. Bugbot and Automations comments on Origin pull requests now show native Fix with Agent and Add to chat actions instead of raw image buttons.
- **Browser tabs you open stay with your workspace.** Browser tabs you open yourself in the Agents Window now persist with the workspace and stay visible as you switch between agents, like your own terminals. Browsers an agent opens stay tied to that agent. Each workspace also keeps its own cookies, logins, and storage, and signing out of Cursor clears browser data for every workspace.
- **Syntax highlighting now matches your editor theme.** Code in diffs, PR review cards, and the plan tab is highlighted with the same grammars and theme colors as the editor. It updates when you change or import a theme, and no longer drops colors like numeric literals.
- **Markdown previews render math and remember where you were.** Display math wrapped in `$$` now renders as formatted equations in the Markdown preview. Previews also keep their scroll position and cursor per file when you switch tabs and come back.
- **Terminals are easier to reach from more places.** The Terminals pill and platter for an agent's terminals and background shells now also appear in the fullscreen editor's agent overlay. Clicking a headless background shell now opens its output in a tab, Toggle Terminal hides the panel again when a terminal is already open, and the Terminals pill on Project agents opens and closes the terminals tray again.
- **Fresher pull request status.** Cloud agent pull requests now refresh CI checks, reviewers, and mergeability every few minutes, so a stale Debug CI Failure pill clears once checks go green.
- **Fixed missing Git remotes when your Git config uses includes.** Remotes defined in files pulled in with `include` or `includeIf` in your Git config are now detected. Remote URLs that contain spaces, and config sections with comments, are also read correctly.

### Navigation and layout

- **Pinned cloud agents sync across devices.** Cloud agents you pin are now saved to your account for everyone, so they stay pinned across windows and devices. The sidebar's Pinned section also shows them right away at startup instead of waiting for the agent list to load.
- **Better agent search ranking in the Cmd+K palette.** When you search agents with Cmd+K, agents whose conversation contains your search now rank above agents that only loosely match by name or PR link. Typing a pull request number still finds its agent.
- **Open IDE opens the folder you picked.** After running `cursor .` or choosing a folder with Open Folder in the Agents Window, Open IDE now opens that folder in the editor instead of an empty window, even before you start an agent.

### Customization and settings

- **Fixes to MCP approvals and sign-in.** The MCP tool approval prompt no longer offers "Always Allow" when your team's settings or a permissions file manage the allowlist, where the choice had no lasting effect. MCP servers whose saved sign-in was rejected, such as X, now show as needing authentication with a login option instead of failing to load. MCP sign-in cards in cloud agents are no longer dismissed early, and cards you already answered no longer reappear.
- **Close the Automations panel with Esc or Cmd+W.** The Automations panel now closes on Esc or Cmd+W (Ctrl+W on Windows and Linux), just like Settings and Customize. Before, Esc did nothing there, and Cmd+W could prompt you to close the whole window. Esc still goes back one step when you're inside an automation, and it won't close the panel while you're typing in a field.

### Fixes

- **Fixes to agent reliability on long runs.** Cloud agents that keep repeating the same tool call now get the same nudge to break the loop that local agents get. Long turns with many tool calls no longer get stuck summarizing context over and over without freeing any space. File edits no longer fail when a model sends its patch in a different format.
- **Fixes to cloud agent workspaces and slash menus.** Cloud agent workspaces that lose their connection are repaired in place instead of needing a window reload. After you switch accounts or teams, cloud agent slash menus no longer show the previous team's skills.
- **Fixes to the sidebar.** Clicking + on a repository section starts the new agent on exactly that section's repositories. Project rows show the unread dot even while child agents are still working and no longer show an expand chevron when the Projects section is collapsed, and titlebar icons no longer shift when the sidebar collapses.
- **Fixes to workspace search and SSH workspaces.** Workspace search no longer hangs on cloud and remote workspaces. It shows a message while the workspace connects or reconnects, and ends with a clear message if the remote host stops responding. Adding an SSH workspace with several remote folders is also faster.
- **Fixes to the model picker.** Saved MAX-only model variants, like 1M context, now reset only when you turn MAX off, not when you use the picker in a non-MAX chat. When your team lifts a "Restrict to Auto" model policy, the picker no longer keeps showing the restriction notice or hiding the search bar.
- **Fixes to the browser.** Open in External Browser on a local HTML file opens your system browser, and when an admin blocks browser automation your saved browser mode is no longer reset to Off.
- **`/subscribe` works with Origin repositories.** Cloud agents in a repository hosted on Cursor Origin now wait for its CI results and pull request activity with the Origin subscription tools instead of polling. The agent picks the tool that matches the pull request link, so an Origin link no longer goes to a GitHub tool and fails.
- **Fixes to the agent panel.** The agent panel no longer gets replaced by a "Something went wrong" screen when a chat that is still open is unloaded in the background. The chat stays on screen.

## 3.21

### Browser

- **Separate browser sessions per workspace.** The built-in browser now keeps cookies, logins, and storage separate for each workspace, so sessions from one project no longer carry into another. See [session persistence](https://cursor.com/docs/agent/tools/browser.md#session-persistence). Signing out of Cursor clears browser data for every workspace. Element selection and area screenshots respond only to your own clicks, so a web page can't inject fake selections into chat.

### Agent

- **Agent responses start faster.** Cursor prepares the agent in the background when you focus a chat and again when you send a message, so the first response arrives sooner.
- &#x20;**Team rules with file patterns apply only to matching files.** A team rule scoped to a pattern such as `*.py` used to be added to every agent conversation. Now the agent picks it up only when it reads a matching file or you add one to context. Team rules without a pattern still always apply. See [how Team Rules are applied](https://cursor.com/docs/rules.md#format-and-how-team-rules-are-applied).
- **The @ menu no longer shows non-working Docs options.** The Docs category and Add New Custom Docs option had already stopped adding documentation to agent context, so they're gone from the @ mentions menu. Docs chips in older conversations still display.
- **The steering prompt opens Settings.** The Steer New Messages? banner above the queue now opens Settings at New Messages instead of changing the setting for you.

### Editor

- **Math and better code highlighting in the Markdown editor.** The Markdown editor renders `$$` display math blocks as formatted equations. Code blocks in the Markdown and plan editors get the same syntax highlighting and theme colors as the code editor, and update when you switch themes.

### Fixes

- **Removed lines stay removed in agent edit diffs.** In the diff shown for an agent edit, a removed line that starts with "--" stays a removed line.
- **Fixes to editing previous messages.** Editing and resubmitting an earlier message reliably sends your edited text and refreshes checkpoints. While editing in place, Cmd+/ opens the model picker for that message, Escape closes an open picker without cancelling the edit, Shift+Tab works, and the Cmd+Enter-to-submit setting is respected.
- **Fixes to Cloud Agents.** [Cloud agent](https://cursor.com/docs/cloud-agent.md) workspaces no longer show the folder trust prompt or a file-watcher warning you can't fix.
- **Fixes to agent reliability.** Long turns no longer get stuck compacting context on every step, and agent edits no longer fail when the model wraps a patch in JSON. Chats stay attached to their folder after Add Folder to Workspace, and unread badges on agent chats clear when you focus them.
- **Fixes to the model picker.** Saved model variants that need Max Mode, like 1M context, no longer reset when you use the model picker in a chat without Max Mode; they revert only when you turn Max Mode off. When a team lifts its "Restrict to Auto" model policy, the picker drops the old restriction notice and brings back the search bar.
- **Fixes to MCP servers.** The [MCP](https://cursor.com/docs/mcp.md) approval prompt no longer offers "Always Allow" when your team or a permissions file controls the MCP allowlist. MCP servers whose saved token was revoked ask you to log in again instead of showing a connection error. MCP sign-in cards in cloud agents are no longer dismissed early, and cards you already answered no longer reappear.
- **Fixes to git and the editor.** Git remotes defined through `include` or `includeIf` in your git config are detected, and the status bar blame always matches the active editor. The extension host no longer fails to start when an environment variable name begins with a digit, and backups for deleted or unreadable files no longer reopen on every window open. In the Review Changes pane, an older refresh no longer overwrites the newer Issues Found list.
- **Search in remote workspaces no longer hangs.** When search isn't available yet, it now times out and shows an error instead of waiting forever.
- **Fixes to agent visualizations.** Visualization cards from `/visualize` now render in the IDE. Shaded areas in charts no longer render solid black, and the visualization loading row lines up with other tool calls.

## September 17, 2026 release

- **Team details in `origin auth status`.** `origin auth status` prints your teams, role, and organization ids, and `--json` prints them as JSON for scripts.

## 1.9.0

### Composer

- **Attach any file type from Files.** When you add context in the composer, the Files picker now lets you pick any file, not just a fixed list of types. Images attach as images, and other files such as archives, audio, or source code attach as documents. Videos aren't supported and show a message instead.
- **See your words while dictating.** When you dictate in the composer, a live caption shows your words as you speak, with the part still being recognized in gray italics.

### Agents

- **Preview cards in agent chats.** When a cloud agent shares its running app, Cursor for iOS shows a preview card with a screenshot, title, and description. Tap Preview to open the agent's desktop view on cursor.com.
- **MCP sign-in requests.** A cloud agent waiting for you to sign in to an MCP server shows as Needs Attention in the inbox and on the Live Activity until you tap Skip or Authenticate. The sign-in card then says the server is authenticated or that authentication was skipped.

### Agent list

- **Collapse Pinned and Drafts on iPhone.** Tap the Pinned or Drafts header in the agent list to collapse or expand that section. The setting carries over to the iPad sidebar.

### Review

- **Review Origin pull requests.** On Cursor Origin pull requests, a Review button opens a sheet where you can Comment, Approve, or Request Changes with a message.

### Fixes

- **Agent chats.** Links in agent messages open as soon as you tap them, and a new agent's prompt stays pinned to the top instead of jumping when the reply starts. Partly loaded finished conversations reload without duplicating messages, and the loading animation's dots are visible again.
- **Pull requests and repository names.** Tapping Mark Ready on a draft pull request opened from a link now marks it ready for review. Repositories hosted on Cursor Origin or with URLs ending in `.git` show as `owner/repo`.
- **Composer and keyboard.** Renaming an agent no longer pushes the composer bar up with the alert's keyboard. The composer placeholder changes smoothly between new-agent and follow-up text, and the quick-action pills above the composer fade in place, with a plain fade when Reduce Motion is on.
- **Copy and visual polish.** The profile sheet shows chart titles and gridlines while stats load. In-progress labels read "Working" and "Thinking", and the Customize sheet sections are renamed Show and Agent Properties.

## September 16, 2026 release

- **Clearer stack status.** `origin pr stack` shows how each pull request in a stack relates to its parent and the action that repairs it.

## v2026.09.15

### ACP

- **Agent Client Protocol (ACP) clients can show subagents as their own sessions.** Clients that advertise the `subagents` capability get each subagent as a child session linked to the parent Task tool call, with streamed text, thinking, tool calls, and a final completed, failed, or cancelled state. For those clients, a prompt waits for its background subagents and includes their results in the same turn. Cancelling the prompt stops them, and loading a saved session shows its past subagents again. Clients without the capability keep receiving [`cursor/task`](https://cursor.com/docs/cli/acp.md#cursortask) notifications.

### Sign-in

- **Sign-in trusts your operating system's CA certificates.** The proxy-aware fetch that `agent login` uses for its auth requests, directly or through [`HTTPS_PROXY`](https://cursor.com/docs/cli/reference/configuration.md#proxy-configuration), now adds your system's trusted CA certificates to the bundled set, so sign-in works behind corporate TLS inspection once your company's root certificate is in your system's trust store.

### Fixes

- &#x20;**Team rules with file patterns no longer load into every prompt.** A team rule scoped to a pattern such as `*.py` now applies only when the agent reads a matching file. [Team rules](https://cursor.com/docs/rules.md#format-and-how-team-rules-are-applied) without a pattern still apply to every request.
- **`agent models` lists your team's Bedrock models.** When your team connects AWS Bedrock through an IAM role, `agent models` and `--list-models` now show the Bedrock models for your region instead of an empty list. The list matches what `--model` accepts.
- **Shell commands run on macOS computer-use workers.** On a Mac worker started with [`--computer-use`](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md#macos), shell commands no longer fail with "The shell command returned no exit status" before they run.
- **Fixes to agent tools and turns.** When the agent waits on a running shell command, it now moves on as soon as the command finishes or its output matches the pattern the agent is watching for, instead of idling until the timeout. File edits no longer break when the model wraps its patch in JSON. Stopping the agent keeps working after a turn retries a failed connection.
- **Fixes to long turns and Auto-review.** Long turns with many tool calls on Claude and GPT models no longer get stuck compacting context on every step without freeing space. Auto-review now works out a decision from the blocked action when its classifier reply leaves the decision out.
- **Fixes to self-hosted workers.** Workers started with [`--clone-git-repos`](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools) now clone repositories stored without a scheme, such as `github.com/owner/repo`, instead of failing because git read them as local paths. When Cursor rate-limits `agent worker controller`, it waits for the server's `Retry-After` time, up to 1 hour. A pool worker that reconnects with a stale claim now drops it instead of rejecting its next agent, and a worker that fails account validation shows the server's reason instead of a bare "Error".
- **Loop reminders on every model.** When an agent on any model, not just Composer, keeps repeating the same tool calls or messages, it now gets a reminder to try something different instead of looping until it hits the step limit.
- **Asking the agent to stop a goal closes it.** When you ask the agent to stop working toward a [`/goal`](https://cursor.com/docs/cli/reference/slash-commands.md), it can now mark the goal complete instead of leaving it active.

## September 15, 2026 release

### Repositories

- **Edit repository settings.** `origin repo edit` sets the default branch, visibility, allowed merge methods, and delete-branch-on-merge. `origin repo view` shows those settings, and `origin repo list --json <fields>` prints repositories as JSON with optional `--jq` filtering.
- **Manage access from the CLI.** `origin repo access` and `origin namespace access` list, grant, change, and remove access for teams, users, and organization groups, and list the roles you can assign. On repositories in your personal namespace, `origin repo access` also lists, grants, and removes external collaborators, with Read or Write access.
- **Manage GitHub mirrors.** `origin repo mirror` starts a mirror transition, watches its status, syncs a ref on demand, and detaches the mirror, with `--json` output.
- **Verify a migration.** `origin repo verify-migration` compares a GitHub repository's default branch, visibility, merge settings, labels, and rulesets against its Origin copy and exits 1 on a mismatch. Use `--namespace` to check every repository in a namespace.
- **Rulesets, labels, and apps.** `origin ruleset create`, `update`, and `delete` manage rulesets from flags or a JSON spec, and `origin ruleset import --from-github` converts GitHub rulesets or branch protection. `origin label` lists, creates, edits, deletes, and bulk-imports labels. `origin app` manages Origin apps, their signing keys, and webhook deliveries.
- **Stricter CloneKit downloads.** `origin repo clone-fast` checks every range response against the kit's size. If the server stops honoring byte ranges, it downloads the pack as one file, and a range that returns the wrong number of bytes fails the kit download with an error.

### Pull requests

- **Set the merge commit message.** `origin pr merge` accepts `--subject`, `--body`, and `--body-file` to set the commit message for a single pull request. When a stack lands as one commit, the flags are ignored instead of failing the merge.
- **Diffs for very large pull requests.** `origin pr diff` and `origin pr view` fetch the diff in pages, so very large changes no longer fail on an oversized response.
- **Request changes from the CLI.** `origin pr review --request-changes` (`-r`) submits a request-changes review instead of erroring. Pass exactly one of `--approve`, `--request-changes`, or `--comment`.

## Week of Sep 14, 2026

### Web

- **Clearer repository access, and access is removed when people or groups go away.** The Permissions tab in codebase and repository settings is now called Access, and each group there shows whether it's a Team Group, Org Group, or Synced Group from your identity provider, with its member count. When someone leaves a team or organization, they lose the repository access they had through its groups. When an organization group is deleted, the repository and namespace access it granted is removed automatically.
- **Emails when team or group changes affect your repo access.** When you join or leave a team or group, Origin now emails you once per change, listing the repositories and codebases you gained or lost access to. Each resource in access emails links to its page in Origin.
- **Redesigned Apps pages with a Marketplace and clearer install screens.** The Apps page in your codebase settings now opens to a Marketplace for browsing apps, with a separate Manage view for installed apps. The install screen shows whether an app is Verified by Cursor, meaning it's listed in the Marketplace, or Not verified by Cursor. It also has a simpler choice of repositories. App pages can list the publisher's public Cursor plugins, and every viewer of a repository's Apps settings can open installed apps' pages.
- **Faster pull request, repository list pages.** Pull request pages now show the title, status, branches, Auto-merge badge, and existing reviewers on first paint instead of placeholders. Repository lists and a repository's Pull requests list render their first page with the page.
- **Build pull request searches with suggestions.** The search box on the pull requests list now suggests qualifiers like `author:`, `label:`, `assignee:`, `review:`, `is:`, and `sort:` as you type, along with matching values such as repository collaborators and labels. Recognized qualifiers are highlighted in the box so you can see which filters apply.
- **Submodule updates show up properly in pull request diffs.** When a pull request adds, updates, or removes a submodule, the Files changed tab now shows a submodule card with the old and new commits instead of an error or an empty file. When both commits come from the same repository on GitHub or Origin, the card links to a comparison between them.
- **Repository downloads start right away and extract into one folder.** Downloading a repository archive from the codebase page now returns the file directly, even when it has not been prepared yet, so you no longer need to wait and retry. Archives extract into a single `owner-repo-shortsha/` folder and download with that name, matching the layout other Git hosts use. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Clearer names for Bugbot and Security Review checks.** Bugbot checks on pull requests now appear as "Cursor / Cursor Bugbot" and "Cursor / Cursor Bugbot Autofix" under one Cursor group, instead of repeating the same name twice. Security Review checks now appear under "Cursor Security Agent" with the automation name as the check title, instead of an internal account name.
- **Create a repository from the Codebase welcome screen.** If you can create repositories, have none yet, and haven't dismissed the Codebase welcome screen, it now has a Create Repo button under Sync from GitHub that opens the New Repo dialog.
- **Safer pushes, app installs, and rebases.** Pushing a branch or tag whose name isn't valid UTF-8 now rejects only that ref with a clear error, while the rest of the push lands. Creating or installing an app is now refused for namespaces that can't write to Origin, matching repository creation. Commits Origin replays, for example when rebasing a pull request, now keep their jj change-id so jj users keep change identity.
- **Fixes to stacked pull requests and retargeting.** Retargeting a pull request to the base it already has, or to a merged ancestor's branch, no longer detaches it from its stack, and merged stack members now show the branch they landed on as their base. Restacking works on branches that contain merge commits, CODEOWNERS review requests after a retarget match the rules the merge check enforces, and reopened pull requests run CI against a fresh merge with the current base.
- **Fixes to pull request diffs and the API.** Diff timeouts now show a timeout error instead of a generic error, the HTTP API `:syncMirror` endpoint works again, and browsing a repository with no commits reports an empty repository error.
- **Search commits by SHA.** A repository's Commits page now has a search box. Type at least five characters of a commit SHA to preview matching commits, or press Enter to list the commits that start with that SHA.

### API

- **Search file contents through the Origin API.** A new Grep Contents operation in the Origin API searches the files in a repository at any ref and returns the matching lines. You can use a regular expression or exact text, ask for surrounding context lines, and narrow the search with include and exclude globs. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Check whether a pull request can merge from the API.** A new preview endpoint in the Origin API tells you whether a pull request is mergeable and, if not, what is blocking it: required checks, approvals, code owner approvals, merge conflicts, or the shape of its stack. You can pass an expected head commit so the answer fails fast if the pull request has moved. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Sort pull requests by recent activity and list only merged ones.** When you list pull requests through the Origin API, you can now sort them by last update instead of creation time and filter to merged pull requests only. Sorting by update time also works in the Origin MCP server's pull request listing tool. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Delete branches through the Origin API.** You can now delete a branch from a script or integration with the Origin API, without pushing a deletion. The default branch and branches in mirrored repositories can't be deleted this way, and open pull requests from the deleted branch are closed. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Add repositories to an existing app installation through the Origin API.** Namespace admins can now add repositories to an app installation through the Origin API without going through the install flow again. The call only adds repositories and never changes the app's permissions. If the app isn't installed yet, the error now explains that an admin must finish the first install in the browser and includes the link to open. Listing an installation's repositories now also accepts a case-insensitive filter on repository name or `owner/repo`. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Webhooks for pull request labels.** Origin apps can subscribe to `pull_request.label.added` and `pull_request.label.removed` events, so your automations can react when labels change on a pull request. Each event includes the pull request and the label, and label-added events also include who added it. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for payload details.
- **Email alerts when webhook deliveries pause.** If your Origin app's webhook deliveries are paused automatically after repeated failures, namespace admins and the people who created or last edited the app now get an email with a failure summary, recovery steps, and a link to manage deliveries. Receivers now have up to 10 seconds to respond before a delivery times out, up from 5. Check run created and completed payloads no longer include a top-level `actor`; use `check_run.actor` instead. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).
- **Scope changes for apps and repository creation.** Reading app details through the Origin API now requires the namespace apps read scope, and creating or mirroring repositories requires the "Create repositories" scope. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.

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
- &#x20;**Admins can run team MCP servers on members' machines.** A new Run team MCP servers on members' machines switch in the Team MCP Servers section of the Plugins & MCPs tab runs every team HTTP MCP server, and each member's own MCP servers, locally in members' IDEs after a confirmation. Cloud agents still run team servers from Cursor's servers. Teams and members can also configure up to 1,000 MCP servers each.
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

## Week of Sep 14, 2026

- **Clearer Bugbot check names on Origin.** On Origin pull requests, Bugbot's checks are now named "Cursor / Cursor Bugbot" and "Cursor / Cursor Bugbot Autofix". Required-check rules that already list Bugbot keep matching.

## 3.20

*Enterprise teams get Projects from 3.21.9 unless opted in.*

### Agents

- **Stopping a subagent now stops its nested subagents too.** Clicking Stop on a subagent, or Stop all, now also stops every subagent it started, including finished or idle ones that had been unloaded and background subagents still running. Questions those subagents were waiting on are cancelled, and the parent's task shows as stopped.
- **Goals and background tasks now keep your chat's Auto-review setting.** When a goal continues on its own or a background task wakes the agent, it now uses the same Auto-review setting as the messages you type in that chat.
- **Asking the agent to stop a goal closes it.** When you ask the agent to stop a goal, it can now mark the goal complete instead of leaving it active.
- **Saved MAX model variants stay selected.** Picking a model in a chat without MAX Mode no longer resets your saved MAX-only variants, such as a 1M context window or Fast. Those saved choices now reset only when MAX Mode actually turns off.
- **No more CPU-sampling stalls on many-core Linux machines.** On Linux, Cursor no longer stalls while sampling CPU usage on machines with many cores.

### Chat and composer

- **Answer subagent questions without leaving the parent chat.** When a subagent is waiting on a question, the parent chat's question tray now shows it under "Question from" and the subagent's name, and clicking Answer on a subagent row brings its question up there too, including for cloud subagents. You can also collapse the tray to a Questions pill that shows the count and reopens it, and file and web links in questions now open when clicked.
- **Status pills above the prompt are easier to scan.** Pills above the prompt now list live status first (pending input, Changes, Agents, Terminals, Canvas, Queue), then quick actions, and status pills stay visible when a tray is open. The Terminals pill shows a spinner while an agent's command is running, and the branch-mismatch pill now reads Checkout Branch with the branch name in a tooltip.
- **Scroll the chat with Page Up, Page Down, Home, and End.** Page Up and Page Down scroll by about a page, and Home and End jump to the top or bottom of the conversation. Pressing End while the agent is still replying keeps the view following new output.
- **Cleaner links and code blocks in agent responses.** Long bare URLs in agent responses now show as the site's host plus a shortened path, so they no longer stretch across the conversation. Code blocks labeled with a file extension, like the file-referenced blocks agents use for `.rs` files, are now syntax highlighted instead of shown as plain text.
- **More reliable file attachments in prompts.** You can now attach `.har` files from the + menu, the same way as JSON files. Documents you add show up as file mentions again and stay attached when you switch a new chat between local and cloud before sending. Removing a file's mention from a cloud agent prompt now stops that file from being uploaded.
- **Live microphone meter while recording voice input.** While you dictate, the voice toolbar now shows a compact live meter next to the recording time, so you can see the mic is picking you up. Background noise settles into dots, and the bars rise only when you speak.
- **Clearer diagrams in chat.** Diagrams the agent draws inline now open with a title and an optional short subtitle, the same header charts use. Explanations stay in the chat reply instead of inside the figure, outlines are darker so shapes read at a glance, and diagrams size to the chat column, down to narrow widths.

### Projects

- **A simpler Create Project dialog.** The Create Project dialog has a new layout: an icon picker, a centered name field, and rows to choose the project's Workspace and Model.
- **Edit Workspace for SSH and WSL multi-root workspaces.** You can now use Edit Workspace on multi-root workspaces that run over SSH or WSL, when the workspace file is on your computer, to rename them and to add or remove folders. Add Folder opens a folder browser on that remote machine. Edit Workspace is still not offered for dev containers.

### Cloud agents

- **Retry cloud agents that stop on an error.** When a cloud agent stops with a retryable error, the Agents Window now shows a Retry button in the transcript that resumes the run without sending a new message. Generic failures show "This run hit an unexpected error. Retry or send a follow-up below." instead of a raw error, and interrupting a running cloud agent with a new message now shows status text like "Changing course…".
- **Validation for cloud environment config.** Editing `environment.json` now validates and autocompletes the egress allowlist and mode, inline Dockerfile contents, base image, and testing fields.

### Files, changes, and pull requests

- **Switch repositories and filter files in the Changes tab.** When a workspace has more than one repository or Cursor worktree, a picker in the Changes tab header lets you switch between them, with worktrees labeled as such. The local changes file tree also gains search and options to show or hide deleted and test files, and stage, unstage, and discard all act only on the files you can see while filters are active.
- **Empty editor panel tabs now help you get started.** Empty Files and Browser tabs now open to a searchable start page, so you can find a file or page without leaving the tab, and the Browser start page includes suggested recents. An empty Changes tab lets you search the branch's pull requests when it has any, and a Changes tab with nothing to show now says that changes on this branch will appear there.
- **Clearer errors when pull request actions fail.** When merging, creating, marking ready, closing, or reopening a pull request fails, the error toast now names the action and shows the actual reason, and it appears again if you retry.

### Navigation and layout

- **Remove from Sidebar and Archive All now act on just the group you clicked.** Removing a sidebar group, including a cloud or named-environment group, hides only that group and leaves the repo's other groups in place. Archive All on a group now also archives its cloud agents that hadn't loaded yet, and Undo restores them. Sidebar rows also animate when they reorder, unless reduced motion is on.
- **Roomier window chrome and consistent icons.** The Agents Window titlebar, tab strips, and file, diff, pull request, and terminal panel headers are taller, with more space beside the macOS window controls. Icons in the search panel, window controls, dialogs, and quick picks now use Cursor's own icon set, and the apps rail Collapse/Expand button stays in place when you toggle between the labeled and icon-only rail.

### Customization and settings

- **Easier MCP setup and more reliable MCP sign-in.** When several MCP config entries point at the same server, the MCP view now shows them as one group with a label for each entry. Plugin MCP configs that use `${env:NAME}` placeholders now resolve those values. Sign-in also works more reliably for Microsoft servers in tenants where an admin already granted consent and for connections behind corporate certificate authorities.
- **Clearer API key settings for OpenAI, Anthropic, and Google.** In Settings, Models, each provider now has its own labeled API Key field, a Use API Key switch that appears once a key is saved, and, for OpenAI, a Base URL override switch with its own field. Keys save when you leave the field or press Enter, and you can remove a saved key by clearing the field.
- **MCP, plugin, rules, and hooks settings open in Customize.** Commands and links that open MCP, plugins, rules, or hooks settings, including the MCP link in Automations, now go to the matching Customize page. MCP servers in Customize show a yellow status dot when they need sign-in, are connecting, or are degraded.
- **Security fixes.** Terminals in an untrusted workspace no longer start a shell after you decline or dismiss the trust prompt, and opening a `cursor://` extension link no longer runs built-in handlers until the link is trusted or you approve it. Spawned processes and remote terminals no longer inherit injection variables such as `NODE_OPTIONS` and `LD_PRELOAD`, and extensions that receive binary command results or webview resources get only the requested bytes, not shared internal memory.
- **`/canvas` is for work you come back to.** The agent now creates a canvas for reports, dashboards, and data-heavy investigations you may revisit, refine, or share.

### Fixes

- **Fixes to cloud agents.** Cloud agents now open reliably on the first click, retrying briefly if the agent isn't ready, and no longer ask you to trust each agent's workspace.
- **Fixes to subagents and Project workers.** Running Project workers no longer look finished in the subagent tray, worker counts aren't inflated, and dismissed errored workers stay dismissed. Approval prompts from background subagents reach you, and a failed worker's kickoff prompt no longer lands in your new-agent input.
- **Fixes to the New Agent screen.** Clicking New Agent now reliably shows the new agent input. A chat that's still loading, a view reload, a workspace switch, tiled conversations, or a fullscreen editor no longer replaces it with the previous chat or a blank pane. Opening a folder with `cursor <folder>` also always starts a new agent draft instead of doing nothing.
- **Fixes to the chat transcript.** Charts and diagrams in chat no longer stay blank, hovering a pull request link no longer blanks the chat pane, and forking a chat with missing message content now works instead of failing. File links in transcripts open faster on remote workspaces, and user messages no longer render at the wrong height.
- **Prompt autocomplete respects .cursorignore.** Autocomplete suggestions in the prompt no longer include files excluded by .cursorignore.
- **Fixes to settings search.** Settings search no longer shows duplicate results.

## 3.20

### Agent

- **Agents can use the browser by default.** Browser tools are now on by default, so the agent can open your app and check its own UI changes without you turning the [browser](https://cursor.com/docs/agent/tools/browser.md) on first. Admins who turned off browser features for their team keep them off.
- **Stopping a subagent now stops its nested subagents too.** Stop on a [subagent](https://cursor.com/docs/subagents.md), or Stop all, now also stops every subagent it started, so nested work no longer keeps running in the background. Questions pending from the stopped subagents are dismissed.
- **Page through agent chats from the keyboard.** With the agent chat focused, Page Up and Page Down scroll by a page, and Home and End jump to the top or bottom. Pressing End while a reply streams keeps following new output.
- **Live microphone meter while dictating.** When you [dictate](https://cursor.com/docs/agent/prompting.md#voice-input) into the agent input, the recording indicator is now a compact meter that follows your microphone level, so you can see that Cursor hears you.
- **Long links in chat no longer take over the conversation.** Long raw URLs from the agent now show the full hostname and a shortened path, with query strings and fragments collapsed. Clicking the link still opens the full address.
- **Fixed HAR files not attaching to the agent prompt.** HAR files you pick or drag into the agent prompt now attach instead of being dropped.

### Models

- **Claude Fable 5.1 makes smaller, more focused edits.** Agent runs on [Claude Fable 5.1](https://cursor.com/docs/models/claude-fable-5-1.md) now use instructions written for that model. It writes plainer prose, asks for permission less often, stays within the task's scope, and makes smaller, targeted edits.
- **Fixed saved Max-only model variants resetting.** Picking a model in a chat without [Max Mode](https://cursor.com/docs/models-and-pricing.md#max-mode) no longer resets saved Max-only variants, such as a 1M context window or fast mode.

### MCP and plugins

- **Fixed sign-in for plugins whose MCP servers need your own values.** [Plugins](https://cursor.com/docs/plugins.md) whose MCP configuration references `${env:NAME}` values now show a field for each value when you install or edit the plugin, and Cursor fills in what you enter. Before, the placeholder text went to the server as-is, which broke sign-in for some marketplace plugins.
- **MCP, plugin, rules, and hooks settings open in Customize.** Commands and links that open MCP, plugins, rules, or hooks settings now go to the matching Customize page. MCP servers in Customize show a yellow status dot when they need sign-in, are connecting, or are degraded.
- **One group for MCP entries that share a server.** When several [MCP](https://cursor.com/docs/mcp.md) config entries point at the same server, the MCP list shows them as one group, titled with the name the entries share. If you select more than one entry in the group, each selected entry gets its own label.

### Cloud agents

- **Fixed false errors when editing cloud agent environment files.** Editing `.cursor/environment.json` no longer flags valid fields as errors. The editor now validates and autocompletes `egressAllowlist`, `egressMode`, `image`, inline `build.dockerfileContents`, `chromeExecutablePath`, and `enable_testing`. See [cloud agent setup](https://cursor.com/docs/cloud-agent/setup.md).

### Editor and Tab

- **Signature help remembers the overload you picked.** When you cycle to a different overload in TypeScript and JavaScript signature help, it stays selected as you keep typing arguments.
- **Tab auto-import works with Pyrefly.** With the Pyrefly language server for Python, Tab now offers to import names Pyrefly reports as undefined, as it already did for Pylance and basedpyright.

### Fixes

- **Security fixes.** Terminals in an untrusted workspace no longer start a shell after showing the trust error, and `cursor://` extension links no longer run handlers before you approve them. Processes Cursor starts, including remote terminals, no longer inherit environment variables that can inject code, such as `NODE_OPTIONS` and `LD_PRELOAD`. JavaScript and TypeScript language features are now off in untrusted workspaces.
- **Fixed MCP sign-in and connections.** Signing in to Microsoft [MCP](https://cursor.com/docs/mcp.md) servers no longer asks for admin approval when your tenant admin already granted consent, and servers that use OAuth dynamic client registration no longer fail with an `invalid_scope` error. On Windows, MCP servers behind enterprise certificate authorities now connect when the certificate is in the Intermediate or machine-wide stores.
- **Fixed subagents.** Approval prompts for tool calls from background [subagents](https://cursor.com/docs/subagents.md) now appear instead of being auto-rejected, and subagent cards from older conversations load reliably.
- **Fixed the agent chat transcript.** After Restore Checkpoint, the restored turn and later turns no longer show stale footers, and autocomplete suggestions in the agent input skip files excluded by `.cursorignore`.
- **Fixed editor stability and layout.** Webviews stay aligned with their editor while you scroll or resize. On Linux, Cursor no longer runs out of file descriptors under heavy load. The built-in Browser's DevTools loads again, and Git remotes defined through `include` or `includeIf` are detected.

## September 8, 2026 release

- **Print your auth token.** Run `origin auth token` to print the access token the CLI is configured to use.
- **Git authenticates with `CURSOR_AUTH_TOKEN`.** When `CURSOR_AUTH_TOKEN` is set, git operations through the Origin credential helper use it before stored credentials, so headless jobs can export the token instead of running `origin auth login`.
- **Clear error for an expired token.** If `CURSOR_AUTH_TOKEN` has expired, the CLI stops with a message that the token must be refreshed instead of sending it and failing with a 401.
- **Control CloneKit fallback.** `origin repo clone-fast --fallback never` exits non-zero instead of falling back to `git clone`, and the command now reports which phase stopped.

## Week of Sep 7, 2026

### Web

- **Stacked pull requests merge as one commit, and your commit text lands.** Merging a pull request in a stack now lands it together with the open pull requests below it as a single commit. When you merge a single pull request, the commit title and message you edit in the merge popover now land exactly as written.
- **Pause, resume, and test app webhook deliveries.** Your app's settings page now has a Webhook Deliveries section. Once the app has a webhook URL, the section shows whether deliveries are active or paused, and has Pause, Resume, and Send Test Delivery buttons. Events that queue up while deliveries are paused are dropped, not sent late when you resume. Origin may also pause deliveries on its own, but only after a receiver has failed every delivery for 72 hours, with at least 20 failed deliveries in that time.
- **Codebase settings has a sidebar and linkable sections.** Codebase settings now uses a sidebar instead of tabs, with a Back to Codebase link at the top. Each section, such as Permissions and Apps, has its own URL you can bookmark or share, and older settings links redirect to the right section.
- **Download a copy of your repository.** Repository settings now have a Data section on the Advanced tab with a Download repository button that saves a tarball of the latest default branch. Origin API clients can request the same archive for any ref; see the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).
- **See the pull requests behind a commit.** When a commit was pushed as the head of an Origin pull request, or is the merge commit Origin created when landing pull requests, its commit details now include a References section listing those pull requests' branches, with links to each branch and its pull request. Each pull request shows whether it is open, draft, merged, or closed, and long lists collapse behind More and Less. References appear on repositories hosted on Origin, not on repositories mirrored from GitHub.
- **Easier-to-scan pull request lists.** Pull request lists now show larger titles that wrap instead of truncating, with a line under each title showing the pull request number, its author, and how long ago it was opened. Rows highlight on hover and match the style of the commits table.
- **Image previews in pull request changes.** Added or changed PNG, JPEG, GIF, and WebP files in a pull request's Changes tab now show a preview instead of an empty binary file card. Transparent images sit on a checkerboard background, so light icons stay visible in light theme and dark icons in dark theme.
- **Safer pushes to Origin repositories.** Origin now refuses a `git push` that deletes a repository's default branch, with the error "refusing to delete the current branch", matching Git and GitHub. Other branches can still be deleted. Pull request refs under `refs/pull/` and `refs/changes/` no longer appear when you push and can't be overwritten by a push.
- **Pull request bases must be existing branches.** Creating or retargeting a pull request now rejects a base that is a commit SHA, a tag, or a branch that doesn't exist, with an error saying the base must name an existing branch. Before, these bases were accepted but left the pull request unable to get a merge ref for CI or to be merged.
- **Merge when ready no longer gets stuck on pull requests that can never merge.** If a queued merge fails for a permanent reason, such as missing permissions or a pull request that no longer exists, merge when ready now turns itself off instead of retrying indefinitely. Merge conflicts and a changed head still leave it on.
- **Re-run checks on pull requests.** Completed checks whose app allows retries now show a re-run button on the pull request, and you can also re-run them with a new Origin API endpoint. The check reads as pending, and still blocks merge if it is required, until the app posts a new result. Apps receive a new `repository.check_run.rerequested` webhook, and check runs now include `rerequested_by`.
- **Fixes to pull request pages and sign-in.** A brief problem with Cursor's session check no longer signs you out of pull request pages, and stack pages load faster and still open for large organizations.
- **Fixes to repository reads and merge errors.** File and blame reads on repositories with long delta chains no longer fail. Merging branches with unrelated histories, and checking whether stacks with more than 200 pull requests can merge, now return clear errors instead of internal server errors.
- **Fixes to repository pages and links.** Commit links in GitHub's URL format (`/owner/repo/commit/<sha>`) on Origin's git host now redirect to the repository page instead of failing. Pinned and Recently Viewed repository cards now update their source icon when a repository's mirror status changes, and the "Origin access is not enabled" error now points you to cursor.com/codebase to request access.

### API

- **Manage Origin apps from the API.** You can now create, list, view, and update your namespace's apps through the Origin API, and add or revoke the signing keys they authenticate with, so you can script app setup and rotate keys without the web UI. App responses also include the owning namespace, description, website, and default scopes. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for endpoint details.
- **Manage repository mirrors from the Origin API.** You can now change a mirrored repository's mirror state, detach it from its upstream source to make it a native repository, and poll the transition job until it finishes, all from the Origin API. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for endpoints and required scopes.
- **Choose merge or squash when merging through the API.** The Origin API's Merge Pull Request operation and the `merge_pull_request` MCP tool take an optional merge method, `merge` or `squash`. Leave it out to use the repository's default. If you ask for a method the repository doesn't allow, the error starts with the same sentence other forges use, so existing merge tooling recognizes it. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).
- **Service account keys can read repository settings.** Repo-scoped team API keys for service accounts can now read repository settings, rulesets, and labels through the Origin API, so automation can audit rulesets and compare settings without a user token. Changing settings still requires a user. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **More detail in Origin API webhooks.** Installation objects in webhook payloads now include when the installation was last updated, comment-created events carry the new thread's created and updated times, and every event payload is now documented with a sample. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for field details.
- **Fixes to Origin API comments and webhooks.** Creating an inline comment or review through the Origin API with a line range past the end of the file now fails with a clear error naming the file and its line count, instead of being accepted. Webhook events are no longer dropped when a brief database outage interrupts delivery; they are retried. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Manage owner and repository access from the Origin API.** You can now list, grant, change, and remove the access that users, groups, and team groups have on an owner or a repository through the Origin API. Each grant shows its permission level. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for endpoints and required scopes.
- **Update repository settings from the Origin API.** You can now change a repository's default branch, allowed merge methods, automatic branch deletion on merge, and visibility through the Origin API. Repository responses also include these settings, so you can read and update them programmatically. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for endpoint details.

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

## Week of Sep 7, 2026

- **Large generated files no longer block reviews.** Files marked `linguist-generated` in `.gitattributes`, such as lockfiles, are left out of Bugbot's size check even when they are larger than 2 MB. Bugbot reviews the rest of the pull request instead of skipping it as too large.
- **Bugbot dashboard dialogs close with Escape.** The disable, bulk repository action, and cancellation dialogs in the Bugbot dashboard now close when you press Escape.
- **Azure DevOps fixes.** When a pull request summary would exceed Azure DevOps's 4,000-character description limit, Bugbot posts the full summary as a comment and says so in a shorter description. Organizations whose tenant check names no tenant can now enable Bugbot instead of failing tenant discovery. When an Azure DevOps pull request event includes its head commit, Bugbot queues the review without first reading the pull request from Azure DevOps, so a brief Azure DevOps or Entra outage no longer fails the event.

## September 4, 2026 release

- **Faster CI clones with CloneKit.** For repositories with CloneKit turned on, `origin repo clone-fast` downloads a prebuilt clone kit, verifies it, fetches newer objects, checks out the default branch, and prints how long each phase took.
- **More reliable large clones.** `origin repo clone` raises git's HTTP post buffer, so large fetches no longer fail with "unable to rewind rpc post data" after a dropped connection.

## 1.0.31

- **Background subagents report back.** When the agent runs a subagent in the background, its result now returns to the parent as a follow-up turn on the same run instead of being dropped when the parent turn ends. `run.stream()` keeps yielding through those turns and `run.wait()` resolves after them. Local agents, in TypeScript and Python.
- **Annotate custom tools.** `annotations` on a `local.customTools` entry passes MCP tool annotations (`title`, `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`) through to the model. They are descriptive hints only; the SDK does not enforce them. TypeScript only.

## 3.19

### Agents

- **Stopping a subagent now stops its nested subagents.** Stopping a subagent from the Agents Window now also stops every subagent it started, including ones you haven't opened. Previously only the selected subagent stopped while its children kept running. The parent task is also marked as interrupted.
- **Subagents show the model you asked for.** Subagent cards now show the model and subagent type their task requested. Task calls that use an older spelling of a model name now run on the matching model instead of failing.
- **Clearer errors when deploying with Vercel.** When the deploy-with-vercel skill hits a Vercel error, such as a project that already exists, the Vercel app missing access to your repository, Hobby plan limits, or a protected deployment, the agent now relays the actual error and what to do next. If the Vercel app can't access your repository, the agent links the app install page with that repository already filled in.

### Chat and composer

- **Copy tables from agent replies as Markdown.** Right-click a table in an agent's reply and choose Copy Table to copy it as Markdown, ready to paste into docs, issues, or another chat. The same menu also offers Copy Message to copy the whole reply.
- **`/summarize` works on cloud agents.** Running `/summarize` (or typing `/compact`) on a cloud agent now summarizes the conversation on the cloud agent itself, freeing up context without leaving the chat. If the agent is still working, you'll see a notice asking you to wait, and `/summarize` no longer wrongly refuses on agents moved from cloud to local.
- **Collapse the Questions tray and come back to it.** When an agent asks you questions, you can now collapse the Questions tray into a pill in the agent header that shows how many questions are waiting, then click it to reopen the tray and answer. The tray also has larger question text, with step navigation moved into the footer, and its title says "Question" when there is only one.
- **Clearer choices when you resubmit an earlier message.** When you edit and resubmit an earlier message after files have changed, the dialog now asks "Revert files to this message?" and explains that later messages will be removed either way. Choose Revert Files to restore files to that point, or Keep Files to resubmit without touching your changes.
- **Dictated text settles while you keep talking.** During voice dictation, text the speech provider has already finalized no longer shows as pending until you stop talking.

### Cloud agents

- **See and manage what your cloud agent is listening for.** When your cloud agent has active subscriptions, a **Listening** pill with a count appears above the chat input. Click it to see each event or schedule the agent is waiting on and when it last fired or was set up, remove ones you no longer need, or open the full Subscriptions tab.
- **Pick team pools and remote machines faster from Run on.** For teams that require self-hosted workers, the Run on menu now lists recently active pools with free machines directly and no longer shows Cloud options. Under Remote Machines, pools with free machines are suggested first and each pool's repository is shown, and handing a local agent off to a remote machine with Remote Control always uses the exact machine you picked, even when several share a name.
- **Reconnect to remote workspaces without reloading the window.** When the Agents Window can't restore a connection to a remote workspace or cloud agent, it now shows a notification with a Reconnect button that stays open until you act on it, so you no longer have to reload the window. If a manual reconnect fails, the notification says the workspace is still disconnected and offers Try again. Cloud agent connections also stop retrying automatically after about three minutes instead of retrying forever.
- **Desktop and Environment tabs for more cloud agents.** Cloud agents running on your own machine or a private worker now show the Desktop tab once the worker is connected and sharing its desktop, without reselecting the agent. If you close the Environment tab, you can reopen it from the new tab menu or the collapsed apps rail, and secrets and builds in that tab now apply to the saved environment the agent started from.

### Files, changes, and pull requests

- **Paste files from Finder or Explorer into the Files tree.** Copy files in Finder or File Explorer, click into the Files tree, and press Cmd/Ctrl+V to add them to the selected folder or the current file's folder. Copy and cut in the Files tree now use the system clipboard, and Paste always appears in the context menu.
- **Create files and folders right where you need them.** In the Files panel, hover a folder to reveal New File and New Folder buttons that create the item inside that folder. Folders also show open and closed folder icons, with the expand chevron appearing on hover.
- **Remove a pull request from the GitHub merge queue.** When a pull request is in the GitHub merge queue, the PR header now shows a Remove From Queue button instead of a disabled In Merge Queue label. After you confirm, the PR leaves the queue; adding it back later puts it at the end.
- **Quicker pull request tab actions.** Close PR in the pull request tab menu now closes the PR right away without a confirmation dialog, and the copy and edit buttons next to the PR title are always visible. The stack navigator refreshes on its own and when opened.
- **Collapse or expand every file in a diff with one shortcut.** Press `Ctrl+Shift+;` on macOS or `Shift+Alt+;` on Windows and Linux in the Diff, Agent Changes, or pull request tab to collapse every file card, then press it again to expand them. The tab's menu now shows the shortcut next to Collapse All and Expand All.

### Navigation and layout

- **Jump to unread agents from the macOS Dock.** On macOS, right-clicking the Cursor Dock icon after using the Agents Window now shows an Unread section listing agents with new results, and clicking one opens it. Agents that are still running no longer count as unread.
- **Jump to a running agent from the quit dialog.** When you quit or restart while agents are still working, click any agent listed in the confirmation dialog to cancel quitting and open that agent so you can check on it.
- **More precise Remove from Sidebar.** Remove from Sidebar now hides exactly the group you clicked, such as a named cloud environment, a repo's cloud agents, or the whole repo, and creating an agent there brings the group back.
- **Command palette keyboard navigation.** In the Cmd+K palette, Tab again moves focus between the search box and the filter chips; use Cmd+\[ and Cmd+] (Ctrl+\[ and Ctrl+] on Windows and Linux) to change filters.

### Customization and settings

- **More reliable MCP sign-in for cloud agents.** Signing in to an MCP server for a cloud agent on desktop now finishes through a local redirect back to Cursor, so servers that reject custom app links work.
- **Clearer plugin details in Customize.** For plugins you have installed, the plugin page in Customize now shows the plugin's own version, plus links to its homepage and repository when the plugin lists them. If your version of Cursor can't install a plugin, its page shows install as unavailable.
- **Clearer automation status and settings.** If you can't turn an automation on or off, its detail and Run History pages now show a plain Active or Inactive status instead of a greyed-out toggle. Opening an automation now loads its saved environment into the form, and the Microsoft Teams channel picker uses checkboxes and lists your selected channels at the top.
- **Index New Folders is gone from settings.** Settings no longer show the Index New Folders toggle, and the network diagnostic no longer runs a Codebase Indexing check.

### Fixes

- **Fixed certificate errors on Windows corporate networks.** On Windows, MCP servers (including MCP sign-in) and other network requests now trust certificates from the Intermediate store and from machine-wide and enterprise CA stores that IT deploys through group policy. This fixes errors like `UNABLE_TO_VERIFY_LEAF_SIGNATURE` when you connect through a corporate proxy or to an internal MCP server.
- **Fixes to subagent Task cards and status.** Task cards for subagents settle as stopped or finished instead of spinning forever, and the subagent tray and agent list show accurate statuses without duplicate or lingering rows for finished subagents. Archiving an agent whose cloud subagents have finished no longer asks for confirmation. A cloud subagent that fails before its first response no longer leaves its kickoff prompt in the New Chat input.
- **Fixes to the subagent tray.** Subagent rows also show an environment icon only when the subagent runs somewhere different from its parent, with a desktop icon for self-hosted workers.
- **Fixes to steering messages.** Steering messages a cloud agent can't take mid-run now move to the queue as editable follow-ups instead of looking sent, and steers no longer appear twice, pin to the top of the chat, or leave stray rows in the queue.
- **Fixes to follow-ups.** A follow-up you start typing on a just-created cloud agent is no longer lost when you switch away and come back.
- **Editing an earlier message in a cloud agent clears stale follow-ups.** Editing an earlier message in a cloud agent clears stale queued follow-ups and uses the model you picked.
- **Fixes to agent questions.** Typing a follow-up while an agent is asking questions now closes the question tray right away and marks the question as skipped, and questions from finished runs no longer stay stuck as pending.
- **Fixes to MCP servers and hooks.** Connecting to MCP servers that use OAuth dynamic client registration no longer fails with an invalid scope error, and OAuth sign-in to the Stripe Link MCP server now completes. `beforeMCPExecution` hooks receive the server's command or URL instead of an empty value.
- **Fixes to local agent runs.** File and symbol suggestions respect `.cursorignore`, and goal continuations and background wakeups follow the chat's Run Mode.
- **Performance and stability fixes.** Notifications from closed workspaces no longer linger in the tray, and Cursor no longer runs out of file descriptors on Linux. Forking or duplicating a long local chat with /fork is also faster, because its messages are copied as-is instead of rewritten.
- **Fixes to chat and the prompt.** Chats with a corrupted saved canvas no longer crash the agent panel, and HEIC/HEIF images attach correctly. Sharing a chat that's too large now gives a clear error, and Report Bug shows when it's sending or has failed.
- **Fixes to Agents Window panels, tabs, and menus.** Markdown Preview and the Plans tab now refresh when their files change on disk. Floating toolbars in browser, image, and PDF tabs no longer hide behind the fullscreen composer, top bar buttons respond to clicks reliably, Changes opens even while the workspace is still loading, and settings search no longer leaves the pane clipped.
- **Fixes to skills in Customize.** Skills in the User section of Customize no longer wait on team rules to load from the dashboard before appearing.

## 3.19

### Agent

- **Voice dictation detects your spoken language automatically.** Dictation in the agent input recognizes the language you speak instead of assuming US English. Auto-Detect is the new default in the voice settings menu shown while recording, and you can still pick a specific language there. See [voice input](https://cursor.com/docs/agent/prompting.md#voice-input).
- **`/summarize` works in cloud agent chats.** Running `/summarize` on a cloud agent conversation summarizes it on the cloud agent instead of doing nothing. Typing `/summarize` or `/compact` in the chat input also triggers summarization, and you get a notice if the agent is still working.
- **Copy tables from agent responses as Markdown.** Right-click a table in an agent response and choose Copy Table to copy it as Markdown, or Copy Message to copy the whole response.
- **Clearer prompt when resubmitting an earlier message.** When you edit and resubmit an earlier message and your files have changed since that point, Cursor asks "Revert files to this message?" and explains that later messages are removed either way. Choose Revert Files (Enter) to restore your files to that point or Keep Files (Shift+Enter) to keep your current changes. In Ask mode, resubmitting leaves your files alone and doesn't ask. See [checkpoints](https://cursor.com/docs/agent/overview.md#checkpoints).
- **Faster Fork Chat on long chats.** Fork Chat on a long local chat is faster, because its messages are copied as-is instead of rewritten.

### Subagents

- **Approve subagent file edits and MCP tool calls from collapsed cards.** Collapsed [subagent](https://cursor.com/docs/subagents.md) cards show Allow for pending file edits and MCP tool calls, not only terminal commands, so you can approve without expanding the subagent.
- **Stopping a subagent stops its nested subagents too.** When you stop a subagent, every subagent it started also stops, including ones you never opened, so no background work keeps running. The parent task is marked as interrupted.

### MCP and plugins

- **More reliable sign-in for cloud MCP servers.** Signing in to a cloud MCP server completes through a local browser redirect, fixing servers that rejected the sign-in with an invalid redirect error, and gives you up to 15 minutes to finish consent. In Customize, the server's auth status updates on its own when you return to Cursor, and removing a cloud account asks you to confirm. See [MCP authentication](https://cursor.com/docs/mcp.md#authentication).
- **Plugin pages show fuller details.** Plugins your Cursor version can't install show a disabled Install button with a clear message. Plugin pages in Customize show the author's declared version, homepage, and repository links.

### Remote development

- **Reconnect to a remote workspace without reloading the window.** When Cursor can't reconnect to a remote workspace, it shows a persistent "Unable to reconnect to the remote workspace" notification with a Reconnect Now button instead of a dialog asking you to reload the window. The reconnecting progress notification no longer offers Reload Window, so you keep your window state while retrying.

### Fixes

- &#x20;**Fixed certificate errors on Windows corporate networks.** On Windows, MCP servers, MCP sign-in, and extensions trust certificates from the Intermediate store and from machine-wide, group policy, and enterprise CA stores. This fixes TLS errors such as `UNABLE_TO_VERIFY_LEAF_SIGNATURE` when IT deploys certificates to those stores.
- **Fixes to subagents.** Tool calls inside subagents that need approval show the approval card instead of stalling. Cloud subagents no longer go missing from the agent list in runs with more than 100 of them.
- **Fixes to queued and steering messages.** Queued messages keep the mode they were queued in and are no longer posted twice when the agent has an unanswered question. Editing and resubmitting a cloud agent message uses the model you pick, and the first follow-up after starting a cloud agent is no longer lost.
- **Fixes to cloud agent status and streaming.** Cloud agents no longer get stuck on a stale status. Conversations keep streaming new output after an agent goes idle and resumes, and the first cloud agent follow-up after Cursor has been idle no longer fails with a "Canceled" error.
- **Fixes to MCP sign-in.** Connecting to MCP servers that use OAuth dynamic client registration no longer fails with an invalid scope error, and signing in to the Stripe Link MCP server no longer fails with an invalid redirect error. The Authenticate button fetches a fresh sign-in link when the cached one is missing.
- **Fixes to the agent chat transcript.** Chats no longer stay stuck on generating after a turn finishes, so queued messages send. Sharing a chat that is too large shows a clear error.
- **Fixes to the agent prompt input.** Focus returns to the prompt after you pick a model or close the model picker. Attaching HEIC and HEIF images works again, and autocomplete in the prompt no longer suggests files excluded by `.cursorignore`.
- **Performance fixes on Linux.** Cursor no longer pauses periodically while sampling CPU usage on machines with many cores, and bursts of internal messaging no longer exhaust a window's file descriptors.
- **Fixes to agent tools and hooks.** When the agent waits on a terminal command, it stops as soon as the command finishes or its output matches what it is waiting for, instead of always running out the full timeout. Agent directory listings honor `.cursorignore` patterns from parent folders when listing a subfolder. `beforeMCPExecution` hooks get the MCP server's command or URL instead of an empty value.
- **Fixes to editor menus and dialogs.** Quick Fix and refactor menus you open manually no longer go blank or fail to run when the lightbulb refreshes in the background. In the simple file picker, typing a folder path that ends with `/` opens that folder. Hidden dialogs no longer capture keyboard input, so typing and shortcuts keep working.
- **Fixes to skills and Agent Store links.** Skills in the Customize view no longer wait for team rules to finish loading before they appear. Clicking a built-in skill in a cloud agent chat opens its SKILL.md file instead of an empty tab, and clicking an Agent Store file citation in chat opens the latest version instead of a stale copy.
- **Fixes to plan recognition.** Pro Student subscribers are recognized as paid, so they get the correct model access and usage banners instead of Free plan limits.

## Week of Aug 31, 2026

### Web

- **Let specific people and apps bypass a ruleset.** In a repository's **Settings > Rules and Protections**, the ruleset dialog now has a **Bypass list**. You can add up to 15 people with repository access or installed apps, and set each one to **Always** or **Pull requests only**. Bypass actors can merge pull requests into refs that the ruleset would otherwise block, for example with a block-merges rule.
- **App creators can manage the apps they create.** When you create an Origin app, you're now made its admin, so you can view and update its settings, signing keys, and icon without being a namespace admin. Namespace and team admins can still manage the app, and permission checks for app settings now give the same answer as the actions themselves.
- **Clearer app permission updates.** When you update an installed app's permissions, the review page now lists new permissions, permissions that will be revoked, and a collapsible list of permissions you've already granted. Apps that request a write permission now also get the matching read permission, so they can read the data they're allowed to change.
- **Simpler app pages and clearer publisher details.** Creating an app no longer asks for a slug, and app pages under codebase settings now use the app's ID, so links stay stable. The app details page shows who created and last updated it. Clicking an installed app in a repository's Apps settings tab opens its installation details, and policy dialogs list app scopes in their own section.
- **Email notifications when your repository access changes.** Origin now emails you when you're granted or lose access to a repository or namespace, including changes that come through a group or team membership. You don't get an email for changes you made yourself, or for the temporary draft repositories created when you start a new project with an agent.
- **Clearer repository access controls.** The Add People button and dialog on the codebase and repository Permissions tabs are now called Grant Access, and people or groups who already have access show their current access level, including custom policies, instead of "Already added." Repository settings now describe Private visibility as "Only users with direct access and codebase admins."
- **Request reviews on personal repositories.** On repositories owned by a personal account, the pull request reviewer picker now lists the owner and people you've granted access to the repository, and you can request their review. Previously the picker showed no one for personal repositories.
- **Simpler commenting on your own pull requests, and replies held in your pending review.** On a pull request you authored, the review button now reads Comment and opens a comment-only composer, without approve or request-changes options. Replies to review threads now join your pending review and stay private until you submit it.
- **Readable author filters on the pull requests page.** When you pick an author from the filter dropdowns on a repository's pull requests page, the search box and URL now show the person's name, like `author:"Ada Lovelace"`, instead of an unreadable ID. Shared links that use names still resolve to the right people.
- **Audit logs now show who pushed to a repository.** Repository push entries in your team's audit log now record the pushing user's email instead of "unknown". Pushes made by an app or service account show that account instead. Review authors and CI check actors now appear as public IDs (`user_…`, `app_…`, `sa_…`) instead of older internal ID formats.
- **Fixes to merging and restacking pull requests.** Squash merges no longer land on the base branch while leaving the pull request open, and stack merges no longer fail with an orphan-commit error after the merge has landed. Merges and restacks no longer fail when the base branch moves at the same moment, and restacking works when a pull request's recorded base has drifted from its branch. Merges in repositories mirrored to GitHub no longer wait on the GitHub push.
- **Fixes to pull request pages.** Agent-generated images in code tours load correctly, and commits signed by Cursor Agent show the Cursor Agent name and avatar. Code tours on stacked PRs no longer show a stale tour after the base changes.
- **Fixes to clone, fetch, and push reliability.** Clones and fetches of large or mirrored repositories no longer fail with a 504 or drop while the server prepares the pack, and no longer briefly miss branches or tags during a repository restore. Pushes no longer print a spurious mirror warning when mirroring is disabled, and pull request diffs, mergeability checks, and blame no longer return server errors when repository metadata can't be read.

### API

- **Commit files and create branches through the Origin API.** You can now commit file changes directly to an existing branch and create new branches at a given commit using the Origin API, without a local clone. Commits can require the branch to still point at an expected commit, so concurrent writes don't overwrite each other. The Origin Go SDK supports both. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Apps are now identified by ID and display name across the Origin API, SDK, and webhooks.** App objects, app actors, and webhook app payloads, including the test ping, no longer include a `slug` field. Check run groups no longer return the deprecated `app_name`, so read `actor.display_name` instead. If your integration keys on the app slug, switch to the app `id`. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for the affected fields.
- **New webhook events and faster recovery from failed deliveries.** Apps can subscribe to a new `repository.metadata.updated` webhook, which fires when a repository's default branch changes and includes the full repository. Installed apps now also get an `installation.updated` event when a namespace is renamed, with the new namespace and repository coordinates. Failed deliveries are retried after 5 seconds first, so brief network blips recover sooner. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Filter pull request comments and comment on whole files from the API.** You can now list pull request comments within a creation-time window or only from specific threads, and open comment threads on an entire changed file instead of a single line, from the Origin API and Go SDK. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **More precise check-run and pull request lists in the Origin API.** You can now filter a commit's check runs by check name and status (queued, in progress, or completed), and check-run lists for a commit or suite now return only the latest attempt of each run instead of superseded retries. Filtering pull requests by author now also accepts a user's email address, matched case-insensitively. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **API responses and webhooks now say more about who did what.** User actors in Origin API responses and webhooks now include a display name and, for users with a public profile, their handle. App actors include the app's registered display name, and requested reviewers include their email. REST responses also return fields that hold default values, such as `draft: false`, instead of leaving them out. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for field details.
- **The Origin API spec now lists the credentials and scopes each endpoint needs.** Each operation in the Origin API's OpenAPI spec now says which credential types can call it (app, installation, or user) and which scopes it requires. Operations that need no extra scope, such as app and installation metadata and webhook deliveries, are marked as authentication-only. Duplicate operation IDs for the extra repository tarball and matching-refs routes are fixed, so client generators no longer fail on the spec. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).

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

## Week of Aug 31, 2026

### Reviews

- **Bugbot explains when a pull request is too large to review.** When a pull request changes more than 100,000 lines or 3 million characters, Bugbot skips the review and posts a comment saying the pull request is too large to review, suggesting you split it into smaller pull requests.
- **Bugbot keeps Security Reviewer reviews.** When Bugbot reruns on a pull request, it hides only its own earlier reviews. Reviews from Security Reviewer now stay visible.
- **Fewer failed reviews from brief network errors.** A brief network error while Bugbot rechecks the pull request just before posting no longer fails the run and restarts the review.

### Learned rules

- **Learned rules work on Origin repositories.** Bugbot now learns rules from merged pull requests on Origin repositories. Previously, learning failed on Origin pull requests.
- **Learned rules work for teams that restrict models.** If your admin model settings block Bugbot's default learning model, learning falls back to another allowed model. If every option is blocked, Bugbot skips the learning run instead of failing, and you aren't billed for it.

### Dashboard

- **Bugbot dashboard fixes.** Tables no longer make the whole page scroll sideways on narrow or mobile screens, and clicking a section header to copy its link only responds on the label itself.

## v2026.08.26

### Persistent sessions

- **Keep agents running after you disconnect.** Start a persistent session with `agent persist`, detach with `/detach`, and reconnect later with `agent persist attach`. Use `agent persist list|stop` to manage sessions or `agent persist --resume` to continue an existing chat.

### Self-hosted workers

- **Viewers watch the agent's live desktop.** Workers started with `--computer-use --share-desktop` now share the managed desktop the agent uses instead of a separate session. Cursor clears stale worker-owned displays so later sessions start clean.
- **Wake hibernated workers for follow-ups.** `agent worker controller` can wake a claimed, hibernated worker through the `--spawn` hook, so a follow-up returns to the same workspace during the reconnect window. Its queue watch now uses server-sent events to reduce polling and handle rate limits.
- **Computer use works on macOS workers.** Start a worker on a Mac with `agent worker --computer-use start`, and Cloud Agents can click, type, and take screenshots on its signed-in desktop. The first start installs the Cursor Computer Use helper app, and `agent worker debug` confirms it's there. Grant the helper Accessibility and Screen Recording as described in [macOS setup](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md#macos).

### Enterprise and team controls

- &#x20;**Team model restrictions apply in the CLI.** When an admin limits your team's models, for example to Auto only, `agent models` and the `/model` picker show only the models you can use. Passing a blocked model to `--model` exits with the restriction message, and a saved model outside the list switches to an allowed one. Admins set this up in [model access control](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control).

### Fixes

- **Fixed warm pools that stopped spawning idle workers.** A [warm pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#warm-pool) controller (`agent worker controller --warm-idle <count>`) failed to read the pool list when Cursor's API returned fields it didn't know. It now ignores those fields and keeps spawning idle workers.

## 1.0.30

- **Long-running local agents keep their credentials fresh.** Local runs in TypeScript and Python refresh the short-lived access token before it expires, so agents that run for more than an hour no longer fail with authentication errors. Cloud runs are unaffected.

## 1.0.29

- **Output schemas on custom tools.** `outputSchema` in TypeScript and `output_schema` in Python declare a JSON Schema for a custom tool's structured result, advertised to the model as the tool's MCP output schema. Results are not validated against it. Local agents only.

## 1.0.28

- **Ship the SDK as a single file.** Under Bun, `@cursor/sdk` now resolves to a flat single-file bundle, so `bun build --compile` works with no import change and no more `Cannot find module './986.js'`. `@cursor/sdk/bundled` and `@cursor/sdk/bundled/sqlite` expose the same build as explicit entries for other single-file bundlers such as esbuild. TypeScript only.

## v2026.08.11

### Steering and subagents

- **Steer a running turn, then interrupt.** Pressing Enter while the agent works now sends your queued message into the active run at a safe boundary to steer it, and only interrupts the turn if you press Enter again.
- **Single-turn runs wait for their subagents.** Headless and single-turn runs drain delegated subagents and include their completion before exiting, instead of cutting off while background shells or dev servers are still running.
- **Read the full subagent transcript.** Drilling into a subagent shows its complete, ordered transcript, including the prompt, thinking, tool calls, and final response, instead of only tool rows.
- **Choose the Explore subagent's model.** Set the Explore subagent to the default, disabled, inherit the parent model, or a specific model from `/config`.
- **Background task follow-ups are back.** Completion follow-ups for finished background tasks fire again in interactive and headless sessions.

### Skills, custom modes, and goals

- **Sticky skills and custom modes.** A skill slash entry attaches once when you press Enter, and Option+Enter invokes a mode-backed skill as a sticky custom mode that stays active until you exit it.
- **Managed skills can ship Markdown resources.** Managed-skill sync now materializes a skill's nested Markdown files under `~/.cursor/skills-cursor`, so skills that reference extra resources work.
- **Skill discovery skips hidden directories.** Skill and subagent scans no longer descend into hidden dot-directories, avoiding slow loads from large nested folders.
- **Durable goals.** `/goal` tracks a durable goal with an active or paused status line, continues the goal across idle and headless runs, and pauses it on Ctrl+C. This is rolling out and gated.

### Models

- **Auto stays pinned in the picker.** Auto is pinned to the top of the `/model` list, matching the IDE.
- **Editing a model's parameters selects it.** Adjusting parameters in `/model` now selects that model, so pressing Esc leaves your updated choice active.
- **Headless keeps Max-mode variants.** A headless `--model` selection that requires Max Mode now sends it, so max-context variants are no longer clamped down.

### MCP and plugins

- **Simpler MCP login for known hosts.** Logging into servers like Slack from the `/mcp` pager uses default authentication, avoiding dynamic-client-registration failures.
- **Plugin hooks run from installed plugins.** Hooks defined by installed plugins, including those loaded with `--plugin-dir`, now execute and refresh when plugins reload.
- **Secrets stay masked in plugin config.** Plugin configuration forms mask credential-named and secret-typed fields like tokens, API keys, and passwords.

### Terminal and rendering

- **Inline image previews.** Attached and generated images render inline in terminals that support it, with text fallbacks everywhere else.
- **LaTeX math renders as Unicode.** Math in Markdown renders as terminal-friendly Unicode instead of raw TeX.
- **Cleaner shell output and transcripts.** Long shell output no longer has zero-width spaces injected into it, so copied paths and tokens stay intact; the working-directory note is hidden when a command runs in the current directory; hidden tool-call groups no longer leave blank lines; and queued "+N more pending" approval previews stack without gaps.
- **Responsive `@` file palette.** Typing stays responsive in large repositories while the `@` palette computes file suggestions.
- **Steadier custom status line.** A custom `statusLine` command keeps its throttle during streaming updates and restarts only when the command or working directory changes.

### Approvals and security

- **Timed mode-switch approvals.** Approving a mode switch now uses the pager UI with a 15-second countdown and auto-rejects when left unattended, matching the IDE.
- **Hardened git commands.** Repository-controlled git configuration, including fsmonitor, hooks, attributes, and external diff programs, no longer runs during the agent's own git operations.
- **Sandbox read access and git over SSH.** Sandbox policy gains a read-access boundary, and sandboxed git-over-SSH on macOS and Linux routes through the SOCKS proxy so allowlisted remotes work and denied ones fail with a clear error.
- **Sudo uses your latest input.** Submitting a sudo password now sends exactly what you typed rather than a stale rendered value.

### Reliability and startup

- **Faster startup.** Syntax-highlighting grammars and the background-composer client load lazily off the boot path, and a slow plugin list falls back to a plugin-less session instead of stalling startup.
- **Long headless sessions no longer hang.** Wedged uploads on long-running headless HTTP/1.1 sessions are detected and retried instead of silently stalling.
- **Faster resume on network filesystems.** The resume picker scans sessions in parallel and keeps your newest chat selected while the full cross-workspace list loads.

### Self-hosted workers

- **More control over self-hosted workers.** Workers can join a named pool with `agent worker --pool <name>`, default to releasing after an hour idle (`--idle-release-timeout 0` keeps them running), start from a non-git directory with `--worker-dir`, take a data-directory lock to prevent duplicate daemons, and run session-start and session-end hooks on claim and release.

### Enterprise and install

- &#x20;**Admin command denylist enforced in the CLI.** A team admin's command denylist is enforced in local shell execution and refreshed per request, with a killswitch. Admin-controlled.
- &#x20;**MDM sign-in policy.** CLI login sends and enforces MDM sign-in policy, including organization, team, email, and domain allowlists, and reports enforcement denials. Admin-controlled.
- **Windows uninstall can remove your data.** The Windows uninstaller can optionally delete Cursor user data, including the `~/.cursor` folder that stores CLI credentials.
- **Resilient install script.** The install script falls back to wget or python3 when curl is broken.

## 1.0.27

- **Restrict the agent's toolset.** `tools` allowlists the built-in tools offered to the model (`[]` means text-only), and `disallowedTools` removes tools while keeping the rest. Both take public names like `"read"` or capability groups like `"shell"` and `"mcp"`, in TypeScript and Python (`tools`, `disallowed_tools`). Local agents only for now, and not persisted across `resume`.
- **Log in from the browser in TypeScript.** `Cursor.auth.login()` opens a browser login, mints an API key, and stores it in `~/.cursor/sdk/auth.json`; `Cursor.auth.status()` and `Cursor.auth.logout()` round it out. After login, `Agent.create()` and the `Cursor.*` reads work without `apiKey` or `CURSOR_API_KEY`.
- **Usage and cost for local agents.** `agent.getUsage()` in TypeScript and `agent.get_usage()` in Python now work for local agents too, returning a per-turn breakdown. Pass a `runId` from a previous result to narrow to one turn.
- **Open PRs as the Cursor GitHub App.** `cloud.openAsCursorGithubApp` in TypeScript and `open_as_cursor_github_app` in Python control PR authorship. Service-account keys default to the app; user keys default to the key's owner.
- **Multi-root local workspaces.** Pass `local.dirs` to load rules, skills, and project context from several folders; `cwd` stays the single primary working directory. Replaces the `cwd` array form, which only ever used the first entry.
- **Clearer Python errors.** Failures that previously surfaced as a bare "internal error" now carry the underlying message and code.
- &#x20;**Admin command denylists apply to local runs.** Shell commands matching your team's admin denylist are rejected with a policy message before they execute, including on paths that skip approval prompts.

## 1.0.26

- **Warm up a local workspace before the first send.** `platform.prewarmLocalWorkspace(options)` resolves rules, skills, MCP servers, and ignore files ahead of time, so the first `send()` against that workspace starts immediately. It returns a release function to call on shutdown.
- **Control how long workspace scans stay cached.** `configureCursorSdk({ local: { workspaceScanCacheTtlMs } })` sets the cache lifetime for workspace scans, and the `CURSOR_RIPWALK_CACHE_TTL_MS` environment variable sets the same value for hosted deployments. Long-lived servers on stable checkouts can now skip repeated re-scans.
- **Custom tools run without approval prompts.** Host-defined tools passed via `customTools` no longer fail with an interactive-approval error on sandboxed or auto-review local runs. Deny rules and sandbox limits still apply.
- **Signed macOS binaries.** The `@cursor/sdk` macOS platform packages now ship code-signed binaries, so Gatekeeper and endpoint security tools no longer block them.
- **Cleaner Python exception hierarchy.** `PermissionDeniedError`, `BadRequestError`, and `InternalServerError` now inherit directly from `CursorSDKError` instead of `AuthenticationError`, `ConfigurationError`, and `NetworkError`, so `except` blocks catch what their names say.
- **Fixed intermittent startup failures in Python.** Roughly 1 in 64 agent launches failed before reaching the first send. Launches are now reliable.

## 1.0.25

- **Billed usage and cost on demand.** `agent.getUsage()` in TypeScript and `agent.get_usage()` in Python return token usage, billed cost, and a per-run breakdown for cloud agents, and `Agent.getUsage(agentId)` works without a handle. Cost is server-derived, includes discounts, and settles shortly after a run ends. Cloud-only for now; local runs throw a typed configuration error.

## v2026.07.20

- **`--trust` works in interactive sessions.** Previously `--trust` required headless mode. Passing it in an interactive session now trusts the workspace up front and skips the trust dialog, recording the same saved trust decision the dialog writes when you accept.
- **Clear errors instead of hangs at login.** MCP OAuth login fails fast with an actionable message when the callback port is already taken, instead of hanging on "Listening for the OAuth callback". On macOS, keychain failures at startup now explain the cause and the fix, like unlocking a locked keychain or logging out and back in, instead of a raw exit code.
- **The model catalog stays fresh in long sessions.** The CLI refetches the model catalog every 10 minutes in the background, so newly released models appear in `/model` and shortcuts without restarting. If a refresh fails, the CLI keeps the current catalog and retries on the next interval.
- **Cleaner rendering.** Completed tool rows no longer disappear for a frame when the agent moves to its next step, markdown tables with emoji or CJK text keep their columns aligned, typing a path like `/tmp` followed by a space no longer leaves the slash palette stuck on "No matches", and subagent rows drop the Ctrl+O expand hint (the shortcut still works).
- **Fixed CPU spinning from the branch watcher.** When the watcher that keeps the prompt footer's git branch current could not attach, most commonly after exhausting the inotify watch limit on Linux, it retried in a tight loop that pegged a CPU core. Failed attaches now back off exponentially, and branch switches still update the footer immediately.

## v2026.07.13

### Plugins and MCP

- **Manage plugin marketplaces from the shell.** Script marketplace management without an interactive session: `agent plugin marketplace add <git-url>` registers a marketplace (pin a branch, tag, or commit with `--git-ref`), `list` prints each marketplace's name, scope, and git URL (`--format json` for scripts), `update` re-indexes one from its repository, and `remove` deletes a user-scoped marketplace.
- **One server for duplicate MCP configs.** When the same remote MCP server is configured in more than one scope, such as your user `mcp.json` and a project's `.cursor/mcp.json`, the CLI now runs a single instance instead of duplicates. Pick which scope's configuration wins from the new Configure Scope tab in a server's `/mcp` detail view. The choice is saved per project.

### Usage and models

- **See plan usage and spend in `/usage`.** `/usage` now shows your account's included-usage meters with Auto and API breakdowns, on-demand spend against your limit, plan name, and billing-cycle reset date. Enterprise pooled plans get a spend chart for the current billing cycle compared with the previous period of the same length, plus a link to the usage dashboard.
- **Fixed Max Mode sticking on.** Choosing a variant that requires Max Mode, like `/fast` or a 1M-context option, no longer leaves Max Mode silently enabled for other models and future sessions: it clears when your selection stops requiring it, while an explicit `/max-mode` choice stays sticky. The MAX indicator is also back in the prompt bar, after the model's parameter summary.
- **Fixed the empty `/model` picker on slow connections.** If the model catalog fetch timed out at startup, `/model` stayed empty for the whole session. Opening the picker now refetches the catalog, and an open picker fills in as soon as the list arrives.

### Approvals and trust

- **Auto-accept web searches.** A new Auto-Accept Web Search permission lets the agent run web searches without pausing for approval each time. It is off by default. Toggle it under Permissions in `/config` or set `autoAcceptWebSearch` in `cli-config.json`. Honored in interactive, headless, subagent, and Agent Client Protocol runs.
- **Steer the agent from shell approval prompts.** The skip option on shell approvals is now labeled "Skip & tell the agent what to do instead", and choosing it opens a composer whose message is sent to the agent as the reason the command was skipped. Submitting an empty message just skips.
- **Worktree setup respects workspace trust.** Setup commands from `.cursor/worktrees.json` now run only after the workspace is trusted, through the trust prompt, a saved trust decision, or `--trust` in headless runs. Untrusted workspaces skip setup with a visible notice.

### Reliability

- **Resuming chats is faster.** The resume picker shows your current workspace's chats immediately and fills in other workspaces in the background, and selecting a chat no longer waits on a model-catalog fetch when your stored model is already cached.
- **Network blips no longer kill runs.** DNS failures and network-unreachable errors, like those during a VPN transition, retry with backoff like other transport errors. If the network stays down, the CLI shows an actionable hint covering network, VPN, DNS, and proxy configuration instead of a raw network error.
- **Subagents survive transient failures.** A momentary network error no longer kills a running subagent with a terminal error. Subagent turns retry with the same policy as regular turns, resuming from their last checkpoint when one exists.
- **Updates no longer break running sessions.** Auto-update cleanup could delete the installed version a long-running session was launched from, crashing it mid-turn. Running processes now mark their install directory as in use so cleanup skips it, and if install files still disappear, such as after a Homebrew upgrade, the CLI asks you to restart instead of failing with a module error.
- **`/btw` fixes.** Side questions no longer fail with an internal blob error in long or compacted sessions, and the slash palette no longer pops up over your question while you type it.

## v2026.07.06

### Models and skills

- **New installs start on Auto.** Fresh CLI installs default to Auto model routing. Existing choices are unchanged; switch anytime with `/model` or `--model`.
- **Switch models instantly from slash commands.** Type a shortcut like `/opus` or `/composer` to jump straight to a model, no picker needed; each family shortcut remembers your last choice. `/fast` toggles Fast when the current model supports it. Disable shortcuts under Model slash commands in `/config`.
- **Keep model-only skills out of slash commands.** Set `user-invocable: false` in a skill's `SKILL.md` frontmatter to hide it from `/` autocomplete and typed `/skill-name` resolution while keeping it available to the model.

### Reliability

- **Fixed memory growth from per-turn cancellation state.** Long chats no longer accumulate abort listeners and controllers; each turn releases them when it finishes.
- **Quitting returns you to the shell promptly.** Exit no longer waits on MCP servers or other background tasks to wind down, and quitting from the workspace-trust prompt no longer flashes "Trusting workspace…".
- **Fixed config corruption when running several agents at once.** Concurrent CLI processes could interleave writes to `cli-config.json` and block later startups. Each write now stages to its own temp file before an atomic rename.

### Sessions and subagents

- **Resume chats from any directory.** `agent ls`, `agent --resume`, and `/resume` open All chats across workspaces by default. Use Left/Right to switch to This workspace; chats from other directories show a folder label, and resuming one loads the full conversation instead of an empty one.
- **Subagents keep their context across resumes.** Completed subagents persist checkpoints, so resuming one restores its prior context instead of starting empty. Background subagents include their final message in the completion notification, and resuming an unavailable subagent fails clearly.

### Login and MCP

- **Log in from another device with a QR code.** During `agent login` or first-run onboarding, press `q` to reveal a QR code for the same login URL, then scan it from a phone to finish authentication over SSH without copying a long link. Narrow terminals and non-interactive sessions continue to show the URL only.
- **Filter MCP servers and see login start immediately.** Type to filter the `/mcp` server list. Selecting Login shows "Preparing login…" right away, and SSH OAuth instructions no longer use `ssh -N`, which failed through some proxies.
- &#x20;**Fixed MCP allowlist and approval bugs.** Team network allowlists now accept HTTP(S) origins with explicit ports, such as local servers on non-default ports. Personal MCP tool approvals work again when team admin tool controls are empty or unset.

### Input and terminal

- **Long prompts stay within six visual lines.** The prompt bar and queued-message editor scroll to keep the cursor visible instead of growing without bound. Large pastes stay collapsed as a pill when recalled from history while the agent receives their full content, and Working appears immediately after you submit.
- **Fixed terminal state after Ctrl+Z.** Suspending the CLI restores your shell's keyboard modes until you `fg`. Backspace no longer swallows the letters typed right after it when the interface briefly stalls, and typing stays responsive while the agent streams output.
- **Fixed queued sudo prompts.** Each sudo request opens a fresh password prompt instead of sticking on "Authenticating…". Escape and Ctrl+C cancel during submission, and the mask uses `•` instead of `*` to avoid misalignment with terminal font ligatures.
- **Debug mode cards use debug mode colors.** The reproduction-steps decision card uses the red debug accent instead of plan-mode yellow, so the active mode stays clear.

## v2026.06.29

### Workspaces and commands

- **Start multi-root sessions from the command line.** Repeat `--add-dir <path>` to add directories at launch, including with `--workspace`. `/add-dir` refreshes slash skills and custom commands immediately; restart only when you want the agent to discover new skills automatically.
- **Plugin reloads refresh commands.** Reloading a plugin refreshes its slash commands and palette. Long skill and custom-command names resolve correctly, and `/add-dir` keeps directory completion open while you browse.
- **Queued follow-ups send on the second Enter.** Press Enter again on an empty prompt to stop the current turn and send your queued message immediately, including while a `beforeSubmitPrompt` hook is running.
- **Fixed input lag during agent runs.** Typing and queuing follow-ups no longer rerender the full transcript on every keystroke while output streams.
- **Fixed model options resetting.** Changing Fast, reasoning effort, or context in `/model` preserves your other compatible choices and keeps Max Mode in sync.

### Cloud and Auto-review

- **Cloud transfers preserve model and workspace context.** For Git repositories with Cloud Agents access, transfers preserve the selected model and workspace path. The prompt shows transfer status, `Esc` or `Ctrl-C` cancels, and failure details remain visible.
- **Auto-review considers invoked instructions.** Admins can control availability. When Auto-review is enabled for your account and selected model, the classifier can inspect invoked skill and file-backed custom-command files before deciding whether a tool call needs approval. Existing hard approval boundaries are unchanged.

### Authentication and MCP

- **Run Cursor in sandboxes without macOS Keychain.** Set `AGENT_CLI_CREDENTIAL_STORE=file` to store credentials unencrypted in an owner-only file. Use private storage that persists across runs; packaged Unix builds also skip system CA loading in this mode.
- **Fixed false MCP connection errors.** Working servers no longer appear disconnected in `/mcp` and `agent mcp list` when their tools or instructions are available.

### Reliability and updates

- **Windows updates suppress PowerShell progress output.** Native updates no longer draw PowerShell's progress bar over the CLI or incur its download overhead.
- **Fixed memory growth in long CLI sessions.** The CLI now saves only new transcript entries at each checkpoint instead of reloading and rewriting the full conversation.

## v2026.06.22

### Auto-review

- **Auto-review run mode.** Cursor's Auto-review run mode comes to the CLI: a middle ground between Allowlist and Run Everything that keeps the agent moving with fewer approval prompts. Shell, MCP, and Fetch calls are checked in order: allowlisted calls run immediately, calls that can be sandboxed run in the sandbox, and the rest go to a classifier that allows the call, tries a different approach, or asks you to approve. Turn it on with `--auto-review`, in `/config`, or with `/auto-review`, and steer the classifier with `allow`/`block` instructions in `permissions.json`.

### Workspaces

- **Named multi-directory workspaces.** Run the agent across several repositories at once: add directories mid-session with `/add-dir`, save the set with `/save-workspace`, reload it later with `/load-workspace`, or start scoped with `--workspace`.

### Commands

- **`/rewind` is on by default.** The turn-by-turn undo timeline no longer needs turning on in `/config`.
- **`/vim` anywhere in the prompt.** Trigger inline Vim editing from any position, not just an empty prompt.
- **Richer `/copy`.** Pick a single step of a multi-step reply from a per-step picker, copy the agent's responses alongside your own messages, and copy long replies without the terminal stalling.
- **`/logs` on shared machines.** Debug logs are written per user so multi-user hosts don't hit permission errors, and the `/logs` path lingers on screen longer.

### Terminal experience

- **Prompt history is per conversation.** Up-arrow recalls what you typed in this session instead of a single history shared across every chat.
- **The jobs list shows everything running.** Foreground shells and subagents appear in the jobs pager alongside background tasks.
- **Steadier rendering.** Mermaid diagrams stay drawn after a turn finishes, long shell-output previews clip instead of wrapping, and the screen clears once per resize instead of twice.
- **Your draft survives the resume picker.** Cancelling `/resume` keeps what you had already typed.
- **Plan editing.** Esc returns to Vim normal mode while you revise a plan.

### Reliability

- **Lower memory in long sessions.** Fixed a leak where per-turn abort signals held on to conversation state.
- **No crash on missing approval state.** Sessions tolerate credential stores that haven't recorded an approval mode yet.

### MCP and skills

- **Editor-provided MCP servers are trusted.** MCP servers passed in over the Agent Client Protocol (Zed and other editors) load instead of being silently dropped.
- **MCP tools survive a plugin reload.** The MCP lease refreshes after a plugin reloads, so its tools no longer wedge with "Not connected" errors.
- **Skills found through symlinks.** The skills menu follows symlinked directories when discovering skills.

### Install and updates

- **Reliable channel switching.** Switching release channels applies on the first try and immediately fetches the target channel's build.
- **Windows and shim fixes.** The Windows launcher matches timestamped version directories, and the `cursor` shim no longer errors on shells that treat unset variables as failures.

### Enterprise and team controls

- &#x20;**Team gating for Auto-review.** Admins control whether Auto-review is available to their members.
- **Stable self-hosted worker identity.** `worker start` waits for the bridge to connect before reporting ready, and workers keep a stable logical ID scoped per authenticated user, so fleets on shared machines match the right worker to the right person.
