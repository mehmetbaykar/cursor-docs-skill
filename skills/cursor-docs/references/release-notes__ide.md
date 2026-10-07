---
title: "Cursor IDE release notes"
source: https://cursor.com/docs/release-notes/ide
path: /docs/release-notes/ide
---

# Cursor IDE release notes

New features, improvements, and fixes in the Cursor IDE. Each entry covers one minor version, including the patch releases that follow it. Changes to the [Agents Window](https://cursor.com/docs/release-notes/agents-window.md) have their own page.

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
