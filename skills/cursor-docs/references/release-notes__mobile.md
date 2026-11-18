---
title: "Cursor mobile release notes"
source: https://cursor.com/docs/release-notes/mobile
path: /docs/release-notes/mobile
---

# Cursor mobile release notes

New features, improvements, and fixes in [Cursor for iOS](https://cursor.com/docs/cloud-agent/mobile.md). Each entry covers one app version.

## 1.18.0

### Voice calls

- **Voice calls keep going past two hours and through server drops.** A [voice call](https://cursor.com/docs/agent/voice-chat.md) no longer ends at the two-hour mark. The app moves the call to a fresh connection during a pause, with no reconnect chime, and the conversation carries on. Calls the server drops now reconnect to the same conversation instead of hanging up.
- **Hear Project worker results during voice calls.** If a team admin has turned on [Projects](https://cursor.com/docs/agent/projects.md), a voice call in a Project's chat reads each worker's result aloud once, as soon as that worker finishes. Results keep coming even if you cover or leave the chat during the call.
- **Voice calls can send requests while a plan waits for Build.** Asking a question or giving a follow-up during a voice call no longer fails with "The agent needs you in the chat" when the agent's plan is waiting for you to build it. The request goes through like a typed message. Calls still hold your request while the agent waits on an open question or a sign-in prompt.
- **Voice call turns read like typed ones.** Messages a voice call sends to the agent are now hidden in every call mode, and the "Sent by voice call" label is gone. Work from a voice turn shows the same Worked sections, replies, and Changes cards as a typed request, and an instruction given mid-turn continues that turn instead of starting a new one. Messages stay hidden after you reopen the chat.
- **Choose which status chimes play.** During a [voice call](https://cursor.com/docs/agent/voice-chat.md), the Settings menu has a Status Chimes submenu with a switch for each chime: Task Sent, Result Arrives, Needs Decision, and Error. Your choices carry over to later calls, starting from your previous chime setting.
- **See which agent has a live voice call.** While you're away from its chat, an agent with a voice call in progress shows a green waveform chip with the call timer in the agent list. Tap the row to return. Double-tapping Stop or the mic no longer starts a voice call by accident, and links in a call's transcript now open.

### Agents

- **Open Agent Store files and Project notes from chat.** Tapping a file path in an [Agent Store](https://cursor.com/docs/agent/projects.md#shared-context), such as a Project's Context, or a Project notes link in an agent's reply or tool details opens the file in the in-app markdown preview instead of doing nothing. Links inside a previewed file open their own preview, so you can follow a plan or task note without leaving the chat.
- **Running agent chats open without a blank screen.** Opening a chat whose agent is still working shows the recent conversation right away, then fills in the rest of the running turn. Before, a running turn with many steps could keep the chat blank until every step loaded. Turns you expand while it fills in stay expanded.

### Fixes

- **Voice calls.** If you stay quiet when a call opens while the agent is mid-task, the call now greets you after a short pause instead of staying silent. After a dropped call reconnects, the voice keeps its context without repeating earlier updates. In any chat, an edit you reject no longer shows up in the turn's Changes card.
- **Returning to the app.** Coming back to Cursor from the background refreshes your sign-in, team memberships, and plan again, instead of leaving them out of date. The machine and pool list in the composer also updates when you return.

## 1.17.0

### Voice calls

- **Voice calls give up-to-date answers about the agent's work.** A [voice call](https://cursor.com/docs/agent/voice-chat.md) now knows the recent chat, including the last week of messages and earlier calls, and keeps up with the agent's branch, pull request, test runs, and to-dos as they change, so asking how the work is going gets a current answer. A request that can't reach the agent within 20 seconds is reported as unreachable instead of being sent late, and a call that starts or reconnects while the agent is idle or already working no longer resends your last request.
- **Voice call answers are shorter and stick to what the agent knows.** Answers start with a short spoken summary of about 30 words and offer to go deeper, and calls no longer read out URLs, long file paths, full commit hashes, or tool names. When you ask for an exact value or a code walkthrough, the call looks it up instead of guessing, and it reports test and CI results without speculating about why they passed or failed.
- **Talk over the agent in voice calls.** The agent's voice fades down as soon as you start talking and comes back if it was only background noise. When you interrupt a reply, the agent knows which part you heard and can pick up the rest instead of repeating or dropping it.
- **Voice calls read out the agent's plans.** When the agent ends a turn with a plan during a voice call, the call reads out the plan's name, overview, and to-dos instead of only saying it needs you in the chat. The full plan stays in the chat.
- **Short tones tell you what the agent is doing.** During a voice call, a soft tone plays when a task is sent, when a result is about to be read after a pause, when the agent needs your decision, and when something goes wrong. Tones play alongside speech without interrupting it. Turn them off with Status chimes in the voice call settings.
- **Voice calls understand your repo, file, and agent names.** Voice calls, including on CarPlay, recognize spoken repository, branch, file, and agent names from the current conversation more reliably. Asking to send to or switch to an agent works with names in Japanese, Chinese, Korean, Thai, Arabic, and accented Latin, and interrupted replies in those languages pick up at the right spot.
- **Voice calls show on CarPlay.** When a [voice call](https://cursor.com/docs/agent/voice-chat.md#ios) plays through your car's CarPlay audio, its Live Activity appears on the CarPlay display with the agent, a live timer, and a Hang up button. Muting from the Live Activity or the system call screen stays in sync, and a Live Activity you dismiss stays dismissed for that call.

### Composer

- **Edit your words while you're still dictating.** Tap the live caption while [dictating](https://cursor.com/docs/agent/prompting.md#voice-input) in the composer to edit what you've said so far. Your edits stay, and anything you say next is added after them without doubled spaces or punctuation. Dismissing mid-dictation now only hides the keyboard.

### Account and billing

- **Clearer warning before deleting an account merged with Grok.** If your Cursor account is merged with a Grok account, the Delete Account page warns that deleting it also permanently deletes your Grok account and any Grok plan, with no way to restore them.

### Fixes

- **Voice calls.** What you say while a call is still connecting is no longer lost, and a two-part question no longer ends in silence. The call no longer greets you after it has already started talking, and it keeps track of the agent's latest progress during long tasks. Voice call cards stay visible and attached to your last typed message.
- **Foldable layouts and large text sizes.** Folding or unfolding your phone, or switching iPad layouts, keeps your place in the chat you were reading, and returning from the background no longer resets navigation. At the largest accessibility text sizes, sidebar icons, round buttons, and the composer's repo row and toolbar no longer overlap or clip. Slash command suggestions also come back when you return to a draft.
- **Conversation loading and sign-in.** Sign-in and session refresh work even when your phone's clock is wrong. Opening a large Project loads back to your last message instead of stalling, and a follow-up sent before leaving a chat shows in the right place when you return. The paywall sheet no longer shows two back controls.

## 1.16.0

### Voice calls

- **Voice calls show on the Lock Screen and keep the chat focused.** When iOS can't show a voice call on the system call screen, Cursor for iOS shows it as a Live Activity on the Lock Screen and Dynamic Island, where you can mute or hang up. During a call, the chat hides your transcribed speech and Worked sections with nothing in them, so you see only the agent's replies, questions, plans, and edits. Call cards appear in the conversation where the call started, not pinned to the bottom.

### Account and billing

- **Manage Plan when you hit included usage on the top plan.** If you're on the highest personal plan and use up your included usage, the Included Usage Reached message now includes a Manage Plan button.

### iPhone Duo

- **The sidebar and chat split at the fold on iPhone Duo.** On iOS 27.1 or later, when iPhone Duo is half open in landscape, the agents sidebar ends at the hinge so the sidebar and chat each sit on their own half of the screen instead of straddling the fold. If either side would be too narrow, the usual layout stays.

### Fixes

- **Layout and visual polish on iPhone and iPad.** The composer and the iPad sidebar's account row sit on the bottom safe area and line up with each other, without an extra gap above the home indicator. Toolbar icons match the size of native toolbar symbols, the sheet grabber shows only on resizable sheets, and the Access Disabled screen keeps a readable width on iPad.
- **Conversations and the repo picker.** The app no longer crashes on iOS 27 when loading conversations or the profile screen. A lone Thinking step in a running conversation updates to show how long it took once it finishes, and the repo picker no longer lists or preselects unpublished Start from scratch drafts.

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

## 1.13.0

### Review

- **Source and base branches in Review.** The pull request Review screen in [Cursor for iOS](https://cursor.com/docs/cloud-agent/mobile.md) shows the source branch and the branch it merges into under the title, and the base branch follows the pull request's current target. VoiceOver reads full branch names even when long names are cut off on screen.

### Fixes

- **Chat and review display.** Text references from cloud agents show as cards instead of raw markup when their tags span multiple lines. When a cloud agent's diff is too large to show, the Review screen says it has too many files or some files are too large. Visualizations that can't render on mobile tell you to open them in the Cursor desktop app.

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

## 1.10.0

### Projects

- **Projects.** Cursor for iOS now supports Projects. Your Projects appear in their own section of the inbox; tap one to open its chat. On iPhone, the New Project row starts a Project from a name, with an optional repository, branch, and model. If a team admin turns off Projects for the team, the Projects section and New Project are hidden.

### Fixes

- **iPad chat.** On iPad, the chat stays readable while the keyboard is up instead of being blurred at the bottom.

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
