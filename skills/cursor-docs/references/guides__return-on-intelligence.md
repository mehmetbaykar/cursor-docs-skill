---
title: "Maximizing return on intelligence"
source: https://cursor.com/guides/return-on-intelligence
path: /guides/return-on-intelligence
---

Aug 12, 2026·Strategy

# Maximizing return on intelligence

8 min read

By David Pan

Toward the end of last year, agentic engineering finally started working. And once it worked, everything grew at once. More engineers picked up the tools. They started using them for more tasks. And each task got more expensive as a result of more thinking and tool calls. Those three things multiply, which is how so many engineering teams watched their AI spend go on a J curve.

These teams will tell you the spend has been worth it. They are shipping faster and getting real value. But worth it or not, they're flying past their 2026 budgets, and nearly every customer we talk to now has some version of the same mandate: keep accelerating AND get disciplined about the cost.

Easier said than done. Here's my take on some of the questions that come up most often.

## [#](#1-should-i-use-cheaper-models)1. Should I use cheaper models?

Everyone can see that Fable & Opus are quite expensive so the obvious first question is whether you can use something cheaper. But there's plenty of reasonable skepticism. If the cheap model produces work that has to be redone, you didn't save anything. You paid twice and wasted time.

Late last year, Opus 4.5 was the only model you could trust with serious engineering work. Today a dozen models outperform it. Among the top models, the range of intelligence is now [quite narrow](https://artificialanalysis.ai/agents/coding-agents#coding-agents-index) while the range of price and speed is [very wide](https://artificialanalysis.ai/agents/coding-agents#cost-to-run). The same task can often be done just as well for a fraction of the cost, if you pick the right model.

Picking well is the catch. No model is best at every task, and the frontier changes every couple of weeks. Keeping that matrix in your head isn't a reasonable thing to ask of your engineers. As it turns out, this is another job for AI. We built a model router, powered by a custom-trained model to do exactly this: figure out which models can handle a given task with confidence, then route to the cheapest one that clears the bar. Our router delivers [Fable-level user satisfaction at 68% lower cost](https://cursor.com/blog/how-cursor-router-works).

So yes, cheaper models save real money. Just don't make your engineers do the routing.

## [#](#2-should-i-be-using-open-weight-models)2. Should I be using open weight models?

In principle, sure. If an open weight model offers the best performance per dollar on a given task, it belongs in your mix, ideally sitting behind a router like everything else.

In practice, as of this writing, they aren't at the Pareto frontier. When we [run the evals](https://cursor.com/evals) and account for token efficiency rather than just headline price, the leading closed models still deliver more intelligence per dollar.

The good news is that you benefit from open weight models even if you never run one. Every leading lab pays close attention to the open weights ecosystem, and it's certainly a factor in how the closed models get priced. So keep rooting for open weights. You win either way.

## [#](#3-should-i-use-cloud-agents-arent-they-expensive)3. Should I use cloud agents? Aren't they expensive?

There's a lot of excitement about "software factories" right now, fleets of cloud agents producing software around the clock. A common reaction from engineering leaders is some version of: that sounds great, but I'm already spending too much.

Fair. But much of the spend that a cloud agent might introduce is already happening at your company every day. Your engineers already use agents to help with code reviews, merge conflicts, CI failures, etc. Except currently these tasks are also soaking up a lot of engineering time and they're being executed inconsistently from engineer to engineer.

Take code review for example. A fully loaded engineer hour might cost $100, so a half hour spent reviewing a PR costs $50. A Bugbot review costs less than a dollar, and it keeps getting better. The latest version is [over 3x faster, 22% cheaper, and finds 10% more bugs](https://cursor.com/blog/bugbot-updates-june-2026). That math doesn't need a fancy ROI model.

A half hour of human review costs about $50 at a $100 fully loaded engineer hour, while a Bugbot review of the same pull request costs under $1.

There's a simple playbook for any cloud agent workflow: make it work, then make it great, then make it cheap. You've got time on your side. The cost of intelligence will only go down as the months pass.

## [#](#4-what-metrics-should-i-be-tracking)4. What metrics should I be tracking?

Choose metrics that map to what you're trying to accomplish. That usually means three stages. Start with adoption: are people actually using the tools? Then measure engineering metrics: are you shipping faster? Are you shipping efficiently? Only after you've proven that should you try to connect those gains to the business.

For adoption, skip lines of code and token spend. Both are easy to game and can push people toward counterproductive behavior. Instead measure how many engineers use the tools every day and the depth of that usage.

For engineering metrics, these are some that work well. Pair them with guardrail metrics so you notice if the gains are costing you elsewhere.

- **Velocity:** PR velocity, ticket completion rate, story point rate. End-to-end project delivery speed against your pre-AI baseline.
- **Efficiency:** time recovered by automating repeated tasks, and cost per task on those workflows.
- **Guardrails:** bug volume, revert rate, code turnover.

Measuring impact on the business is the hard one, and I won't pretend there's an easy answer. The higher your AI spend gets, the more pressure there will be to connect it to business results. And for good reason. Your company's board does not care about your engineering metrics. They want to see impact on the top and bottom line.

## [#](#5-should-i-set-spend-budgets-per-engineer)5. Should I set spend budgets per engineer?

Probably yes. Where you set them depends heavily on your company, and there's no single right number. A few tips that hold up broadly.

Use soft caps that can be raised instead of hard caps, and make the first increase low friction. That creates awareness of the spend while leaving the decision mostly in your engineers' hands. Then do more diligence as the increases get large. AI spend isn't so different from hiring a contractor, and you wouldn't issue a blank check for that.

And expect a power law. Some engineers will spend dramatically more than others, and that's not necessarily bad. Our usage data shows a [wide gap between power users and everyone else](https://cursor.com/insights/developer-habits#the-power-user-gap), and the heaviest spenders are often some of the most efficient users of AI in the entire company.

## [#](#6-how-should-i-be-reviewing-my-ai-spend)6. How should I be reviewing my AI spend?

You're not going to like this answer: you should be reviewing your spend regularly, and in partnership with your finance team. Most software organizations already track and optimize their cloud spend with real discipline. If you're reading this article, your AI spend is probably large enough to deserve the same treatment. Your finance team will love you for it. These questions are so top of mind for CFOs that we launched a [CFO Council](https://cursor.com/blog/cfo-council) just to work through them.

Segment the usage data four ways: by team, by project, by workflow, and by work type. A good test of whether you have the visibility you need: can you answer questions like these?

- How much of my spend is going toward each of my top three product initiatives?
- An engineer on my team spent $10k on tokens last month. Was it productive spend?
- What's my median token cost to fix a bug and how is it trending?

Chase down the outliers and any large buckets of "unknown" spend. Dig in until you understand all of it and feel comfortable with how it is delivering value for your business.

Then act on what you find. Double down in the areas where AI is really working. Give your high ROI users more budget, not less. Lastly, try to keep budget changes as close to zero-sum as possible. If one area needs to go way over, it has to come from somewhere.

## [#](#7-how-should-i-be-coaching-my-team)7. How should I be coaching my team?

It's easy to fall into bad habits when you're not the one paying the bill, and in many organizations the teams never even see the bill. So start with cost transparency.

Then cascade accountability down the management chain. Your first line engineering managers should feel that it's part of their job to make sure their team's AI spend is money well spent, the same way they'd feel about a hiring decision or a big tech debt investment.

Get those two things right and most of the coaching takes care of itself. Engineers are optimizers. Give them visibility into the cost and ownership of the outcome, and they'll find the efficient path on their own.

Filed under: Strategy

## Related guides

[Model routing: right model, right job, right price

Model routing sends each request to the model that fits the job, so routine work stops billing at frontier prices. How it works, what to measure, and how to run it.](https://cursor.com/guides/model-routing)

[AI code review: more context, fewer bugs

AI code review only helps with real codebase context. What changed as agents grew, what to measure, and how to run Bugbot and Agent Review.](https://cursor.com/guides/ai-code-review)

[View all guides →](https://cursor.com/guides)
