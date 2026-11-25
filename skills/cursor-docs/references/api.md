---
title: "Cursor APIs Overview"
source: https://cursor.com/docs/api
path: /docs/api
---

# Cursor APIs Overview

Cursor provides multiple APIs for programmatic access to your team's data, AI-powered coding agents, and analytics.

## Available APIs

| API                                                                                   | Description                                                                                                          | Availability                   |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| [Admin API](https://cursor.com/docs/account/teams/admin-api.md)                       | Manage team members, settings, usage data, spending, and model access. Build custom dashboards and monitoring tools. | Enterprise teams               |
| [Analytics API](https://cursor.com/docs/account/teams/analytics-api.md)               | Comprehensive insights into team's Cursor usage, AI metrics, active users, and model usage.                          | Enterprise teams               |
| [AI Code Tracking API](https://cursor.com/docs/account/teams/ai-code-tracking-api.md) | Track AI-generated code contributions at commit and change levels for attribution and analytics.                     | Enterprise teams               |
| [Bugbot API](https://cursor.com/docs/bugbot.md#api)                                   | Trigger Bugbot reviews and retrieve per-review analytics.                                                            | Enterprise teams               |
| [Cloud Agents API](https://cursor.com/docs/cloud-agent/api/endpoints.md)              | Programmatically create and manage AI-powered coding agents for automated workflows and code generation.             | Beta (plans with Cloud Agents) |
| [Origin API](https://cursor.com/docs/api/origin.md)                                   | Work with Origin repositories, commits, checks, pull requests, and app installations.                                | Early Beta                     |
| [TypeScript SDK](https://cursor.com/docs/sdk/typescript.md)                           | Run Cursor agents from TypeScript with one interface for local and cloud runtimes.                                   | All users                      |
| [Python SDK](https://cursor.com/docs/sdk/python.md)                                   | Run Cursor agents from Python with sync and async clients for local and cloud runtimes.                              | All users                      |
| [SDK Bridge](https://cursor.com/docs/sdk/bridge.md)                                   | Build agent SDKs in other languages on the open bridge protocol and standalone binaries.                             | All users                      |

The Cloud Agents API and SDKs run Cursor agent workflows (workspace context, tools, commands, and edits). They are not a standalone model-inference or chat-completions API. [Cursor Router](https://cursor.com/docs/cursor-router.md) selects models for those agent runs when you use Auto / `auto-smart`; see [Router in the TypeScript SDK](https://cursor.com/docs/sdk/typescript.md#cursor-router) or [Python SDK](https://cursor.com/docs/sdk/python.md#cursor-router).

## Authentication

The Admin, Analytics, AI Code Tracking, and Bugbot APIs accept Basic Authentication. The Cloud Agents API accepts Basic or Bearer authentication. The Origin API uses Bearer credentials through the Origin CLI or an Origin App.

### Basic Authentication

Use your API key as the username in basic authentication (leave password empty):

```bash
curl https://api.cursor.com/teams/members \
  -u YOUR_API_KEY:
```

Or set the Authorization header directly:

```bash
Authorization: Basic {base64_encode('YOUR_API_KEY:')}
```

### Bearer Authentication (Cloud Agents API)

The [Cloud Agents API](https://cursor.com/docs/cloud-agent/api/endpoints.md) also accepts `Authorization: Bearer <key>` headers. Both schemes behave identically — use whichever your HTTP client makes easier:

```bash
curl https://api.cursor.com/v1/me \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Creating API Keys

Team administrators can create and manage API keys from the API Keys page in the dashboard.

#### Admin API & AI Code Tracking API

1. Navigate to **cursor.com/dashboard** → **API Keys**
2. Click **New API Key**
3. Give your key a descriptive name (e.g., "Usage Dashboard Integration")
4. Copy the generated key immediately. You won't see it again

Key format: `crsr_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

Required scope: `admin:*`

#### Analytics API

Generate an API key from [Cursor Dashboard → API Keys](https://cursor.com/dashboard/api).

#### Cloud Agents API

Create a user API key from [Cursor Dashboard → API Keys](https://cursor.com/dashboard/api), or use a [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md) from team settings.

API keys are tied to your organization and viewable by all admins. Keys are unaffected by the original creator's account status.

#### Origin API

For user-authenticated requests, sign in with the Origin CLI or provide it a personal user API key. The CLI exchanges the key for a short-lived access token before it calls Origin. Team Admin API keys with the `admin:*` scope do not authenticate to Origin. Apps use app JWTs and installation access tokens. See [Origin API authentication](https://cursor.com/docs/api/origin/reference/authentication.md).

## Rate Limits

All APIs implement rate limiting to ensure fair usage and system stability. Limits apply per authenticated user, team, or organization, and most are scoped to a single endpoint. Unless an endpoint documents a different limit, the default is 20 requests per minute.

### Rate Limits by API

| API                      | Endpoint Type                                                             | Rate Limit                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Admin API**            | Most endpoints                                                            | 20 requests/minute                                                                                                                         |
| **Admin API**            | `/teams/filtered-usage-events` and `/organizations/filtered-usage-events` | 60 requests/minute                                                                                                                         |
| **Admin API**            | `/v2/teams/billing-items`                                                 | 60 requests/minute                                                                                                                         |
| **Admin API**            | `/teams/user-spend-limit`                                                 | 250 requests/minute                                                                                                                        |
| **Admin API**            | `/teams/user-spend-limits`                                                | 20 requests/minute                                                                                                                         |
| **Organization API**     | Most endpoints                                                            | 20 requests/minute per endpoint                                                                                                            |
| **Organization API**     | `GET /organizations/teams/{teamId}/grok-bot/operations/*`                 | 120 requests/minute per endpoint                                                                                                           |
| **Analytics API**        | Most team-level endpoints                                                 | 100 requests/minute                                                                                                                        |
| **Analytics API**        | `/analytics/team/conversation-insights`                                   | 20 requests/minute                                                                                                                         |
| **Analytics API**        | By-user endpoints                                                         | 50 requests/minute                                                                                                                         |
| **AI Code Tracking API** | All endpoints                                                             | 20 requests/minute per endpoint                                                                                                            |
| **Bugbot API**           | `/bugbot/review`                                                          | 30 requests/minute                                                                                                                         |
| **Bugbot API**           | `/bugbot/review` with `dryRun: true`                                      | 10 requests/minute (in addition to the trigger limit)                                                                                      |
| **Cloud Agents API**     | Every endpoint                                                            | A per-minute and a per-hour limit for each endpoint. See [Cloud Agents API limits](https://cursor.com/docs/api.md#cloud-agents-api-limits) |

### Cloud Agents API limits

Each Cloud Agents API endpoint has its own budget, and a request must fit under both its per-minute and its per-hour limit.

- **Budgets belong to the caller, not the key.** Requests with a service account API key count against the service account, so every key on one service account shares one budget. Requests with a user API key count against the user, across all of that user's keys.
- **Windows start with the first request.** Each window opens on the first request it counts and resets a minute or an hour later, not on the clock minute or hour.
- **The numbers are defaults.** Cursor can adjust them for a team, raising or lowering any limit. On a `429`, the `X-RateLimit-Limit` header shows the limit that applied.

| Endpoint                                                   | Per minute | Per hour |
| ---------------------------------------------------------- | ---------: | -------: |
| `POST /v1/agents`                                          |        100 |    1,000 |
| `GET /v1/agents`                                           |        200 |    4,000 |
| `GET /v1/agents/{id}`                                      |        300 |    6,000 |
| `GET /v1/agents/{id}/stream`                               |         60 |      600 |
| `POST /v1/agents/{id}/runs`                                |         30 |      300 |
| `GET /v1/agents/{id}/runs`                                 |        300 |    6,000 |
| `GET /v1/agents/{id}/runs/{runId}`                         |        300 |    6,000 |
| `GET /v1/agents/{id}/runs/{runId}/stream`                  |         20 |      600 |
| `POST /v1/agents/{id}/runs/{runId}/cancel`                 |        100 |    1,000 |
| `GET /v1/agents/{id}/usage`                                |        300 |    6,000 |
| `GET /v1/agents/{id}/artifacts`                            |        300 |    6,000 |
| `GET /v1/agents/{id}/artifacts/download`                   |        300 |    6,000 |
| `POST /v1/agents/{id}/archive`                             |        100 |    1,000 |
| `POST /v1/agents/{id}/unarchive`                           |        100 |    1,000 |
| `DELETE /v1/agents/{id}`                                   |        100 |    1,000 |
| `POST /v1/environments`                                    |         20 |      200 |
| `GET /v1/environments`                                     |         60 |    1,200 |
| `GET /v1/environments/{id}`                                |        300 |    1,200 |
| `PATCH /v1/environments/{id}`                              |         20 |      200 |
| `DELETE /v1/environments/{id}`                             |         20 |      200 |
| `GET /v1/environments/{id}/history`                        |         20 |      600 |
| `GET /v1/environments/{id}/builds`                         |        300 |    1,200 |
| `POST /v1/environments/{id}/builds`                        |         20 |      200 |
| `GET /v1/environments/{id}/builds/{buildId}`               |        300 |    1,200 |
| `GET /v1/environments/{id}/builds/active`                  |        300 |    1,200 |
| `GET /v1/secrets`                                          |         60 |    1,200 |
| `GET /v1/environments/{id}/secrets`                        |        300 |    1,200 |
| `PUT` or `DELETE /v1/environments/{id}/secrets/{name}`     |   300 each | 600 each |
| `GET /v1/team/secrets`                                     |         60 |    1,200 |
| `PUT` or `DELETE /v1/team/secrets/{name}`                  |   300 each | 600 each |
| `PUT` or `DELETE /v1/me/secrets/{name}`                    |   300 each | 600 each |
| `GET /v1/automations`                                      |         60 |    1,200 |
| `GET /v1/automations/{id}`                                 |         60 |    1,200 |
| `PATCH /v1/automations/{id}`                               |         20 |      200 |
| `POST /v1/sub-tokens`                                      |         30 |      600 |
| `GET /v1/me`                                               |         60 |    1,200 |
| `GET /v1/models`                                           |         30 |    1,800 |
| `POST /v1/models/estimate-cost`                            |        600 |   12,000 |
| `GET /v1/repositories`                                     |          5 |       30 |
| `GET /v0/private-workers`                                  |         30 |      600 |
| `GET /v0/private-workers?workerIds=`                       |        120 |    7,200 |
| `GET /v0/private-workers/summary`                          |         60 |    1,200 |
| `GET /v0/private-workers/{id}`                             |         60 |    3,600 |
| `GET /v0/private-workers/{id}` with a team service account |        600 |   24,000 |
| `GET /v0/private-workers/pools`                            |        300 |    6,000 |
| `POST /v0/private-workers/pools`                           |        300 |    6,000 |
| `DELETE /v0/private-workers/pools`                         |         30 |      600 |
| `GET /v0/private-workers/pending-requests`                 |        300 |    6,000 |
| `GET /v0/private-workers/pending-requests/stream`          |        200 |    6,000 |
| `POST /v0/private-workers/claim`                           |        600 |   12,000 |
| `POST /v0/private-workers/tokens`                          |        600 |   12,000 |
| `POST /v0/private-workers/worker-session`                  |        600 |   12,000 |
| `POST /v0/private-workers/claims/{id}/release`             |         60 |    1,200 |
| `POST /v0/private-workers/claims/{id}/fail`                |        600 |   12,000 |

A `PUT` and a `DELETE` on the same secrets path each have their own budget.

Two private-worker reads pick their budget from the request. `GET /v0/private-workers` with a `workerIds` query looks up several workers in one call and draws from its own budget, not the list budget. `GET /v0/private-workers/{id}` called with a team service account's credentials, which is how a pool controller calls it, gets the larger budget, because a controller reads every live worker on each pass. Other callers, user API keys included, stay on 60 per minute and 3,600 per hour.

The [legacy v0 routes](https://cursor.com/docs/cloud-agent/api/v0.md) share the budget of the matching v1 route, so v0 and v1 calls add up:

| v0 route                                               | Shares the budget of                      |
| ------------------------------------------------------ | ----------------------------------------- |
| `POST /v0/agents`                                      | `POST /v1/agents`                         |
| `GET /v0/agents`                                       | `GET /v1/agents`                          |
| `GET /v0/agents/{id}`                                  | `GET /v1/agents/{id}`                     |
| `POST /v0/agents/{id}/followup`                        | `POST /v1/agents/{id}/runs`               |
| `DELETE /v0/agents/{id}`                               | `POST /v1/agents/{id}/archive`            |
| `GET /v0/agents/{id}/artifacts`                        | `GET /v1/agents/{id}/artifacts`           |
| `GET /v0/agents/{id}/artifacts/download`               | `GET /v1/agents/{id}/artifacts/download`  |
| `GET /v0/agents/{id}/conversation/stream-state`        | `GET /v1/agents/{id}/runs/{runId}/stream` |
| `GET /v0/automations`                                  | `GET /v1/automations`                     |
| `GET /v0/automations/{id}`                             | `GET /v1/automations/{id}`                |
| `GET /v0/me`, `GET /v0/models`, `GET /v0/repositories` | The matching `/v1` route                  |

`DELETE /v0/agents/{id}` archives the agent, so it draws from the archive budget, not the budget of `DELETE /v1/agents/{id}`.

These v0 routes have budgets of their own:

| v0 route                                  | Per minute | Per hour |
| ----------------------------------------- | ---------: | -------: |
| `GET /v0/agents/{id}/conversation`        |        300 |    6,000 |
| `GET /v0/agents/{id}/conversation/stream` |         20 |      600 |
| `GET /v0/agents/{id}/logs/stream`         |         10 |      600 |
| `POST /v0/agents/{id}/stop`               |        100 |    1,000 |

### Rate Limit Response

When you exceed the rate limit, you'll receive a `429 Too Many Requests` response. Admin and Organization API responses include `Retry-After: 60` and this body:

```json
{
  "code": "error",
  "message": "Rate limit exceeded"
}
```

Cloud Agents API responses include these headers:

| Header                  | Value                                          |
| ----------------------- | ---------------------------------------------- |
| `X-RateLimit-Limit`     | The limit you exceeded, per minute or per hour |
| `X-RateLimit-Remaining` | `0`                                            |
| `X-RateLimit-Reset`     | Unix time, in seconds, when that window resets |
| `Retry-After`           | Seconds until that window resets               |

The message names the limit, the window, and the endpoint. `/v1` routes return:

```json
{
  "error": {
    "code": "rate_limit_exceeded",
    "message": "You have exceeded the rate limit of 300 requests per hour for the add_followup endpoint (request ID: 9b2c4e1a-5f3d-4a8e-b7c6-2d1e0f9a8b7c)."
  }
}
```

`/v0` routes, including `/v0/private-workers`, return:

```json
{
  "error": "Rate limit exceeded",
  "message": "You have exceeded the rate limit of 30 requests per minute for the add_followup endpoint (request ID: 9b2c4e1a-5f3d-4a8e-b7c6-2d1e0f9a8b7c). Contact hi@cursor.com if you need a higher limit."
}
```

Wait for `Retry-After` seconds before you retry the same endpoint.

## Caching

Several APIs support HTTP caching with ETags to reduce bandwidth usage and improve performance.

### Supported APIs

- **Analytics API**: All endpoints (both team-level and by-user) support HTTP caching
- **AI Code Tracking API**: Endpoints support HTTP caching

### How Caching Works

1. **Initial Request**: Make a request to any supported endpoint
2. **Response Includes ETag**: The API returns an `ETag` header in the response
3. **Subsequent Requests**: Include the `ETag` value in an `If-None-Match` header
4. **304 Not Modified**: If data hasn't changed, you'll receive a `304 Not Modified` response with no body

### Example

```bash
# Initial request
curl -X GET "https://api.cursor.com/analytics/team/dau" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -D headers.txt

# Response includes: ETag: "abc123xyz"

# Subsequent request with ETag
curl -X GET "https://api.cursor.com/analytics/team/dau" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "If-None-Match: \"abc123xyz\""

# Returns 304 Not Modified if data hasn't changed
```

### Cache Duration

- Cache duration: 15 minutes (`Cache-Control: public, max-age=900`)
- Responses include an `ETag` header
- Include `If-None-Match` header in subsequent requests to receive `304 Not Modified` when data hasn't changed

### Benefits

- **Reduces bandwidth usage**: 304 responses contain no body
- **Faster responses**: Avoids processing unchanged data
- **Rate limit friendly**: 304 responses don't count against rate limits
- **Better performance**: Especially useful for frequently polled endpoints

## Best Practices

### 1. Implement Exponential Backoff

When you receive a 429 response, wait before retrying with increasing delays:

```python
import time
import requests

def make_request_with_backoff(url, headers, max_retries=5):
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            # Exponential backoff: 1s, 2s, 4s, 8s, 16s
            wait_time = 2 ** attempt
            print(f"Rate limited. Waiting {wait_time}s before retry...")
            time.sleep(wait_time)
            continue

        return response

    raise Exception("Max retries exceeded")
```

### 2. Distribute Requests Over Time

Spread your API calls over time rather than making burst requests:

- Schedule batch jobs to run at different intervals
- Add delays between requests when processing large datasets
- Use queuing systems to smooth out traffic spikes

### 3. Leverage Caching

**For Analytics API and AI Code Tracking API:**

These APIs support HTTP caching with ETags. See the [Caching](https://cursor.com/docs/api.md#caching) section above for details on how to use ETags to reduce bandwidth usage and avoid unnecessary requests.

**Key benefits:**

- Reduces bandwidth usage
- Faster responses when data hasn't changed
- Doesn't count against rate limits (for 304 responses)

Use date shortcuts (`7d`, `30d`) instead of timestamps for better caching support in Analytics API.

### 4. Monitor Your Usage

Track your request patterns to stay within limits:

- Log API call timestamps and response codes
- Set up alerts for 429 responses
- Monitor daily/weekly usage trends
- Adjust polling intervals based on actual needs

### 5. Batch Wisely

For endpoints with pagination:

- Use appropriate page sizes to get more data per request
- For Analytics API by-user endpoints: Use `users` parameter to filter specific users
- For large data extractions: Use CSV endpoints when available (they stream data efficiently)

### 6. Poll at Appropriate Intervals

Don't over-poll endpoints that update infrequently:

- **Admin API** `/teams/daily-usage-data`: Poll at most once per hour (data aggregated hourly)
- **Admin API** `/teams/filtered-usage-events`: Poll at most once per hour (data aggregated hourly)
- **Admin API** `/organizations/pooled-usage`: Poll at most once per hour (data aggregated hourly)
- **Admin API** `/organizations/filtered-usage-events`: Poll at most once per hour (data aggregated hourly)
- **Analytics API**: Use date shortcuts (`7d`, `30d`) for better caching support
- **AI Code Tracking API**: Data is ingested in near real-time but polling every few minutes is sufficient

### 7. Handle Errors Gracefully

Implement proper error handling for all API calls:

```javascript
async function fetchAnalytics(endpoint) {
  try {
    const response = await fetch(`https://api.cursor.com${endpoint}`, {
      headers: {
        'Authorization': `Basic ${btoa(API_KEY + ':')}`
      }
    });

    if (response.status === 429) {
      // Rate limited - implement backoff
      throw new Error('Rate limit exceeded');
    }

    if (response.status === 401) {
      // Invalid API key
      throw new Error('Authentication failed');
    }

    if (response.status === 403) {
      // Insufficient permissions
      throw new Error('Enterprise access required');
    }

    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('API request failed:', error);
    throw error;
  }
}
```

## Common Error Responses

All APIs use standard HTTP status codes:

### 400 Bad Request

Request parameters are invalid or missing required fields.

```json
{
  "error": "Bad Request",
  "message": "Some users are not in the team"
}
```

### 401 Unauthorized

Invalid or missing API key.

```json
{
  "error": "Unauthorized",
  "message": "Invalid API key"
}
```

### 403 Forbidden

Valid API key but insufficient permissions (e.g., Enterprise features on non-Enterprise plan).

```json
{
  "error": "Forbidden",
  "message": "Enterprise access required"
}
```

### 404 Not Found

Requested resource doesn't exist.

```json
{
  "error": "Not Found",
  "message": "Resource not found"
}
```

### 429 Too Many Requests

Rate limit exceeded. Implement exponential backoff.

```json
{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded. Please try again later."
}
```

### 500 Internal Server Error

Server-side error. Contact support if persistent.

```json
{
  "error": "Internal Server Error",
  "message": "An unexpected error occurred"
}
```
