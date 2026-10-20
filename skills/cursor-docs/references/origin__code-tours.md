---
title: "Code Tours"
source: https://cursor.com/docs/origin/code-tours
path: /docs/origin/code-tours
---

# Code Tours

Origin is currently released in early beta. You can create repos, push and pull with git, mirror from GitHub, browse and search code, open and merge pull requests, and share with your Cursor team.

Code Tours walk you through a [pull request](https://cursor.com/docs/origin/pull-requests.md) in the order that makes sense to review it. Cursor reads the diff, groups related changes, and explains each group next to its code. Every pull request on Origin has a tour on its **Changes** tab.

Here's a tour of a pull request that moves webhook retries onto a queue:

![A Code Tour of a webhook retry change: an overview, then the retry path with a timeout risk called out above its diff](https://cursor.com/docs-static/images/origin/code-tour-guided.png)

## Open a tour

### Open the pull request

At [cursor.com/codebase](https://cursor.com/codebase), open a repository, select **Pull Requests**, and open a pull request.

### Switch to Tour

On the **Changes** tab, select **Tour** in the **Diff** / **Tour** control, or press T. Press T again to go back to the diff.

Most of this page applies to pull requests in repositories created on Origin. GitHub pull requests in a [mirrored GitHub repository](https://cursor.com/docs/origin/mirror-github.md) get tours too, with fewer features.

## What a tour gives you

Each tour is written for its pull request. A small fix might get a few sentences, while a large change gets a longer walk through its parts.

Most tours start with what the change does and why, written for someone who hasn't worked in that part of the codebase. Then the tour walks through the changes in groups and explains each one next to its code. Along the way, it points out what deserves a closer look, like behavior other code relies on. When you want more, ask Cursor about any part of the tour, or switch to **Diff** to see file changes only.

Terms you might not know have a dotted underline. Hover over one, or focus it with the keyboard, to see a short definition. Screenshots and recordings from the pull request description, or from the [cloud agent](https://cursor.com/docs/cloud-agent.md) that authored it, may show up where they help. When an agent authors a pull request, the tour may also use the agent's notes on why it took its approach, what to watch for, and what it tested.

## Find your way around

- **Jump to a section.** Select the short lines at the top left of the tour to list its sections, then pick one.
- **Share a section.** Select the link icon next to a section heading to copy a link to it.
- **Mark a section reviewed.** Check the box next to a section to mark its files as viewed. The **Diff** view keeps the same progress.
- **Expand a file.** Test files start collapsed so the code under review comes first. Deleted, generated, and binary files may start collapsed too.

## Customize a tour

To get a different tour, open the **Generate custom tour** menu next to the tour's title. From there, you can:

- Start with the highlights
- Choose which files the tour covers
- Set the depth
- Add your own instructions

For GitHub pull requests in a mirrored GitHub repository, everything except highlights is available.

To tour part of the pull request's history, pick a version, a commit, or a range in the version picker above the files, and the tour follows. Pick **Changes since your last review** to see only what changed since you last reviewed.

## Ask Cursor about a tour

Select **+** next to a section heading to add that section to the **Ask Cursor** box at the bottom of the page, then type your question. To ask about a specific passage, select the text and choose **Add to chat**, or press Cmd I. You'll see both when chat is available on the pull request page.

A [cloud agent](https://cursor.com/docs/cloud-agent.md) working on the pull request can also edit the tour. Ask it to rewrite a section, add a screenshot or recording of the change, or write the whole tour again with different instructions.

## When you finish a tour

On pull requests with more than three files, a **What next?** card may appear after the last section. It suggests a few follow-up tours, like **Changes since your last review**, **Files you own**, or a **Detailed version of this tour**. Select **Something else…** to describe a different one. The card may also offer **Add media to this tour**, which asks a cloud agent to add screenshots, recordings, diagrams, or tables to the tour.

After a tour finishes loading, **Is this tour helpful?** lets you leave a thumbs up or down, and a comment if you want.

## When tours are written

Cursor writes tours ahead of time only for repositories created on Origin and owned by a team. In those repositories, it writes the tour in the background when a pull request opens, including drafts, and when new commits are pushed. It's usually ready before the first reviewer looks.

If a tour isn't ready when you open it, Cursor writes it on the spot, and you can read each section as it appears. Tours you ask for, like a different depth or a version range, are written when you ask.

## New commits

When someone pushes to the pull request, Cursor writes a tour for the new commit in the background. You keep reading the current one, and **Updating…** appears next to the **Diff** / **Tour** control. If you're on the latest version, the new tour replaces the old one when it's ready. If you're looking at an earlier version, select **See latest** when you want to move. Cursor checks with you first if you have an unsaved comment.

On an earlier version, comments on code that isn't in that version are marked **Not in this version**.

## Large pull requests

Some pull requests are too large for a tour. You'll see **Too large for a tour** with a **View files** button that takes you back to the diff. Smaller pull requests each get their own tour.

## Usage and billing

Tours that Cursor writes ahead of time don't count toward your usage. When Cursor writes a tour because you opened it or asked for one, it counts toward your [Cursor usage](https://cursor.com/docs/models-and-pricing.md) the same way an agent request does. Reading a tour that's already written doesn't use any. When a cloud agent edits or rewrites a tour, that work counts toward the agent's usage.

To have Cursor write a tour when you open it or ask for one, you need a paid Cursor plan. On a free plan, or an individual plan that's still in its trial, you can read tours that already exist.

## Privacy

Code Tours follow the [Privacy Mode](https://cursor.com/help/security-and-privacy/privacy.md) of the team or person who owns the repository, like the rest of Origin. To write a tour, Cursor sends the pull request's diff and description to a model. The tour is saved with the pull request, and anyone who can see the pull request can read it.

## FAQ

### Why does the tour say "Too large for a tour"?

The pull request is bigger than Cursor can write a tour for. Select **View files** to review it in the diff. If you split the work into smaller pull requests, each one gets its own tour.

### The tour failed or stopped partway. What do I do?

Select **Retry** under **Couldn't generate the tour**. If it keeps failing, check that you're on a paid plan. See [Usage and billing](https://cursor.com/docs/origin/code-tours.md#usage-and-billing).

### Why don't I see the newest commits in the tour?

Cursor is still writing the tour for the latest commit. Once **Updating…** goes away, the tour switches on its own. If it doesn't, select **See latest**.

### Can I get a shorter tour, or one about only my files?

Yes. Open the **Generate custom tour** menu to set the depth or choose which files the tour covers. See [Customize a tour](https://cursor.com/docs/origin/code-tours.md#customize-a-tour).

## Related

- [Pull requests](https://cursor.com/docs/origin/pull-requests.md) - open, review, and merge pull requests
- [Browse & Search](https://cursor.com/docs/origin/browse.md) - browse files, search code, and inspect commit history
- [Origin](https://cursor.com/docs/origin.md) - overview, access, and privacy
