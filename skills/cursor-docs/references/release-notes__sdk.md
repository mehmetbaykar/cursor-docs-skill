---
title: "Cursor SDK release notes"
source: https://cursor.com/docs/release-notes/sdk
path: /docs/release-notes/sdk
---

# Cursor SDK release notes

The latest features, improvements, and fixes shipping to the Cursor SDK, covering `@cursor/sdk` on npm and `cursor-sdk` on PyPI.

## 1.0.35

- **Custom tools know which session called them.** The `execute` callback of a `local.customTools` entry now receives `context.sessionId`, the local session that invoked the tool. Subagents started with `Task` pass their own id, so a host can keep separate state for each child agent. TypeScript only; unset when the runtime has no session id.
- **Fixes to local agents and TypeScript types.** Local agents now work on FIPS-enabled hosts, and existing local agent stores move to the new location automatically. Agents restored from the same process or VM snapshot no longer reuse request and session IDs, so concurrent runs don't collide or get stuck. The `LocalSubagentInherit` type declarations now resolve without an unpublished internal package, using the newly exported `LocalSubagentResourceProviderFields` and `LocalToolExecutor` types.

## 1.0.34

- **Subagents can inherit the parent's executors and tool limits.** Set `local.subagentInherit` so that agents started by the `Task` tool, including nested ones, use the same custom read, write, and shell executors and reported workspace path as the parent, and the same allowed and excluded tools. Pass it on `Agent.create()` or override it for one `send`. TypeScript local agents only. If you leave it unset, subagents behave as they did before.
- **Fixed requests stalling on dropped connections in long-running agents.** When an agent sits idle between runs, the SDK now closes unused HTTP/2 connections after 29 seconds. It also checks a connection that has been quiet for about a minute before reusing it. Requests no longer get written into a connection the server has already closed, where they used to hang until the stall timeout aborted them.
- **Stalled connections are retryable and bounded.** When a connection stalls, the run fails with a retryable `NetworkError` carrying the code `connection_stalled`, and a streak of stall retries stops after 3 minutes instead of retrying indefinitely.
- **Fewer dependencies installed with the SDK.** Installing `@cursor/sdk` no longer adds `@connectrpc/connect-node` or `undici` 5.x to your project's dependency tree, so installs are smaller and you no longer get version conflicts or audit warnings from those packages.

## 1.0.32

- **Steer an agent while it waits on background subagents.** `run.steer(text)` used to resolve `revert_to_followup` when the agent had ended its turn to wait on background subagents, so your message waited until that work finished. Now the steer runs right away as the next turn, and background results still arrive afterward. TypeScript local runs only.
- **Know when a step has finished requesting tools.** `onDelta` now receives a `tool-requests-listed` update with a `callCount` once the model finishes listing its tool calls for a step, while those tools may still be running. Use it to tell when every tool call in a step has started, for example to group or batch a step's tool calls in your UI.
- **Fixes to cloud agent creation.** For cloud agents, the first `send()`, which creates the agent on the server, no longer fails with an id conflict when the SDK generated the agent id: it retries with a fresh id, or continues with the agent if its own earlier create already succeeded. SDK-generated agent and run ids also no longer repeat when a process is restored from the same snapshot more than once. Ids you pin yourself still report the conflict.
- **The bridge ignores your project's `.env` and `bunfig.toml`.** The standalone `cursor-sdk-bridge` executables no longer load `.env` or `bunfig.toml` from the working directory, which is usually your project when the SDK starts the bridge. Files in a checkout can no longer change the bridge's endpoints, tokens, or preloaded code.

## 1.0.31

- **Background subagents report back.** When the agent runs a subagent in the background, its result now returns to the parent as a follow-up turn on the same run instead of being dropped when the parent turn ends. `run.stream()` keeps yielding through those turns and `run.wait()` resolves after them. Local agents, in TypeScript and Python.
- **Annotate custom tools.** `annotations` on a `local.customTools` entry passes MCP tool annotations (`title`, `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`) through to the model. They are descriptive hints only; the SDK does not enforce them. TypeScript only.

## 1.0.30

- **Long-running local agents keep their credentials fresh.** Local runs in TypeScript and Python refresh the short-lived access token before it expires, so agents that run for more than an hour no longer fail with authentication errors. Cloud runs are unaffected.

## 1.0.29

- **Output schemas on custom tools.** `outputSchema` in TypeScript and `output_schema` in Python declare a JSON Schema for a custom tool's structured result, advertised to the model as the tool's MCP output schema. Results are not validated against it. Local agents only.

## 1.0.28

- **Ship the SDK as a single file.** Under Bun, `@cursor/sdk` now resolves to a flat single-file bundle, so `bun build --compile` works with no import change and no more `Cannot find module './986.js'`. `@cursor/sdk/bundled` and `@cursor/sdk/bundled/sqlite` expose the same build as explicit entries for other single-file bundlers such as esbuild. TypeScript only.

## 1.0.27

