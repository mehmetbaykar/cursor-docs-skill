---
title: "AI code review: more context, fewer bugs"
source: https://cursor.com/guides/ai-code-review
path: /guides/ai-code-review
---

Aug 12, 2026·code review

# AI code review: more context, fewer bugs

8 min read

Code review is often slow and uneven: diffs wait in queues, and feedback depends on who is online.

AI code review only helps when the reviewer has real codebase context.

AI code review works best when the reviewer already has the full repo, recent changes, tests, and a clear set of rules. AI code review with this context catches problems a standalone bot staring at a single diff will never see. Review is most useful as part of the same system that produced the change.

## [#](#what-changed-about-code-review)What changed about code review

Coding agents did not invent long pull requests, but they made the old review math fail faster.

Developers working with coding agents are shipping bigger changes. [Data from millions of Cursor sessions](https://cursor.com/insights/developer-habits) shows lines added per PR (p75) up about 2.5x year over year. Mega PRs of 1,000+ changed lines are a growing share of merges, with a clear jump in January 2026 as agents and models improved. Agent sessions got deeper too: mean tool calls per session rose about 30% in a recent two-month window. More of the AI-authored code survives. Accepted AI lines still present after 60 minutes rose from roughly 76% to 81% since the start of 2026. Agent-generated changes that reach commits without a separate manual diff-acceptance step grew more than 5x over that period.

Human review capacity did not scale with any of that. Classic peer-review guidance has long treated a few hundred lines of careful reading as the range where quality holds.

AI code review is how you keep a quality gate when the volume of change outruns the number of senior engineers who can read every diff.

More of the code under review was written with AI assistance. Humans are good at catching "this does not match how we build here." They are worse at staring down a large, plausible, mostly-correct agent patch for the one subtle break, which is where a reviewer with real repo context helps. Writing a large change and checking it are different skills, and review is the check.

## [#](#questions-before-launching-ai-code-review)Questions before launching AI code review

If you are evaluating AI code review tools, work through these concepts first.

### [#](#what-is-ai-code-review)What is AI code review?

AI code review is software that reads a change (usually a pull request, sometimes a local diff) and comments on bugs, regressions, and risk before merge. The useful versions reason over more than the changed lines in front of them. They pull related files, tests, config, and team rules. The weak versions restate the diff in prose or nag about comments and naming.

A weak AI reviewer only sees the diff. A useful one also has the repo, tests, recent changes, and team rules.

### [#](#how-is-it-different-from-linting-or-ci)How is it different from linting or CI?

Linters and typecheckers encode rules you already know how to write. CI runs the checks you automated. AI review is for the residue: logic errors, race conditions, auth mistakes, breaks a few folders away, and mismatched docs and behavior. It overlaps CI. It does not replace it.

### [#](#does-ai-code-review-replace-human-review)Does AI code review replace human review?

No. It changes what humans spend time on. [Only about half of human review comments](https://www.youtube.com/watch?v=TswQeKftnaw) lead to a change in the same PR anyway. Healthy review cultures include fix-forward notes and FYI context. You want to clear high-confidence, machine-tractable bugs so people can stay on architecture, product risk, and tribal knowledge the model does not have yet.

### [#](#what-makes-ai-review-noisy)What makes AI review noisy?

Noise comes from comments people do not want from a bot. Style nags, vague "add tests" notes with no failing test, and rewrite suggestions that do not catch a bug all train people to ignore the review. Separate what the model can catch from what people actually want it to flag. AI code review should flag real bugs, accidental commits, performance and security issues, and places where the docs and the code disagree. When [Graphite scoped its AI reviews to that overlap](https://www.youtube.com/watch?v=TswQeKftnaw), about 52% of comments led to a code change (roughly the same rate as human reviewers), with downvotes under 4%.

### [#](#what-should-we-measure)What should we measure?

Resolution rate: at merge time, was the flagged issue actually fixed in the final code? Resolution rate beats comment volume.

This is also the metric we used to improve Bugbot: [resolution moved from 52% to over 70%](https://cursor.com/blog/building-bugbot) across 40 experiments, bugs flagged per run from 0.4 to 0.7, and resolved bugs per PR from roughly 0.2 to about 0.5, across [more than two million PRs reviewed per month](https://cursor.com/blog/building-bugbot). By [May 2026](https://cursor.com/blog/may-2026-bugbot-changes), default-effort resolution had reached about 80% of bugs resolved by merge time. If your resolution falls while comment volume rises, the bot is generating noise.

The [Bugbot dashboard](https://cursor.com/dashboard/bugbot) charts resolution rate over time for each repository, alongside the volume of issues found and fixed, so you can see whether reviews are catching real problems and getting resolved before you widen what the bot comments on.

### [#](#when-should-review-run-locally-on-the-pr-or-both)When should review run: locally, on the PR, or both?

Both, with different jobs. Local review (after an agent task, before push) catches issues while context is still warm and the thread does not exist yet. PR review is the team contract: shared rules, shared history, and a shared merge gate. Security-focused passes can sit on either side depending on how you ship.

### [#](#do-we-need-the-review-tool-to-live-in-the-same-product-as-the-agent)Do we need the review tool to live in the same product as the agent?

You can buy a standalone reviewer. Many teams do. The cost is context switching and a thinner view of how the code was produced. When review runs in the same system that wrote the change, it already knows the open files, the repo map, and the rules you maintain next to the code. Fixes can deep-link back into the editor or spawn an agent with the finding loaded. That loop is hard to fake with a bolt-on.

## [#](#how-to-run-ai-code-review-in-cursor)How to run AI code review in Cursor

Cursor's path is local review in the editor, Bugbot on the pull request, then a fix loop that returns you to the same toolchain.

AI code review in Cursor runs locally in the editor, then on the pull request, then back into a fix loop.

**Local.** After agent work, run [Agent Review](https://cursor.com/docs/agent/agent-review). You can type `/agent-review` in the agent input, run it from the Source Control tab to compare local changes against your main branch, or turn on automatic reviews after every commit. Before you push, you can also run Bugbot or a Security Agent locally with the `/review-bugbot` and `/review-security` skills. This is where you clear obvious problems while the session still has context.

**On the PR.** [Bugbot](https://cursor.com/docs/bugbot) reviews pull requests on GitHub, GitLab, and Bitbucket. Encode team invariants in `.cursor/BUGBOT.md`, plus team rules and repo rules. Learned rules (`@cursor remember`) fold feedback into future runs. Watch resolution rate in Bugbot Automations before you widen comment categories.

**Fix loop.** Findings show up on the PR with paths back into Cursor (Fix in Cursor and Fix in Web). Bugbot Autofix can spawn a Cloud Agent to propose repairs. For security, Cursor's [Security Agents](https://cursor.com/docs/security-agents) cover the two jobs: Security Reviewer checks PRs before merge, and Vulnerability Scanner scans the codebase at rest.

**Start.** The docs cover setup end to end: connecting your repo, choosing which repos and people trigger reviews, effort level, and `.cursor/BUGBOT.md`. Follow along at [cursor.com/docs/bugbot](https://cursor.com/docs/bugbot).

## [#](#automate-the-routing-and-sign-off)Automate the routing and sign-off

Finding bugs is not the whole review job. Two Cursor automations handle the mechanical parts.

**Auto-approve low-risk changes.** [Approval Agents](https://cursor.com/docs/approval-agents) score each pull request by risk and approve the ones that clear the bar you set. A copy tweak or a config bump can merge without waiting on a human. Anything above your risk threshold is held. Bugbot and Security Agent findings feed that decision, so a risky change does not get waved through.

**Route to the right reviewers.** When a PR needs a person, Approval Agents assign reviewers based on the part of the codebase it touches, using per-area routing policies you define. The change goes to the team that owns that code instead of a shared queue.

## [#](#keep-review-close-to-the-code)Keep review close to the code

AI code review is how teams keep a quality gate while agents increase the size and speed of change. The versions that work have repo context, a narrow comment policy, and a metric that tracks whether findings get fixed.

Review belongs close to where the code was produced, with the same rules and the same fix path. Turn [Bugbot](https://cursor.com/docs/bugbot) on for a busy repo, watch resolution in [Bugbot Automations](https://cursor.com/automations/from-cursor/bugbot) for a week, and only then decide which categories deserve more volume.

Filed under: code review

## Related guides

[Model routing: right model, right job, right price

Model routing sends each request to the model that fits the job, so routine work stops billing at frontier prices. How it works, what to measure, and how to run it.](https://cursor.com/guides/model-routing)

[MCP for coding agents: how agents plug into your stack

MCP connects coding agents to your databases, tickets, docs, and error trackers. Which servers to start with, and how to add one in minutes.](https://cursor.com/guides/coding-agent-mcp)

[View all guides →](https://cursor.com/guides)
