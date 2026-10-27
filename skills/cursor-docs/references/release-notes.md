---
title: "Release notes"
source: https://cursor.com/docs/release-notes
path: /docs/release-notes
---

# Release notes

Every Cursor product in one timeline, newest first, with up to 10 recent releases each. Filter by product, open a product's page for its full history, or follow along with the [RSS feed](https://cursor.com/docs/release-notes/rss.xml).

## 3.27

### Projects

- **Project split panes keep your focus and come back after a reload.** In a [Project](https://cursor.com/docs/agent/projects.md)'s split panes, the pane you focused stays focused when panes return or the window reloads, and the editor panel follows whichever pane you focus, including chats dropped in from outside the Project. A chat you opened in another Project's split reopens in that split after a reload or Back/Forward, and the Project's own chat tab stays pinned first in its tab strip.
- **Calmer start for new Projects.** While a new [Project](https://cursor.com/docs/agent/projects.md) sets up, its conversation now shows a single "Setting up project" row until the agent's first output, instead of reflowing through environment setup steps. A new Project starts with its apps panel closed, and the Project app opens on its own once the first task appears.
- **Track a Project's tasks in List and Board views.** Starting in 3.26, a [Project](https://cursor.com/docs/agent/projects.md)'s notes are a task tracker that the coordinator keeps up to date, with each task's status, ID, agents, and pull requests, shown as a List or a Board. The Project tab stays pinned first in the right panel, and its header switches between List, Board, and Library. While the Project's files sync, the tab shows a loading state, or an error if sync fails, instead of looking empty.
- **Filter tasks in Project notes.** In a [Project](https://cursor.com/docs/agent/projects.md)'s Notes tab, a Filter button next to find narrows the task List or Board by Status, PR, Tags, or Owner. Active filters show as chips you can edit, switch between "is" and "is not", remove, or clear, and typing in the find bar filters tasks by text too.
- **Tasks with several PRs stay readable in Project notes.** In a [Project](https://cursor.com/docs/agent/projects.md)'s task List, a task whose PR chips would crowd its title shows a single "N PRs" pill with an icon for each PR's state. Click the pill to open a menu of that task's pull requests.
- **Find repositories, folders, and environments faster in the project picker.** The project picker opens on a search field, with your repositories, folders, and cloud environments in one list and owners shown on search results. Paste a clone URL to clone it from the picker, or use the footer to clone a repository, start from scratch, or create a new repository.
- **No more accidentally stopping a Project's coordinator.** While a [Project](https://cursor.com/docs/agent/projects.md)'s coordinator is working, its chat input keeps the Send button instead of swapping it for Stop, so you can keep sending messages without cutting off a long-running coordinator by mistake.
- **Project workers stay on their assigned task.** When a [Project](https://cursor.com/docs/agent/projects.md) worker runs a plan handed down from its coordinator, it works on its own task instead of acting like the Project's coordinator.

### Chat and composer

- **Project messages collapse into one line in the chat.** When a [Project](https://cursor.com/docs/agent/projects.md) sends messages to an agent, they now collapse into one centered line, such as "Messages from Hare, Tortoise", instead of filling the conversation. Click an agent's name to open the Project's chat at that message, or expand an "Update from" entry to read the update.
- **Fixes to prompt attachments.** Attached images and videos in sent messages are labeled with their file name, and images with very long file names attach instead of failing to save. Adding a HEIC or HEIF image on Windows or Linux now explains that those images need macOS, and slow HEIC conversions get more time and a clear timeout message. Pasted documents with no local file attach to cloud agent prompts, and videos or documents that can't be attached show a warning instead of disappearing.
- **More reliable queued messages and action buttons.** Action buttons that send a message, such as git actions, now follow your queue or steer behavior and keep your typed draft and attached context. Send Now on a queued message you just edited sends your saved edit from any composer, and shows an error instead of sending stale text if the save fails. Delivered messages from other agents no longer linger in the queue.
- **New chats no longer pick up a Project's environment.** Starting a new agent while a [Project](https://cursor.com/docs/agent/projects.md) chat is selected no longer runs the new chat in that Project's environment. With the new-agent default set to Last Used, New Chat uses the environment of the last chat you used outside a Project, including when a Project worker was opened before its Project finished loading.
- **Chat bubbles grow with your chat width.** Your messages and the agent's replies are no longer held to a fixed maximum width, so widening the Chat Width setting gives bubbles more room for long text, tables, and code.

### Navigation and layout

- **Tabs keep your place across agent switches and restarts.** Tabs in the Agents Window now return to where you left them after you hide the panel, switch agents, or restart. Files reopen at the same PDF page and zoom, image zoom and pan, CSV scroll, and code scroll and cursor; the Changes tab keeps its scope, branch, and picked commits; canvases keep their Rendered or Source view; and expanded folders, open find bars, and agent-opened tabs like Agent Changes and Desktop come back too.
- **The sidebar remembers which sections you collapsed or expanded.** Collapsing the Pinned section or the Repositories, Workspaces, or Chats header now sticks across reloads and restarts, and sections you expanded with More keep showing the same number of rows. A repository or workspace section you expand stays open after a reload, even if its agents are idle, until one of them has new activity. Starting a new chat also unfolds a collapsed Repositories or Workspaces header so the chat is visible.
- **Edit > Undo and Redo now act on what you were working in.** Undo and Redo from the menu bar apply to the prompt, editor, terminal, or browser that had focus before you opened the menu. They undo window actions like archiving an agent only when nothing editable has focus, so typing in the prompt and then archiving from the sidebar no longer sends Undo to the prompt.

### Files, changes, and pull requests

- **Clearer merge actions on pull request tabs.** The merge button on a pull request tab now shows how many pull requests the merge will land, and hovering Remove from Queue shows the pull request's position in the merge queue. Pull request links in chat show a status icon right away, and the header no longer shifts when live changes replace the cached diff.
- **See how stacked pull requests build on each other in the PRs tray.** The PRs tray in a [Project](https://cursor.com/docs/agent/projects.md) groups stacked pull requests on a rail, so you can see how each PR builds on the one below it. Forked stacks branch off the parent line, and the tray's stack view matches the stack navigator in the PR tab.

### Customization and settings

- **Hide the unread count next to the menu bar icon.** On macOS, the menu bar menu has a new Show Count option. Turn it off to keep the menu bar icon without the unread agent number beside it. It's on by default and persists across restarts.

### Browser

- **Preview pages on iPhone Duo and rotate any device in the browser.** The browser's responsive design mode adds iPhone Duo (Closed) and iPhone Duo (Open) device presets. Rotate works for every preset, including Laptop and Desktop, and the rotation carries over when you switch devices.

### Fixes

- **Fixes to sidebar keyboard navigation.** Arrow keys, Home, and End now move through every reachable row and button in the sidebar, skip hidden groups and hover-only buttons, and no longer open a preview card on each row. Keyboard focus stays in place when you pin, unpin, move, archive, or collapse agents, or press More. Screen readers also stop announcing repository headers as keyboard-reorderable.
- **Fixes to loading agents and Project workers.** Opening a finished cloud subagent from a link or by id no longer fails because it was unloaded first. Agents hidden from the sidebar now load their tiles instead of waiting indefinitely, and a Project no longer shows as running because of workers that already finished.
- **Fixes to transcript and prompt styling.** Steer messages and Send now interrupts no longer appear grayed out while they wait for the agent to pick them up. Time markers in the transcript now show as a label between two lines, lined up with message bubbles.
- **Fixes to voice calls.** Voice calls in the Agents Window no longer error out when the agent you're talking to is closed, unloaded, or hasn't loaded its conversation yet.
- **Fixes to agent reliability.** On Windows, hooks now get clean UTF-8 payloads, and screen readers announce the Restore Checkpoint control in chat.
- **Fixes to Projects.** Opening a newly created [Project](https://cursor.com/docs/agent/projects.md) no longer briefly fails to load its tasks and files, and Project tabs you return to restore their layout and scroll position. A Project split showing a chat from outside the Project no longer collapses when another view briefly takes the panel, and long task lists in hidden tabs no longer crash. The coordinator keeps its instructions on turns started by notifications, and unpublished draft repositories no longer appear in the cloud repository picker's Recents.
- **Fixes to browser Annotate mode.** Pressing Cmd/Ctrl+L while editing page text in Annotate mode adds the edit to the chat input instead of queueing it. Picked elements show as inline mentions in notes again.
- **Fixes to subagent rows.** Subagent rows in an agent's conversation no longer turn into empty rows of another tool when a late update arrives for the same call.

## 3.27

### Editor and app

- **Reduce Motion now covers Cursor's own UI, and drop overlays snap into place.** With `workbench.reduceMotion` on, Cursor's spinners, loading bars, menus, and dialogs pulse or fade instead of spinning or scaling, even when your OS preference is off. When you drag an editor or terminal to split it, the drop overlay snaps straight to each target instead of sliding.
- **Expand, zoom, and copy Mermaid diagrams in markdown preview.** Mermaid diagrams in markdown preview now have the same controls as diagrams in chat. Open one in a larger view to zoom around it, or copy its source.
- **Cursor opens its first window faster.** Cursor now waits until the first window is open before it loads error reporting, so that work no longer delays a cold start.

### Agent and chat

- **Agent no longer garbles non-UTF-8 and non-ASCII text.** Agent terminal output no longer garbles non-ASCII characters split across output chunks, and file reads and edits keep the original bytes when a file has some invalid characters. Codebase indexing now reads Latin-1, Windows code page, and legacy CJK files as text, so semantic search finds matches in them.
- **Hooks can tell which agent spawned a subagent.** [Hook](https://cursor.com/docs/hooks.md) scripts now receive `parent_agent_id`, the conversation ID of the agent that spawned the subagent, on `subagentStart` and `subagentStop`, so scripts no longer have to rebuild the agent tree from earlier events.

### Fixes

- **Fixes to agent links and tool rows in chat.** Links to cloud agents in chat now show the agent's name as soon as its details load, instead of waiting on an unrelated update. When an agent that manages other agents changes their tags, the chat now shows a clear "Updating tags" or "Updated tags" row.
- **Fixes to MCP.** When an [MCP server](https://cursor.com/docs/mcp.md) asks for input, the form in the agent chat now scrolls so its Submit and Cancel buttons sit above the prompt box, and the buttons are reliably clickable. MCP sign-ins whose OAuth refresh token has expired now ask you to reconnect instead of failing over and over.
- **Clearer Add to Chat button in Review Changes.** The Add to Chat button in the Review Changes file list now uses a chat bubble with a plus icon.

## v2026.10.22

### Cloud Agent environments

- **Update an existing environment with `agent env deploy --env`.** Pass `--env <id>`, using the public ID that `agent env list` shows, to redeploy an environment file onto an existing Cloud Agent environment. The environment keeps its name and repositories, so `--repo` becomes optional. If `--name`, `--repo`, or `--scm-repo-node-id` don't match the stored environment, the command stops with an error that explains the mismatch.

### Self-hosted workers

- **Self-hosted workers run under the team you selected.** `agent worker start` and `agent worker debug` now register and check the worker under the team you picked at `agent login` or with `agent team switch`, instead of your account's default team. If that team doesn't allow you to use Cloud Agents, the worker exits with a message naming the team and suggesting `agent team switch`.
- **Fixes to self-hosted workers.** Workers sharing a machine no longer fail to start the editor server when another worker is running an older build of it, and workers answer editor connections right away while that server downloads instead of hanging. Connections a worker can't serve now fail immediately, backend connections no longer drop when the machine is busy, and the first turn of a session no longer misses the skills of the person who started it.

### Subagents

- &#x20;**Custom subagents no longer fail when their model can't run.** When a custom subagent is pinned to a model your team's admin settings block, that requires Max Mode, or isn't available, it now runs on the parent agent's model instead of erroring out. The subagent's result notes which model it ran on, so the agent knows the pinned model was skipped. See [when the configured model won't be used](https://cursor.com/docs/subagents.md#when-the-configured-model-wont-be-used).
- **Composer 2.5 subagents run and bill at the speed you picked.** Subagents set to Composer 2.5 now run and are billed at standard speed instead of the fast tier. Subagents on Composer 2.5 Fast run at fast speed without failing with an "Unknown model ID" error.
- **Fixes to subagents.** When the agent waits on a subagent that failed or was stopped, it now sees the failure instead of treating the subagent as finished.

### Rules

- **Nested `AGENTS.md` rules now apply when the agent edits a file.** When the agent edits or creates a file in a subdirectory, it now sees that directory's [`AGENTS.md`](https://cursor.com/docs/rules.md#agentsmd) and nested always-apply rules, even if it never read a file there first. Each rule is shown once per conversation, and glob-scoped and root rules behave as before.

### Fixes

- **Fixes to background summarization.** Long agent sessions now keep summaries computed in the background instead of discarding them and summarizing again.
- **Fixes to tool call display.** Edit, shell, and task tool calls now show as started while the agent is still writing them.
- **Fixes to agent image generation and web fetch.** Image generation prompts written in Chinese, Japanese, Thai, and similar scripts are no longer rejected as too short. Web fetch no longer fails on long pages when the cutoff lands inside an emoji, and video generation now explains why it couldn't read an input image.
- **Fixes to Auto-review.** Auto-review of MCP tool calls now sees the tool's input schema when the server sends it as a JSON string.
- **Fixes to MCP servers.** A single invalid tool or a tool schema without a type no longer hides the rest of an MCP server's tools, and a server that fails to list its tools now reports an error to the agent.
- **Fixes to Windows.** Shell commands the agent runs in PowerShell now use UTF-8, so non-ASCII output no longer appears garbled. Staged updates are no longer held back by leftover markers from crashed or killed processes, and the background update check no longer flashes console windows.

## 1.15.0

### Voice calls

- **Voice calls reconnect after network drops.** In [Cursor for iOS](https://cursor.com/docs/cloud-agent/mobile.md), a voice call that loses its connection reconnects on its own and continues the same conversation instead of hanging up. Work the agent finished while the line was down is passed along once the call is back.
- **Voice calls hang up when you go quiet.** A voice call ends on its own after about 10 minutes of silence from you while the agent has no work in progress, so a forgotten call doesn't stay open. It ends like a normal hang-up, not an error, and a reply that's still playing is never cut off.

### Projects

- **Project replies stream in, with the coordinator's work in Worked sections.** In a Project's chat, the coordinator's replies appear as they are written, and its thinking and tool work fold into a Worked section with a duration before each reply. Chats opened from history show the same view, and a finished turn no longer leaves stray Worked rows below its final reply.
- **See when a Project is waiting on you.** When a Project's coordinator or one of its workers pauses on a question or an MCP sign-in, its inbox row shows Input Needed, and the Agents pill in the Project chat reads Input Needed with a count. The waiting worker shows Input Needed in the Agents sheet instead of Working, so you no longer have to open each worker to find the question.
- **Working Projects show up in the Working tile.** If a team admin has turned on Projects, the inbox Working tile on iPhone and iPad counts Projects whose coordinator or workers are running, and the Working list shows each one once with a working indicator. Archived Projects leave the Projects section and appear only in lists whose status filter includes Archived.

### Pull requests

- **Restack stacked Origin pull requests.** When a Cursor Origin pull request in a stack falls behind its base, the review card shows Restack instead of Update Branch, which Origin doesn't allow for stacked pull requests. Tap it to restack the whole stack, the same as on the web pull request page. If the restack hits a conflict, you see Origin's message.
- **Checks waiting on a reviewer show as Action Required.** When a pull request's only failing checks are waiting on someone's approval, such as a code owner review, the status card, checks list, and agent list show a yellow Action Required status instead of failed checks, and Fix with Agent is hidden for those checks. If real CI failures are mixed in, the checks still show as failed.
- **Faster, steadier Pull Requests list.** The Pull Requests sheet shows line counts and open or merged state right away from recently loaded data, then refreshes faster when an agent has many pull requests. Rows stay in place as details fill in, the Open, Draft, Merged, and Closed filters are always shown, and a message appears when a filter matches nothing.
- **Pull request links show their status in agent conversations.** Pull request links in agent conversations appear as compact number chips with a GitHub or Cursor icon, matching desktop and web. When the pull request belongs to the agent, the icon shows whether it is open, draft, merged, or closed, and VoiceOver reads that status. Custom link text is kept, and copying a link still gives you the original text.
- **Tables, images, and collapsible sections render in pull request descriptions.** HTML and markdown tables in pull request descriptions and agent messages, such as before and after screenshot grids, render as real tables with images and videos inside the cells instead of raw text. Screenshots attached to pull request descriptions and comments load, and the check Details sheet shows collapsible sections and line breaks instead of raw HTML.
- **Review picks up new commits automatically.** With a pull request open on the Review screen, changed files and line counts update within about 30 seconds of a new commit, without pulling to refresh or reopening the app. Existing file rows stay on screen while the update loads.

### Agents

- **Open files from cloud agent links.** Tapping a file link in a cloud agent's transcript opens that agent's chat and shows the file at the linked line, read live from the agent's machine. Links to files in Agent Stores open too, and you get a clear message when a file is missing, isn't text, or fails to load.

### Composer

- **Start agents on repos from your own machines.** The composer's repo picker lists repositories checked out on your online personal machines, even when they aren't connected through source control. Pick one and the agent runs on that machine. Cloud isn't offered for these repos, so the Cloud option shows "Not available for this repository."
- **Dictation works over CarPlay and Bluetooth.** Composer dictation records from CarPlay and Bluetooth hands-free microphones. If the audio route changes partway through, for example when your car connects, the recording keeps going instead of stopping.

### Inbox

- **Pull to refresh the Inbox.** Pull down on the Inbox on iPhone or iPad to reload your agents and the status of their open pull requests, instead of waiting for the next update or reopening the app.

### iPhone Duo

- **Better support for iPhone Duo.** On the unfolded inner screen of iPhone Duo, Cursor for iOS rotates with the device and stays upright when you unfold the phone while the app is open. Sheets like the model picker, search, and pull request review keep their close button in the top bar, and the Inbox profile button moves into the sidebar.

### Account and billing

- &#x20;**Clearer plan management for team accounts.** Tapping Manage Plan on a team account tells you who manages your plan: team members are asked to contact a team admin, and enterprise admins are pointed to their account team. Self-serve team admins get a Manage team subscription row in their profile that opens the team subscription on cursor.com, where the App Store region allows it. If you belong to several teams, the app opens your paid team instead of a Free one, unless you picked the Free team yourself.

### Fixes

- **Voice calls.** Voice calls no longer go silent when started right after dictation, show a failure message after you hang up, or play the greeting over your first words. Muting ends your turn so the assistant replies, and the live transcript no longer repeats your turn. When the microphone can't be used, the app says whether it is blocked, unavailable, or the permission prompt went unanswered.
- **Chat history and follow-ups.** Earlier messages in long chats load as you scroll up instead of all at once on open, and live replies keep streaming while history loads. Follow-ups show the moment you tap Send and no longer vanish or duplicate after a reconnect, and open questions reappear when you reopen a chat. Idle Projects stay in the Projects section, and Back from a Project in the Inbox always returns to the Inbox.
- **In-app purchases and the paywall.** The paywall no longer gets stuck on a blank screen or spinner; it shows an error with a Try again option instead. If a purchase you paid for was not granted because the sheet closed, buying it again recovers it instead of charging twice, and "product not found" errors happen less often. Accounts with no monthly spend limit that hit a usage block go to the web dashboard instead of a Contact Sales dead end.
- **Performance and stability.** The Inbox and Composer no longer hang when you have thousands of repositories, and chats with many pull requests open faster. The app no longer crashes at launch on iOS 26 or when you rotate the device while a video is playing, and the Game of Life animated background renders again.
- **Composer, sheets, and pull request actions.** The composer no longer ends up behind the keyboard after tapping Fix Checks with Agent, or drawn over the toolbar after replying to a long text selection. Search, Checks, and Pull Requests sheets have opaque headers so rows no longer show through, and the Live Activity timer hides instead of truncating in a narrow Dynamic Island. Agent and pull request links in transcripts open in the app you're using, and failed pull request actions explain what went wrong.

## 3.26

### Projects

- **Search, sort, and browse a Project's Library files.** In a [Project](https://cursor.com/docs/agent/projects.md)'s Library, All Files is now a table with Name, Kind, Modified, and Size columns. You can search files, filter by kind, folder, or modified date, sort by any column, limit the list to Project or User files, or switch to a grid of preview cards grouped by folder, and your choices are saved for each Project. Recents now update within seconds of agents writing files, and you can move through the Library with the keyboard.
- **Mention a Project's tasks from the @ menu.** In a [Project](https://cursor.com/docs/agent/projects.md) chat, the @ menu now has a Tasks folder that lists the Project's tasks grouped by status, in the same order as the task list in the right panel. Type a task ID (or just its number) or words from its title to find it, and pick it to add a task chip with its status icon. Mentions of Project members now show as plain @Name chips, and the coordinator's @ menu no longer offers a Branch row it can't use.
- **Faster first replies from a Project's coordinator.** When you message a [Project](https://cursor.com/docs/agent/projects.md), its coordinator now replies right away with a short answer, or a quick acknowledgement and its first step, before it starts reading files or launching workers.
- **Choose which machines a cloud Project can use.** In a cloud [Project](https://cursor.com/docs/agent/projects.md)'s chat, the Run on menu below the chat input now lists your machines and pools, so you can search and check the ones the coordinator may place workers on without asking first.
- **Add a local folder to a Project's allowed machines.** In a cloud [Project](https://cursor.com/docs/agent/projects.md)'s Allowed machines menu, the Machines submenu now has an Add folder on This Mac row. Pick a folder and the Agents Window starts a worker for it and allows it for the Project, showing Starting and Allowing progress, with an error message if it fails.
- **Better keyboard and screen reader support for Project tasks.** In a Project's task List and Board, each task's title is now the control that opens it, so Tab moves cleanly between tasks and focused Board cards scroll fully into view. Screen readers now announce each task's status, the task a status button changes, and PR counts by state such as "3 PRs: 2 open, 1 merged". Focus also follows a task when you change its status, and returns to where you were when you close find in Project notes.

### Chat and composer

- **Voice calls speak the agent's own updates.** On a voice call, the agent now chooses what to say: short progress notes while it works, a brief spoken answer when it's done, and a quick update when workers it started report back, instead of the call reading its chat replies aloud. Calls also show a reconnecting state with the clock running when the line drops, acknowledge tasks right away, and say so when a task can't reach the agent within 20 seconds.
- **Fixed mode slash commands dropping the prompt you typed after them.** Typing a mode command followed by a prompt, such as `/ask explain this file` or `/plan fix the tests`, and pressing Enter no longer clears the input and sends nothing. The Agents Window now switches to that mode and sends your prompt.
- **Long messages you send to a Project collapse with Show more.** In [Project](https://cursor.com/docs/agent/projects.md) chats, long messages you send now show up to 30 lines with a fade and a Show more button that expands the full message, instead of a small scrolling box. Show less collapses it again.
- **Right-click links in Markdown files for the same actions as agent replies.** Right-clicking a link in a Markdown file now shows the same menu you get on links in an agent's reply, with Open, copy, and file actions. File links open relative to the document, and links to a heading in the same file offer Copy only.

### Navigation and layout

- **Split panes keep their own controls and survive reloads.** When you split conversations into panes, each pane now has its own "…" chat actions menu and Project members for the chat it shows, and a tile's title bar is trimmed to just its actions menu and the show-panel button. Splits, the pane you had focused, and each tile's selected agent now come back after a reload, even when a conversation loads late or is hidden from the sidebar. A Project's own chat tab stays pinned at the front of its pane, and drag-and-drop, narrow tiles, keyboard focus, and cycling between panes behave more reliably.
- **Undo an archive with Cmd+Z, and get a warning before archiving agents with running processes.** After you archive an agent or a group, press Cmd+Z (Ctrl+Z on Windows and Linux) or use Edit > Undo while no text field is focused to bring it back, and Cmd+Shift+Z to archive it again. Archiving an agent that still has background processes running now asks for confirmation first, including Archive All on a sidebar group.
- **Drop files onto an agent in the sidebar.** Drag files from your desktop onto an agent or Project in the sidebar to open that chat with the files attached to its prompt. The row highlights while you drag so you can see where the files will go.

### Files, changes, and pull requests

- **Easier pull request review in the PR tab.** The PR tab now remembers whether you were on Changes, Description, Commits, Checks, or Reviews when you switch agents or restart, and Cmd+click (Ctrl+click on Windows and Linux) on a diff line opens that line on GitHub or Origin. Generated files start collapsed with a Generated badge, the Merge button stays disabled while an Origin rule blocks the merge, and merges that bypassed rules now show in the timeline. Pull request chips in prompts and messages show the PR's current status, such as merged or closed.

### Cloud agents

- &#x20;**Open the live workspace for agents on self-hosted workers.** Cloud agents running on a Linux [self-hosted worker](https://cursor.com/docs/cloud-agent/self-hosted/private-workers.md) now show the Changes panel, file tree, terminal, and forwarded ports in the Agents Window, as Cursor-hosted cloud agents do. Start the worker with `agent worker --connect-workspace start` to turn it on. If the worker restarts or goes offline, the workspace reconnects when the worker is back, and an outdated worker shows a message asking you to update it.
- **Clearer status for cloud agents on self-hosted workers.** When a cloud agent's self-hosted worker disconnects, the editor panel shows Worker offline and reconnects automatically once the worker is back.
- **Point environment setup at any environment.json in your repos.** The [environment setup](https://cursor.com/docs/cloud-agent/setup.md) dialog no longer waits to detect `.cursor/environment.json`. Under environment.json location, it starts on Start from scratch and lists every repo in the setup. Pick a repo to load an existing file, and enter its path, which starts filled in as `.cursor/environment.json`.

### Browser and design mode

- **Edit CSS on an element you annotate in Design Mode.** When you leave a note on a single element in [Design Mode](https://cursor.com/docs/agent/design-mode.md), you can open a CSS inspector to filter, edit, and live-preview its properties, then send those edits to the agent with your note. You can pin the inspector to a corner of the page while you work. Leaving Design Mode also gives the page its own cursor back right away.
- **Simpler built-in browser toolbar.** The built-in browser no longer has a bookmarks bar, a favorites and history sidebar, or the Cmd+D bookmark shortcut. Your browsing history is still available from the address bar suggestions and the new tab menu.

### Account

- &#x20;**Switch models when you hit the weekly limit.** When you reach the weekly usage limit on a model your allowance does not cover, the notice can now offer a Switch Model button next to Buy Credits to move to a covered model. On Enterprise plans, the Personal Usage chart in Plan & Usage settings also opens instantly from your last saved data and shows the right spend type if you belong to more than one team.

### Accessibility

- **More accessibility and reduced motion fixes.** Screen readers now announce the chat transcript as a "Chat transcript" region, and announce the branch menu, project selector, font picker, and automation trigger pickers as busy while they load. With reduce motion on, dialogs fade in place instead of scaling or sliding.

### Fixes

- **Steadier agent transcripts.** Reopening a recent agent restores its transcript layout instead of jumping while rows re-measure. After a cloud agent reconnects, output written while you were disconnected now appears in the conversation.
- **Fixes to the subagent tray.** Tray rows and breadcrumbs keep their task names and status in long chats, rows no longer get stuck loading behind one that keeps failing, and a shared Project no longer appears as its own subagent. Tracked task chips show the agent's real name instead of "Agent", and opening a finished cloud subagent reliably loads it.
- **Fixes to the prompt box and chat switching.** Switching chats keeps your cursor where you left it in each prompt, and the composer glides into place instead of jumping. The fullscreen prompt now shows attached videos, stays visible but read-only when follow-ups are unavailable (for example after a failed worktree setup), and a locked prompt no longer accepts dropped or pasted files. Signing out now clears the remembered conversation, and a failed or cancelled agent creation returns you to your draft.
- **Fixes to the sidebar.** Local chats open faster from the sidebar, and the window loads only your most recent chats at startup. Collapsed Pinned sections and stale sections you re-expand now stay that way across reloads, and sidebar rows no longer show stale labels while animating. Cloud agents without a repo no longer show "Cloud" twice in their tooltip, and Projects no longer appear as running when only finished workers remain.
- **Fixes to panels, menus, and the project picker.** The Changes view now names nested repositories correctly and refreshes diffs when you switch repos. Opening a file that isn't on the agent's machine shows a clear message instead of a raw error, Cmd+A in the Files tree selects tree rows, and Chat actions menu picks keep focus in the dialog they open. The project picker keeps the multi-repo Save button visible while searching and stays responsive with very large repo lists.
- **Fixes to cloud Projects.** In a cloud Project, a child agent's forwarded ports menu shows that child's ports, and the coordinator only plays the finished chime when it actually messages you.

## 3.26

### Agent and chat

- **Agents stopped by an extension host crash can be resumed.** If the extension host running a local agent exits mid-run, for example after running out of memory, the chat now shows an "Extension host stopped unexpectedly" error with a Resume option instead of looking like you stopped it. Affected chats are marked unread, and if Cursor is not focused, one system notification covers all agents that stopped.
- **Fixed skills not showing up when you edit an earlier message.** When you edit an earlier message in agent chat, typing / now opens the skill and command picker instead of an empty list, so you can add a skill before you resubmit. The list updates when your skills, commands, or subagents change.
- **Cleaner @, #, and + menus in chat.** The empty @ menu no longer lists Branch or Browser (type to find them), and a # query that matches no pull request now hides the menu, like / and @. The + menu's file item is now called Attach, Summarize appears in the / menu as soon as a chat has a message, and tooltips in menus like the mode picker no longer cover menu items.
- **Review changes with Bugbot in Mercurial repositories.** Reviewing changes with Bugbot from the editor now works in Mercurial checkouts, with file paths resolved from the Mercurial root even when it sits inside a git repo or you open a subfolder.

### Customization and settings

- &#x20;**Always Run on terminal approvals now sticks when permissions.json manages your allowlist.** When your own `~/.cursor/permissions.json` sets the terminal allowlist, choosing Always Run on an agent's terminal approval now adds the command to that file's `terminalAllowlist`, so the same command stops prompting every time. When your team's admin settings control the allowlist, the approval card no longer offers Always Run, since that choice would be ignored. See [permissions](https://cursor.com/docs/reference/permissions.md).
- **Clearer MCP server status and fewer connection mix-ups.** In Customize, [MCP servers](https://cursor.com/docs/mcp.md) that are still reconnecting show "Connecting…" instead of "0 tools" or a sign-in warning, and a local server your Cursor account already has offers "Use the account version". Editing a project's mcp.json while a server connects now uses the new config, and local MCP sign-ins with OAuth now give you up to 15 minutes to finish in the browser.
- **Agent no longer gets duplicate project instructions.** When `CLAUDE.md` is a symlink, hard link, or identical copy of `AGENTS.md`, the agent now receives those instructions once instead of twice. On Windows, [rules](https://cursor.com/docs/rules.md), nested `AGENTS.md` files, and skills now apply even when paths differ only in drive-letter case.

### Fixes

- **Fixes to agent reliability.** Agent chats that contain large numbers now save correctly. Grep and Glob searches that time out keep the matches found so far, notebook edits keep fields the agent didn't touch, and on Windows hooks receive non-ASCII text correctly.
- **Fixes to agent chat and the prompt.** Images attached in the chat prompt are no longer lost if the prompt closes while they save, and pressing send twice no longer sends a duplicate request. Questions from the agent are no longer skipped after you reopen a chat, typing in a chat moved to a separate window no longer reverses or drops characters, and Undo in the chat's file list now reverts files on Windows.
- **Fixes to the editor, terminal, and source control.** Terminals you have already typed in are no longer reset when extension environment variables change, closing a terminal right after opening it no longer leaves a stray shell behind, and zsh shell integration now sets up on the first terminal. Search results group hits from the same file under one entry again, the References view now appears after Find All References, and remotes from partial clones and push-only remotes are now recognized. On macOS, an update that stalls while installing is now detected and retried.
- **Fixes to the built-in browser.** PDFs opened in the built-in browser now show their pages instead of an empty viewer. Agent browser actions no longer fail right after a tab opens or moves between windows, and they stop immediately instead of hanging when the page navigates away or the browser closes.

## 1.0.40

- &#x20;**Choose which team an SDK agent runs under.** If your login belongs to more than one team, pass `teamId` in `Agent.create(...)` options to run the agent under that team. The same option works on `Agent.list`, `Agent.get`, archive and delete calls, and on `Cursor.me`, `Cursor.models.list`, and `Cursor.repositories.list`. It isn't saved, so pass it again on `Agent.resume` and later calls. TypeScript only.
- **Claude Code hooks that deny a tool call now block it in local agents.** Fixed a bug where a `PreToolUse` hook from a Claude Code `settings.json` returned `permissionDecision: "deny"` under `hookSpecificOutput`, but the local SDK agent still ran the tool call. Local agents now treat that [nested response](https://cursor.com/docs/reference/third-party-hooks.md#response-format-compatibility) as a deny.
- **Local runs keep their output when the local agent store can't be opened.** If the local database can't be opened partway through a run, a turn that already streamed text now finishes with that text as its result instead of ending as an error. The run keeps going in memory, and the stream emits a `status` message warning that the run's checkpoint may not be available after the process exits.

## 1.0.39

- **Python runs report why they failed.** When a run fails after it starts, `run.wait()` in the Python SDK now returns `error_code` and `error_message` on the `RunResult`, and stream result events carry the same fields. Before, Python only saw an error status.
- **Fixes to local MCP servers and transcripts.** Passing `mcpServers` on an individual send in a local run no longer drops MCP servers loaded from `settingSources`. Local agents also keep writing transcripts when the home directory is missing or read-only, using `CURSOR_DATA_DIR` when set or a private temporary directory otherwise.

## Week of Oct 19, 2026

### Web

- **Slack DMs for merge queue changes.** Turn on the new **Merge queue** switch in your personal [Notifications settings](https://cursor.com/docs/origin/settings.md#notifications) to get a DM when your pull request is added to or removed from the merge queue. If the queue evicts it, the DM says why, for example which checks failed. If you turned on merge when ready for someone else's pull request, you also get the DM when it enters the queue.
- **See which checks got a pull request removed from the merge queue.** When the merge queue removes a pull request because checks failed, the Slack notification lists up to 10 failing required checks with links to each run, and the Removed from merge queue row in the pull request timeline shows the check status of the commit the queue tested. Check details appear only to people who can read the repository's checks; others still get the removal notice.
- **Choose merge queue checks during first-time setup.** When you set up a merge queue for a repository, the Merge queue settings tab now shows the validation checks picker right away. A single Save turns the queue on with the checks you picked, instead of requiring a second save after the queue exists.
- **The merge queue no longer gets stuck on pull requests it can't build.** If Origin repeatedly fails to create the merge commit or queue branch that CI tests a pull request on, the merge queue now removes that pull request instead of retrying indefinitely. The removal message names the last error and asks you to re-enqueue once it is fixed.
- **Cancel Origin CI runs and jobs.** If you have write access to a repository, you can cancel a running CI run or a single unfinished job from its CI page. A confirmation lists the jobs waiting on the one you cancel, which also show as cancelled, and stopped jobs end within about 10 seconds. The job's check shows who cancelled it.
- **See where CI time goes with job and run timelines.** Origin CI job pages now show a Timeline of queue wait, slot hold, and each phase, including checkout broken into its parts; click a phase to see only its log, and failed jobs open the failing phase with the exit code and first error line. Run pages add a Timeline tab showing each job's waits and phases on one clock alongside the run's slot use against your repository's limit, and group jobs under Failed, Running, Waiting, and Passed, with a Next failure button to step through failures.
- **Origin CI jobs wait their turn instead of failing when capacity is short.** Origin CI jobs now wait for a free slot in their repository's job queue, and when the cluster is full they wait and retry instead of failing right away. Job pages show a waiting job as Queued with its place in the queue, or as Waiting for cluster capacity with how long it has waited, and finished jobs show how long they were queued. A new All jobs in this repository tab on the run page lists queued, running, and finished jobs, which you can filter by status, branch or pull request, and run ID.
- &#x20;**Ask an app to break glass or grant an ownership exemption on a blocked pull request.** When a pull request is blocked, its merge options now list the apps that can break glass or grant an ownership exemption. You can send a request to one of them, see it while it's pending, and cancel it. Apps grant a request by creating the exemption. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- &#x20;**Ownership exemptions now last through new pushes and show as waived.** An ownership exemption granted on a pull request now stays in effect after you push new commits, so you don't have to grant it again. In the merge box, code owner groups and owner policies covered by the exemption now show as "Waived · exemption" with who granted it, instead of waiting or disappearing. Review requirement and mergeability responses in the Origin API also include the exemption's reason and granter.
- **Merge a pull request that targets another open pull request's branch.** When a pull request's base is the branch of another open pull request it isn't stacked on, you can now merge it into that branch from the pull request page instead of being blocked. The merge box shows a Stack onto row so you can stack it on the other pull request in one click. The merge queue and auto-merge still wait until the other pull request merges.
- **Updating a stacked pull request no longer brings back removed code.** After a parent pull request is squash-merged, Update branch and applying a merge-conflict resolution on its child now stop and ask you to restack onto the base branch when a merge could reintroduce changes the child removed. The pull request page also hides Restack and Update branch when a restack is known to stop on a conflict at or below that pull request; merging is unaffected.
- **Commit rows credit co-authors and the person behind agent commits.** Commits on a pull request now list the people named in Co-authored-by trailers after the commit author. Commits a Cursor agent made for you show your avatar with a Cursor "via" badge instead of a generic Cursor Agent avatar.
- **Fixes to reviewer groups and bots on pull request pages.** A requested reviewer group on a pull request now shows its members and their review status, even when the group isn't in your reviewer list. In a pull request's Activity, review requests to a bot show the bot's name instead of a blank reviewer, and requests to a group that was later removed show the group's name instead of a raw ID.
- **Never open pull requests as drafts.** A new **Never open PRs as drafts** setting, under Pull requests in your Origin settings, makes every pull request you or your agents open start ready for review, even when a draft is requested. It applies to all your pull requests, whether you open them from the web, the Origin API, or a cloud agent.
- **Pushes now warn you when they add a secret.** When you push to an Origin repository, Origin scans the pushed changes for secrets such as API keys and tokens. If it finds one, `git push` prints a warning naming the commit, file, and line, with steps to remove it. The matched secret itself is never printed or logged.
- **Push rejections now match Git's wording.** When Origin refuses part of a push, each ref now shows the same reason Git would give, such as "deletion of the current branch prohibited". If a push rule couldn't be checked, the message says so, and a ruleset that actually blocked the push is named first. On repositories with a storage limit, pushes made at the same time can no longer go over the limit together, and the push after one that crosses the limit is rejected right away.
- &#x20;**The audit log records more Origin changes.** Your team's audit log now records repository ruleset creates, updates, and deletes, label changes on repositories and pull requests, merge-when-ready being turned on or off, repository deletions, review dismissals, and changes to a namespace's inbound IP allowlist. Each entry includes the acting member's public user ID, which also appears as a new User ID column in CSV exports, and app installation entries list the permissions the installation holds. Repository events that were sometimes dropped right after a repository was created or deleted are now recorded too.
- &#x20;**Clearer names for bypass users in ruleset settings.** In a repository's [Settings > Rules and Protections](https://cursor.com/docs/origin/settings.md#rules-and-protections), people on a ruleset's bypass list no longer show up as bare user IDs. Someone you don't have permission to see reads "Hidden user", a removed account reads "Deleted user", and an account with no name or email reads "Unnamed user". Hover a row to see the reason and the user ID.
- &#x20;**Cloud agents work on teams with an inbound IP allowlist.** Cursor cloud agents can now clone, push, use Origin MCP, and open the raw file, tarball, and clone links they create, even when your team has an inbound IP allowlist. The exemption covers only your own team's repositories. Concurrent allowlist edits are now applied one at a time, so two admins editing at once can no longer lock each other out or go over the entry limit.
- **Jump from a Cloud Agent's comment to its run.** Comments, threads, and reviews a Cloud Agent posts on a private Origin pull request now end with an Open in Web button that opens the agent run that wrote them. Comments on public repositories don't include the link.
- **Slack notifications for mentions, with cleaner formatting.** In [Notifications settings](https://cursor.com/docs/origin/settings.md#notifications), you can now turn on Slack DMs for when someone mentions you, and mentions written in bold or after punctuation now count. Pull request and comment bodies in Slack now show links, code, headings, lists, and collapsed sections as readable text, not raw HTML tags. When you subscribe a Slack channel to a repository, the confirmation tells you whether a test message was sent or skipped because the channel is shared with another company.

### API

- **List commits that touch a file or directory through the Origin API.** Listing commits through the Origin API, Origin SDK, or the Origin MCP server's `list_commits` tool now takes a `path`, so you get only the commits that change that file or directory, as `git log -- <path>` does. Paths containing `..` are rejected. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).
- **Find pull requests by merge commit or merge time in the Origin API.** You can now list the pull requests that landed as specific commits, up to 100 at a time, or those merged within a date range, so it's easier to map commits back to pull requests or build release reports. The same filters work in the Origin MCP server's pull request list tool. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Request, list, and remove bot reviewers through the Origin API.** Requested reviewers in the Origin API now come back in a single `reviewers` list that includes your team's service accounts alongside users and groups, and you can request or remove any of them by kind and ID. Reviewer webhooks now fire for service-account reviewers instead of skipping them, and the Origin SDK supports the new fields. The older `users` and `groups` fields are deprecated but still accepted; see the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).
- **Origin MCP tools can list changed files between refs and fetch agent screenshots from pull requests.** The `compare_commits` [MCP tool](https://cursor.com/docs/api/origin/mcp.md) has a new `files` view that pages through every file that differs between two refs, with per-file patches. `summary` is still the default. `get_pull_request_attachment` can also fetch cloud agent screenshots and recordings linked in a pull request, from an artifact share link or an agent's artifacts page, for users who can view that agent.
- &#x20;**Apps and service accounts can do more through the Origin API.** Apps installed on a whole namespace can now be granted the Create repositories permission and create repositories through the Origin API. Service accounts and app installation tokens, including tokens acting as a member, can now download repository tarballs through a signed download link instead of failing. Listing namespaces now also returns namespaces other teams have shared with you. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Check runs reject oversized names and links, and mergeability names code owners.** When you post a check run through the Origin API, a check or suite name over 255 characters or a details URL over 8,192 characters now returns an invalid-argument error instead of being accepted. When you ask the mergeability endpoint for owner rules, it now also returns the owning users' names and avatars, so you can show who owns the files instead of raw user IDs. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).

### Fixes

- **Fixes to code owner reviews.** Code owner review requests are no longer removed unexpectedly, and pull requests in very large stacks now get them. On pull request pages, owners named by `@login` now show their approvals correctly, and editing a rule prompt in an `.agentic-owners` directory now refreshes merge readiness. The Code Review Gate check no longer gets stuck in progress, and reporting a gate result right after a push no longer fails as a stale head.
- **Fixes to mergeability and merge conflicts.** Mergeability checks no longer fail while a repository is being compacted. Pull requests with very large numbers of conflicts mark the conflicting file list as incomplete, merge results follow the repository's current `.gitattributes` rules, and directory-rename conflicts are now reported as their own kind of conflict.
- **Fixes to pull request pages.** Pull request pages now update live when merge details or the author change, and reconnect right after the network returns. Files over 10 MiB show "Too large to count" instead of +0 -0.
- **Fixes to Origin CI.** CI jobs no longer fail when the runner cluster briefly stops responding or a runner is slow to start; they wait and retry up to the job's deadline. Retried runs now resume from their saved progress, and a run whose `origin.ci.ts` compiles to no jobs no longer cancels older runs in the same concurrency group.
- **Fixes to Slack notifications.** Slack and email notifications no longer arrive twice, review reminders are no longer sent twice when clocks fall back, and reminders that don't require review requests no longer list your own pull requests. Subscribed channels no longer miss events when many channels follow a repository, and no longer get close or merge posts for drafts that were never marked ready for review. Slack reminder and channel settings now refresh after a failed save or removal.
- **Fixes to the merge queue.** Converting a pull request to draft or marking it ready from the pull request list now shows why Origin refused the change, such as the pull request being in the merge queue. The Merge Queue tab, page title, and settings section are now labeled consistently.
- **Fixes to Git operations.** Commits with malformed author lines or non-UTF-8 encodings now load and display as `git log` shows them, and changing a default branch no longer fails after an interrupted write.
- **Fixes to GitHub mirrors.** Branch updates, merges, and deletes made in Origin now reliably reach the GitHub mirror, and a push no longer fails when GitHub refuses hidden refs or a branch was deleted in the meantime. Fetching pull request refs or new commits from a mirrored repository no longer times out or stalls while the mirror catches up.
- **Fixes to pull request search.** An `app/<slug>` qualifier that can't be resolved now suggests using the app's `app_…` id, and searches from a repo-limited token against a repository it can't read are refused without counting against your search rate limit.

## Week of Oct 19, 2026

### Agents

- &#x20;**Agents know when a subagent fell back to a different model.** When a custom [subagent](https://cursor.com/docs/subagents.md) is set to a model your team's admin settings block, that needs Max Mode, or that isn't valid, the parent agent now learns that the subagent ran on the parent's model instead. Subagents that inherit the parent's model also no longer get blocked on teams that disallow the Fast tier when the parent isn't using Fast.
- &#x20;**Computer use stays on when your team blocks the video review model.** Fixed an issue where blocking Gemini 3.1 Pro in team model settings turned off computer use for every Cloud Agent on the team, even when the computer use models were allowed. Now only video review is unavailable, and the agent keeps testing with computer use.
- **Broken skills are flagged in the run.** When a skill's SKILL.md has invalid frontmatter, no description, or can't be read, the Cloud Agent run now shows a warning naming the skill and how to fix it. Previously the agent quietly skipped the skill or was unlikely to pick it.
- **Faster follow-ups after turns that only read files.** When a turn only reads or searches files, or sends messages, the next turn now starts sooner. The agent no longer waits on a workspace snapshot that wasn't needed because nothing changed.

### Pull requests

- **Pull requests open ready for review by default.** Cloud Agents, including Project workers, now open pull requests ready for review instead of as drafts, unless you or the task ask for a draft. A new Never open PRs as drafts switch in the Pull requests section of your codebase settings keeps every new pull request you and your agents open ready for review, even when a draft is requested.
- **Agent comments on private Origin pull requests link back to the run.** When a Cloud Agent posts a comment, reply, or review on a private Origin pull request, the comment now ends with an Open in Web button that opens the agent run, so reviewers can jump straight to the agent's work.

### Projects

- **Project coordinators keep the task tracker accurate.** In Projects that use the task tracker, the coordinator now links each pull request a worker reports to the right task, unlinks workers from finished tasks, and closes Queued or parent tasks once other work has delivered them. Workers now report status to their coordinator.
- **Parent tasks in a Project's tracker now follow their subtasks.** In a [Project](https://cursor.com/docs/agent/projects.md)'s task tracker, a parent task with no pull request or agent of its own now takes the status of its most active subtask (In Progress, then For Review, then Queued) and moves to done once every subtask is complete. The status updates on every change to its subtasks, so the List and Board views no longer show a parent stuck behind its children.
- **Project workers can check the task tracker.** In a [Project](https://cursor.com/docs/agent/projects.md) that tracks tasks, workers and child coordinators can now read the Project's task tracker to see the status of other tasks, without being able to change it. Workers that are still busy with a follow-up message, or that belong to a teammate, also no longer get unlinked from closed tasks when their turn ends.
- **Project workers get short topic names you can find later.** When a Project coordinator starts workers, it now names each one for what the work is about, like "Webhook retry backoff", instead of a role, action, or PR number. A worker started from only a PR or issue number is renamed once its first report says what the work is about.

### Environments

- **Manage an environment's secrets from its dashboard page.** Each environment's page in the Cloud Agents dashboard now has a [Secrets section](https://cursor.com/docs/cloud-agent/setup.md#environment-scoped-secrets) where you can view that environment's secrets and add new ones, unless its configuration is locked.
- &#x20;**Admins can turn off personal secrets for Cloud Agents.** Team admins can turn on **Disable personal secrets** in the Cloud Agents [security settings](https://cursor.com/docs/cloud-agent/settings.md#security-settings). Members then can't add or edit personal secrets, and secrets they already added are no longer given to Cloud Agents. Members can still delete their existing personal secrets.
- &#x20;**Agents without a repository run on your team's shared default environment.** When a member of a team starts a Cloud Agent without picking a repository or environment, the agent now runs on the team's default no-repo environment instead of a personal hidden one. Nobody can edit, rename, rebuild, delete, or add environment secrets to the team default, but personal and team secrets still apply to it. An unnamed personal environment with no repositories is locked until you give it a name.
- **New environments created by a Cloud Agent now use your repo's `environment.json`.** When a Cloud Agent starts on a single repository with no environment yet, it now boots with the repository's committed [`.cursor/environment.json`](https://cursor.com/docs/cloud-agent/setup.md#configuration-in-code-with-environmentjson) instead of ignoring it. The new environment keeps tracking that file, so later agents and builds use it too.
- **Agents started on a specific environment build use that build's config.** Cloud Agents and subagents started on a specific [environment build](https://cursor.com/docs/cloud-agent/builds.md) now boot with the `environment.json` and settings recorded for that build, instead of the repository's current file or the parent agent's newer environment version. This keeps an agent's setup consistent with the build it starts from.
- **Verify an environment build with an agent from the Builds section.** An environment's Builds section on the Cloud Agents dashboard now has a Verify with Agent link next to Trigger build. It opens a new agent in a new tab, ready to check that the build works. The link appears when you can trigger builds and your team allows manual builds.
- **Pick Origin repositories shared with you when setting up an environment.** When you create a Cloud Agents environment or edit its repositories, the repository picker now also lists Origin repositories from other teams' namespaces that you've been granted access to, after your own team's repositories. This lets you build a multi-repository environment across namespaces from the dashboard instead of only through the API.
- &#x20;**Tighter, more reliable restricted network access.** Cloud Agents with restricted network egress no longer reach every `*.cloudfront.net` host by default; only the CloudFront hosts needed to pull public container images stay allowed, so add any other CloudFront domain your environment needs to your [network allowlist](https://cursor.com/docs/cloud-agent/security-network.md#network-access). Repositories hosted on Cursor now clone faster under restricted egress, and changing network settings while an agent runs now applies that agent's current environment allowlist instead of a stale one.
- **Default environments no longer trust two compromised root certificates.** Cloud Agents' default environments now distrust the emSign ECC Root CA - G3 and AAA Certificate Services roots after private keys for intermediates under them were exposed. The system certificate store is updated, and on the default image the Java trust store is rebuilt from it, so connections signed through these roots fail instead of being trusted.

### Self-Hosted Machines

- **Open the live workspace of agents on Self-Hosted Machines.** Agents running on Self-Hosted Machines can now be opened from the Cursor desktop app with their files, changes, a terminal, and forwarded ports. Turn on the [live workspace](https://cursor.com/docs/cloud-agent/self-hosted.md#live-workspace) when you start a Linux machine. If the machine restarts, opening the agent reconnects to it.
- &#x20;**Send self-hosted runs to a team default pool.** Team admins can pick a [**Default pool**](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#default-pool) in the Self-Hosted section of the Cloud Agents dashboard, and self-hosted runs that don't name a pool or machine go there instead of routing by repository alone. If the default pool serves the run's repository, it takes the run. If not, another team pool that serves the repository takes it, and an any-repo default pool takes everything else. Repository access checks still apply.
- **Agents on Self-Hosted Machines wait for a dropped machine to come back.** When a Self-Hosted Machine drops its connection in the middle of a run, the agent now waits up to 10 minutes for it to come back before reporting the machine as disconnected. If another machine in the pool is free, the agent moves to it instead.

### Web

- **New agent transcript on the web.** Cloud agent conversations at cursor.com/agents, the pull request agent panel, and side chats now use the same transcript as the Agents Window. Your first message in a new agent shows up right away, images included, and in the agent sidebars on codebase pages the mouse wheel and Page Up and Page Down scroll the transcript.
- **Fix with agent on pull request pages goes to the right agent.** On cursor.com pull request pages, Fix with agent and similar actions now follow up the agent that opened the pull request, or your most recently active agent on it, instead of whichever agent is newest.
- **Agent pages show their details sooner on the web.** When you open a link to a cloud agent directly, its header, status, and starting prompt appear sooner.
- **Share canvases with your whole organization.** The share sheet for a canvas can now open it to everyone in your organization, shown as "Anyone at" your organization, or grant access to other teams in your organization.

### Integrations

- **Linear sessions link to the agent and its PR, and PRs close their Linear issue.** Cloud Agent sessions in [Linear](https://cursor.com/docs/integrations/linear.md) now show Open in Web, Open in Cursor, and Pull Request links, and the final reply is a plain summary that no longer appears twice. Pull requests from runs started on a Linear issue now end with a `Fixes <ISSUE-ID>` line, so Linear links the PR and closes the issue when it merges.

### MCP

- **MCP tools that need an extra permission now ask you to grant it.** When an MCP server refuses a Cloud Agent's tool call because your sign-in is missing a permission the server names, the agent shows a sign-in card that names the tool and the permission it needs, instead of failing. If signing in again can't grant it, the agent tells you an admin needs to approve it. Permissions you grant this way are kept the next time you sign in.
- **Fixes to Gmail and Google Calendar tools.** When Gmail rate-limits a request, the agent now waits briefly as Google asks and retries the call, instead of having later Gmail calls blocked for a cooldown period. When a Google Calendar call fails because the connection is missing a permission, the agent now tells you to reconnect the account instead of showing a raw permission error.
- **Google Sheets calls recover when the wrong account is connected.** If a Google Sheets tool call fails because the account in use can't open the spreadsheet, the agent now sees your other connected Sheets accounts and can retry with one that has access.

### Fixes

- **Fixes to Self-Hosted Machines.** When a Self-Hosted Machine drops mid-run, Cloud Agents now reconnect to it or move to another free machine in the pool instead of losing the run.
- **Fixes to MCP connectors.** Common argument mistakes in Slack, Google Sheets, Airtable, and Jira tool calls are repaired automatically, and signing in to a team-owned MCP server no longer conflicts with your own entry for the same URL.
- **Fixes to environment builds.** The Trigger build dialog now scrolls so its button stays reachable when an environment has many repos.
- &#x20;**Fixes to Cloud Agents dashboard errors.** Team preferences on the Cloud Agents page no longer ask paid, Enterprise, or merged teams to upgrade. When a prepaid balance runs out, the error now names it instead of pointing to on-demand usage settings.
- **Fixes to agent stores.** Project members can open links to a Project's store, and subagents running on their own machine keep access to their Project store after a checkpoint or finished turn. Store traffic from cloud agent machines no longer counts against your own rate limit, and the Agent Stores page shows the server's error message when it fails to load.
- **Fixes to how agents handle Origin pull requests.** When an agent checks CI on an Origin pull request, checks that are still running but already failing are now flagged, so the agent can start fixing them without waiting. Merge-conflict notices say "at least N" conflicted paths when the list was cut short, and merging a pull request hosted elsewhere now points the agent to that host's tooling. Commits from subagents of a Slack thread agent now carry the same co-author line, and agents no longer commit a stray file created by the co-author git hook.
- **Fixes to app publishing.** Confirming a publish no longer fails as out of date when the agent committed outside the app's folder or its machine had shut down; the machine now wakes and the confirm retries automatically. New apps are named after their folder or repository instead of a generic name, and a first publish no longer waits on missing secret values. After publishing, the agent names the repository and folder the app came from and links to it, and no longer says secret changes are waiting in the publish dialog.
- **Fixes to Pages.** Published pages now show updates on the next load after you republish, unpublish, rename, or change their address. Pages no longer fail to compile when code blocks or comments mention `import`, and images hold their shape with a blurred preview while loading. Creating a page in a team thread where team sharing is restricted now shows your admin's sharing policy instead of a generic error.

## Week of Oct 19, 2026

### Automations

#### Triggers

- **Security Reviewer runs on GitHub label changes.** Security Reviewer automations with a [Pull request label changed trigger](https://cursor.com/docs/cloud-agent/automations.md#github-triggers) now run when a matching label is added to or removed from a GitHub pull request. Before, they never ran. To apply the fix to an existing automation, open it and save it.

#### Automation runs

- &#x20;**Automations start on teams with an inbound IP allowlist.** Personal automations on teams with an inbound IP allowlist no longer fail with an "IP address is not on this team's inbound IP allowlist" error. Scheduled runs, webhook deliveries, and CI triggers start normally, and Cursor still checks your sign-in and repository access. Manual runs and API-key webhook calls still have to come from an allowed IP address.
- **Clearer failure messages for runs and webhooks.** When a [webhook-triggered](https://cursor.com/docs/cloud-agent/automations.md#webhook-triggers) automation fails to start, the webhook response gives the same failure title and reason as run history, instead of a generic error. Rate-limited runs explain that the limit can apply across all of Cursor and suggest trying again after a short wait. Runs whose agent fails to start tell you to retry and to contact support if it keeps happening.
- **Scheduled automations start up to 5 minutes after their set time.** Each [scheduled run](https://cursor.com/docs/cloud-agent/automations.md#scheduled-triggers) can start up to a fifth of its interval late, capped at 5 minutes. This applies to every schedule, not only hourly and top-of-hour ones. A schedule that runs every 15 minutes can start up to 3 minutes late, and a daily schedule up to 5 minutes late. How often a schedule runs does not change.

#### Integrations

- **Clearer errors when connecting Linear or linking Jira.** If you aren't a team admin, connecting Linear from a [Linear trigger](https://cursor.com/docs/cloud-agent/automations.md#linear-triggers) tells you only team admins can connect it, instead of showing a generic failure. Linking your Jira account explains when you aren't on the Cursor team connected to that Jira site, or when the site isn't connected to a Cursor team yet.

#### Fixes

- **Fixes to the repository picker.** The repository picker in the automation editor labels partial lists as Recent, shows a spinner while more repositories load, and says clearly when a search fails.
- **Fixes to the PR Approver and pull request creation.** The PR Approver automation finds [routing policies](https://cursor.com/docs/approval-agents.md#routing-policies) in `.cursor/approval-policies/`, including `ROUTING.md`, and reviewer-specific criteria in `.cursor/approvals/`. Automations that open GitHub pull requests no longer fail silently when Cursor can't find the repository. The agent gets a clear error instead.

## Week of Oct 19, 2026

### Team settings

- &#x20;**Choose whether Bugbot automatically reviews outside contributors on public repositories.** Admins can turn off automatic reviews of pull requests from bots and people outside the team on public repositories. Use the **Public repositories** setting in Bugbot's [Team settings](https://cursor.com/docs/bugbot.md#configuration). Manual reviews, private repositories, and pull requests from team members work as before. Existing teams keep reviewing these pull requests until an admin changes the setting, and new teams start with it off.
- &#x20;**Fixed Bugbot skipping reviews for some Enterprise teams.** Bugbot no longer skips pull request reviews with "Bugbot plan is disabled for this team" on Enterprise teams whose dashboard shows Bugbot as enabled. On Teams plans, Bugbot still follows the team's Bugbot setting.

### Reviews and checks

- &#x20;**Bugbot checks no longer stay pending when your team hits its daily cap for bot pull requests.** When your team reaches its daily cap of reviews on pull requests opened by bot accounts, Bugbot finishes its [check](https://cursor.com/docs/bugbot.md#ci-check-statuses) right away and shows the cap message. On GitHub, Bitbucket, and Azure DevOps the check fails, so a required Bugbot check blocks the merge until Bugbot reviews the pull request. On GitLab it finishes as neutral.
- **Bugbot explains when it can't push Autofix changes.** When you ask Bugbot to push [Autofix](https://cursor.com/docs/bugbot.md#autofix) changes and the push fails, Bugbot replies on the pull request with the reason instead of staying silent. The reply names the cause, such as a merge conflict, branch protection, missing permission, a mirrored repository, or a merge queue lock.

### Fixes

- **Fixes to GitLab webhooks.** GitLab no longer disables the Bugbot webhook after repeated errors. Bugbot skips merge request events that arrive without a head commit instead of failing on them. When Bugbot rejects a webhook delivery, GitLab's recent events show how to fix it: delete leftover webhooks in the project's Settings > Webhooks, and turn Bugbot off and on for the project if reviews stopped.

## v2026.10.17

### Hooks and subagents

- **Post-tool hooks now fire for subagents.** [`postToolUse`](https://cursor.com/docs/hooks.md#posttooluse) and `postToolUseFailure` hooks that match the `Task` tool now run when a subagent finishes or fails. Before, only `preToolUse` fired for subagents. Any `additional_context` a hook returns now reaches the main agent, and Claude Code `PostToolUse` matchers for `Task` work too.
- **Hooks in subagents get the right transcript.** Subagent transcripts are now saved inside the parent conversation's folder, under `agent-transcripts/<parent>/subagents/`. Hooks that run inside a subagent now receive that file as [`transcript_path`](https://cursor.com/docs/hooks.md#common-schema) and `CURSOR_TRANSCRIPT_PATH`.

### Self-hosted workers

- **Health checks track self-hosted workers through shutdown.** On a worker started with `--management-addr`, [`/readyz`](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#monitoring) now keeps answering while the worker shuts down, returning 503 with `draining: true` so orchestrators stop sending it work. The worker now fails to start if it can't bind the management address after a few retries, instead of running without health checks. Pool workers also exit after dropping a stale claim, so your host can replace them.
- **Fixes to self-hosted workers.** Workers running `agent worker` no longer drop their connection when heavy local builds stall the machine for a few seconds, and no longer exit mid-session when briefly offered another agent. Closing the terminal or losing the SSH session now shuts the worker down cleanly, and a worker that is shutting down refuses new runs instead of accepting one it can't finish.

### Agent

- **Fixed unanswered approvals being reported as cancelled.** If you send a new message while a tool call is still waiting for your approval, the agent no longer tells you that you interrupted or cancelled it. Tool calls that already finished before a pause also no longer run a second time when the agent resumes.

### Rules

- **Fixes to rule matching on Windows.** Nested `AGENTS.md` files, [rules](https://cursor.com/docs/rules.md), and skills now apply on Windows even when the workspace path and rule path differ only in drive-letter case.

## 1.0.38

- **Fixed local agents failing on models that only run in max mode.** Local agents created with a model variant that requires max mode, such as a 500k-context selection, now send max mode automatically instead of failing with invalid parameters, and keep it across later sends and resumes. `Cursor.models.list()` marks those variants with `isMaxMode`, and `ModelSelection` accepts an optional `maxMode`.
- **Computer use tool calls show up in run events.** When an agent uses computer use, tool call events now carry a typed `computerUse` call instead of dropping it. `args.actions` lists each action (`click`, `type`, `scroll`, `key`, `drag`, `screenshot`, and more), and `result` reports the action count, duration, screen settle time, and an optional screenshot path or error message.
- **`zod` is now a peer dependency.** `@cursor/sdk` now uses the `zod` you install yourself (3.25 or later in the 3.x line, or 4.x), so your schemas and the SDK's share one copy. The exported schemas are built with the `zod/v3` API, which both supported versions include. Add `zod` to your dependencies if your project doesn't already have it.
- **Slow-starting stdio MCP servers can take longer to connect.** Local agents now honor `startupTimeoutSec` on a stdio server in your MCP config, so a server that is slow to start no longer fails at the fixed 60-second connect limit. You can set up to 5 minutes; servers without the setting still default to 60 seconds.
- **Brief server outages no longer fail one-off SDK requests.** When the server reports a temporary outage that is safe to retry, the SDK resends a one-off request once, after a short random delay of up to 1 second, instead of failing right away. Streaming calls such as agent runs are never replayed.
- **Background subagents keep running after the tool call that started them.** When a local agent starts a subagent in the background, the subagent no longer gets cancelled as soon as the launching tool call returns.
- **Fixed sandboxed runs failing on a non-executable sandbox helper.** The SDK's platform packages now install the sandbox helper with execute permission.
- **Fixed Python cloud launches with a named cloud environment.** Launching a cloud agent from the Python SDK with a named cloud environment and no repos no longer fails validation.

## v2026.10.15

### Agent tools

- **Grep and Glob search folders outside the workspace.** When the agent asks to search a folder outside your open workspace, Grep and Glob now search that folder. Before, they quietly searched the workspace instead and returned results from the wrong place. `.cursorignore` and Read deny rules still apply to files outside the workspace, and Glob now says when its results were cut off.

### Cloud Agents

- **`agent env` commands work with your personal environments and public IDs.** `agent env get <repoUrl>` now shows your saved [personal environments](https://cursor.com/docs/cloud-agent/setup.md#environment-resolution-order) for that repo, each with its `environment.json`, and `agent env list` shows each environment's public ID first, also in JSON output. `agent env delete` takes that public ID and explains what to pass if you use an old numeric ID. `agent env get` no longer takes `--ref`.

### Self-hosted workers

- **Give slow MCP servers more time on self-hosted workers.** Use the repeatable `agent worker --mcp-tool-timeout server=seconds` or `server/tool=seconds` option to raise or lower how long a stdio [MCP](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md#mcp-servers) tool call can run, instead of the fixed 60 seconds. Workers also respect a stdio MCP server's `startupTimeoutSec`, so servers that start slowly are no longer cut off after 90 seconds.
- **Windows workers explain when Git Bash is missing.** On Windows, `agent worker start` now exits with a message saying the worker requires Git for Windows, including Git Bash, and where to install it, instead of failing later. The same message is appended to `%LOCALAPPDATA%\cursor-agent\worker-startup.log`, and `agent worker --help` lists the requirement.

### Fixes

- **Fixes to agent search, read, edit, and shell tools.** Searches that time out now keep partial results, and invalid regexes or empty patterns get clear errors instead of matching everything. Reads with huge offsets no longer end the session, and edits no longer silently change only the first of several overlapping matches. Shell output no longer runs stdout and stderr lines together, and waiting on a background command tracks it instead of sleeping the full timeout.
- **Fixes to subagents.** When a subagent fails, the agent now sees the subagent's ID and the reason it failed, not a generic error. Subagents asked to use a model name with an extra `cursor-` prefix or a `-fast` suffix that doesn't exist now run the requested model instead of erroring or switching to Composer. Resuming a failed subagent keeps its original type and model.
- **Fixes to long sessions, memory, and summarization.** Long sessions use less memory: very long todo lists and turns that end during a background summary no longer bloat the agent, and turns no longer fail if summarization can't start near the context limit. Context usage after a summary is more accurate, oversized web search results and runaway tool-call streams no longer overflow the context, and stopping an agent keeps tool results that had already returned.
- **Fixes to self-hosted workers.** Workers no longer time out agent claims when the agent store is slow to open, and they keep recognizing a running Cursor server after the process that launched it exits. A worker also no longer fails when another worker on the same machine installs the same server build while it is downloading.
- **Fixes to hooks and shell commands on Windows.** Hooks that fail or point at a command that can't be found are now reported as failed instead of silently succeeding. The agent also no longer tries to use tmux for shell commands on Windows.
- **Fixes to file suggestions, archived agents, and local addresses.** Running the CLI from your home folder on macOS no longer triggers permission prompts for protected folders like Desktop, Documents, or Library when building `@` file suggestions. Messaging an archived agent now says so clearly instead of showing a generic not-found error, and unrelated errors that mention "archived" are no longer misreported. IPv6 hosts such as `[::1]` are now recognized as loopback, and the full link-local range is treated as private.

## 3.25

### Browser and design mode

- **Edit CSS in Design Mode more like browser DevTools.** The CSS inspector in Design Mode notes now works like browser DevTools. Use the Up and Down arrows to step a value (hold Shift for steps of 10), drag a number to scrub it, or type a bare number like `8` to get `8px`. Color and length rows suggest the page's own CSS variables, and the values shown now come from the browser's real cascade, including nested rules, adopted stylesheets, and cross-origin stylesheets.
- **Pick parent elements with the arrow keys in Design Mode.** While hovering in [Design Mode](https://cursor.com/docs/agent/design-mode.md), press Up to move the highlight to the parent element and Down to go back, then click to select it. The hint bar shows the shortcut, and the selection ring around a picked text element now sits slightly off the text instead of hugging the letters.
- **Browser tabs reload on their own when your dev server comes back up.** A browser tab pointed at a local port that had stopped responding now reloads when a terminal command or an agent's background shell starts serving that port again, so you no longer have to refresh by hand after restarting a dev server. A new Reload Browser Tab command (Cmd/Ctrl+R) reloads the active tab.

### Navigation and layout

- **A cleaner, faster command palette.** The Cmd+K palette now offers Select Model, Archive, and New Side Chat. Paste a pull request URL or type a pull request number to jump straight to that pull request. Rows fit on one line, shortcuts shown next to commands match what runs them, and the palette opens and searches faster when you have many agents. Ctrl+Tab now opens the recent agents switcher, which uses the same look as the palette, even while the palette is open.
- **Back reopens tabs you just closed.** After closing a tab in the Agents Window, such as a file, terminal, browser, Changes, Output, or a side chat, press Back to bring it back where it was, with its navigation history intact. Cmd+Shift+T focuses a tab that Back already restored instead of opening a duplicate. Mouse side buttons pressed in a chat pop-out window also no longer navigate the main window.

### Files, changes, and pull requests

- **Play audio files and scroll through whole PDFs in file tabs.** Opening an audio file such as .mp3, .wav, .ogg, .aac, or .opus in a file tab now shows a built-in player instead of a binary placeholder, and it pauses when you switch away. PDFs now scroll continuously through every page, the toolbar shows the current page with buttons to jump between pages, and zooming keeps your place. The CSV preview's row-number column also no longer lets scrolled cells show through.

### Cloud agents

- **Agents on Self-Hosted Machines are grouped by machine in the sidebar.** The sidebar now groups agents running on [Self-Hosted Machines](https://cursor.com/docs/cloud-agent/self-hosted/pool.md) into one section per machine or pool, labeled with the machine name even before a worker picks up the run. Agents keep the machine you picked across refreshes, forks, and other windows, and for workers that can't serve live changes, the Changes tab explains why instead of spinning.
- **Add a folder to a Project's allowed machines.** In a Project's Allowed machines menu, the Machines list now ends with an Add folder row for this computer. Pick a folder and the Agents Window starts a worker for it and allows it on the Project, showing Starting and then Allowing until it's done.
- **More reliable forwarded ports for cloud agents.** In the editor panel's forwarded ports menu, a cloud agent port that can't be reached now shows a red dot and the error, such as a timed-out connection, until a connection succeeds. Opening a second cloud workspace no longer breaks port forwarding for the first, and turning off Auto-Forward Ports now closes ports that were forwarded automatically and keeps them from being forwarded again.
- **Fixed wrong Dockerfile path errors in cloud environment config.** Editing `environment.json` now checks `build.dockerfile` and `build.context` against the paths the cloud build uses, resolved from the repository's `.cursor` folder. False missing-Dockerfile errors go away, a missing build context folder is flagged, and agents setting up an environment write paths that build correctly.

### Customization and settings

- &#x20;**Claude Opus 5.5 and Sonnet 5.5 on AWS Bedrock.** Teams that route models through [AWS Bedrock](https://cursor.com/docs/customizing/aws-bedrock.md) can now pick Claude Opus 5.5 and Claude Sonnet 5.5 in the Agents Window's model settings.

### Privacy and security

- **Safer handling of branch names in git and GitHub commands.** Fixed an issue where a branch name or commit ref containing shell characters could run unintended commands during pull request lookup, CI reruns, or the branch diff. Unsafe names now skip the GitHub CLI lookup, and the diff falls back to comparing against origin/main.

### Agent and chat

- **Add links and media from the transcript to chat.** Right-click a pull request, agent, project task, canvas, file, folder, or line-range link in a conversation and choose Add to Chat to insert it as a chip, or as a plain link for other URLs. Images, videos, and text artifact cards also offer Add to Chat alongside Download, Copy Image, or Copy Text, and web search results, terminal citations, and thinking blocks now open the same link menus.
- **Links added to chat become compact chips.** Using Add to Chat on a GitHub issue, commit, Linear issue, or web link in an agent reply now inserts a short labeled chip with an icon instead of the raw URL. The full URL is still sent to the agent and shown on hover, and clicking the chip opens the link.
- **Inline code formatting in the prompt.** Text you type or paste between single backticks in the prompt now shows as inline code, and is sent with its backticks. Press Backspace right after the conversion to get the plain backticks back.
- **Find any pull request from the `#` menu by number.** In the prompt box's `#` menu, typing a pull request number that isn't in the list now looks it up and adds it, with a loading status while it searches and "No matching pull requests" when nothing matches. Pull requests you opened moments ago on Origin also show up in the menu within seconds.
- **Clearer live status while agents work.** When a subagent needs your approval or an answer, the main conversation's status line now says "Waiting for approval" or "Waiting for response" and shows what it's asking for. Each finished turn shows how long the agent worked, the transcript stops jumping when a turn ends, and messages sent by another agent name the agent that sent them.
- **Cmd/Ctrl+F works inside canvases.** Pressing Cmd/Ctrl+F in a canvas opens its find bar, or puts focus back in the bar if it is already open, without losing your current match.

### Fixes

- **Fixes to Annotate.** Escape now exits Annotate (or dismisses a model warning) without collapsing the apps panel or dropping your note, and dictation goes into a focused note. Element and region screenshots frame the right area on zoomed tabs, scrolling a note or the CSS inspector no longer scrolls the page, and pin hover cards no longer block picking elements beneath them. Notes no longer jitter as they resize, the annotate cursor no longer lingers after you leave, and clicking a saved note while drafting a comment opens it after asking whether to discard your draft.
- **Fixes to switching between agents and keyboard focus.** Going Back to a subagent no longer clears Forward history, and Cmd-N reliably puts the cursor in the agent's prompt without jumping mid-typing. Shortcuts no longer reach hidden agents, the hidden chat behind fullscreen Apps, or the main window from a chat pop-out. Files and pull requests opened right after starting a New Agent now stay open.
- **Fixes to trays above and below the prompt.** Notices on the new-agent screen now show one at a time without shifting the composer, and pressing Escape on a blocking tray no longer opens the Browser pane. Trays in short agent tiles stay inside the tile instead of overlapping the tabs, focus returns to the prompt when a tray you were typing in gets covered, and trays you opened or closed stay that way when you switch agents.
- **Fixes to files and the editor panel.** Opening a file path that doesn't exist yet from the command line now opens a new editor that saves to that path, instead of a tab that fails to load. On macOS, background file watching and scans no longer reach into protected folders like Desktop, Documents, and Downloads when your workspace contains them, so you stop getting access prompts. While a workspace connects, the editor panel shows a small spinner: hover it to see the status, or click it to view the remote connection output.
- **Fixes to window appearance.** On macOS, the window's translucent background tint now updates when you switch between light and dark themes. The collapsed apps rail beside a conversation is no longer faded out when you scroll the transcript.
- **Fixes to outage notices.** The sidebar status card now shows the real incident name and latest update from the Cursor status page, and says when the incident is resolved. The Cloud option in the Run on picker only reflects Cloud Agents incidents, without the extra warning text.
- **Fixes to the Cloud Desktop tab.** The Cloud Desktop tab draws screen updates more efficiently and stops streaming while another tab is selected. When you switch back, it reconnects reliably with a fresh connection instead of one that may have expired.
- **Fixes to voice calls.** Voice call transcripts with cloud agents now sync while the call is live, so other devices show turns mid-call. Call cards for calls on another device no longer flash an inflated duration, and the return bar in other agents shows the called agent's current title after a rename. Closing a window while voice was starting no longer crashes the voice service.
- **Fixes to agent transcripts.** Messages sent from another device no longer remount or land out of place in the transcript. Cloud agent output written while disconnected now appears after reconnecting instead of going missing.
- **Fixes to the prompt box menus.** The / menu no longer lags when many commands match, and typing after choosing /add-plugin no longer freezes the input. Arrow keys now wrap around in the @ and + menus, right-clicking inside an open menu no longer opens a second menu, and tiny attached images now preview at a readable size.
- **Fixes to the @ mention menu.** Late-arriving results no longer move the row you've highlighted, rows no longer flash while results load, and slow sources still show up. For cloud agents, the menu shows the agent's last known files right away, refreshes on its own when the file list loads, and only suggests folders the agent's machine has.
- **Fixes to File Blame in multi-folder workspaces.** File Blame now reads history from the repository that owns the file when the workspace has several folders, instead of always using the first one.
- **Fixes to reviewing changes.** Opening a large GitHub pull request for review no longer freezes the window. Reviewing an agent's changes on long chats that touched many or large files uses less memory and stays responsive.
- **Fixes to blocked pull request merges.** The merge button in the diff header now says why a merge is blocked, showing "Needs restack" when the branch must be restacked onto its base, or "Checking for conflicts…" while the conflict check is still running.

## 3.25

### Cloud agents

- **Cloud agents on Self-Hosted Machines stay on the machine you picked.** Cloud agents started on a specific Self-Hosted Machine keep that machine after the agent list refreshes and when you fork them, so follow-ups run on the same machine.
- **More reliable forwarded ports for cloud agents and remote windows.** Connections to a cloud agent's forwarded ports that get no answer now close after 20 seconds instead of hanging and blocking other ports, and opening a second cloud workspace no longer breaks port forwarding for the first. With `remote.autoForwardPorts` off, ports that were forwarded automatically are no longer restored when you reopen a remote window.
- **Fixed wrong Dockerfile path errors in cloud agent environment files.** Editing `.cursor/environment.json` now checks `build.dockerfile` and `build.context` against the same paths the cloud build uses, resolved from the repository's `.cursor` folder. False "Dockerfile does not exist" errors go away, a missing build context folder is now flagged, and hover text explains the path rules. See [cloud agent setup](https://cursor.com/docs/cloud-agent/setup.md).

### Customization and settings

- **Agent Store sync keeps working after you switch teams.** Your local Agent Store no longer stops syncing when you change your active team, as long as you're still a member of the team the store was created under. When sync is briefly refused, Cursor now waits the suggested interval before retrying.
- **Skill warnings and clearer skill menus.** Customize > Skills now shows a warning icon on skills whose name, description, or body go past the Agent Skills limits; hover to read what to fix, or click to copy it. Skills that share a name show as separate rows in the / menu instead of collapsing into one, skills appear there sooner after you open a window, and /skill mentions stay highlighted in sent messages.
- **Delete Old Chats reclaims disk space.** After you run **Developer: Delete Old Chats**, Cursor offers **Rewrite Now** to give freed space in its local database back to your disk. Cleanup also removes leftover message data from deleted chats without freezing the editor, and deleted chats, including ones moved from a cloud agent to local, no longer reappear in the chat list.
- **YAML keys stand out in the Cursor Dark themes.** In Cursor Dark, Cursor Dark High Contrast, and Cursor Dark Colorblind, YAML keys now have their own color instead of matching their values. Booleans and `null` now use the regular text color, so `paused: false` no longer looks like a string.
- **View in Cursor opens the plugin you were looking at.** Clicking View in Cursor on a plugin's marketplace page now opens that plugin's page in Customize, instead of the general plugins settings.

### Agent and chat

- **New installs steer the running agent by default.** On a fresh install, messages sent while the agent is running, including ones sent manually from the queue, now steer it instead of queuing or interrupting, and Steer is listed first in Settings. Existing installs keep their current behavior.
- **Add file links from chat back into the composer.** Right-click a file link in an agent reply and choose Add to Chat to attach that file to your current message. File and link menus now also work in thinking blocks and on file chips in your own messages, and clicking a chat mention in a sent message opens that chat.
- **Inline code formatting in the agent prompt.** Text you type or paste between single backticks in the agent input now shows as inline code, and is sent with its backticks. Press Backspace right after the conversion to get the plain backticks back.
- **Clearer live status in agent chat.** When a subagent needs your approval or an answer, the main chat's status line now says "Waiting for approval" or "Waiting for response" instead of "Waiting for subagent". The transcript also stops jumping when a response finishes, and messages sent by another agent name the agent that sent them.
- **Background shells keep running between turns, and archiving a chat stops them.** Dev servers and other background shells an agent starts keep running after the turn ends and when the chat's workspace folders or worktree change, so they still answer in the next turn. Archiving the chat stops them instead of leaving them running.
- **A cleaner, more compact agents sidebar.** Agent rows in the agents sidebar now take up a single line, so more agents fit at a glance, and they can show when each agent was last updated. A new Search row opens the chat history picker in place of the inline search box, and keyboard shortcuts for rows appear only when you hover.

### Privacy and security

- &#x20;**Subagents respect your Private Inference model choices.** With Private Inference, subagents no longer run on models you turned off in Settings > Models. Custom subagents pinned to a turned-off model run on the parent agent's model instead.
- &#x20;**Security hardening for git diffs, links, and repository blocklists.** Viewing diffs, blame, or history no longer runs a repository's configured external diff or textconv command, so opening an untrusted repo can't execute code. Wildcard trusted domains in link protection no longer match lookalike hosts, and agent shell commands that list directories now respect admin repository blocklists, including `**` globs.

### Fixes

- **Accessibility fixes.** Images in chat can be reached with Tab and opened with Enter or Space, and screen readers now name the agent status icon, the plan Build options menu, and the built-in browser by its page title. In Cursor Settings, the Partial Accepts tooltip shows the actual keybinding, the Open and Invite buttons have names, and Tab reaches a model's switch before Remove.
- **Smoother Cloud Desktop viewer.** The Cloud Desktop viewer for cloud agents decodes screen updates more efficiently, using less CPU.
- **Fixes to agent chat scrolling and rendering.** Long agent chats no longer jump while you scroll, and loading a large cloud agent conversation no longer blocks the editor. Streamed messages stay in one bubble, user messages no longer show internal automation tags, and code blocks, lists, and equations no longer add extra gaps between messages.
- **Fixes to agent tools.** Agent sessions no longer end when the model sends an out-of-range value to Shell, Grep, or Read, and long todo lists no longer crash the agent. Glob now finds empty and binary files, edits no longer change only the first of several overlapping matches, and web search and mode switch calls show up in chat before they ask for approval.
- **Fixes to the agent chat input menus.** The / menu no longer lags when many commands match, and typing after choosing /add-plugin no longer freezes the input. Arrow keys now wrap around in the @ and + menus, closing the + menu returns focus to the + button, and tiny images in the image preview are enlarged so they're readable.
- **Fixes to the @ mention menu in chat.** Late-arriving results no longer move the row you've highlighted, rows no longer flash while results load, and slow sources still show up. For cloud agents, including when editing a sent message, the menu shows the last known files right away, refreshes once the file list loads, and only suggests folders the agent's machine has.
- **Fixes to Review Changes.** Opening a large GitHub pull request in Review Changes no longer freezes the editor. Review Changes also uses less memory and stays responsive on long agent chats that touched many or large files.
- **Fixes to loading local media files.** Local video and audio files now play and seek correctly in the editor. AVIF, ICO, WebM, and M4V files from anywhere on disk now load in previews, and files under a symlinked home or extensions folder are no longer refused.
- **Fixes to saving Markdown files from the preview.** Saving a Markdown file from the Markdown preview editor without editing it no longer rewrites its formatting. Edits made in the preview no longer remove the file's final newline or add a blank line after a trailing list, code block, table, or heading.
- **Fixes to model settings.** The Explore Subagent Model help in Settings no longer shows two tooltips at once, and the model picker no longer shifts sideways when you change the selection.

## Week of Oct 12, 2026

### Web

- &#x20;**Restrict merge methods per branch with rulesets.** In a repository's [Settings > Rules and Protections](https://cursor.com/docs/origin/settings.md#rules-and-protections), the ruleset dialog has a new **Restrict merge methods** option that limits pull requests on matching branches to merge commits, squash merging, or both. The merge button only offers methods the target branch allows. When no method can land, the pull request shows a blocker that names the branch, the rulesets involved, and how to fix it, instead of failing at merge time.
- **Choose how auto-merge lands your pull request.** When you enable auto-merge on a [pull request](https://cursor.com/docs/origin/pull-requests.md#pull-request-page), you can now pick squash or merge commit, and the commit title and message you edited are used when it lands. The button shows your pick, for example "Enable auto-merge (squash)", and once auto-merge is on, the merge popover shows the chosen method and commit.
- &#x20;**Block large files with a maximum file size rule.** In a repository's [Settings > Rules and Protections](https://cursor.com/docs/origin/settings.md#rules-and-protections), you can now create a **Repository** ruleset with a **Maximum file size** limit of up to 100 MB. Origin rejects any push that adds a file over the limit and names the files that are too large. The ruleset list summarizes each rule by its limit, for example "Files up to 5 MB". The rule is also available through the Origin API and Go SDK; see the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- &#x20;**Require approvals from specific groups before merging.** In a repository's [Settings > Rules and Protections](https://cursor.com/docs/origin/settings.md#rules-and-protections), a ruleset can now require approvals from specific groups, each with its own minimum number of approving members, chosen from an **Add group** menu. A pull request blocked on this shows a blocker naming the group, with how many approvals it still needs and how many it has, and suggests requesting review from that group. Group rows show the group's name, type, and member count, and groups that can't be named read "Deleted group" or "Group outside this organization."
- &#x20;**Choose how code owners review pull requests in rulesets.** In [Settings > Rules and Protections](https://cursor.com/docs/origin/settings.md#rules-and-protections), the ruleset editor now has a **Code owner review** setting with Off, Classic, and Agentic options. It replaces the "Require review from code owners" toggle. Classic requires an approval from a code owner for the files they own. Agentic still enforces CODEOWNERS, but when Origin's agent reviews ownership on a pull request, its decision replaces the approval count. When a change is blocked, Origin shows which owners need to approve and for which files.
- &#x20;**Apps can be code owners.** You can name an app as a code owner in your `ORIGIN_CODEOWNERS` file with `app_<id>`, and an approval from that app satisfies the paths it owns, provided the app is installed on the repository's namespace. On the pull request page, app owners show their name and avatar. Apps that aren't installed appear muted with a "Not installed" hint, and the codeowners preview explains why they can't approve.
- &#x20;**Ruleset saves no longer overwrite someone else's changes.** In [Settings > Rules and Protections](https://cursor.com/docs/origin/settings.md#rules-and-protections), if someone changed a ruleset after you opened it, saving now asks you to reload first. Descriptions can span multiple lines, and pushes blocked by a ruleset name that ruleset. Active rulesets are now always enforced, even in repositories with many disabled ones.
- &#x20;**See which rules were skipped when a pull request merges with a bypass.** When someone on a ruleset's bypass list merges a pull request without meeting all its rules, the pull request's activity now shows an entry like "merged, skipping 2 rules" that lists each skipped rule, such as required reviews or required status checks. The bypass is also recorded in audit events.
- **Large pull requests load every file.** The Files changed view now keeps loading files on large pull requests instead of stopping at 500, including when you compare two versions. If a list still stops short, a line tells you how many files are shown.
- **Run agent prompts as Origin CI jobs and steps.** You can now give an Origin CI job or step a `prompt`, and optionally a `model`, and a Cursor agent carries it out in the job's workspace, running shell commands and reading, editing, and searching files there. The agent can mark the check neutral or skipped instead of passed or failed, and neutral checks don't fail the overall CI status. Prompt steps run as your team's Origin CI service account, so the repository's namespace needs a team owner.
- **More flexible inputs and larger outputs for Origin CI jobs.** In `origin.ci.ts`, a job can now use the whole repository with `inputs: ["**"]` or `glob("**")`. A leading `/` on an input or output path means the repository root, even in a nested package config, and `exists()` and `glob()` now check the files in the commit. Jobs can publish and cache outputs of up to 64,000 files, outputs that contain symlinks publish instead of failing, and an invalid symlink makes the check name the paths at fault.
- **CI job pages show what a job is waiting for.** A queued CI job now says which upstream jobs it's waiting for. After a job's commands finish, its status reads Publishing outputs until its outputs are saved. Job pages link to upstream jobs and to the jobs that need this one, and the job log ends with a one-line summary of the uploaded outputs: file count, size, and upload time.
- **Exclude, date-filter, and label-filter pull requests in the list search.** On a repository's pull requests list, you can now exclude results with negated qualifiers like `-author:@me`, `-label:bug`, or `-is:draft`, and filter by date with `created:`, `updated:`, `merged:`, and `closed:` using dates, comparisons, or ranges such as `merged:2026-09-01..2026-09-30`. Rows now show their labels, and clicking one adds it to your search; `label:a,b` matches either label. Merged and closed rows also say when they merged or closed, and loading more pages in large repositories is faster.
- **Keyboard shortcut sheet on pull requests.** Press `?` on a pull request page, or choose Keyboard shortcuts from the overflow menu, to see every available shortcut, including the keys for switching tabs and moving through the diff.
- **Discard a pending review.** When you have pending review comments on a pull request, the review menu in the pull request header now offers Discard review. After you confirm, Origin deletes your pending review and all its draft comments.
- **Symbol navigation and a Raw button in codebase file views.** When you [browse a file](https://cursor.com/docs/origin/browse.md) on a wide screen, hover a symbol to see its signature, or click it to jump to its definition and references. File views also have a Raw button, next to copy and download, that opens the file's plain contents in a new tab.
- **More reliable code tours.** Code tours that fail to generate now retry once automatically, and if a default tour fails partway, you see the saved tour instead of an error. In a whole-stack tour, each chapter shows the change made by that chapter's pull request, and a Files you own tour follows the files you own when you switch comparisons. When a Cloud Agent edits a pull request's tour, you see that edit instead of an older tour you generated.
- **Jump to a pull request author's Cursor profile.** On pull request pages, author names and avatars in the timeline, comment threads, and hover cards now link to the person's public Cursor profile when they have one. Authors in a pull request stack now appear the same way they do on the pull request itself, and profile links no longer disappear while the page updates.
- &#x20;**Ruleset bypass for apps pushing directly is clearer.** An app on a ruleset's **Bypass list** can now push directly to a branch that blocks direct pushes when it uses its own installation token. An app pushing with a person's token no longer gets that person's bypass, so it has to open a pull request instead.
- **More reliable Git LFS downloads, with clearer errors when a file is missing.** In [repositories mirrored from GitHub](https://cursor.com/docs/origin/mirror-github.md), Git LFS downloads now fall back to GitHub when a file isn't in Origin yet. When a file is missing everywhere, the error names the object and explains how to upload it with `git lfs push` or skip it with `GIT_LFS_SKIP_SMUDGE=1`. If GitHub rate-limits a download, Git LFS is told to retry later.
- **Push-triggered automations now know who pushed.** Automations triggered by a push to an Origin repository now get the pusher as the actor, the same as pull request, comment, and label events already did. Actor-based filters now match valid pushes instead of skipping them. If the pusher is hidden or can't be resolved, the automation still won't run.

### API

- **Manage auto-merge from the Origin API.** You can now turn auto-merge on or off for a pull request through the Origin API, see who turned it on and how it will merge, and get webhook events when auto-merge is turned on or off. These endpoints and events are in preview. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Create a repository through the Origin MCP server without picking an owner.** The `create_repository` [MCP tool](https://cursor.com/docs/api/origin/mcp.md) now works without an owner: Origin sets up your personal namespace the first time and creates the repository there. This needs an eligible plan and a Privacy Mode setting that allows code storage. Team members and app tokens still need to pass an owner.
- **New webhook events for drafts, authorship changes, and repository labels.** Origin apps can subscribe to `pull_request.unpublished`, sent when a pull request is moved back to draft, and `pull_request.commandeered`, sent when someone takes over a pull request's authorship, with the previous author in the payload. Apps with read access to repository labels can also subscribe to `repository.label.created`, `repository.label.updated`, and `repository.label.deleted`. Pausing or revoking an app now stops installation webhook deliveries right away, and reviewer webhooks are no longer sent with an empty reviewer. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for payload details.
- **Create missing labels while labeling a pull request through the Origin API.** Adding or setting pull request labels through the Origin API and Origin SDK now accepts `create_missing`, so automations can apply a label that doesn't exist yet in the repository without a separate create call. Existing labels match by name regardless of case, and creating labels requires permission to manage labels. Without the option, the error now lists every missing label name. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md) for details.
- **Origin MCP tools accept GitHub-style arguments.** Agents and scripts written for GitHub's MCP server now run against the [Origin MCP server](https://cursor.com/docs/api/origin/mcp.md) with fewer errors. Tools accept `owner/name` strings, `full_name`, nested repository objects, and `ref` in place of `sha`. The tree, commit, and pull request read tools also work without a `sha` or view, defaulting to `HEAD`, metadata, and the summary.

### Fixes

- **Fixes to Origin CI.** Checkouts that include committed symlinks no longer fail or drop files, and input globs with `?` or `{a,b}` now match the files you expect. Re-running a push check runs that check's commit. `ecrLogin` without a region now uses the deployment's region (or `$AWS_REGION` locally) instead of silently defaulting to us-east-1.
- **Generated-file markers in diffs respect `linguist-generated=false`.** Files marked `linguist-generated=false` in `.gitattributes` are no longer shown as generated in pull request diffs.
- **Fixes to Git pushes and repository reads.** Pushes evaluate rulesets with many wildcards quickly, a recreated repository no longer serves the old repository's refs, and commits with large messages now return their metadata.
- **Fixes to team and namespace setup.** Merged teams that have members but no seats are no longer treated as inactive. Auto-merges no longer stall, review reminders and Slack DMs arrive, and the team's privacy mode applies. More plans can now write to their personal namespace without an upgrade prompt, and automatic namespace setup picks an available name when your preferred one is taken.
- **Pull request pages no longer show checks from a different base.** Checks reported against a different base no longer appear on a pull request page, including as live updates arrive or after the base moves.

## Week of Oct 12, 2026

### Projects

- **Project coordinators can start workers wherever your code lives.** A Project coordinator can list your environments and repositories, then start a worker in the environment that holds the code, or directly on a repo using its default setup, even when the Project has no repository of its own. Environments and repos outside the Project need your approval from a card that names them, and approved ones appear in the Project's allowed list, where you can revoke them.
- &#x20;**Project agents ask before using a new machine or environment.** For every team, a Project's agents now ask a person to approve the first time they use a Self-Hosted Machine, pool, or environment. Team admins can turn on [Automatically allow Projects to place their work](https://cursor.com/docs/cloud-agent/settings.md) in the Dashboard under Cloud Agents → Security. Approvals you already granted still apply, and an approval for a repository also covers its GitHub or Origin mirror.

### Agents

- **Messages sent as an agent finishes are answered in the same run.** If you send a message to a Cloud Agent just as it is wrapping up, the agent picks it up as one more step instead of queuing it as a separate follow-up.
- **Start Cloud Agents from a short commit SHA.** You can start a Cloud Agent on a GitHub repository from an abbreviated commit SHA of 7 or more characters, like the ones `git log --oneline` prints, instead of getting a "branch or commit not found" error. Branch and tag names with the same text still take precedence.
- **Agents can update pull request descriptions they didn't write.** When you ask a Cloud Agent to update a GitHub or Cursor-hosted pull request it didn't open, it now adds its content below the existing description instead of refusing, and it can fill in an empty description. Agents in a single-repository environment no longer need the repository named to create or manage pull requests, and completed pull request actions show as finished in the conversation.
- **A clearer agents sidebar on pull request pages.** The agent list in the floating dock on cursor.com pull request pages opens right above the input and shows how many agents are working or need attention. When the agent you have open is idle but agents under it are still working, its header says "Waiting on" those agents. The sidebar shows a Retry notice instead of loading forever, or tells you when Privacy Mode (Legacy) blocks Cloud Agents.
- &#x20;**Teammate follow-ups on agents without a repository follow your team settings.** Teammates can follow up on a colleague's Cloud Agent that runs on a personal environment with no repository, as your team's Team Followups and Allow VM Sharing settings allow. Before, those agents were read-only to teammates. A teammate who opens or follows up on someone else's agent must also have access to every repository the agent was granted.
- &#x20;**Clearer messages when usage limits block a Cloud Agent.** When a usage limit stops a Cloud Agent from starting or taking a follow-up, the error tells you what to do next: turn on on-demand usage, raise your own or your team's on-demand limit, or, on a trial, switch to a Cursor model or Auto. If you switch a follow-up to Auto after a trial limit, the agent continues instead of being blocked again.
- &#x20;**Clearer answers when a team model block turns off computer use.** If your team admin has disabled a model that computer use depends on, the Cloud Agent tells you that computer use is unavailable, which model is blocked and what it's used for, and that an admin can re-enable it in team model settings.
- **Open Settings with a keyboard shortcut.** Press Cmd+, (Ctrl+, on Windows and Linux) on the agents pages to open Settings. The collapsed sidebar no longer pops open when you hover over it; click the Open sidebar button instead. Opening a conversation only collapses the sidebar on windows narrower than 1024px.

### Environments

- **Rename environments and find config-as-code ones on the dashboard.** Rename an environment from its detail page with the pencil button next to its name. Environments defined by a committed environment file show a Config as code badge, and a Config as code switch filters the list to them. When a build fails because the GitHub App can't access a repository, the banner names the affected repositories and links to your GitHub installation settings.
- **Environment builds no longer silently use the wrong `environment.json`.** When an environment's tracked [`environment.json`](https://cursor.com/docs/cloud-agent/setup.md) is missing, empty, or can't be read, the build now fails with an error that names the file and repository, instead of quietly falling back to `.cursor/environment.json` or an older saved config. New environments track the repository's `environment.json` only when you choose that option.
- **Fewer duplicate and overwritten environments.** Creating an environment from the dashboard or promoting a personal environment to your team now always creates a new environment instead of overwriting one with the same name or repositories. If a team environment with that name already exists, you're asked to rename yours first. Agents started on the same set of repositories reuse one environment.
- &#x20;**Environment build cache is encrypted with your customer-managed key.** For Enterprise teams with a [customer-managed key](https://cursor.com/docs/cloud-agent/security.md), the Cloud Agents environment build cache is encrypted with a key your customer-managed key controls. If you revoke access to your key, or you have no key in the build's region, environments build without a cache.

### Self-Hosted Machines

- &#x20;**Teams that require Self-Hosted Machines stay off Cursor-hosted machines.** When a team admin turns on [Require Private Workers for All Cloud Agents](https://cursor.com/docs/cloud-agent/self-hosted/private-workers.md), Cursor no longer builds or snapshots environments for that team or its members, and the Builds tab says builds are turned off. Agents that already ran on Cursor-hosted machines stop accepting follow-ups and ask you to start a new agent on a Self-Hosted Machine.
- **Agents on Self-Hosted Machines handle offline machines better.** When a pool machine running your agent goes offline, the agent waits for that same machine to come back and continues there, and moves to another machine only after that. If you start an agent or send a follow-up to My Machine while it's disconnected, you get a machine-offline message after about 15 seconds instead of waiting for minutes.

### Integrations

- **Jira automation rules and GitHub Enterprise `@cursor` comments launch Cloud Agents correctly.** Jira automation rules start a Cloud Agent with the rule's prompt as its task, including rules with no work item attached. `@cursor` comments on GitHub Enterprise Server repos now work, and run under the team that owns the GitHub app when you belong to it.
- **Azure DevOps repos work as `org/project/repo` shorthands.** You can point a Cloud Agent at an Azure DevOps repository with a three-part shorthand like `my-org/My Project/portal`, for example when switching repos or setting a default repo in Microsoft Teams, instead of pasting the full `dev.azure.com` URL.
- &#x20;**Cloud Agent commits in OpenTelemetry Export.** Enterprise teams using [OpenTelemetry Export](https://cursor.com/docs/enterprise/opentelemetry-export.md) receive a `cursor.cloud_agent.commit` log for each commit a Cloud Agent pushes to a GitHub repository. Each log includes the commit SHA, the repository URL, the number of files changed, and line counts when available, and links back to the agent run.

### MCP

- &#x20;**Cloud Agents follow your team's plugin and MCP allowlist.** When an admin turns on Team list enforcement, Cloud Agents connect only to plugins and MCP servers on the Team list, and the tool restrictions set for each server apply. When enforcement is off, those tool restrictions no longer block other MCP servers.
- **Cloud Agents no longer get stuck on sign-in cards for command-based MCP servers.** Cloud Agents no longer pause on an MCP sign-in card for stdio servers, which run as a command on the agent's machine and have no Cursor sign-in. Before, the run waited until you clicked Skip or the card timed out. Cloud Agents also no longer ask you to sign in to a server that is still loading.

### Fixes

- **Fixes to agent runs.** Stopping an agent while it continues after a stop hook now works, parallel file writes in one step no longer overwrite each other, and agents no longer get duplicate AGENTS.md or CLAUDE.md instructions. Follow-ups sent during a CI-fix turn run as you, and Bugbot's Fix in Web continues the existing pull request instead of opening a new one.
- **Fixes to environment builds and network allowlists.** Environment setups longer than an hour no longer fail partway for teams using PrivateLink. A Cloud Agent whose VM is recreated on a follow-up boots the environment's latest successful build, and changing a team environment's egress settings triggers a rebuild. One malformed network allowlist entry is now skipped instead of breaking or widening the whole policy.
- **Fixes to repository access.** Cloud Agents on GitLab instances that require Git protocol v2 now start, brief GitLab outages are retried, and failed access checks show GitLab's actual response. Tokens or passwords embedded in repository URLs are stripped before they're stored.
- **Fixes to Project coordinators and workers.** Workers that a coordinator starts with a variant of its own model keep the coordinator's context window instead of jumping to 1M. Coordinators with more than 1,000 workers list their newest workers, and renaming a Project before its first turn now sticks.
- **Fixes to Self-Hosted Machines.** Runs that land on a machine that is shutting down start on another machine in the pool, and pool machines left behind by a deleted run reset so the next agent can claim them. Agents recover from a lost machine connection by reconnecting on the next step, and Windows machines resolve skill, plugin, and workspace paths correctly.
- **Fixes to MCP connections.** MCP servers that don't need sign-in no longer have their tools disappear between listings, and servers whose sign-in was revoked or expired show as needing authentication instead of exposing cached tools. A newly added server or tool is no longer reported as missing, and an expired server session reconnects instead of failing the call.
- **Fixes to Gmail and Slack tools.** When Gmail refuses to open a thread for permission reasons, agents read the thread's first message and note that later messages weren't included. Slack tool calls no longer fail when a channel is given as a #name or a pasted channel link.
- **Fixes to code tours.** Code tours for pull requests in tall stacks now generate instead of failing, and a tour that fails mid-generation ends with an error instead of leaving the viewer waiting.
- **Fixes to recording annotations.** Large screen recordings now get chapters, a thumbnail, and trim points instead of being skipped, and annotations are no longer lost when another save happens at the same time.
- **Fixes to the web app.** The agents navigation drawer no longer opens empty at fractional browser widths, and you see all of your pinned agents, not just the first 1,000.
- **Fixes to Slack replies.** Agent replies in Slack keep dollar sequences like `$1`, `$&`, or `$$` exactly as written instead of repeating or dropping parts of the message.

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

## Week of Oct 12, 2026

### Teams and installations

- &#x20;**Bugbot runs under the right team on shared GitHub installations.** When a GitHub installation is shared across Cursor teams, Bugbot reviews on a repository run under the team it was granted to, using that team's settings and plan, instead of the installation owner's or the PR author's. The Bugbot repository list shows an "Enabled by" badge naming the team on repositories another team already runs Bugbot on, and explains why you can't enable them there.
- &#x20;**Manage Bugbot on GitHub installations shared with your team.** If another team in your organization shares its GitHub installation with your team, you can change per-repository Bugbot settings from the dashboard without taking over the installation. The installation details page marks these installations as Shared and names the owning team, which still manages installation-level settings.

### Reviews

- **Local reviews work in Mercurial repositories.** When you [run Bugbot from your agent](https://cursor.com/docs/bugbot.md#run-in-your-agent) or run a security review on local changes, it now reviews Mercurial checkouts as well as git repositories, without running the repository's hooks. If a folder has neither, the review says so and names the path. If your Mercurial client is too old to skip hooks safely, it asks you to upgrade.
- **Rule violations are no longer dropped when a pull request calls them intentional.** Bugbot now keeps a finding that correctly flags a violation of one of your team, project, or manual [rules](https://cursor.com/docs/bugbot.md#rules), even if the pull request description says the change was deliberate. Findings that cite a rule the diff doesn't break are still filtered out.
- **Long local reviews finish with results.** When you [run Bugbot from your agent](https://cursor.com/docs/bugbot.md#run-in-your-agent) and a review runs unusually long, Bugbot stops investigating at a set limit and replies with the bugs it has already verified, instead of running on or ending without an answer.

### Settings and access

- &#x20;**Restrict Access works with pull requests from Cursor agents.** When a Cursor agent opens a pull request, the team's Restrict Access allowlist or blocklist now checks the GitHub account of the person who launched the agent, not the bot. When Restrict Access blocks a review, Bugbot's "couldn't run" comment says which list blocked it and how an admin can fix it, instead of suggesting a seat limit increase.
- **Manual Only holds when your GitLab or Bitbucket account is linked to several Cursor accounts.** Fixed an issue where Bugbot could still review your merge requests and pull requests automatically on GitLab and Bitbucket in that case. If Manual Only is on in any of the linked accounts, Bugbot now waits for you to trigger it.

### Dashboard

- &#x20;**Clearer account list in the Bugbot dashboard.** The coverage table now labels its first column Account, shows the GitHub account name for each installation, and marks personal accounts with a Personal badge. Accounts you manage are listed first, then organizations, then personal accounts. Bugbot's installation pages and MCP tools also open correctly from the Automations and Custom Agents pages.
- &#x20;**Sign in to team MCP servers from the Bugbot dashboard.** When a team [MCP server](https://cursor.com/docs/bugbot.md#mcp-support) in Bugbot's MCP tools settings needs authentication, its status shows a **Needs Auth — Sign in** button that opens the server's sign-in page. Each click gets a fresh sign-in link, so a stale or used link no longer blocks the connection.
- **Open Settings from Bugbot pages with a keyboard shortcut.** Press Cmd+, on macOS or Ctrl+, on Windows and Linux on Bugbot pages to open your Settings, the same shortcut the Cursor desktop app uses. It works on non-Latin keyboard layouts and does nothing while you're typing in a text field.

### Fixes

- **Fixes to review reliability.** Bugbot still posts its review when the Autofix pre-check fails, and skips Autofix for that run. On GitLab, a manual Bugbot command that hits a temporary user lookup failure now gets a reply explaining what happened instead of being dropped. Bugbot also handles its own outdated inline comments again, such as minimizing previous comments.

## 3.24

### Chat and composer

- **Goal, queue, debug, canvas, and browser panels now open from pills above the prompt.** Your conversation goal, queued follow-ups, Debug mode reproduction steps, canvas preview, and local dev server preview each have a pill above the prompt (Goal, Queued, Debug, Canvas, and Open Browser) that opens or minimizes its panel. Each panel opens by itself when there is something new, such as a new goal, your first queued message, or a ready repro step, and closing it keeps the pill.
- **Expand and copy Markdown tables in one click.** Hover a Markdown table in an agent's reply or a Markdown file to show Expand table and Copy table buttons beside it. Expand table opens the table in a full-size view with wrapped columns and working links, and Copy table pastes as a real table into docs and chat apps, or as Markdown into plain text.
- **Download files from chat links.** Right-click a file link in an agent's chat and choose Download File to save a local copy, with \~/Downloads as the default. It also works for files a cloud agent built in its workspace.
- **Mute toggle for video players.** Inline and fullscreen videos in the Agents Window now have a Mute/Unmute button, and each new video starts muted or unmuted the way you left the last one.
- **Editing an earlier message keeps the agent's memory of the turns above it.** Fixed an issue where editing an earlier message in a reopened or synced Agents Window conversation restarted the model from an empty history. The edit now resumes from that turn's state, and if that state can't be found, the edit fails and leaves your transcript intact.
- **Queued messages wait for Debug mode reproduction steps.** When a Debug mode turn ends with reproduction steps, a follow-up you queued no longer sends right away and hides the steps. The Debug pill stays next to the queue until you click Proceed or Mark Fixed, or switch out of Debug mode.
- **Cloud agents can build canvases.** [Canvases](https://cursor.com/docs/agent/tools/canvas.md) a cloud agent creates are saved to the cloud and open as read-only previews in a Canvas tab, including from links in the agent's chat. For cloud agents, Canvas also shows up in the New Tab menu.
- **Pick the right element in Design Mode with the arrow keys.** In [Design Mode](https://cursor.com/docs/agent/design-mode.md), you can now select a container even when a small child element sits on top: press ↑ to move the hover highlight to the parent element and ↓ to move back down, then click to select it.

### Cloud agents

- **Fixes to cloud agent connections.** Cloud agents reconnect on their own after your computer wakes from sleep instead of failing, and conversations and the agent list keep updating through network drops, proxy errors, and server deploys. A cloud agent whose machine went away reconnects its workspace when you send a new message.
- **Move a cloud agent into a local worktree.** If a cloud agent works on a single repository you also have cloned locally, the environment picker in the status bar now lets you continue the agent in one of that repo's existing Cursor [worktrees](https://cursor.com/docs/configuration/worktrees.md) or in a new one, without touching your main checkout.

### Navigation and layout

- **Closing and reopening tabs takes you back where you were.** Cmd+W on a tab now returns you to the tab you were on before, even across split panes, and closing a split tile or pane puts focus back on the one you last used instead of the first or an empty one. Cmd+Shift+T reopens whatever you closed most recently, chat or app tab, including Agent, Environment, Changes, Desktop, Machine, and voice call transcript tabs.
- **Chat tabs that fit their titles, with agent details on hover.** Chat tabs in the Agents Window now size to their titles and the tab strip scrolls when they don't fit. Hovering a chat tab, a standalone chat's title, or a tile header shows the same agent card as the sidebar, and moving between tabs moves the card without waiting again. Standalone chats and tiles now use the same tab strip as other panes, so you can double-click a tab to rename it, and with the sidebar hidden, holding Cmd (Ctrl on Windows and Linux) shows each agent's shortcut on its tab.
- **Drag tiles between splits.** In a split, drag a tile's main chat tab onto another tile to move the tile there. A chat hidden from the sidebar also keeps its own name in its tile header.
- **Subagents and side chats open as tabs on their parent agent.** Opening a subagent or side chat from a link, the command palette, or another agent now opens its parent agent with the subagent or side chat as a tab beside it, so you keep the parent conversation in view. A + button on the agent's tab strip opens its subagents as tabs. Back goes to where you were before the subagent opened, not to the parent agent. Subagents of automation runs still open on their own.
- **Reach every side chat from the side rail and new-tab menu.** The side rail now lists your five most recently updated side chats, with the rest behind an "N more" menu, and when the rail is collapsed to icons a single Side chats button opens all of them. The new-tab menu's Side Chats and Plans submenus now list every entry instead of stopping at 10, and add a search box once there are more than 10.
- **Fixes to unread agents in the menu bar and Dock.** Agents you mark as unread, or that finish while you're viewing another agent, now show in the menu bar and Dock menus without a restart. Unread agents take the first spots in the menu, with an "N more unread" entry when they don't all fit, and the badge counts only what the menu shows. A Project's row now lights up when one of its threads is unread.
- **Browser tabs reload when your dev server comes back up.** A [browser](https://cursor.com/docs/agent/tools/browser.md) tab pointed at a local port that wasn't serving now reloads by itself when a terminal command or an agent's background shell starts a dev server on that port, so you don't have to refresh it by hand. You can also reload a tab with the new Reload Browser Tab command in the Command Palette or with Cmd/Ctrl+R.
- **File links in agent replies open faster.** Hovering or focusing a file link in an agent's reply starts loading the file tab in the background, so the file is ready when you click.

### Projects and workspaces

- **Clone a repo to run it on your machine.** If a repository isn't cloned on your machine yet, its local row in the Run on menu now says "Not cloned". Pick that row to clone the repo. A notification shows progress while it clones.
- **Add local agents to cloud Projects.** Drag a local agent onto a cloud Project in the sidebar, or use Add to Project, to make it a worker in that [Project](https://cursor.com/docs/agent/projects.md) without losing its conversation. The agent keeps running on your computer through Remote Control, so Remote Control needs to be on for that workspace.
- **See what a Project's coordinator is working on.** A [Project](https://cursor.com/docs/agent/projects.md)'s coordinator now reports a short status for its current step while it works, such as the subtask it is handing out or reviewing. The status shows live in the Project chat and in the fullscreen editor's agent overlay.
- **Easier-to-scan messages in Projects.** In a [Project](https://cursor.com/docs/agent/projects.md)'s main conversation, your messages now show as flat, filled bubbles with no border, so they stand apart from the agent's replies. The fill follows your theme, and Tech Lead conversations use the same style.

### Files, changes, and pull requests

- **Clearer pull request stacks and PR tab actions.** In the PRs tray and the PR tab's stack navigator, closed PRs in a stack now fold into an "N closed" row, and a stack stays grouped even when only some of its PRs belong to the Project, with rows like "1 PR not in this project" marking the gaps. Merging an Origin PR that lands its open downstack now reads "Merge N PRs" and notes that it lands as one commit. The PR tab menu adds View on Web, follow-up pills such as Fix CI name the pull request they act on, and Fix with Agent on a Bugbot finding no longer clears your draft or resends the Bugbot report with your next message.
- **Open in Browser works for HTML files on remote and cloud machines.** Right-click an HTML file in the file tree on a Remote SSH machine, cloud agent, or self-hosted worker and choose Open in Browser to preview a local copy. If it can't open, a message explains why, for example when the remote machine isn't connected or the file is too large.

### Customization and settings

- **Adjustable chat width.** A new Chat Width slider in Settings > Appearance > Agent Conversations sets how wide agent conversations can grow, from Narrow to Wide (600 to 1600px). Widen it to give tables and code more room, or narrow it for easier reading.
- **Fixed the translucent window tint on macOS when switching themes.** On macOS, the Agents Window's translucent background tint now updates every time you switch between light and dark themes. Before, it could keep the previous theme's tint.

### Plans and billing

- &#x20;**Clearer credit prompts and automatic top-up in the Buy Credits dialog.** When a model needs credits to run, the usage notice now explains why and puts Buy Credits first if there's no plan to upgrade to. The Buy Credits dialog also has a Set Up row for automatic top-up, so you can save a top-up rule or turn it off without leaving the dialog. This applies to plans with a weekly usage allowance.
- &#x20;**Fixes to the Enterprise usage chart.** On Enterprise plans, the Cumulative Spend chart in Settings > Plan & Usage now stays readable at large totals, with short axis labels like $1.5M, and a spend limit far above current spend shows in the legend instead of squashing the plot. Cached usage and chart data appear right away instead of a loading state, and an error or stale-data banner from a previous team or user no longer shows for the current one.

### Fixes

- **Fixes to Computer Use on macOS.** The Enable Computer Use permissions window no longer keeps reopening while permissions are missing. Computer Use also no longer gets stuck saying another Cursor window is installing it after a window quit or crashed mid-install.
- **Fixes to trays and pills above the follow-up input.** Opening trays, pills, or prompts above the input no longer shifts the conversation, and interrupted tray animations no longer jump. Approval, error, and branch mismatch prompts can no longer be dismissed by accident with Escape, the environment setup popout keeps your edits when another tray covers it, and pills stay visible and show as selected only while their tray is open. Answering an agent's questions in the fullscreen editor no longer crashes the view.
- **Fixes to switching between agents.** Switching back to a recent agent no longer reloads the chat, loses your scroll position, or flashes while it loads, and a hidden chat no longer captures your typing. A chat pop-out for a Project worker now stays open, and closes when its agent is archived or deleted.
- **Fixes to the sidebar and composer.** Typing while an editor panel is fullscreen now goes to the prompt, the New Agent button no longer disappears from grouped sidebars, and long agent titles fade out instead of hiding the peer count. If starting a cloud agent from a sidebar draft fails, your prompt comes back instead of being lost. Stopping a new agent's first message keeps the browser panel and its tabs.
- **Fixes to file search, file tabs, and the Changes panel.** File search and Quick Open stay responsive while you type, and pressing Enter opens the top result for what you actually typed. File tabs open faster on remote workspaces and refresh when a cloud agent edits the file. The Changes panel updates sooner after outside git commands, and a refresh no longer undoes a stage or unstage.
- **Fixes for errors when no editor is open.** The Agents Window no longer throws errors when you open a file link, switch into the agent layout, or have unsaved files change while no editor is open. Changing the sidebar position and viewing a transcript for a conversation that is no longer loaded also no longer fail.
- **Fixes to cloud agent status and history.** Cloud agents no longer get stuck on an outdated status, flicker back to running, or flip back to unread when a stale update arrives, and loading earlier messages reliably loads the previous page. Re-recorded videos and retaken screenshots show the new content, Project worker headers update right away, and only the coordinator's turn plays the finished chime. A cloud agent started on a picked self-hosted machine keeps that machine after refreshes and forks, and retrying a failed start from a saved environment keeps its repo configuration.
- **Fixes to agent transcript scrolling and loading.** Scrolling long agent transcripts no longer makes messages jump or shows a blank band at the top. Opened agents appear sooner and show mid-turn messages right away. The transcript no longer shifts when a turn finishes.
- **Fixes to the @ mention menu.** The @ menu no longer stays stuck loading when one source hangs, and the Branch row and past chats appear right away. For cloud agents, file mentions load as soon as you focus the input, typing stays responsive in large repos, and the slash command menu no longer goes empty while the cloud workspace starts. Editing a sent message now lists the same past chats as the follow-up input.
- **Fixes to agent chats.** Charts in agent replies no longer clip tooltips or cut off long labels, Windows file path links open the file, and Copy Link on a PR chip no longer opens the PR. Cancelling a commit in Review Changes no longer goes on to open a pull request, and the new-agent model picker keeps the model and reasoning effort you just sent.
- **Fixes to Design Mode in the browser.** The [Design Mode](https://cursor.com/docs/agent/design-mode.md) pill no longer appears on a local browser tab when nothing is serving it or when its dev server runs in another workspace. Elements you pick stay on the right element after a hot reload.
- **Fixes to voice call cards.** A voice call card for a call on another device no longer briefly shows an inflated duration when that call goes silent. It now shows as ended at the time it was last heard.
- **Fixes to plugin skills, chat sync, the compact composer, and the sidebar.** Cloud plugin skills that failed to load now come back in the `/` and `+` menus when you reopen the menu or return to the window, and chats started or steered in another window no longer miss later turns. In a narrow compact composer, long model names no longer crowd out the text field, and the sidebar no longer lists the same folder twice when its path differs only in letter case.

## 3.24

### Agent and chat

- **Auto-review stops risky deletes for your approval.** [Auto-review](https://cursor.com/docs/agent/security/run-modes.md) now asks before running a recursive, force, wildcard, or mirror delete whose target could resolve differently than written, such as an unquoted path with spaces, an unset variable, or a relative path after a directory change that can fail. Commands that match one of your block instructions now always show the approval card. With Run Everything on, agents now run without the sandbox unless your permissions.json restricts that mode.
- **Copied tables keep their formatting in docs and chat apps.** Copy Table in the right-click menu of an agent response table now pastes as a real table in rich editors like Google Docs, Notion, and Slack. Plain-text destinations still get Markdown.
- **Smoother scrolling while an agent streams.** When the agent chat follows a streaming reply, it now glides smoothly to new output instead of moving in uneven steps.
- **Agent Review fixes and better Fix in Cursor prompts.** Fix in Cursor from a Bugbot report now drafts a prompt that lists the affected files and line ranges, even when code selections can't be attached. Agent Review tabs stay open when you open or close the chat Review tab or revert a plan checkpoint, and Agent Review shows again for users who had turned on the removed Beta "Hide Agent Review" setting.

### Cloud agents

- **Cloud Agent links from the editor open in the Agents Window.** Clicking an "Open in Cursor" link for a Cloud Agent while an editor window has focus now opens that agent in the Agents Window. Previously the editor tried to match the agent's repository and could show an "Incorrect Repository" dialog instead of opening the agent.
- **Cloud agents recognize out-of-memory kills.** When a shell command in a cloud agent started from Cursor is killed because the machine ran out of memory, the agent is now told so, along with the memory limit, so it can explain the failure and retry using less memory instead of guessing.

### MCP

- **More reliable MCP server sign-in.** MCP servers whose OAuth apps reject redirect URLs that point to your own computer can now sign in through a Cursor-hosted callback page. Sign-in also completes when another Cursor window or app holds the local callback port, and no longer fails on large browser request headers.

### Customization and settings

- **Easier hook correlation for shell and MCP calls.** Shell and MCP execution [hooks](https://cursor.com/docs/hooks.md) now receive a `tool_use_id` that matches the `preToolUse` event, so one script can follow a tool call from start to finish. Every hook now gets the `.jsonl` transcript in `transcript_path` when one exists, and `CURSOR_TRANSCRIPT_PATH` always matches it.
- **Claude Opus 5.5 and Sonnet 5.5 on AWS Bedrock.** If you [connect your own AWS Bedrock account](https://cursor.com/docs/customizing/aws-bedrock.md), you can now pick Claude Opus 5.5 and Claude Sonnet 5.5 from the Bedrock model list in Cursor Settings.

### Privacy and security

- &#x20;**Admins can restrict Agent to approved remote workspaces.** A new managed policy, AgentRemoteWorkspaceAuthorities, turns off Agent in local Cursor windows and allows it only in remote workspaces. You can optionally limit it to remote authorities that match a comma-separated list of patterns, with `*` wildcards. If a user starts Agent in a local window or an unapproved remote workspace, they see a message that their administrator has disabled it.

### Git

- **Clear error when Origin rejects a push for a file over 100 MB.** When Source Control pushes to an Origin repository and the push is rejected because a file exceeds the 100 MB limit, the error now names the oversized file or files instead of telling you to pull first. It also explains how to fix it: track the file with Git LFS and remove it from every commit in the push.

### Fixes

- &#x20;**Okta FastPass sign-in works in the built-in browser again.** Signing in with Okta FastPass in the built-in browser no longer stops at "Okta FastPass requires network permission". The browser now grants the local network permission Okta Verify needs.
- **Fixes to agent tools.** Agent edits to very large files no longer cut off the rest of the file, loose one-line replacements no longer splice the wrong text, and reads right after an edit in the same step return the updated file. The agent no longer hangs on unknown tool calls, and background shells survive idle chats. Also fixes a shell injection risk from crafted branch names when the agent gathers git diffs or looks up a branch's pull request.
- **Fixes to long-conversation summarization.** Agent chats that hit the context limit now compact and continue instead of failing repeatedly at the limit, and summaries no longer drop facts from early in the conversation. The agent also keeps your latest request word for word after summarization, and near the limit it reuses a summary started in the previous turn instead of starting over every turn.
- **Fixes to MCP sign-in and settings.** Connecting a Microsoft MCP server now shows the account picker, and edits to a project MCP server config show up in settings right away.
- **Fixes to remote connections and file watching.** Connecting to an SSH, container, or tunnel remote no longer hangs when the connection drops during the handshake, and remote windows opened without a folder finish connecting. The explorer and editors keep picking up remote file changes after a reconnect, and absolute watcher exclude paths are now honored. The agent's branch display shows the new branch on the first refresh after a checkout.
- **Fixes to the built-in browser, settings, storage, and crash handling.** New browser tabs no longer flash white, switching tabs no longer shows the previous page, and the Cursor Settings sidebar stays pinned with its bottom items reachable. Opening Cursor while a previous instance is still closing no longer discards local state, and sandboxed agent commands on Linux with AppArmor 4 can reach the network again. Repeated out-of-memory crashes no longer fill the disk with debugging data.
- **Fixes to Tab, Customize, and the Debug Console.** Multi-line Tab suggestions now display correctly in files with Windows (CRLF) line endings. The "Use your skills with Cloud Agents" banner in Customize renders with its proper styling, and the Debug Console no longer throws an error when styles change before a debug session has been focused.
- **macOS no longer asks for Music or Photos access.** On macOS, opening a folder that contains your Music, Movies, or Pictures folders no longer triggers Apple Music, Photos, or other access prompts. File watching and file search, including the @ menu, now skip those folders.
- &#x20;**Fixed Always Run on terminal approvals when your allowlist is managed.** When a team policy or [permissions.json](https://cursor.com/docs/reference/permissions.md) sets your terminal allowlist, the agent's terminal approval card no longer offers Always Run. Before, choosing it had no effect, so the same command kept asking for approval.
- **Smaller local state files.** Cursor now reclaims unused space in its local state databases when you quit, so they shrink over time instead of only growing. Cursor limits how long the cleanup runs, so quitting stays fast.

## v2026.10.08

### Auto-review

- **Auto-review is stricter about risky deletes.** Auto-review now asks for approval before recursive, force, wildcard, or mirror deletes whose target could resolve differently than written, such as an unset variable or a stray space in a path. See [Configuring Auto-review](https://cursor.com/docs/agent/security/run-modes.md#configuring-auto-review).

### Models

- **Claude Opus 5.5 and Sonnet 5.5 on Bedrock.** If you set up [AWS Bedrock](https://cursor.com/docs/customizing/aws-bedrock.md) with `agent bedrock`, you can now pick Claude Opus 5.5 and Sonnet 5.5 from the bring-your-own-key model list.

### Skills

- **`/skills` flags skills that break the Agent Skills limits.** Skills that load but exceed the spec's limits now show a yellow warning count in `/skills`, and selecting one lists what to fix under it. Warnings cover a name over 64 characters or not in lowercase-hyphen form, a frontmatter `name` that doesn't match the folder, a description over 1,024 characters, and a body over about 5,000 tokens. See the [SKILL.md format](https://cursor.com/docs/skills.md#skillmd-file-format).

### ACP

- **ACP clients now get wakeups from watched background shells.** In [ACP](https://cursor.com/docs/cli/acp.md) mode, when the agent starts a background shell that watches for output, the prompt now stays open and the agent wakes up and responds whenever the output matches. Previously the agent said it would be notified, but the wakeup never arrived. While the prompt waits, the client shows an in-progress `Watching: <reason>` tool call. Cancelling the prompt or sending a new one ends the wait without stopping the shell.
- **ACP sessions no longer keep running under your old team after you switch teams.** If you switch teams while the [ACP](https://cursor.com/docs/cli/acp.md) server is running, `session/new`, `session/load`, and `session/prompt` requests now fail with `Your team has switched to <team>. Create a new session to continue.` and the server exits. Before, it kept working under the team it started with.

### Self-hosted workers

- **Any-repo pool agents now work inside the repo they claimed.** On a worker started with [`--clone-git-repos`](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#any-repo-pools), an agent's tools, shells, rules, skills, and subagents now run in the checkout cloned or reused for its claim, then go back to the worker directory when the claim ends. The worker also clones fresh instead of reusing a checkout that has untracked rules, skills, or `AGENTS.md` files an earlier agent may have left there, and the worker log lists the files that blocked reuse.
- **Self-hosted workers stop when they register too many repositories.** When Cursor refuses an `agent worker` because it registers more repositories than a worker allows, the worker now exits with a message giving the count, the limit, and how many repository folders to remove before starting it again, instead of reconnecting endlessly.
- &#x20;**Verify who a claimed run is for before you provision it.** `agent worker controller --identity-audience <aud>` asks each claim for a short-lived signed [identity token](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#identity-tokens) bound to your audience and a fresh nonce. Your `--spawn` hook receives `CURSOR_IDENTITY_TOKEN`, `CURSOR_IDENTITY_TOKEN_EXPIRES_AT`, and `CURSOR_IDENTITY_NONCE`, so the hook can check the agent and its owner before it creates a machine or hands out credentials. If a claim comes back without a token, the controller releases the claim and exits. The flag works in claim mode only and can't be combined with `--warm-idle`.

### Cloud Agents

- **`agent env deploy` accepts comments and trailing commas.** Environment files passed to `agent env deploy` can now include comments and trailing commas, so you can annotate your Cloud Agent setup in place. Invalid files fail with a syntax error that points to where parsing stopped.

### Fixes

- **MCP OAuth no longer sends unfilled client ID placeholders.** When an MCP server's OAuth config still has an unresolved `${VAR}` client ID, the CLI now treats the client ID as unset. It no longer sends the literal placeholder to the authorization server, so login no longer fails with a confusing client error.
- **Fixes to agent tools.** The agent no longer hangs when the model calls an unknown tool, and sessions no longer end on out-of-range Shell or Grep arguments. Edits to large files fail safely instead of truncating them, loose one-line replacements no longer splice the wrong text, and a Read right after an edit or a file-creating shell command returns the new content. Glob now finds empty and binary files and skips `.git`, and generated images are saved with the right file extension.
- **Fixes to MCP tools.** MCP sign-in no longer fails when another Cursor app is already using the login callback port. The agent now refreshes a server's tool list when a tool seems to be missing. When a tool doesn't exist, the error now lists the tools the agent can call.
- **Fixes to self-hosted workers.** Workers no longer drop their connection while uploading large messages on slow links, report themselves ready before the server accepts them, or delete git credentials another worker pushed on the same machine. Existing checkouts are no longer refused because of system or global git config, and stopping a worker now prints the reason. Agent stores you removed stay removed after a restart, and a store that hangs while closing reopens on the next claim.
- **Fixes to long sessions and summarization.** Sessions that hit the context limit now summarize and continue instead of getting stuck, and your latest request is kept word for word after summarization. Debug mode no longer fails a turn after the conversation is summarized, and images attached to a message queued during an interrupted turn are now sent on the next turn.
- **Agent store sync keeps working after you switch teams.** Local agent stores no longer fail to sync after you change your active team, as long as you are still a member of the team that owns the store.

## October 6, 2026 release

### Pull requests

- **See what a pull request still needs to merge.** `origin pr requirements` lists required gates and their status at head, needed approvals, human-only paths, the Code Review Gate, and blockers in the stack. Add `--json` for scripts.
- **Safer merges and merge-when-ready status.** `origin pr merge --expect-head <number>=<sha>` refuses to merge if a listed pull request has moved, and `--auto --downstack` turns on merge-when-ready for every open pull request below this one. `origin pr view`, `status`, and `requirements` show a `Merge-when-ready` line, and `--json mergeWhenReady` returns it.
- **Manage reviewers and labels from the CLI.** `origin pr reviewer list`, `request`, and `remove` manage review requests for users, teams (`org/team`), and service accounts. `origin pr create` takes `--label` and `--reviewer`, and checks both before creating the pull request.
- **Wait on more than CI, and filter checks.** `origin pr watch --until` can wait for `merged`, `head:<sha>`, or `comment:<regex>`, and `--json` returns one result object. `origin pr checks --name <pattern>` limits output and the exit code to matching checks, and the output names the commit the checks ran on.
- **Edit and delete comments, and view one review thread.** `origin pr comment edit` and `origin pr comment delete` change or remove a comment you wrote, and `--edit-last` or `--delete-last` act on your newest one. `origin pr thread view <thread-id>` prints a single review thread, and comment JSON now includes a `url`.
- **Limit `origin pr diff` to specific paths.** List files, directories, or globs after `--`, as in `origin pr diff 123 -- src/ '*.md'`. In pathspecs and `--exclude`, `**` now matches any depth, including the top level.
- **See a pull request's cloud agents.** `origin pr view <number> --agents` lists the cloud agents attached to a pull request, and `--json agents` returns them for scripts.
- **More GitHub search syntax in `origin pr search`.** Negated qualifiers such as `-label:bug`, `has:` qualifiers, `OR` between scopes, and `mentions:` now work. `origin pr search --help` lists every supported qualifier.

### Stacks

- **Server-side restacks.** `origin stack restack --server` has Origin rebase your stack and move its branches in one atomic step, so your clone force-pushes nothing. Add `--dry-run` to preview first.

### Scripting

- **More `gh` JSON fields, and `--json help`.** `origin pr view` and `origin pr list` accept more `gh` field names, such as `body`, `state`, `headRefName`, and `isDraft`. Pass `--json help` to `origin pr view` or `origin pr list` to list the fields they accept.
- **Set a default repository with `ORIGIN_REPO`.** Commands that take `-R, --repo` fall back to the `ORIGIN_REPO` environment variable, then your clone's `origin` remote.
- **Find the Origin copy of a GitHub repository.** `origin repo from-github owner/repo` shows the Origin repository that mirrors a github.com repository, with its clone URL and source of truth, using your `gh` login.

### Reliability

- **Requests no longer hang.** Origin requests time out after 60 seconds by default; set `ORIGIN_TIMEOUT_MS` to change it, or `0` for no limit. `origin pr merge --match-head-commit <sha>` refuses the merge if the head has moved, and common server refusals print a suggested fix.
- **Shorter, clearer errors.** A mistyped command prints the error and a pointer to `--help` instead of the full help text. In a cloud agent VM, `origin api` stops with guidance instead of failing with a bare HTTP 401.
- **`origin auth login` shows who you signed in as.** After a successful login, including with `--api-key`, it prints the email of the account you signed in to.

### Fixes

- **Fixed stack navigation and restacking.** `origin stack up`, `down`, `top`, and `bottom` now work in single-branch and shallow clones when the target branch exists only on the remote. After a parent squash-lands, `origin stack restack` no longer replays trunk commits a child had merged in.
- **Fixed `--remote` handling.** Commands that take `--remote` now fail clearly when it is repeated or malformed, and a remote name starting with `-` is no longer read by git as an option.
- **Fixed pull request diffs and repo arguments.** `origin pr diff` shows real file modes and applies cleanly with `git apply`. Repo arguments ending in `.git` or `/` resolve correctly, and `origin pr list --mine` gives working steps in token sessions.

## Week of Oct 5, 2026

### Web

- **More GitHub-style pull request search.** Pull request search supports `has:label` and `has:assignee`. Searching `review-requested:<user>` or `review-involves:<user>` also matches review requests sent to that person's teams that you can see.
- **Merging no longer lands a pull request on another pull request's branch by accident.** If a pull request targets the head branch of another open pull request it isn't stacked on, or of one closed without merging, merging is blocked with a message explaining where it would land. You can merge the parent first, retarget, reopen and stack it, or use Merge anyway on the pull request page.
- **Stacked pull request merge blockers say what to do.** When a stacked pull request can't merge, the blocker tells you how to fix it, for example by naming the pull request to restack from, or the default branch to retarget onto when the base branch was deleted. A pull request with its own merge conflicts is no longer shown as only waiting on a conflict lower in the stack.
- **Undo a conflict resolution from the pull request timeline.** When a conflict resolution is applied to a pull request, the Activity timeline shows it with the commit it created, and the most recent one has an Undo button that restores the previous head. The timeline also records who undid it and which commit was restored. For stacked pull requests, the button's tooltip shows how many pull requests in the stack the undo affects.
- **See and load every file on very large pull requests.** When a pull request has more files than the Files view loads at once, the list shows how many files remain, counted by top-level folder and by added, deleted, modified, or renamed. On pull requests with more than 50,000 changed files, Load the next 50,000 files continues the list from where it stopped.
- **More accurate review filters in inbox sections.** In inbox section filters, "Has 1 or more requested reviewers" counts only review requests nobody has answered yet, and "Has an active review" counts only open feedback from someone other than the author, ignoring dismissed reviews. A pull request requested from your team stops waiting on you once another team member reviews it, as on GitHub.
- **Custom code tours can cover up to 500 files.** When you pick files for a custom code tour, you can select up to 500 of them instead of 100, and Generate no longer refuses a selection because the file paths are too long.
- **Link pull requests with `#` in comments.** Typing `#` in a pull request comment suggests the repository's recent pull requests, so you can link to one without leaving the page. Before, the menu opened empty.
- **Filter a repository's commit history by author.** The commits page has an author picker next to the branch selector. Choose a contributor or type an email address to list only that person's commits on the branch, and share the filtered view by its URL.
- **Simpler personal Slack notification settings.** In [Notifications settings](https://cursor.com/docs/origin/settings.md#notifications), each personal Slack notification switch saves as soon as you toggle it and shows an error if the save fails, and you can connect Slack without leaving the page. Slack pull request cards have a Manage notifications menu, and review reminder digests link straight to your notification settings.
- &#x20;**The audit log records repository visibility changes.** When someone makes an Origin repository public, internal, or private, your team's audit log records who changed it, the old and new visibility, and when, including when an agent's draft repository is published.
- **Clearer push errors and more reliable large pushes.** When a push is rejected for a file over 100 MB, Git tells you how to fix it: track the file with Git LFS, and remove it from every commit in the push with `git rm --cached` or `git filter-repo`. Large pushes, including `git push --quiet`, no longer time out while Origin processes them, and pushes rejected by push rules show a message for each rejected ref instead of dropping the connection.
- **More control over merge queue throughput.** Repository merge queue settings have a separate Maximum concurrent validations field alongside Maximum speculation depth, and both accept values up to 1000. Speculation depth now counts the pull request at the front of the queue, so a depth of 1 tests one pull request at a time. New merge queues default to a depth of 5 and 5 concurrent validations.
- **The merge queue no longer races your edits while it lands a pull request.** Closing, moving to draft, retargeting, or removing a pull request from the merge queue while the queue is finishing a land attempt is refused instead of conflicting with the land. The error names the branch the queue is landing into and tells you what to do once the attempt completes.
- &#x20;**The merge queue explains when a ruleset blocks it.** If a repository ruleset stops the merge queue from writing its branches or refs, the affected pull requests are removed from the queue instead of left stuck. The Removed from merge queue row in the pull request timeline names the ruleset and tells you to add an exclusion for the queue's refs or adjust the rule, then re-enqueue.
- &#x20;**Origin CI and the merge queue show up by name.** Checks from Origin CI appear as the Origin CI app, and merge queue landings name Origin Merge Queue as the pusher in push webhooks and audit logs, instead of an unnamed account or an empty pusher. Commits written by Origin apps are authored under the app's display name without a \[bot] suffix.
- **Run Origin CI jobs from a Cloud Agent environment.** Set `agentEnvironment` on a job, a package, or as the workspace default in `origin.ci.ts`, and the job boots from that environment's latest successful build instead of a container image, with the same tools and dependencies your Cloud Agents use. The environment must belong to the same repository, can't be combined with `image`, and runs on Linux only.
- **More control over Origin CI jobs.** In `origin.ci.ts`, jobs can set `platform.disk` (for example `"32Gi"`) to reserve their own disk size, and a job-level `workingDirectory` applies to every step that doesn't set its own. You can also put jobs in a `group` and list that group in another job's `needs` to wait for all of them.
- **Origin CI config changes.** A package's `origin.ci.ts` can set `on` so it runs only on the events it lists, and a package without `on` follows the nearest parent workspace that lists it. You can reuse the same object in several places in a config, and a job-level `when` fails with an error telling you to leave conditional jobs out of `jobs`. Origin CI reads only `origin.ci.ts`: configs named `origin.ci`, imports of `.ci` files, and the package `extraPaths` field are no longer supported.
- **Origin CI checks open their job page.** Clicking an Origin CI check on a pull request opens that job's page, or the run page for the overall check, instead of a pane with a log tail. The job page links to the job's `origin.ci.ts` file at the commit the run tested and shows how long the code fetch took.
- **Fixes to the review inbox.** The review inbox no longer jumps around while section counts load. Merged or closed pull requests stop showing up again in their old section, and agent runs on them no longer appear under Needs you. Inbox search picks up a merged pull request's corrected target branch within moments instead of up to an hour later.
- **Fixes to diffs.** Files that start with a byte order mark now show their first line correctly in pull request diffs.
- **Fixes to conflict checks.** While conflicts are still being checked, the merge box shows "Checking for conflicts…" and holds the merge instead of claiming the branch is clean.
- **Fixes to Origin CI runs.** Pull request checks no longer fail when the branch has a merge conflict or shares no history with its base, or when an unrelated `origin.ci.ts` fails to evaluate. Path filters apply on a branch's first push and on force pushes, and steps that call `node` on the default image find it.
- **Fixes to codebase pages and repositories.** Load more in file and commit history keeps loading until new entries appear. Label names and descriptions are counted in characters, so emoji no longer hit the length limit early. Namespace names that collide with codebase routes, such as settings or apps, can no longer be claimed, and Public repositories no longer also show a Shared badge.

### API

- **More ways to find pull requests and automate reviews through the Origin API.** You can filter pull request lists to those carrying every label you name, and sort pull request search results by creation, updates, or relevance in either direction. Team API keys can submit pull request reviews in the repositories they're scoped to. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).
- &#x20;**Member emails and GitHub details in the Origin API require their own scopes.** Origin API responses include actor emails only when the caller has the repository members read scope, and filtering pull requests by author email without it returns a permission error. Team reviewer rosters need the reviewers read scope, and GitHub IDs and mirror details need the mirror read scope. If your app relies on these fields, request the scopes and have an admin approve them; see the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).
- **Origin MCP tools accept more argument styles and link to comments.** Origin MCP tools accept GitHub-style argument names such as `owner`, `repo`, and `pull_number`, a repository given as `owner/name`, and enum values in any case, instead of rejecting the call. The `pull_request_read` tool's comments and threads views include a `url` that opens that comment or thread on the pull request page.
- **Fixes to Origin API responses.** API reads and webhooks no longer fail when an actor's account was deleted, and pull requests, reviews, comments, and reactions show their real author, including service accounts. Paging through change lists, change search results, and comparison files no longer skips or repeats items. See the [Origin API changelog](https://cursor.com/docs/api/origin/changelog.md).

## Week of Oct 5, 2026

### Projects

- **Agents can message and read agents you @-mention.** When you @-mention another agent to a [Project](https://cursor.com/docs/agent/projects.md) coordinator, the coordinator can read that agent's transcript and send it messages. It can also message its own parent coordinator, and the agent that receives a message can reply directly. Access follows yours: the coordinator reaches only agents you mention and can still open.

### Agents

- **Subagent progress shows up live in the parent agent.** When a Cloud Agent hands work to a [subagent](https://cursor.com/docs/subagents.md), the subagent's tool calls and messages now stream in under the parent's task as they happen, instead of appearing only after the subagent finishes.
- **Agent links in summaries now open the right page.** When a cloud agent's summary links to another agent, the link in Slack, GitHub, GitLab, and Bitbucket now opens that agent's page on cursor.com instead of breaking. On the web project board, agent links in coordinator files now open the linked agent, including its Changes tab when the link points there.

### Environments

- **Comments and trailing commas in `environment.json` work everywhere.** Cloud Agents now fully support `//` and block comments and trailing commas in [`.cursor/environment.json`](https://cursor.com/docs/cloud-agent/setup.md), wherever the file is read. Repos with a commented environment file no longer get the "set up your environment" prompt, and their snapshot and network settings now apply instead of being silently ignored.

### MCP

- **Cloud Agents handle MCP rate limits without retry loops.** When an MCP server rate-limits a tool, the agent pauses that tool for as long as the server asks, keeps using the server's other tools, and is told when it can retry. Repeated Slack rate limits now cap the wait at about a minute.

### Self-Hosted Machines

- **Project workers on a named Self-Hosted Machine use that machine's repository.** When a Project coordinator starts a worker on one specific Self-Hosted Machine, the worker now works in the repository or folder registered on that machine instead of the Project's repository. Coordinators without a repository of their own can now place workers on a named machine too. Targeting a pool instead of one machine returns an error asking you to name a machine.

### Slack

- &#x20;**Choose which team your Slack agents run under.** If you belong to more than one paid team, you can now pick the Cursor team that agents you start from Slack run and bill under. Choose it when you link Slack, or change it later with the [Team for Slack agents](https://cursor.com/docs/integrations/slack.md#team-for-slack-agents) setting in Cloud Agents settings. Follow-ups in a Slack thread keep running under the agent's original team, and a team pinned by your Slack workspace takes precedence.
- **Slack previews for agent artifact links.** Links to a cloud agent's artifacts, including public artifact shares, now unfurl in Slack with the file name and type, plus the length for videos. Previews only appear when the person who shared the link has access to the artifact, and are skipped in channels shared outside your workspace.

### Fixes

- **Fixes to agent runs and follow-ups.** A message sent after pressing Stop now runs instead of staying queued, and answered questions stay answered after a reload. A run no longer shows a PR from another branch as its PR link.
- **Fixes to repository access and tokens.** Cloud Agents refresh GitHub tokens during long runs instead of hitting expired tokens mid-run. Repository access errors at start now name the specific repository that is empty, denied, or needs connecting.
- **Fixes to the Cloud Agents web app.** Keys like Ctrl+K and Ctrl+F in the agent terminal now go to the shell instead of triggering page shortcuts. The Connect GitHub card names the repository an agent needs access to.
- **Fixes to MCP tool calls.** MCP tool calls recover after a server restart instead of failing, and invalid-argument errors now show the specific reason. Google Calendar time-range searches return only events in that range, and Gmail searches of Spam and of very recent mail no longer come back empty.
- **Fixes to Self-Hosted Machines.** Agents on any-repo pools no longer pick up untracked rules or instructions left in a checkout by an earlier run. When no worker matches your labels, the error now lists the requested labels.
- **Fixes to Slack launches.** Changing or resetting your default model and settings from Slack now works for accounts linked under a migrated Slack workspace. When an agent started from Slack fails, the ⏳ reaction is now replaced by ❌ instead of staying next to it.
- &#x20;**Fixes to Remote Control.** When [Remote Control](https://cursor.com/docs/cloud-agent/mobile.md#remote-control) is turned off, your phone now shows it as disabled instead of a generic unavailable error. Members of enterprise teams that aren't linked to an organization can no longer turn on Remote Control until an organization admin allows it.

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

## Week of Oct 5, 2026

### Bitbucket

- &#x20;**Clearer Bitbucket Data Center support.** The Bugbot dashboard now names Bitbucket Data Center organizations by their server hostname and labels them Bitbucket Data Center instead of bitbucket.org. Bugbot no longer offers Autofix on Bitbucket Data Center, and its review footnote no longer suggests switching to direct push there. [Bitbucket Data Center](https://cursor.com/docs/integrations/bitbucket.md) requires a Teams or Enterprise plan.

### Reviews

- **Local reviews say what they skipped.** When you [run Bugbot from your agent](https://cursor.com/docs/bugbot.md#run-in-your-agent) or run a security review on local changes and the diff is too large to review in full, the result now says how many changed files were covered and lists the ones that were not reviewed, so you can review them next. Findings in those skipped files are no longer discarded as unrelated. If every reported finding is filtered out, Bugbot says the review was not clean instead of reporting no bugs.
- &#x20;**Manual Only stops automatic learning from merged pull requests.** With Bugbot set to Manual Only for a repository or in your personal settings, it no longer [learns rules](https://cursor.com/docs/bugbot.md#learned-rules) automatically when a pull request is merged or closed, and that learning no longer counts toward your Bugbot usage. `@cursor remember` comments still teach it rules.

### Dashboard

- &#x20;**Consistent daily counts in Bugbot analytics.** The [Bugbot analytics](https://cursor.com/docs/bugbot.md#analytics) dashboard now counts pull requests reviewed per UTC day, so a day's numbers no longer change when you move the date range. The PRs reviewed total counts each pull request once for the whole range, and the date picker is labeled UTC. The review analytics API now counts only reviews inside the requested range, so it matches the dashboard when you request all PR states.

### Fixes

- &#x20;**Fixes to reviews and Autofix.** With run-once enabled, a commit pushed while a review is still running now gets reviewed instead of skipped, and incremental reviews keep your BUGBOT.md rules even when the new push has no diff. Review comments no longer say a cloud agent was started to fix issues when it wasn't; they say the agent failed to start or that no issue met your Autofix severity threshold. Reviews on repositories granted to an Enterprise team now run under that team instead of the installation owner.
- **Fixes to PR summaries.** If a PR summary hangs or fails, Bugbot no longer leaves a stale "generating a summary" placeholder in your PR description or comment. It removes it or shows "Unable to generate summary." Images, videos, and files you paste under the summary are no longer wiped when Bugbot refreshes it.
- **Fixes to the Bugbot dashboard and integrations.** Connecting a self-hosted GitLab instance from the Bugbot dashboard now links it to the right team, and the repository picker during app install now shrinks to fit the window, so its search field no longer opens off-screen. Turning on Bugbot for an Azure DevOps repository after the enterprise app was re-consented now recovers automatically instead of failing. Per-repository Bugbot settings are cleaned up when a GitHub App is uninstalled or repositories are removed.

## 1.13.0

### Review

- **Source and base branches in Review.** The pull request Review screen in [Cursor for iOS](https://cursor.com/docs/cloud-agent/mobile.md) shows the source branch and the branch it merges into under the title, and the base branch follows the pull request's current target. VoiceOver reads full branch names even when long names are cut off on screen.

### Fixes

- **Chat and review display.** Text references from cloud agents show as cards instead of raw markup when their tags span multiple lines. When a cloud agent's diff is too large to show, the Review screen says it has too many files or some files are too large. Visualizations that can't render on mobile tell you to open them in the Cursor desktop app.

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

## 3.23

### Plans and billing

- &#x20;**Plan & Usage shows your plan and prepaid credits.** On Premium, Plus, Super, and Ultra plans, Cursor Settings > Plan & Usage shows your plan by name and your usage reset date. Individual accounts on these plans also get a Credits section with the prepaid balance, pending top-ups, and the auto top-up rule, plus buttons to add credits or change the rule.

### Agent and chat

- **Approval prompts now tell you why the agent is asking.** When the agent asks to read or edit a file outside your workspace, or edit a protected config file, the approval card shows the reason.
- **Clearer errors when image generation fails.** When the agent can't generate an image, it now tells you why instead of showing a raw request error. A content-policy block suggests describing the subject in your own words, and a rate limit or provider outage asks you to try again.

### Cloud agents

- **Slack mentions in cloud agent prompts show as readable names.** When you open a cloud agent started from Slack, people mentioned in its prompts appear as `@Name` instead of raw Slack user IDs, and find in the conversation matches the names you see. Clicking a mention opens that person in Slack.

### Editor

- **AI features recover on their own when the extension host hangs.** If the extension host that powers Cursor's AI features stops responding for about a minute, Cursor restarts it automatically, so you no longer need to reload the window. It also keeps restarting a crashing host with increasing delays, and skips the automatic restart while you debug extensions.

### Privacy and security

- **Privacy mode now blocks automatic crash debugging uploads.** With privacy mode on, Cursor no longer uploads debugging data or emergency memory profiles on its own after a crash or out-of-memory event, even if you turned privacy mode on mid-session.

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

## v2026.07.20

- **`--trust` works in interactive sessions.** Previously `--trust` required headless mode. Passing it in an interactive session now trusts the workspace up front and skips the trust dialog, recording the same saved trust decision the dialog writes when you accept.
- **Clear errors instead of hangs at login.** MCP OAuth login fails fast with an actionable message when the callback port is already taken, instead of hanging on "Listening for the OAuth callback". On macOS, keychain failures at startup now explain the cause and the fix, like unlocking a locked keychain or logging out and back in, instead of a raw exit code.
- **The model catalog stays fresh in long sessions.** The CLI refetches the model catalog every 10 minutes in the background, so newly released models appear in `/model` and shortcuts without restarting. If a refresh fails, the CLI keeps the current catalog and retries on the next interval.
- **Cleaner rendering.** Completed tool rows no longer disappear for a frame when the agent moves to its next step, markdown tables with emoji or CJK text keep their columns aligned, typing a path like `/tmp` followed by a space no longer leaves the slash palette stuck on "No matches", and subagent rows drop the Ctrl+O expand hint (the shortcut still works).
- **Fixed CPU spinning from the branch watcher.** When the watcher that keeps the prompt footer's git branch current could not attach, most commonly after exhausting the inotify watch limit on Linux, it retried in a tight loop that pegged a CPU core. Failed attaches now back off exponentially, and branch switches still update the footer immediately.
