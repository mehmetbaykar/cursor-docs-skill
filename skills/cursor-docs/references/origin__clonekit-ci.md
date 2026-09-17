---
title: "Set up CloneKit in CI with `origin repo clone-fast`"
source: https://cursor.com/docs/origin/clonekit-ci
path: /docs/origin/clonekit-ci
---

# Set up CloneKit in CI with `origin repo clone-fast`

Origin is currently released in early beta. You can create repos, push and pull with git, mirror from GitHub, browse and search code, open and merge pull requests, and share with your Cursor team.

Please submit any and all feedback to [hi@cursor.com](mailto:hi@cursor.com) to help us make the product better.

`origin repo clone-fast` replaces `git clone` in CI jobs. Instead of cloning from scratch, it downloads a prebuilt clone kit, a packed snapshot of the repository that Cursor builds for each repository with CloneKit turned on, then fetches only the objects added since the kit was built. This page shows how to get a short-lived Origin token onto the runner and run the command in [Buildkite](https://cursor.com/docs/origin/clonekit-ci.md#buildkite), [GitHub Actions](https://cursor.com/docs/origin/clonekit-ci.md#github-actions), and [other CI systems](https://cursor.com/docs/origin/clonekit-ci.md#other-ci-systems).

## How it works

Each run of `origin repo clone-fast {owner}/{repo} [DIR]` does the following:

1. Fetches the kit manifest from Origin with the token in `CURSOR_AUTH_TOKEN`. The manifest lists the kit's artifacts and the commit at its tip.
2. Downloads the pack artifacts from `gitcdn.origin.cursor.com` and checks their sizes. With `--verify`, it also checks their hashes while the download runs.
3. Installs them into the destination directory, which must be empty.
4. Tops up the clone: fetches the objects added since the kit was built and checks out the current tip of the default branch. With `--no-top-up`, the checkout stays at the kit's tip. `--bare` creates a bare repository with no working tree.

When the kit path succeeds, the command prints `mode: clone-kit` on stdout. If any step fails, the default `--fallback auto` runs a plain `git clone` instead and prints `mode: git-clone`. Pass `--fallback never` to exit with status 1 instead.

The token and the checkout behave the same way on every CI system:

- **Tokens expire after at most 15 minutes and cannot be refreshed.** Mint one immediately before the clone.
- **The CLI reads the token from `CURSOR_AUTH_TOKEN`.** Export it in the shell that runs `origin`.
- **The clone ends on the default branch tip.** To build a specific commit, run `git fetch origin SHA` and `git checkout SHA` afterwards. Origin serves any reachable commit by SHA.

## Prerequisites

CloneKit is available on Enterprise plans and is turned on per repository; there is no self-serve toggle. Contact your Cursor account team to turn it on for each repository you clone. `origin repo clone-fast --help` lists the command's options.

- The Origin CLI on the runner. Install it with `curl -fsSL https://downloads.cursor.com/origin/install.sh | sh`, which puts the binary at `$HOME/.local/bin/origin`. Linux runners need glibc on x64 or arm64; Alpine and other musl images are not supported. macOS runners are supported. See [Install the Origin CLI](https://cursor.com/docs/origin/cli.md).
- bash, git, jq, curl 7.55 or later, and openssl 1.1.1 or later. `clone-fast` uses `curl` for its downloads.
- Network egress to these hosts:

| Host                       | Used for                                                   |
| -------------------------- | ---------------------------------------------------------- |
| `downloads.cursor.com`     | Installing the CLI                                         |
| `origin.cursor.com`        | The kit manifest and git operations                        |
| `gitcdn.origin.cursor.com` | Kit downloads                                              |
| `api.cursor.com`           | Minting tokens and mirror sync requests from an Origin App |

## Choose a path

| CI system                                                                                 | Where the token comes from                    | Section                                                                            |
| ----------------------------------------------------------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------- |
| Buildkite, hosted or self-hosted agents, with Origin connected as the repository provider | The Buildkite Agent API, in a `checkout` hook | [Buildkite](https://cursor.com/docs/origin/clonekit-ci.md#buildkite)               |
| GitHub Actions                                                                            | Your Origin App, in a workflow step           | [GitHub Actions](https://cursor.com/docs/origin/clonekit-ci.md#github-actions)     |
| GitLab CI, Jenkins, CircleCI, and self-hosted fleets                                      | Your Origin App, in the job                   | [Other CI systems](https://cursor.com/docs/origin/clonekit-ci.md#other-ci-systems) |

## Buildkite

Buildkite mints the token for you. Replace the agent's default git checkout with a `checkout` hook that requests a token from the Buildkite Agent API and runs `origin repo clone-fast`.

You must be a Buildkite organization administrator to connect Origin, and an Origin administrator to install the Buildkite app.

### Connect Origin to Buildkite

In Buildkite, select **Settings** > **Repository Providers** > **Add Provider** > **Origin**, or select **Connect Origin account** on the New Pipeline page. Select the owner and the repositories, then install the Buildkite app. Buildkite requests read access to repository contents and pull requests, and read and write access to checks. For details, see [Origin](https://buildkite.com/docs/pipelines/source-control/origin) in the Buildkite documentation.

### Install the Origin CLI on the agent

Follow the [Prerequisites](https://cursor.com/docs/origin/clonekit-ci.md#prerequisites), with `curl`, `git`, and `jq` on `PATH`.

### Keep the checkout directory empty

If the agent keeps its build directory between builds, empty `$BUILDKITE_BUILD_CHECKOUT_PATH` before the hook runs. `clone-fast` needs an empty directory and falls back to `git clone` when it finds files there.

### Add the checkout hook

On a self-hosted agent, save the script below as `checkout` in the agent's `--hooks-path` directory. On Buildkite hosted agents, ship it as the `checkout` hook of a non-vendored plugin, or set `checkout: { skip: true }` on the step and run the same commands in the step's `command`. A repository hook cannot define `checkout`, because the repository is not checked out yet. See [Agent hooks](https://buildkite.com/docs/agent/hooks) and [Git checkout](https://buildkite.com/docs/pipelines/configure/git-checkout) in the Buildkite documentation.

The hook requests a token scoped to the pipeline's repository, exports it as `CURSOR_AUTH_TOKEN`, clones with `clone-fast`, registers the git credential helper with `origin auth setup-git`, and checks out `$BUILDKITE_COMMIT`. The agent token reaches `curl` through stdin, so it never appears on a command line:

```bash
#!/usr/bin/env bash
set -euo pipefail

body=$(printf '{"repo_url":"%s"}' "$BUILDKITE_REPO")
token=$(printf 'Authorization: Token %s\n' "$BUILDKITE_AGENT_ACCESS_TOKEN" \
  | curl -fsS -X POST -H @- \
      -H 'Content-Type: application/json' -H 'Accept: application/json' \
      --data "$body" \
      "${BUILDKITE_AGENT_ENDPOINT%/}/jobs/${BUILDKITE_JOB_ID}/cursor_origin_access_token" \
  | jq -er '.token')

# clone-fast takes owner/repo, not the clone URL.
repo=${BUILDKITE_REPO#https://origin.cursor.com/}
repo=${repo#git/}
repo=${repo%.git}

export CURSOR_AUTH_TOKEN="$token"
origin repo clone-fast "$repo" "$BUILDKITE_BUILD_CHECKOUT_PATH" --verify
origin auth setup-git
cd "$BUILDKITE_BUILD_CHECKOUT_PATH"
git fetch origin "$BUILDKITE_COMMIT"
git checkout -q "$BUILDKITE_COMMIT"
```

When a build starts without a commit, `BUILDKITE_COMMIT` is `HEAD`. The two `git` lines then fetch the remote `HEAD` and leave the working tree on the default branch tip that `clone-fast` already checked out.

- **Send `$BUILDKITE_REPO` unchanged.** `repo_url` must match the repository URL registered on the pipeline exactly, including `.git`. A different spelling returns HTTP 400.
- **The token is read-only and scoped to the pipeline's repository.** It carries `repository:contents:read` and expires after 15 minutes. A later job, or a git operation more than 15 minutes after the mint, needs a fresh token from the same request.
- **Retry on 503.** If the Agent API answers HTTP 503, wait for its `Retry-After` header and retry, as Buildkite's own credential helper does.

## GitHub Actions and other CI providers

GitHub Actions and other CI systems mint their own tokens. You create an Origin App once, install it on the repositories you clone, and give each job the app's private key and two ids. The job signs a short-lived app JWT and exchanges it for an installation token. For the full field reference, see [App JWT](https://cursor.com/docs/api/origin/llms-full.txt#app-jwt) and [Create Installation Access Token](https://cursor.com/docs/api/origin/llms-full.txt#create-installation-access-token).

### Create an Origin App

You must be a workspace admin to install the app.

#### Register the app

### Generate an Ed25519 key pair

Only Ed25519 keys are accepted:

```bash
openssl genpkey -algorithm ED25519 -out origin-app-private.pem
openssl pkey -in origin-app-private.pem -pubout -out origin-app-public.pem
```

### Create the app and add the public key

In [Origin app settings](https://cursor.com/codebase/settings/apps), create the app and add the contents of `origin-app-public.pem` as a signing key. An app holds up to 10 active signing keys.

### Copy the App ID

The App ID is on the app's page. App IDs start with `app_`.

#### Install the app

### Install the app on your owner

From the app's install page in the same settings, install the app on the owner that holds the repositories you clone, and select those repositories.

### Copy the installation id

The installation id is in the URL of the installation's page, `/codebase/settings/apps/installations/{installationId}`. Installation ids start with `i_`.

To read installation ids programmatically, call [List App Installations](https://cursor.com/docs/api/origin/llms-full.txt#list-app-installations) with an app JWT as the bearer. The response includes each installation's `id`, `target.slug`, `scopes`, and `repoSelectionMode`.

#### Store the credentials

Store the private key as a secret in your CI system and expose it to the job as the environment variable `ORIGIN_APP_PRIVATE_KEY`, containing the full PEM text. Store the App ID and the installation id as the plain variables `ORIGIN_APP_ID` and `ORIGIN_INSTALLATION_ID`. If your CI system mounts secrets as files, load the key first with `ORIGIN_APP_PRIVATE_KEY=$(cat /path/to/origin-app-private.pem)`.

#### Mint a token in the job

The function below signs the app JWT and exchanges it for an installation token. The JWT uses `alg` `EdDSA`, sets `iss` and `kid` to the App ID and `aud` to `origin-apps`, and sets `exp` 15 minutes ahead. The [App JWT](https://cursor.com/docs/api/origin/llms-full.txt#app-jwt) reference suggests a lifetime of about five minutes; because an installation token never outlives the JWT that minted it, this recipe signs a 15-minute JWT so the token gets its full 15 minutes. The request asks for `repository:contents:read`, which covers clone, fetch, and pull. Push needs `repository:contents:write`, and the installation must have granted that scope. Add `"repositoryIds":[...]` to the request body to narrow the token to some of the installation's repositories.

The private key reaches `openssl` through a file descriptor and the bearer header reaches `curl` through stdin, so neither appears on a command line, where other processes on the runner could read it. The function sets and exports `CURSOR_AUTH_TOKEN` directly, so the token never touches a file, and a failed mint stops the job under `set -e`. It needs bash, openssl 1.1.1 or later, curl 7.55 or later, and jq:

```bash
origin_app_token() {
  b64url() { openssl base64 -A | tr '+/' '-_' | tr -d '='; }
  now=$(date +%s)
  header=$(printf '{"alg":"EdDSA","kid":"%s","typ":"JWT"}' "$ORIGIN_APP_ID" | b64url)
  claims=$(printf '{"iss":"%s","aud":"origin-apps","iat":%d,"exp":%d}' \
    "$ORIGIN_APP_ID" "$now" "$((now + 900))" | b64url)
  # openssl -rawin needs a seekable input; the signing input holds no secret.
  signing_input=$(mktemp)
  trap 'rm -f "$signing_input"' EXIT
  printf '%s.%s' "$header" "$claims" > "$signing_input"
  signature=$(openssl pkeyutl -sign -rawin -in "$signing_input" \
    -inkey <(printf '%s\n' "$ORIGIN_APP_PRIVATE_KEY") | b64url)
  app_jwt="$header.$claims.$signature"
  CURSOR_AUTH_TOKEN=$(printf 'Authorization: Bearer %s\n' "$app_jwt" \
    | curl -fsS -X POST -H @- -H 'Content-Type: application/json' \
        --data '{"scopes":["repository:contents:read"]}' \
        "https://api.cursor.com/v1/origin/app/installations/${ORIGIN_INSTALLATION_ID}/access_tokens" \
    | jq -er '.token')
  export CURSOR_AUTH_TOKEN
}
```

Call it immediately before the clone into an empty directory, then register the git credential helper so later git commands authenticate while `CURSOR_AUTH_TOKEN` stays exported. Replace `acme/widgets` with your repository and `COMMIT_SHA` with the commit your CI system exposes for the build:

```bash
set -euo pipefail

origin_app_token
origin repo clone-fast acme/widgets . --verify
origin auth setup-git
git fetch origin "$COMMIT_SHA"
git checkout -q "$COMMIT_SHA"
```

### GitHub Actions

GitHub Actions uses the [Origin App](https://cursor.com/docs/origin/clonekit-ci.md#create-an-origin-app) path, with the private key in an Actions secret and the two ids in repository variables. Because GitHub fires the workflow, the repository lives on GitHub and Origin holds it as a [mirror](https://cursor.com/docs/origin/mirror-github.md). The workflow asks Origin to pull the build's commit, clones with `clone-fast` into the empty `$GITHUB_WORKSPACE`, then checks that commit out. It never calls GitHub, so it needs no `GITHUB_TOKEN` permissions and does not use `actions/checkout`.

### Add the secret

In your repository, select **Settings** > **Secrets and variables** > **Actions**, then add the secret `ORIGIN_APP_PRIVATE_KEY` with the full private key PEM.

### Add the variables

On the same page, add the repository variables `ORIGIN_APP_ID` and `ORIGIN_INSTALLATION_ID`.

### Add the workflow

Save the workflow below as `.github/workflows/ci.yml`, set `ORIGIN_REPO` to the mirror's `{owner}/{repo}` on Origin, and add your build steps after the clone step.

The workflow installs the CLI, mints a token, waits for Origin to mirror the commit, and clones it:

```yaml
name: ci

on:
  push:
    branches: [main]
  pull_request:

permissions: {}

jobs:
  build:
    runs-on: ubuntu-latest
    defaults:
      run:
        shell: bash
    steps:
      - name: Install the Origin CLI
        run: |
          curl -fsSL https://downloads.cursor.com/origin/install.sh | sh
          echo "$HOME/.local/bin" >> "$GITHUB_PATH"

      - name: Clone from Origin with clone-fast
        env:
          ORIGIN_APP_ID: ${{ vars.ORIGIN_APP_ID }}
          ORIGIN_INSTALLATION_ID: ${{ vars.ORIGIN_INSTALLATION_ID }}
          ORIGIN_APP_PRIVATE_KEY: ${{ secrets.ORIGIN_APP_PRIVATE_KEY }}
          ORIGIN_REPO: acme/widgets
          BUILD_BRANCH: ${{ github.head_ref || github.ref_name }}
          BUILD_SHA: ${{ github.event.pull_request.head.sha || github.sha }}
        run: |
          set -euo pipefail

          origin_app_token() {
            b64url() { openssl base64 -A | tr '+/' '-_' | tr -d '='; }
            now=$(date +%s)
            header=$(printf '{"alg":"EdDSA","kid":"%s","typ":"JWT"}' "$ORIGIN_APP_ID" | b64url)
            claims=$(printf '{"iss":"%s","aud":"origin-apps","iat":%d,"exp":%d}' \
              "$ORIGIN_APP_ID" "$now" "$((now + 900))" | b64url)
            signing_input=$(mktemp)
            trap 'rm -f "$signing_input"' EXIT
            printf '%s.%s' "$header" "$claims" > "$signing_input"
            signature=$(openssl pkeyutl -sign -rawin -in "$signing_input" \
              -inkey <(printf '%s\n' "$ORIGIN_APP_PRIVATE_KEY") | b64url)
            app_jwt="$header.$claims.$signature"
            echo "::add-mask::$app_jwt"
            CURSOR_AUTH_TOKEN=$(printf 'Authorization: Bearer %s\n' "$app_jwt" \
              | curl -fsS -X POST -H @- -H 'Content-Type: application/json' \
                  --data '{"scopes":["repository:contents:read"]}' \
                  "https://api.cursor.com/v1/origin/app/installations/${ORIGIN_INSTALLATION_ID}/access_tokens" \
              | jq -er '.token')
            echo "::add-mask::$CURSOR_AUTH_TOKEN"
            export CURSOR_AUTH_TOKEN
          }

          origin_app_token

          # Origin mirrors GitHub with a delay. Wait up to about two minutes for this commit.
          body=$(printf '{"ref":"refs/heads/%s","sha":"%s","wait":true}' "$BUILD_BRANCH" "$BUILD_SHA")
          printf 'Authorization: Bearer %s\n' "$CURSOR_AUTH_TOKEN" \
            | curl -fsS -X POST -H @- -H 'Content-Type: application/json' --data "$body" \
                "https://api.cursor.com/v1/origin/repos/${ORIGIN_REPO}:syncMirror" \
            | jq -e '.synced' > /dev/null \
            || { echo "Origin has not mirrored $BUILD_SHA from $BUILD_BRANCH yet" >&2; exit 1; }

          origin repo clone-fast "$ORIGIN_REPO" . --verify
          origin auth setup-git
          git fetch origin "$BUILD_SHA"
          git checkout -q "$BUILD_SHA"
```

- **On `pull_request`, the workflow builds the pull request head.** `github.sha` is a merge commit that exists only on GitHub, so `BUILD_SHA` and `BUILD_BRANCH` use the pull request's head commit and branch instead.
- **The sync request is [Sync Mirror](https://cursor.com/docs/api/origin/llms-full.txt#sync-mirror).** It accepts the installation token, needs `repository:contents:read`, and returns `200` with `"synced": true` or `202` with `"synced": false` after its wait budget of about two minutes. If Origin is the source of truth and GitHub is the mirror, delete the sync request: the commit is already on Origin, and Origin rejects sync requests for repositories that do not pull from an upstream source.
- **Both credentials are masked.** `::add-mask::` hides the app JWT and the installation token in the job log.
- **Later steps mint again.** A later step that needs Origin git access defines and calls the function again. The token is never written to `$GITHUB_ENV` or `$GITHUB_OUTPUT`, which are files on disk.
- **Pull requests from forks are not mirrored.** Their head branch is not in your repository. Build those from GitHub.

### Other CI systems

GitLab CI, Jenkins, CircleCI, and self-hosted fleets use the [Origin App](https://cursor.com/docs/origin/clonekit-ci.md#create-an-origin-app) path directly. Store the private key and the two ids as described in [Store the credentials](https://cursor.com/docs/origin/clonekit-ci.md#store-the-credentials), then run the function from [Mint a token in the job](https://cursor.com/docs/origin/clonekit-ci.md#mint-a-token-in-the-job) immediately before `origin repo clone-fast`, and fetch and check out the commit your CI system exposes for the build.

## Verify the first run

Run the first job with `--fallback never`. A missing kit then fails the job with exit status 1 instead of silently running a slow `git clone`. Keep the flag on until the kit path succeeds.

A successful run prints `clone-kit: manifest=...`, one download line per artifact, a `clone-kit timings:` block, and `clone-kit: ready DIR (head SHA)` on stderr, then `mode: clone-kit` on stdout, and exits 0. The timings block breaks the run into manifest, download, verify, and checkout phases. To measure the gain, compare its total with a plain `git clone` of the same repository on the same runner.

When the kit path does not complete, stderr shows one machine-readable line, `clone-kit-result: status=fallback phase=PHASE` or `clone-kit-result: status=failed phase=PHASE`, followed by the reason. With the default `--fallback auto`, stdout then shows `mode: git-clone`.

## Troubleshooting

Each entry starts with the line the job log shows.

### Manifest fetch returns 404

`clone-kit-result: status=fallback phase=manifest` with `HTTP 404`. No clone kit exists for the repository yet; contact your Cursor account team to turn CloneKit on. If the URL in the message contains `https://` twice, the command received a clone URL instead of `{owner}/{repo}`.

### Manifest fetch returns 401

`clone-kit manifest fetch failed: HTTP 401`. Origin rejected the token: it expired, was never valid, or its installation was removed. Mint a new token immediately before the clone. With the default `--fallback auto`, the fallback `git clone` fails with the same code and exit status 128, so the log shows both errors.

### Manifest fetch returns 403

`clone-kit manifest fetch failed: HTTP 403`. The installation, or the Buildkite pipeline token, does not cover this repository. Reinstall the app or reselect the repositories it covers. As with 401, the fallback `git clone` fails with the same code and exit status 128.

### Git asks for a username

`fatal: could not read Username for 'https://origin.cursor.com'`. Either the CLI is out of date or `CURSOR_AUTH_TOKEN` is not exported in the shell that runs `git`. Run `origin update`, or export the variable.

### The clone falls back in the auth phase

`clone-kit-result: status=fallback phase=auth` with `Not authenticated`. `CURSOR_AUTH_TOKEN` is not exported into the process that runs `origin`. Export it in the same shell before the `origin` command.

### The mint returns 401 Issuer is not authorized

`401 {"code":16,"message":"Issuer is not authorized"}` from the token endpoint. The `iss` claim is not a registered App ID, or the signing key is not registered on that app. Confirm that `ORIGIN_APP_ID` matches the app and that the app lists the signing key.

### origin auth status reports a valid token but the clone fails

`origin auth status` derives `Token: valid` or `Token: expired` from the expiry claim inside `CURSOR_AUTH_TOKEN`. It does not ask Origin whether it accepts the token, so `valid` means only that the token has not expired. The CLI treats a token as expired five minutes before its expiry claim. `origin` commands refuse an expired token before making any request, and `clone-fast` logs `clone-kit-result: status=fallback phase=auth` with `The injected CURSOR_AUTH_TOKEN session has expired`. Mint a new token and retry.

If the kit path still fails, send your Cursor account team the job log with the `clone-kit-result` line, the repository, and the output of `origin --version`.
