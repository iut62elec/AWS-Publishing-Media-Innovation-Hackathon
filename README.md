# AWS Publishing & Media Innovation Hackathon

Welcome! This repo is everything you need to build your idea today. Read this page first, it takes 3 minutes.

Event page: [awspublishinghackathon032026.splashthat.com](https://awspublishinghackathon032026.splashthat.com/)

---

## What you get on the day

On the day of the hackathon you will receive:

- **An AWS sandbox account**, your team's own account where you can build and deploy real AWS services (Amazon Bedrock, S3, Lambda, Polly, Textract, Translate, Comprehend, and more), not just code — see the full **[Services Guide](SERVICES.md)**, including media services like AWS Elemental Inference and services from our event partners Metal Toad and Progress
- **Claude Code in your browser**, a powerful AI coding agent running on Amazon Bedrock with unlimited tokens, no installation needed, it works entirely through the browser
- **AWS experts** on hand to help you at every step

You only need a laptop, Wi-Fi, and a modern browser such as Chrome.

If you prefer your own local setup with another coding agent, that is fine too, but everything in this guide assumes Claude Code.

## How the day works

1. You will form a team of around five people, one team builds one idea
2. Pick one of the 12 ready made ideas below, or bring your own
3. Follow the **[Build Guide](BUILD-GUIDE.md)**, it gives you the exact prompts to go from idea to working demo
4. Build for about 4.5 hours, then present a short demo to the judging panel, scored using the **[Judging Rubric](JUDGING-RUBRIC.md)**, read it before you build, it tells you exactly what the judges reward

## The ideas

Each idea is a real publishing industry problem, designed to be buildable in an afternoon. Full details, including what to build, AWS services, bonus points, and quick start hints, are in the [`ideas/`](ideas/) folder.

| # | Challenge | In Plain English | Who It's For |
|---|-----------|-----------------|--------------|
| 1 | [AI Backlist Revitalizer](ideas/01-ai-backlist-revitalizer.md) | Find catalog gems that match current trends | Marketing, SEO teams |
| 2 | [Intelligent Content Triage](ideas/02-intelligent-content-triage.md) | Auto-assess submissions so editors read less slush | Editors, content ops |
| 3 | [One Story, Every Format](ideas/03-one-story-every-format.md) | One article in, five formats out (with audio) | All content teams |
| 4 | [AI Rights & Permissions Navigator](ideas/04-rights-permissions-navigator.md) | Ask your contracts questions in plain English | Rights managers, legal |
| 5 | [Immersive Audio Engine](ideas/05-immersive-audio-engine.md) | Text to multi-voice audio in minutes | Audio/podcast teams |
| 6 | [Real-Time Fact-Checker](ideas/06-real-time-fact-checker.md) | Catch factual errors before publication | Editors, reviewers |
| 7 | [Cultural Adaptation Engine](ideas/07-cultural-adaptation-engine.md) | Localize for culture, not just language | International teams |
| 8 | [Reader Drop-Off Predictor](ideas/08-reader-drop-off-predictor.md) | Predict where readers lose interest | Content strategists |
| 9 | [Ask Your Archive](ideas/09-ask-your-archive.md) | Your own AI chat over your content, like "Ask The Post AI" | Product, audience teams |
| 10 | [Subscriber Save Engine](ideas/10-subscriber-save-engine.md) | Spot subscribers about to cancel, win them back personally | Retention, marketing teams |
| 11 | [AI Story Studio](ideas/11-ai-story-studio.md) ⚠️ advanced | An AI newsroom: editor agent directs researcher, writer, illustrator, and fact checker agents | Ambitious teams, editorial |
| 12 | [Autonomous Retention Desk](ideas/12-newsroom-retention-desk.md) ⚠️ advanced | An AI retention team: agents find at-risk readers, pick a save move, write and review the message | Ambitious teams, retention |

Tip: Intelligent Content Triage (#2) is the simplest, start there if you want a quick win. Ask Your Archive (#9) and Subscriber Save Engine (#10) target the two issues publishers rank highest right now, falling search traffic and subscription churn.

**Want a challenge?** Ideas #11 and #12 are **advanced multi-agent builds**: instead of one prompt, you build a team of AI agents that hand work to each other, using the [Strands Agents](https://strandsagents.com/) framework with an orchestrator that calls specialist agents as tools, and optionally deploy to [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/). They take the full afternoon and need Python comfort, but the demo is one few teams will have.

### The ideas in plain English

**1. [AI Backlist Revitalizer](ideas/01-ai-backlist-revitalizer.md)** — Every publisher has thousands of older books or articles that nobody looks at anymore, and some of them would sell again if they matched a topic people care about today. This tool takes your catalog, compares it against current trends, and gives you a ranked list of older titles worth promoting right now, along with a short pitch explaining why each one is timely.

**2. [Intelligent Content Triage](ideas/02-intelligent-content-triage.md)** — Editors spend hours reading through piles of submissions and pitches, and most of them get rejected anyway. This tool does the first read for them. It scores each submission on writing quality and fit, then hands the editor a sorted list with notes on strengths and concerns, so they only spend real time on the promising ones.

**3. [One Story, Every Format](ideas/03-one-story-every-format.md)** — When you publish one article, different people usually rewrite it as a newsletter, a social post, a podcast script, a push notification, and a search summary. This tool takes the original article and produces all five versions at once, including a spoken audio version, with each one written the way that format expects. A person still reviews everything before it goes out.

**4. [AI Rights & Permissions Navigator](ideas/04-rights-permissions-navigator.md)** — Publishing contracts hold answers to questions like whether you can sell an audiobook in Germany, but finding those answers means digging through piles of PDFs. This tool reads your contracts and lets you ask questions in plain English. It answers by pointing to the exact clause in the contract, and if something is unclear it flags it for a lawyer instead of guessing.

**5. [Immersive Audio Engine](ideas/05-immersive-audio-engine.md)** — Recording an audiobook with human narrators costs thousands of dollars per hour of audio, so most older titles never get one. This tool takes a chapter or article, figures out which parts are narration and which are dialogue, and turns it into audio using several different AI voices, giving you a finished recording in minutes instead of weeks.

**6. [Real-Time Fact-Checker](ideas/06-real-time-fact-checker.md)** — Articles are full of facts like dates, prices, and statistics, and checking them by hand is slow and often skipped under deadline pressure. This tool finds every factual claim in a piece of writing, checks each one against your trusted source documents, and marks it as confirmed, disputed, or unverifiable, so errors get caught before readers see them.

**7. [Cultural Adaptation Engine](ideas/07-cultural-adaptation-engine.md)** — Translation gets the words right but often misses the meaning, since a baseball joke or a Thanksgiving reference means nothing in France or Brazil. This tool translates an article and then goes a step further, swapping cultural references, idioms, and humor for ones that make sense to the local audience, and it shows you exactly what it changed and why.

**8. [Reader Drop-Off Predictor](ideas/08-reader-drop-off-predictor.md)** — Publishers usually find out where readers stopped reading only after an article is published, when it is too late to fix. This tool reads a draft before publication, predicts the spots where readers are likely to lose interest, and suggests specific fixes like moving a key section higher or breaking up a dense passage.

**9. [Ask Your Archive](ideas/09-ask-your-archive.md)** — Readers are getting answers from chatbots instead of visiting publisher sites. This tool gives you your own chat experience built only on your own articles, like the Washington Post did with Ask The Post AI. Readers ask a question on your site, get an answer drawn only from your reporting with links to the source articles, and if your archive does not cover it, the tool says so instead of making something up.

**10. [Subscriber Save Engine](ideas/10-subscriber-save-engine.md)** — Most publishers lose around 4 to 5 percent of their subscribers every month, and usually nobody notices someone is drifting away until they cancel. This tool looks at subscriber activity data, flags the people showing warning signs, explains why each one is at risk, and drafts a personal message to win them back based on what that reader used to enjoy.

**11. [AI Story Studio](ideas/11-ai-story-studio.md)** (advanced) — Today, turning a story idea into a published piece takes a whole team, someone researches, someone writes, someone creates art, and someone checks the facts. This project builds that team out of AI agents. You give one editor in chief agent a short brief, and it directs the specialists, the researcher gathers background, the writer drafts the piece, the illustrator generates artwork, and the fact checker reviews the claims and can send the draft back for fixes. You watch the agents work together and get back a complete story package. This one is harder and uses a real multi agent framework, pick it if your team wants a challenge.

**12. [Autonomous Retention Desk](ideas/12-newsroom-retention-desk.md)** (advanced) — Idea 10 flags subscribers who might cancel and drafts one email. This project goes much further, it builds a whole retention team out of AI agents. A supervisor agent directs the specialists, an analyst finds who is at risk and why, a strategist decides the best save move for each person, a copywriter writes the message in your publication's voice, and a reviewer checks the message and rejects it if it is not good enough. The agents hand work to each other and disagree with each other, and you watch it happen. This one is harder and uses a real multi agent framework, pick it if your team wants a challenge.

## Vision documents, your starting spec

Every idea has a ready made one page **vision document** in [`vision-docs/`](vision-docs/). This is your specification, it describes the problem, the solution, the architecture, and what a successful demo looks like. The Build Guide prompts feed this document to Claude Code, so the clearer the spec, the better your final product.

**Bringing your own idea?** Great. Copy [`templates/vision-template.md`](templates/vision-template.md), fill it in (it takes 15 minutes), and use it exactly the same way. A good spec is the single biggest thing you can do to make your coding agent effective.

## Get started

1. **First:** Complete the **[Setup Guide](SETUP-GUIDE.md)** — get credentials, verify AWS access, install dependencies (5 minutes)
   - Browse the **[Services Guide](SERVICES.md)** to see every AWS service and media service available, plus our event partners Metal Toad and Progress
2. **Then:** Follow the **[Build Guide](BUILD-GUIDE.md)** — 6 steps from idea to working demo
3. **If stuck:** Check the **[Troubleshooting Guide](TROUBLESHOOTING.md)** — quick fixes for common issues

The [`starter/`](starter/) folder has ready-to-use templates: a Flask app skeleton, HTML template, smoke test script, and `.gitignore`. Copy them into your project to skip boilerplate.

Good luck, and have fun!
