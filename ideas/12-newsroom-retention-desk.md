## 12. Autonomous Retention Desk (Advanced, Multi-Agent)
*A team of AI agents that runs your subscriber retention desk, a supervisor agent directs analyst, strategist, copywriter, and reviewer agents to find at-risk readers and save them*

**In Plain English:** Idea 10 flags subscribers who might cancel and drafts one email. This project goes much further, it builds a whole retention team out of AI agents. A supervisor agent looks at your subscriber data and directs the specialists, an analyst agent finds who is at risk and why, a strategist agent decides the best save move for each person, a copywriter agent writes the message in your publication's voice, and a reviewer agent checks the message before it goes anywhere. The agents hand work to each other and disagree with each other, and you watch it happen. This one is harder than the other ideas and uses a real multi agent framework, pick it if your team wants a challenge.

**⚠️ Difficulty: Advanced.** This idea takes the full afternoon and assumes your team is comfortable with Python. Consider it the agentic big sibling of idea #10 — if your team wants the safer version, start there.

**The Problem:** The median news publisher loses 4–5% of digital subscribers every month, and the retention response is usually one generic discount email. Even publishers that spot at-risk readers can't act at scale: deciding the right save move per subscriber, writing a personal message, and quality-checking it is a pipeline of human judgment calls. That pipeline is exactly the shape of a multi-agent system — but a single prompt can't do it, because each step needs its own expertise and the steps need to challenge each other.

**Real-Life Example:** Monday morning, the retention desk agent-team runs over the weekend's engagement data. The analyst agent flags 14 at-risk subscribers and explains each one's warning signs. The strategist agent decides: the lapsed foodie gets a content win-back, the price-sensitive skimmer gets an offer, the frustrated commenter gets a service recovery note. The copywriter agent drafts each message in the publication's voice. The reviewer agent rejects two drafts — one sounds desperate, one recommends an article the reader already read — and sends them back with notes. A human retention manager opens a dashboard of 14 finished save plans, each showing the full agent debate that produced it, and approves them with one click.

**What You'll Build:**
- A multi-agent system using the **[Strands Agents](https://strandsagents.com/) framework** with the **agents-as-tools pattern**: a supervisor agent that calls specialist agents as tools
- Four specialist sub-agents: an **analyst** (reads the engagement CSV, assigns churn risk with evidence), a **strategist** (picks the save move per subscriber: content win-back, offer, service recovery, or let-go), a **copywriter** (writes the message in the publication's brand voice), and a **reviewer** (scores the draft against a quality checklist and rejects with reasons)
- A real **revision loop**: when the reviewer rejects a draft, the supervisor routes it back to the copywriter with the objections — show at least one rejection-and-fix in your demo
- A dashboard: at-risk subscribers ranked by risk, each with the chosen strategy, the final message, and an expandable trace of the agent handoffs that produced it
- Use the sample subscriber CSV from idea #10 (or generate your own with planted patterns)

**AWS Services & Framework:** Strands Agents SDK, Amazon Bedrock (Claude for all agents), Amazon S3, Amazon Bedrock AgentCore (stretch goal for deployment)

**Bonus Points:**
- Deploy the supervisor to **Amazon Bedrock AgentCore Runtime** so the retention desk runs as a managed, serverless agent — Strands agents deploy with a small wrapper (`bedrock-agentcore` SDK + `agentcore` CLI)
- Add a **segmentation agent** that groups at-risk subscribers into personas first, so the strategist works per-persona instead of per-person
- Give the reviewer a written quality rubric (no desperation, no repeats, must reference actual reading history) and show its scores
- Aggregate view: a churn-drivers report across the whole file, written by the analyst as editorial feedback
- A/B variants: the copywriter produces two versions per subscriber and explains the difference

**Quick-Start Hint:** Install Strands (`pip install strands-agents`) and use the [agents-as-tools pattern](https://strandsagents.com/docs/user-guide/concepts/multi-agent/agents-as-tools/): each specialist is an `Agent` with a focused system prompt, passed in the supervisor's `tools` array. Make the reviewer strict on purpose — a visible rejection is your demo's best moment. Keep the CSV small (15–20 subscribers with obvious planted patterns) so runs stay fast, and log every agent call to build the trace view. Get it working locally with Streamlit or Flask first; attempt AgentCore deployment only after the local demo works end to end.

---