- **Restrict the agent's toolset.** `tools` allowlists the built-in tools offered to the model (`[]` means text-only), and `disallowedTools` removes tools while keeping the rest. Both take public names like `"read"` or capability groups like `"shell"` and `"mcp"`, in TypeScript and Python (`tools`, `disallowed_tools`). Local agents only for now, and not persisted across `resume`.
- **Log in from the browser in TypeScript.** `Cursor.auth.login()` opens a browser login, mints an API key, and stores it in `~/.cursor/sdk/auth.json`; `Cursor.auth.status()` and `Cursor.auth.logout()` round it out. After login, `Agent.create()` and the `Cursor.*` reads work without `apiKey` or `CURSOR_API_KEY`.
- **Usage and cost for local agents.** `agent.getUsage()` in TypeScript and `agent.get_usage()` in Python now work for local agents too, returning a per-turn breakdown. Pass a `runId` from a previous result to narrow to one turn.
- **Open PRs as the Cursor GitHub App.** `cloud.openAsCursorGithubApp` in TypeScript and `open_as_cursor_github_app` in Python control PR authorship. Service-account keys default to the app; user keys default to the key's owner.
- **Multi-root local workspaces.** Pass `local.dirs` to load rules, skills, and project context from several folders; `cwd` stays the single primary working directory. Replaces the `cwd` array form, which only ever used the first entry.
- **Clearer Python errors.** Failures that previously surfaced as a bare "internal error" now carry the underlying message and code.
- &#x20;**Admin command denylists apply to local runs.** Shell commands matching your team's admin denylist are rejected with a policy message before they execute, including on paths that skip approval prompts.

## 1.0.26

- **Warm up a local workspace before the first send.** `platform.prewarmLocalWorkspace(options)` resolves rules, skills, MCP servers, and ignore files ahead of time, so the first `send()` against that workspace starts immediately. It returns a release function to call on shutdown.
- **Control how long workspace scans stay cached.** `configureCursorSdk({ local: { workspaceScanCacheTtlMs } })` sets the cache lifetime for workspace scans, and the `CURSOR_RIPWALK_CACHE_TTL_MS` environment variable sets the same value for hosted deployments. Long-lived servers on stable checkouts can now skip repeated re-scans.
- **Custom tools run without approval prompts.** Host-defined tools passed via `customTools` no longer fail with an interactive-approval error on sandboxed or auto-review local runs. Deny rules and sandbox limits still apply.
- **Signed macOS binaries.** The `@cursor/sdk` macOS platform packages now ship code-signed binaries, so Gatekeeper and endpoint security tools no longer block them.
- **Cleaner Python exception hierarchy.** `PermissionDeniedError`, `BadRequestError`, and `InternalServerError` now inherit directly from `CursorSDKError` instead of `AuthenticationError`, `ConfigurationError`, and `NetworkError`, so `except` blocks catch what their names say.
- **Fixed intermittent startup failures in Python.** Roughly 1 in 64 agent launches failed before reaching the first send. Launches are now reliable.

## 1.0.25

- **Billed usage and cost on demand.** `agent.getUsage()` in TypeScript and `agent.get_usage()` in Python return token usage, billed cost, and a per-run breakdown for cloud agents, and `Agent.getUsage(agentId)` works without a handle. Cost is server-derived, includes discounts, and settles shortly after a run ends. Cloud-only for now; local runs throw a typed configuration error.

## 1.0.24

- **TypeScript and Python now release together.** Starting with 1.0.24, `@cursor/sdk` on npm and `cursor-sdk` on PyPI ship from the same release and share a version number. Python releases no longer trail TypeScript.
- **More reliable long-running streams.** Streaming responses on heavy runs no longer drop mid-stream, which previously surfaced as network errors in Python clients on long turns.

## 1.0.23

- **Per-send environment variables for cloud runs.** Pass `send(prompt, { cloud: { envVars } })` to scope env vars to a single run, including the first send that creates the agent. `Agent.create({ cloud: { envVars } })` still sets agent-scoped defaults.
- **Error details on failed runs.** Local and cloud runs that fail now expose a structured error with `message` and `code` fields, so you can tell what went wrong without parsing logs. `run.wait()` behaves the same as before.
- **Token usage in Python.** Run streams emit typed `usage` messages with per-turn token counts, and cumulative totals are available on `run.usage` and `RunResult.usage`, matching TypeScript from 1.0.22.
- **Sturdier local run history.** Run history on disk now survives interrupted writes, fixing a class of failures where a crashed process left runs that could not be resumed.
- **Fixed streaming stalls on Bun.** Run streams under Bun no longer stall on long responses.

## 1.0.22

- **Token usage on every run.** Local runs emit per-turn `usage` events on `run.stream()` and cumulative totals on `run.wait()`. Cloud runs surface the same usage on their stream and `wait()` results, and totals persist for detached local handles so a process that reattaches still gets them.

## 1.0.21

- **Run agents under Bun.** `agent.send()` now works under Bun with the same behavior as Node. This also fixes fresh Node installs that could miss a required dependency.
- **Friendlier runtime names in Python.** List APIs and `get_run` accept `runtime="cloud"`, `"local"`, and `"auto"`, matching the documented values.

## 1.0.20

- **The SDK imports cleanly under Bun.** Importing `@cursor/sdk` no longer crashes under Bun. Running agents under Bun follows in 1.0.21.
