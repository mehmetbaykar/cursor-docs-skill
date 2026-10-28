---
title: "Security Agents"
source: https://cursor.com/docs/security-agents
path: /docs/security-agents
---

# Security Agents

Security Agents scan your code for security bugs, risky patterns, and vulnerabilities.

Configure Security Agents in Automations. Each agent type has its own page: [Security Reviewer](https://cursor.com/automations/from-cursor/security-reviewer) and [Vulnerability Scanner](https://cursor.com/automations/from-cursor/vulnerability-scanner).

## How it works

Security Agents include two Cursor-managed agent types:

- **Security Reviewer** checks pull requests before they merge. Use it to catch vulnerabilities during code review.
- **Vulnerability Scanner** scans your codebase at rest. Use it to find pre-existing vulnerabilities, long-standing issues, and problems missed during PR review.

Both agent types run on the Automations platform and require Cloud Agents.

## Setup

Open the [Security Reviewer](https://cursor.com/automations/from-cursor/security-reviewer) or [Vulnerability Scanner](https://cursor.com/automations/from-cursor/vulnerability-scanner) page in Automations to configure that agent type.

### Source control support

Security Reviewer supports pull requests on Origin, GitHub, and GitLab. For pull request reviews on Bitbucket or Azure DevOps repositories, use [Bugbot](https://cursor.com/docs/bugbot.md).

| Source control provider                                                          | Security Reviewer | Bugbot                                                                                                  |
| :------------------------------------------------------------------------------- | :---------------- | :------------------------------------------------------------------------------------------------------ |
| [Origin](https://cursor.com/docs/origin.md)                                      | Supported         | Supported                                                                                               |
| [GitHub](https://cursor.com/docs/integrations/github.md)                         | Supported         | Supported                                                                                               |
| [GitLab](https://cursor.com/docs/integrations/gitlab.md)                         | Supported         | Supported                                                                                               |
| [Bitbucket Cloud](https://cursor.com/docs/integrations/bitbucket.md)             | Not supported     | Supported (public beta)                                                                                 |
| [Bitbucket Data Center](https://cursor.com/docs/integrations/bitbucket.md#setup) | Not supported     | Supported on Teams and Enterprise; automatic reviews only; no `bugbot run`, `cursor review`, or Autofix |
| [Azure DevOps Services](https://cursor.com/docs/integrations/azure-devops.md)    | Not supported     | Supported (public beta)                                                                                 |

Vulnerability Scanner also does not support Bitbucket Cloud or Bitbucket Data Center repositories.

### Triggers

**Security Reviewer agents** support Git-based Automations triggers, including pull request and merge request events. Use these triggers to run security checks when code changes.

![Security Reviewer Git-based trigger configuration](https://cursor.com/docs-static/images/security-review/triggers.png)

**Vulnerability Scanner agents** support cron-based triggers. Use these triggers to scan your codebase on a recurring schedule, independent of pull request activity.

![Vulnerability Scanner cron trigger configuration](https://cursor.com/docs-static/images/security-review/vulnerability-scanner-triggers.png)

Each Vulnerability Scanner has one schedule. To change when it runs, edit its existing trigger. To scan on another schedule, create a separate Vulnerability Scanner. A scan across more than 1,000 repositories can hit provider rate limits, so split large scopes into separate Vulnerability Scanners with smaller repository scopes.

### Security Checks

Both agent types include built-in security checks. Enable or disable individual checks based on what you want each agent to review.

### Custom instructions

Use custom instructions to give each agent more context. You can describe the types of issues to prioritize, explain project-specific security expectations, or define how the agent should behave.

### Tools and MCPs

Both agent types support tools and MCPs. A Security Reviewer needs at least one tool or MCP before you can save it. A Vulnerability Scanner saves without one and reports its findings to the **Remediation agents** section on the [Vulnerability Scanner page in Automations](https://cursor.com/automations/from-cursor/vulnerability-scanner).

Use tools and MCPs to connect Security Agents to the systems where your team tracks security work.

- Send vulnerabilities to a Slack channel, issue tracker, or another connected system.
- Add custom instructions that explain when and how the agent should use each MCP.
- Give the agent extra context from tools or MCPs before it reports a finding.

### Environment Setup

Security Agents run on Cloud Agents, with two exceptions on a team. A team's Security Reviewer runs on Cursor-managed hosting instead of a Cloud Agent when a pull request event triggers it, and a team's Vulnerability Scanner runs its scans there too. Teams that [require Self-Hosted Machines](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#triggering-pool-agents) keep both on Cloud Agents.

You can use Cursor's cloud with no additional setup.

## Run in your agent

Use the `/review-security` or `/review` skills to run the Security Agent from your agent before you push the code.

**What diff is reviewed:** By default, `/review-security` reviews your branch changes: every change relative to the base branch, including committed and uncommitted changes. Ask it to review only your uncommitted changes when you want narrower feedback.

**Against which branch:** `/review-security` compares against your default base branch. When your base branch isn't the default (such as `main`), tell the agent which branch to compare against or let it infer from the context.

![Running the /review-security skill from the agent input](https://cursor.com/docs-static/images/security-review/review-security-skill.png)

`/review` and `/review-security` are available in Cursor 3.7+, at [cursor.com/agents](https://cursor.com/agents), and in the [Cursor CLI](https://cursor.com/docs/cli/overview.md).

## Billing

Security Agents are billed at the team usage level:

- Usage is charged to the team's usage pool.
- Agents run under a shared team service account, so they don't affect any individual user's usage.

## Analytics

Security Agents track three key metrics across agent runs. The [Security Reviewer page in Automations](https://cursor.com/automations/from-cursor/security-reviewer) shows them:

- **Vulnerabilities found**: the number of security findings reported by agents.
- **Issues fixed**: the number of findings that were resolved after they were reported.
- **Resolution rate**: the percentage of reported findings that were fixed.

To determine whether an issue was fixed, Cursor uses LLMs to review incremental diffs and assess whether the flagged issue was resolved.

## Viewing Runs

Every agent run is tracked in Automations. Each agent type's page lists **Recent Runs** for its own agents. Use the run history to see when an agent ran, which tools it used, its final status, and how long it took.

Open a run to inspect the underlying Cloud Agent for more detail about what the agent did. A review or scan that ran on Cursor-managed hosting has no Cloud Agent. Find a hosted review under **Recent Runs** on the Security Reviewer page, where it opens a read-only view of the review session.

![Security Agents run history in Automations](https://cursor.com/docs-static/images/security-review/recent-runs.png)

## Remediation Agents

Remediation agents check the findings produced by the scanner and help you verify and fix them.

For each finding, Cursor starts an agent that writes exploit tests to verify the issue and automatically patch the confirmed ones.

Find it in the [Vulnerability Remediation](https://cursor.com/automations/from-cursor/vulnerability-scanner) section and on each scanner's detail page.

### How it works

Each finding moves through four steps:

1. **Flagged.** Vulnerability Scanner reports the finding.
2. **Verified.** A verification agent writes tests against the real code path and runs them. It returns one of three verdicts:
   - **Confirmed**: the tests confirm the issue.
   - **Refuted**: the tests show the issue can't happen.
   - **Inconclusive**: the agent couldn't reach a conclusion.
3. **Tests PR.** For a confirmed finding, the verification agent opens a draft pull request with its tests. These tests fail on purpose until the issue is fixed.
4. **Fix PR.** A patch agent writes the fix, checks it against the tests, and opens a draft pull request for you to review.

Cursor never merges a fix for you. Merging is always your call.

### Remediation settings

Each Vulnerability Scanner has two remediation settings. Turn them on in the scanner's settings in Automations.

| Setting                                 | What it does                                                                 |
| :-------------------------------------- | :--------------------------------------------------------------------------- |
| **Verify new findings**                 | Starts a verification agent for each new finding the scanner reports.        |
| **Open fix PRs for confirmed findings** | Starts a patch agent for each confirmed finding, which opens a draft fix PR. |

### Reviewing findings

The Vulnerability Remediation section groups findings into tabs by what they need next:

| Tab               | What's in it                                                                                         |
| :---------------- | :--------------------------------------------------------------------------------------------------- |
| **Needs you**     | Findings with a fix PR to review, confirmed findings waiting for a patch, and inconclusive findings. |
| **In flight**     | Findings being verified or patched, and findings queued for either.                                  |
| **Agent-refuted** | Findings the verification agent showed aren't vulnerabilities.                                       |
| **Fixed**         | Findings whose fix PR has merged.                                                                    |
| **Not verified**  | Findings that haven't been queued for verification.                                                  |

Open a finding to take manual actions on it as needed.

### Vulnerability Remediation API

Enterprise teams can use the Vulnerability Remediation API to list findings, request verifications and fixes, and track their progress. Create an API key from [Cursor Dashboard → API Keys](https://cursor.com/dashboard/api) and authenticate with [Basic Authentication](https://cursor.com/docs/api.md#basic-authentication).

Each endpoint allows 20 requests per minute per team. List endpoints use cursor pagination: pass a response's `nextCursor` as `cursor` to read the next page. When `nextCursor` is `null`, there are no more pages.

If Vulnerability Remediation isn't enabled for your team, every endpoint returns `403 Forbidden`.

#### List findings

GET

`/security/findings`

Return the findings your team's Vulnerability Scanners have reported, sorted by repository and then by finding ID.

Requires an API key with `read:*` scope.

##### Query Parameters

`limit` number (optional)

Number of findings per page. Default: `50`, max: `100`.

`cursor` string (optional)

The `nextCursor` from the previous page.

```bash
curl --get https://api.cursor.com/security/findings \
  -u YOUR_API_KEY: \
  --data-urlencode 'limit=50'
```

**Response:**

```json
{
  "findings": [
    {
      "findingId": "3f2b8c1e-7a4d-4e2f-9b6a-1c5d8e0f2a47",
      "repository": "github:your-org/your-repo",
      "severity": "high",
      "title": "Missing authorization check on invoice export",
      "location": "src/billing/export.ts",
      "status": "active"
    }
  ],
  "nextCursor": "Z2l0aHViOnlvdXItb3JnL3lvdXItcmVwbwozZjJi..."
}
```

`severity` is `critical`, `high`, or `medium`. `status` is `active`, or `dismissed` if someone dismissed the finding.

#### Request verifications and fixes

POST

`/security/verifications`

Ask Cursor to verify findings, patch them, or both. The request returns as soon as the work is queued. Agents start within a few minutes.

Requires an API key with `admin:*` scope.

##### Request Body

`findingIds` string\[] (required)

Finding IDs from `GET /security/findings`. Send 1 to 50 IDs per request.

`verify` boolean (required)

When `true`, verify every finding that hasn't been verified. A finding that's already verified, or being verified, keeps its existing verification.

`patch` boolean (required)

Whether confirmed findings get a fix PR. Set `verify`, `patch`, or both to `true`.

- **Both**: verify, then open fix PRs for confirmed findings.
- **`verify` only**: verify without opening fix PRs.
- **`patch` only**: patch findings that already have a verdict, including refuted ones.

These flags override the scanner's **Open fix PRs for confirmed findings** setting.

```bash
curl --request POST \
  --url https://api.cursor.com/security/verifications \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "findingIds": ["3f2b8c1e-7a4d-4e2f-9b6a-1c5d8e0f2a47"],
    "verify": true,
    "patch": true
  }'
```

**Response (`202 Accepted`):**

```json
{
  "verifications": [
    {
      "findingId": "3f2b8c1e-7a4d-4e2f-9b6a-1c5d8e0f2a47",
      "verificationId": "3f2b8c1e-7a4d-4e2f-9b6a-1c5d8e0f2a47"
    }
  ],
  "skipped": []
}
```

Save each `verificationId` to track its progress. A finding that couldn't be queued appears in `skipped` with a reason:

- `finding_not_found`: no finding with this ID.
- `not_verifiable`: can't be verified, such as on an unsupported host.
- `not_verified`: no verdict yet to patch. Request `verify` first.

If your team doesn't have a running Vulnerability Scanner to take the request, the endpoint returns `409 Conflict`:

```json
{
  "code": "error",
  "message": "No vulnerability scanner is running for this team"
}
```

#### List verifications

GET

`/security/verifications`

Return your team's verifications, newest first.

Requires an API key with `read:*` scope.

##### Query Parameters

`limit` number (optional)

Number of verifications per page. Default: `50`, max: `100`.

`cursor` string (optional)

The `nextCursor` from the previous page.

```bash
curl --get https://api.cursor.com/security/verifications \
  -u YOUR_API_KEY: \
  --data-urlencode 'limit=50'
```

**Response:**

```json
{
  "verifications": [
    {
      "verificationId": "3f2b8c1e-7a4d-4e2f-9b6a-1c5d8e0f2a47",
      "findingId": "3f2b8c1e-7a4d-4e2f-9b6a-1c5d8e0f2a47",
      "repository": "github:your-org/your-repo",
      "commitSha": "9f3c2a1b7d8e4f5061728394a5b6c7d8e9f0a1b2",
      "severity": "high",
      "status": "completed",
      "verdict": "confirmed",
      "verifiedAt": "2026-10-20T18:04:11.000Z",
      "testsPrUrl": "https://github.com/your-org/your-repo/pull/128",
      "verificationAgent": {
        "id": "bc-5b1e9d2a-0c47-4f8e-a3d6-7e2b9c4f1a08",
        "url": "https://cursor.com/agents/bc-5b1e9d2a-0c47-4f8e-a3d6-7e2b9c4f1a08"
      },
      "patch": {
        "status": "completed",
        "agent": {
          "id": "bc-8d4a7f3c-2e19-4b6d-9a05-c1f7e8b3d264",
          "url": "https://cursor.com/agents/bc-8d4a7f3c-2e19-4b6d-9a05-c1f7e8b3d264"
        },
        "fixPrUrl": "https://github.com/your-org/your-repo/pull/129",
        "fixPrMerged": false
      }
    }
  ],
  "nextCursor": null
}
```

#### Get a verification

GET

`/security/verifications/{verificationId}`

Return one verification. Use this to poll a request until it finishes.

Requires an API key with `read:*` scope.

The response is a single verification object, in the same shape as the items in `GET /security/verifications`. See [Verification fields](https://cursor.com/docs/security-agents.md#verification-fields). If your team has no verification with that ID, the endpoint returns `404 Not Found`.

```bash
curl https://api.cursor.com/security/verifications/3f2b8c1e-7a4d-4e2f-9b6a-1c5d8e0f2a47 \
  -u YOUR_API_KEY:
```

#### Verification fields

| Field               | Description                                                                |
| :------------------ | :------------------------------------------------------------------------- |
| `verificationId`    | ID of the verification.                                                    |
| `findingId`         | Finding this verification checks.                                          |
| `repository`        | Repository, in `host:owner/repo` form.                                     |
| `commitSha`         | Commit the verification ran against. `null` until known.                   |
| `severity`          | Severity reported by the scanner.                                          |
| `status`            | Where the work stands. See the table below.                                |
| `verdict`           | `confirmed`, `refuted`, `inconclusive`, or `null` while verification runs. |
| `verifiedAt`        | When the verdict was reached. `null` until then.                           |
| `testsPrUrl`        | Draft pull request with the verification tests, when one was opened.       |
| `verificationAgent` | ID and URL of the verification agent. `null` until it starts.              |
| `patch`             | The fix, once Cursor decides whether to patch. `null` until then.          |
| `patch.status`      | Where the fix stands. See the table below.                                 |
| `patch.agent`       | ID and URL of the patch agent. `null` until it starts.                     |
| `patch.fixPrUrl`    | Draft pull request with the fix, once opened.                              |
| `patch.fixPrMerged` | `true` once the fix PR is merged.                                          |

`status` values:

| Value       | Meaning                                                   |
| :---------- | :-------------------------------------------------------- |
| `queued`    | Waiting for a verification agent to start.                |
| `verifying` | The verification agent is running.                        |
| `patching`  | Verification finished and a fix is queued or in progress. |
| `completed` | Nothing more is running for this finding.                 |

`patch.status` values:

| Value            | Meaning                                                          |
| :--------------- | :--------------------------------------------------------------- |
| `queued`         | Waiting for a patch agent to start.                              |
| `running`        | The patch agent is working on a fix.                             |
| `completed`      | The patch agent finished. Check `fixPrUrl` for the fix PR.       |
| `not_requested`  | No fix was requested for this finding.                           |
| `false_positive` | The finding was refuted, so no fix was needed.                   |
| `no_tests_pr`    | Verification ended without a verdict or tests to build a fix on. |
| `failed`         | The patch agent couldn't be started.                             |

#### Errors

Errors return a JSON body with a message:

```json
{
  "code": "error",
  "message": "Vulnerability verification is not enabled for this team"
}
```

| Status                  | When                                                                           |
| :---------------------- | :----------------------------------------------------------------------------- |
| `400 Bad Request`       | The request body or query is invalid, or the cursor wasn't issued by this API. |
| `401 Unauthorized`      | The API key is missing or doesn't have the required scope.                     |
| `403 Forbidden`         | Vulnerability Remediation isn't enabled for your team.                         |
| `404 Not Found`         | The verification doesn't exist for your team.                                  |
| `409 Conflict`          | Your team has no running Vulnerability Scanner.                                |
| `429 Too Many Requests` | You exceeded 20 requests per minute for this endpoint.                         |

#### Verify and fix findings

1. Call `GET /security/findings` and pick the findings you want to act on.
2. Call `POST /security/verifications` with their `findingIds`. Set `verify` and `patch` to `true` to verify them and open fix PRs for confirmed ones.
3. Save each returned `verificationId`.
4. Poll `GET /security/verifications/{verificationId}` until `status` is `completed`.
5. Review the pull request at `patch.fixPrUrl`.

## Related pages

- [Bugbot](https://cursor.com/docs/bugbot.md) reviews pull requests for bugs before they merge.
- [Rollouts](https://cursor.com/docs/rollouts.md) monitors each pull request as it deploys and reports its health in every environment.
