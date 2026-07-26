## 11. AI Story Studio (Advanced, Multi-Agent)
*A newsroom of AI specialists, an editor in chief agent that directs a researcher, a writer, an illustrator, and a fact checker to turn one brief into a finished, illustrated story package*

**In Plain English:** Today, turning a story idea into a published piece takes a whole team, someone researches, someone writes, someone finds or creates art, and someone checks the facts. This project builds that team out of AI agents. You give one editor in chief agent a short brief, and it decides which specialist agents to call and in what order, the researcher gathers background, the writer drafts the piece, the illustrator generates artwork, and the fact checker reviews the claims. You watch the agents work together and get back a complete story package. This one is harder than the other ideas and uses a real multi agent framework, pick it if your team wants a challenge.

**⚠️ Difficulty: Advanced.** This idea takes the full afternoon and assumes your team is comfortable with Python. The reward is a demo few teams will have: real multi-agent orchestration, not a single prompt.

**The Problem:** Producing one publishable story is a relay race across a newsroom: research, drafting, artwork, fact-checking, packaging. Each handoff loses time and context. Single-prompt AI tools can draft text, but they can't run the whole relay — they don't decide what research is needed, they don't commission art, and they don't check their own facts. Publishers need AI that works the way a newsroom works: specialists coordinated by an editor.

**Real-Life Example:** Your features desk gets a brief: "800 words on how independent bookstores are using BookTok, with one hero illustration, by end of day." Today that's four people and six hours. With a story studio, an editor-in-chief agent reads the brief, sends the researcher agent to pull background and angles, hands the writer agent an outline, commissions the illustrator agent for a hero image matching the story's mood, and routes the draft through the fact-checker agent — which flags two shaky claims for human review. A complete, illustrated, pre-checked story package lands in an editor's queue in minutes.

**What You'll Build:**
- A multi-agent system using the **[Strands Agents](https://strandsagents.com/) framework** with the **agents-as-tools pattern**: one orchestrator agent (the editor-in-chief) that calls specialist agents as tools
- At least three specialist sub-agents: a **researcher** (gathers background and key facts from provided source material), a **writer** (drafts the story from the researcher's notes), and an **illustrator** (generates a hero image with an image model on Bedrock, e.g. Amazon Nova Canvas)
- A **fact-checker** sub-agent that reviews the draft's claims against the research notes and flags anything unsupported — the orchestrator sends the draft back to the writer if the fact-checker rejects it
- A visible orchestration trace in your UI: show which agent is working, what it was asked, and what it returned — the coordination IS the demo
- Output: a story package with the article draft, the hero image, and a fact-check report

**AWS Services & Framework:** Strands Agents SDK, Amazon Bedrock (Claude for the agents, Nova Canvas for illustration), Amazon S3, Amazon Bedrock AgentCore (stretch goal for deployment)

**Bonus Points:**
- Deploy the orchestrator to **Amazon Bedrock AgentCore Runtime** so it runs as a managed, serverless agent instead of on your laptop — Strands agents deploy to AgentCore with a small wrapper (`bedrock-agentcore` SDK + `agentcore` CLI)
- Add a **packaging agent** that produces the headline options, social copy, and SEO summary (reuse idea #3's thinking as a sub-agent)
- Let the fact-checker trigger a real revision loop: rejected draft goes back to the writer with the specific objections, and the trace shows the second pass
- Generate 2–3 illustration candidates and let the human editor pick one
- Stream the agent trace live in the UI so judges watch the newsroom think

**Quick-Start Hint:** Install Strands (`pip install strands-agents`) and start with the [agents-as-tools pattern](https://strandsagents.com/docs/user-guide/concepts/multi-agent/agents-as-tools/): define each specialist as an `Agent` with a focused system prompt, then pass them in the orchestrator's `tools` array — Strands converts them into callable tools automatically. Use the `@tool` decorator for the illustrator so you can call Nova Canvas (`InvokeModel` with `amazon.nova-canvas-v1:0`) inside it and return the S3 image URL. Get the whole flow working locally first with a Streamlit or Flask front end; only attempt AgentCore deployment after the local demo works end to end. Budget your time: orchestrator + 2 agents working beats 5 agents half-wired.

---
