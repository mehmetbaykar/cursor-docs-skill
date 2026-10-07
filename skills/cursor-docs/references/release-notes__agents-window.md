---
title: "Agents Window release notes"
source: https://cursor.com/docs/release-notes/agents-window
path: /docs/release-notes/agents-window
---

# Agents Window release notes

New features, improvements, and fixes in the [Agents Window](https://cursor.com/docs/agent/agents-window.md). The Agents Window ships with the Cursor app, so each entry covers one minor version, including the patch releases that follow it. Editor changes are in the [Cursor IDE release notes](https://cursor.com/docs/release-notes/ide.md).

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
- **Cloud Agent links open the right agent.** "Open in Cursor" links for Cloud Agents from cursor.com/agents, Slack, Linear, Teams, or Copy Deep Link now open that agent in the Agents Window, even if you haven't opened it before, and even when the IDE has focus. Previously the link could drop you on a new chat. If the agent can't be found or you don't have access, you now see an error.
- **Side chats now work on cloud agents.** You can open a [side chat](https://cursor.com/docs/agent/overview.md#side-chats) from a cloud agent with `/side`, the + menu, or by selecting text and choosing Add to Side Chat, the same way as on local agents. The side chat runs as its own cloud agent, so you can ask a question without interrupting the main run. Side chats aren't offered inside Projects, which use threads instead.

### Projects and workspaces

- **Edit Workspace keeps your chats when you rename a project.** Renaming a multi-root project in Edit Workspace now moves its local chats and drafts to the renamed project instead of leaving them behind. You can also remove folders until only one remains.

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
- **Clearer explanation of a fixed on-demand limit.** With a personal fixed on-demand limit, Settings > Plan & Usage now explains that requests stop at the limit and that overage from requests already running isn't billed unless you raise the limit that billing cycle. It previously said usage past your limit would be billed later. Team-managed limits keep their existing wording.

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
- **Fixes to voice chat.** An earlier spoken request that got no reply no longer stays open for the rest of the call once a later request finishes. When the agent is waiting on you, the voice explains once that it can't take a new request instead of repeating itself. Hiding the chat no longer hides the floating call controls, so Hang up stays on screen.
- **Fixes to agent questions and tool calls.** Questions and plan approvals the agent asks after a dropped connection are no longer answered with an earlier reply. Built-in tool calls with slightly malformed arguments now run instead of failing, and a native code chunker that fails to load now only disables semantic search. The transcript also holds its position when you scroll past the bottom while new output streams in.
- **Fixes to stability and local storage.** Switching between Private Inference and Cursor-managed models now stays switched after the restart that applies it. Opening the Agents Window while a previous instance is still closing no longer discards local state, and repeated out-of-memory crashes no longer fill the debugging-data folder with gigabytes of files. Okta FastPass sign-in works in the built-in browser again.
- **Fixes to the Agents Window.** Pull request status for agents keeps showing the last known state when GitHub rate limits requests, instead of failing to load. The pinned Build card no longer shows content through it under translucent custom themes. Closing Settings returns straight to the same conversation with its transcript and composer intact.

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
