---
title: "Bugbot release notes"
source: https://cursor.com/docs/release-notes/bugbot
path: /docs/release-notes/bugbot
---

# Bugbot release notes

Weekly changes to [Bugbot](https://cursor.com/docs/bugbot.md). Each entry covers one week of changes and is labeled with the Monday that starts it.

## Week of Sep 28, 2026

### Repository settings

- **Configure Bugbot per repository.** On GitHub pull requests, Bugbot reads a `.cursor/config/bugbot.yaml` file to set its triggers, review effort, incremental review, PR summary, and risk score for that repository. Values in the file override team settings, and the file can lower Autofix but never turn it on. The Bugbot Settings section in the dashboard links to the docs for config files.

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

## Week of Sep 21, 2026

- **More accurate Bugbot checks on Origin.** On Origin pull requests, a Bugbot run that errors or can't post its review now fails the Bugbot check instead of reporting neutral. A run cancelled by a new push is marked cancelled, so it no longer satisfies a required Bugbot check.
- **Bitbucket-only teams can finish Bugbot setup.** Teams connected only through Bitbucket no longer see a prompt to connect GitHub or GitLab during Bugbot setup. The setup steps now show the Bitbucket connection as connected.
- **Reviews continue past oversized files.** When one changed file is too large for Bugbot to review, Bugbot skips that file and still reviews the others. Before, an oversized file could make Bugbot skip every file after it.

## Week of Sep 14, 2026

- **Clearer Bugbot check names on Origin.** On Origin pull requests, Bugbot's checks are now named "Cursor / Cursor Bugbot" and "Cursor / Cursor Bugbot Autofix". Required-check rules that already list Bugbot keep matching.

## Week of Sep 7, 2026

- **Large generated files no longer block reviews.** Files marked `linguist-generated` in `.gitattributes`, such as lockfiles, are left out of Bugbot's size check even when they are larger than 2 MB. Bugbot reviews the rest of the pull request instead of skipping it as too large.
- **Bugbot dashboard dialogs close with Escape.** The disable, bulk repository action, and cancellation dialogs in the Bugbot dashboard now close when you press Escape.
- **Azure DevOps fixes.** When a pull request summary would exceed Azure DevOps's 4,000-character description limit, Bugbot posts the full summary as a comment and says so in a shorter description. Organizations whose tenant check names no tenant can now enable Bugbot instead of failing tenant discovery. When an Azure DevOps pull request event includes its head commit, Bugbot queues the review without first reading the pull request from Azure DevOps, so a brief Azure DevOps or Entra outage no longer fails the event.

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
