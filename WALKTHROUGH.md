# Welcome, Here Is Your Day

*A 10 minute walkthrough of everything you need to know before you build. Presented live at the start of the hackathon, kept here so you can come back to it any time.*

---

## 1. What you get today

- **Your team's own AWS sandbox account**, build with real services, not just code
- **Claude Code in your browser**, an AI coding agent on Amazon Bedrock, unlimited tokens, nothing to install
- **AWS experts in the room all day**, plus our partners Metal Toad and Progress
- All you need is a laptop, Wi-Fi, and a browser

To get in: go to the join link in the [Setup Guide](SETUP-GUIDE.md), enter the event code we give you, and you land on your dashboard.

---

## 2. The latest on AWS, July 2026

The pace right now is remarkable, everything below shipped in the last few weeks:

- **Claude Opus 5** landed on Amazon Bedrock on July 24, zero data retention on by default
- **Claude Sonnet 5** and **Claude Fable 5** arrived in June, both with a 1M token context window
- **OpenAI GPT-5.6** (Sol, Terra, Luna) went live on Bedrock July 13, alongside open weight coding models like Qwen3 Coder and DeepSeek
- **Bedrock AgentCore** now runs production agents with any framework and any model, and the new **Harness** lets you define an agent in configuration alone
- **Strands Agents**, the AWS open source agent SDK, passed 50 million downloads
- One Bedrock endpoint now speaks both the OpenAI and Anthropic APIs, swap the base URL and your existing code works

The takeaway: one API in your sandbox reaches the newest models from two frontier labs, and the model provider never sees your prompts, models run inside AWS operated accounts.

---

## 3. The AI coding agents, and which one you use today

Three agents matter right now, and they all converged on the same idea: **plan first, then execute.**

| Agent | What it is | On AWS |
|---|---|---|
| **Claude Code** | Agentic coding in your terminal or browser | Runs on Bedrock with your AWS account, no Anthropic account needed |
| **Kiro** | AWS's spec first agentic IDE | Built by AWS, Claude Opus 5 and GPT-5.6 added this month |
| **OpenAI Codex** | OpenAI's coding agent, CLI and IDE plugins | GA on Bedrock since June, signs in with AWS credentials |

**Today you use Claude Code.** It is already set up in your browser: open the terminal, type `claude`, and you are in. The sandbox has **Claude Opus 4.6 and Sonnet 4.6**, switch between them any time with the `/model` command. Full steps in the [Setup Guide](SETUP-GUIDE.md).

---

## 4. The method: spec driven development

We all love vibe coding, prompt, prompt, prompt, and something works. The problem: nobody wrote down the assumptions, so it breaks the moment you change it.

Today you work the other way:

1. **Spec first.** Every idea has a one page vision document in [`vision-docs/`](vision-docs/), that is your spec, already written
2. **Feed it to Claude Code.** It proposes requirements and a plan, you approve each stage before it builds
3. **Build in small loops.** Get one thing working, verify it, then add the next thing

You do not have to invent any of this. The **[Build Guide](BUILD-GUIDE.md#step-1-requirements-requirementsmd) has the exact copy paste prompts** for every step, requirements, plan, build, test, and demo prep. Open it, copy the Step 1 prompt, paste in your vision doc, and go.

The loop never changes: **the agent proposes, the human approves.** This is a pocket version of [AI-DLC](https://github.com/awslabs/aidlc-workflows), the open source AI driven development lifecycle from AWS, and it is the single biggest thing that separates teams that demo from teams that debug.

---

## 5. Pick your idea

**[Twelve real publishing problems, browse them all here](README.md#the-ideas)**, each one buildable in an afternoon, each with a plain English explanation, full details in [`ideas/`](ideas/), and a ready made spec in [`vision-docs/`](vision-docs/).

They span the whole publishing world, marketing, editorial, audio, rights, localization, audience, and retention. Ideas #11 and #12 are marked advanced, they are multi agent builds for teams who want the harder challenge. Pick whichever problem your team actually cares about, that is the one you will build best.

**Own idea?** Also welcome. Copy the [vision template](templates/vision-template.md), fill it in, 15 minutes.

---

## 6. Build, then demo

- Teams of about five, one idea per team, about 4.5 hours to build
- Follow the [Build Guide](BUILD-GUIDE.md), six steps with copy paste prompts
- Read the [Judging Rubric](JUDGING-RUBRIC.md) **before** you build, it tells you what judges reward
- Demo is 4 minutes: problem, solution, working demo, impact

Two rules of thumb from us: **one polished feature beats five broken ones**, and the most common mistake every year is building too much. Scope down, then scope down again.

Stuck? [Troubleshooting Guide](TROUBLESHOOTING.md), any AWS expert in the room, or ask Claude Code itself.

**Let's build.**
