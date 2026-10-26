---
title: "Cursor mobile release notes"
source: https://cursor.com/docs/release-notes/mobile
path: /docs/release-notes/mobile
---

# Cursor mobile release notes

New features, improvements, and fixes in [Cursor for iOS](https://cursor.com/docs/cloud-agent/mobile.md). Each entry covers one app version.

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
