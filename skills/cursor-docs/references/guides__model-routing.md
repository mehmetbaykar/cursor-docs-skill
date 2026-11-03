---
title: "Model routing: right model, right job, right price"
source: https://cursor.com/guides/model-routing
path: /guides/model-routing
---

Aug 12, 2026·models

# Model routing: right model, right job, right price

7 min read

[![](https://cursor.com/marketing-static/guides/model-routing-hero-poster.png)](https://cursor.com/marketing-static/guides/model-routing-hero-01.mp4)

Most teams pay frontier prices for work that does not need a frontier model. Someone picks the strongest model they can find, sets it as the default, and every request after that runs at the top rate. The spend climbs faster than the quality of what ships.

Model routing is the fix. Instead of sending every request to one model, a router looks at each request and picks the model that fits. Simple work goes to fast, cheap models. Hard, long-horizon work goes to the frontier models.

Model routing is turning into a standard layer in how teams work with LLMs. The gap between the cheapest capable model and the most expensive one is huge, and most of what you do all day sits at the easy end. Route it well and you keep the quality while meaningfully reducing spend. The rest of this guide covers how routing actually works, what to measure so you know it is working, and how to turn it on.

## [#](#why-model-routing-matters-now)Why model routing matters now

Two things changed at once. Models got more capable across a wide price range, and developers started sending far more requests through them as agents took on more of the work. That combination is where a single-model default gets expensive.

Roughly [60% of developers using Cursor pick a single model as their daily driver](https://cursor.com/blog/router), which means routine work runs at frontier prices and AI spend grows much faster than output quality. A first-party model like [Composer 2.5 runs $0.50 per million input tokens and $2.50 per million output](https://cursor.com/docs/models-and-pricing), while frontier models cost several times that. When most of your volume is ordinary coding work, the model you default to decides most of your bill.

The industry landed on the same answer. Microsoft's Foundry ships a model router with cost, balanced, and quality modes. Research systems like RouteLLM report big cost reductions at close to frontier quality. This is showing up everywhere at once, which usually means the math is hard to argue with.

## [#](#the-questions-worth-answering-before-you-route)The questions worth answering before you route

If you are evaluating model routing, these are the things to settle first. Work through them in order.

### [#](#what-is-a-model-router)What is a model router?

A model router is a system that sits between you and a set of models and picks which one handles each request. It reads the request (the prompt, the context, the kind of task) and sends it to the model most likely to do the job well at the lowest cost. Good routers reason about task type and complexity, not just length. Weak ones route on a crude rule and miss the point.

### [#](#how-does-routing-decide-which-model-to-use)How does routing decide which model to use?

The better systems classify each request before any model runs. Cursor Router, for example, [runs a classifier on each request](https://cursor.com/blog/router) based on query, context, task complexity, and domain, combined with what it knows about how each model behaves. UI work goes to price-efficient models, interface work goes to the model with the best taste, and complex, long-horizon problems go to frontier reasoning models. The classification happens up front, so the choice is made before the expensive model would have been called.

A request moves through a router classifier to a cheaper model for routine work or a frontier model for hard work. Modes are Cost, Balance, and Intelligence.

### [#](#should-routing-be-automatic-or-should-engineers-still-choose)Should routing be automatic or should engineers still choose?

Both, at different levels. The per-request pick should be automatic, because nobody wants to choose a model by hand hundreds of times a day and the right answer shifts with every task. What teams do want is a lever for where they sit overall on the cost-versus-quality tradeoff. The common design gives you a few modes (cost, balanced, quality) that slide the whole team along that curve, with the request-by-request decision handled underneath.

### [#](#does-routing-hurt-quality)Does routing hurt quality?

It should not, if the router is measured on quality and not just cost. Model routing keeps hard tasks on the most capable models and only moves the easy work down. In Cursor's [A/B tests across millions of requests](https://cursor.com/blog/router), the Intelligence mode landed near a frontier model on user satisfaction at about 60% lower cost, and early-access enterprises saw 30 to 50% savings versus routing everything to the top model, with no drop in quality. For most requests the model that does the job well just is not the most expensive one.

### [#](#what-should-you-measure)What should you measure?

Watch cost per unit of real work, not just cost per request. This can be measured by user satisfaction (did the person take the result and move on, or go back and correct it?) and keep rate (how much of the generated code is still in the codebase later). Cursor reports cost per commit as the bottom-line number: in our tests, the Cursor router achieves [$4.63 per commit in Balance and $6.76 in Intelligence, versus $7.34 for an all-Opus 4.8 baseline](https://cursor.com/blog/router). Cost per commit (or per PR) is the number to bring to a budget conversation, because it ties spend to shipped work.

Cost per commit is $4.63 for Cursor Router Balance, $6.76 for Intelligence, and $7.34 for an all-Opus 4.8 baseline.

### [#](#how-does-routing-handle-caching-and-switching-models)How does routing handle caching and switching models?

Switching models across a conversation can miss the prompt cache, which adds cost that a naive before-and-after ignores. Cursor accounts for this by including the cache-miss cost of the routing decisions it makes in its reported savings. When you evaluate a router, ask whether its numbers are cache-aware. If they are not, they are likely overstating savings.

## [#](#how-to-run-model-routing-in-cursor)How to run model routing in Cursor

Cursor Router is the model routing system behind Auto on Teams and Enterprise plans. You choose how aggressively to optimize. On Balance and Intelligence, the router picks the model per request.

**Pick a mode.** Select Auto in the model picker, then choose the optimization mode. [Cost](https://cursor.com/docs/cursor-router#optimization-modes) optimizes token spend. Balance matches the frontier models people like to daily-drive, and Intelligence targets top-tier quality. All Auto modes bill at the routed model's list price.

**Let it classify.** On Balance and Intelligence, the router reads each request and routes by task type and complexity, keeping hard work on the most capable models and moving routine work off frontier pricing. Grok 4.5 needs to be enabled, since the router uses it as the cost-efficient option when it is not calling a frontier model.

**Set the guardrails (admins).** Enable Router per team or group, choose which modes members can use, set the default, and allow or block specific models. It is on by default for Teams plans; Enterprise admins enable it from the dashboard.

**Watch the numbers.** Track usage in the [usage dashboard](https://cursor.com/dashboard/usage) to see how much is running through Cursor's models versus others, and confirm the savings are real before you widen the rollout.

**Next step:** Turn on Auto in the model picker, pick Balance or Intelligence, and follow the full setup at [cursor.com/docs/cursor-router](https://cursor.com/docs/cursor-router). Admins can enable Router and set guardrails from the [team dashboard](https://cursor.com/docs/account/teams/dashboard).

## [#](#match-the-model-to-the-job)Match the model to the job

Model routing works because the strongest model is rarely the right one for most of what you do. Match the model to the job and you keep the quality bar while paying a lot less for the work that never needed a frontier model in the first place. The routers that actually deliver route on real task complexity, keep the hard problems on capable models, and judge themselves on cost per shipped change. If that fits how your team already works, turn routing on for one busy team, watch [cost per commit](https://cursor.com/blog/router) for a week, and let that number tell you how far to push it.

[Start here.](https://cursor.com/docs/cursor-router)

Filed under: models

## Related guides

[MCP for coding agents: how agents plug into your stack

MCP connects coding agents to your databases, tickets, docs, and error trackers. Which servers to start with, and how to add one in minutes.](https://cursor.com/guides/coding-agent-mcp)

[AI code review: more context, fewer bugs

AI code review only helps with real codebase context. What changed as agents grew, what to measure, and how to run Bugbot and Agent Review.](https://cursor.com/guides/ai-code-review)

[View all guides →](https://cursor.com/guides)
