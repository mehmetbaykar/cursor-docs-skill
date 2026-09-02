---
title: "Computer use and desktop sharing"
source: https://cursor.com/docs/cloud-agent/self-hosted/computer-use
path: /docs/cloud-agent/self-hosted/computer-use
---

# Computer use and desktop sharing

Computer use lets an agent on a [Self-Hosted Machines worker](https://cursor.com/docs/cloud-agent/self-hosted.md) click, type, take screenshots, and drive applications with a UI. Agents can also drive a browser when the worker has Chrome or Chromium installed. Desktop sharing lets authorized viewers watch or take control of the agent's desktop from Cursor. For the product behavior on managed Cloud Agents, see [Capabilities](https://cursor.com/docs/cloud-agent/capabilities.md).

Both features are explicit opt-ins and are never enabled by the server.
Computer use currently requires a Linux worker; see
[Requirements](https://cursor.com/docs/cloud-agent/self-hosted.md#requirements).

## Install dependencies

On each Linux worker, install the desktop packages. Cursor does not install system packages for you:

```bash
sudo apt-get install -y --no-install-recommends \
  dbus-x11 ffmpeg tigervnc-standalone-server \
  x11-utils x11-xserver-utils xdotool xfce4
```

`xdotool`, `ffmpeg`, and the X11 utilities are always required. `tigervnc-standalone-server` and `xfce4` are needed when the worker creates a desktop itself: the managed display for computer use on headless machines, and the isolated desktop for desktop sharing.

Install Chrome or Chromium (optional, recommended) for browser computer use.

For [pools](https://cursor.com/docs/cloud-agent/self-hosted/pool.md), bake the packages into your worker image so every machine comes up ready.

## Enable computer use

Start a [My Machines](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md) worker with `--computer-use`:

```bash
agent worker --computer-use start
```

[Pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md) workers take the same flag:

```bash
agent worker --computer-use --pool gpu start
```

## Choose the X11 display

The worker resolves the display for computer use in this order:

1. **`--display <display>`.** Require an existing X11 display, for example `:0`. If the display isn't reachable, worker start fails instead of falling back.
2. **Inherited `DISPLAY`.** Without `--display`, the worker reuses a reachable `DISPLAY` from its environment. If it isn't reachable, the worker falls back to a managed desktop.
3. **Managed desktop.** With no display configured, the worker starts its own TigerVNC desktop running an Xfce session. This is the default on headless machines and needs the `tigervnc-standalone-server` and `xfce4` packages.

```bash
# Reuse a desktop you already run
agent worker --computer-use --display :0 start

# Let the worker create a managed desktop (headless machines)
agent worker --computer-use start
```

## Share the agent desktop

To let authorized viewers watch or control the agent desktop from Cursor, add `--share-desktop`:

```bash
agent worker --computer-use --share-desktop start
```

`--share-desktop` takes an optional mode: `view` (watch only) or `view_and_control` (viewers can take mouse and keyboard control, the default). Sharing uses a worker-created, isolated agent desktop, not the machine's own session, and requires `tigervnc-standalone-server`. A fail-closed input filter on the machine enforces control, and clipboard transfer stays blocked.

Pixels leave the machine only through the worker's existing outbound connection. No inbound ports open.

![Cursor showing a worker's shared desktop with Take control](https://cursor.com/docs-static/images/cloud-agent/private-worker-desktop-share.png)

## Verify the setup

Run the preflight report. It checks each required binary, whether the configured display is reachable, and whether the worker can fall back to a managed desktop:

```bash
agent worker debug
```

## Next steps

- [API reference](https://cursor.com/docs/cloud-agent/api/endpoints.md#workers-and-pools): endpoints for workers, pools, the pending-request queue, and worker tokens.
- [Cloud Agent capabilities](https://cursor.com/docs/cloud-agent/capabilities.md): desktop and browser control on managed Cloud Agents.
