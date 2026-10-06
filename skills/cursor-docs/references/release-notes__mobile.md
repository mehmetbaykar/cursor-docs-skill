---
title: "Cursor mobile release notes"
source: https://cursor.com/docs/release-notes/mobile
path: /docs/release-notes/mobile
---

# Cursor mobile release notes

New features, improvements, and fixes in [Cursor for iOS](https://cursor.com/docs/cloud-agent/mobile.md). Each entry covers one app version.

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
