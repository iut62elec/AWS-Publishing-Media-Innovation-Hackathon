# Autonomous Retention Desk Vision Document (Advanced, Multi-Agent)

> **Difficulty: Advanced.** This build uses the Strands Agents framework and real multi-agent orchestration. Plan for the full afternoon and make sure at least one teammate is comfortable with Python. It is the agentic big sibling of idea #10 (Subscriber Save Engine) -- if your team wants the safer single-prompt version, build that instead.

## Vision

A subscriber retention desk run by a team of AI agents: a supervisor directs analyst, strategist, copywriter, and reviewer agents to find at-risk subscribers, choose the right save move for each, write the message, and quality-check it before a human approves.

## Problem

The median news publisher loses 4-5% of digital subscribers every month, and the usual response is one generic discount email sent after the reader has already decided to leave. Acting personally at scale is a pipeline of human judgment calls -- who is at risk, what save move fits them, what message sounds right, is the message actually good -- and each step needs its own expertise. A single prompt can't run that pipeline; a coordinated team of specialist agents can.

## Solution

The user uploads a subscriber engagement CSV. A supervisor agent built with the Strands Agents framework runs the desk using the agents-as-tools pattern: the analyst assigns churn risk with evidence, the strategist picks a save move per at-risk subscriber (content win-back, offer, service recovery, or let-go), the copywriter drafts the message in the publication's voice, and the reviewer scores each draft against a quality rubric -- rejecting bad drafts back to the copywriter with reasons. The user gets a dashboard of finished save plans, each with an expandable trace of the agent handoffs (including rejections) that produced it.

## Technical Architecture

### Framework

- **Strands Agents SDK** (`pip install strands-agents`) -- the multi-agent framework. The supervisor is a Strands `Agent`; each specialist is a Strands `Agent` passed in the supervisor's `tools` array (agents-as-tools pattern).

### AWS Services

- **Amazon Bedrock (Claude)** -- powers the supervisor and all four specialists via the Strands `BedrockModel` provider
- **Amazon S3** (optional) -- store the CSV and the output plans if you want persistence; local files are fine for the demo
- **Amazon Bedrock AgentCore Runtime** (stretch goal) -- serverless managed deployment of the supervisor once the local build works

### Agent Roster

| Agent | Role | Implementation |
|-------|------|----------------|
| Supervisor | Runs the desk: feeds data to specialists, routes rejected drafts back, assembles the dashboard data | Strands `Agent` with sub-agents as tools |
| Analyst | Reads the engagement CSV, assigns churn risk (high/medium/low) with evidence per subscriber | Strands `Agent` as tool |
| Strategist | Picks the save move per high-risk subscriber and explains why | Strands `Agent` as tool |
| Copywriter | Writes the save message in the publication's brand voice, personalized to reading history | Strands `Agent` as tool |
| Reviewer | Scores each draft against a quality rubric, approves or rejects with specific objections | Strands `Agent` as tool |

### Data Flow

1. User uploads the subscriber engagement CSV (sample provided, 15-20 rows with planted patterns)
2. Supervisor calls the analyst, which returns risk level + warning signs per subscriber
3. For each high-risk subscriber, supervisor calls the strategist for a save move
4. Supervisor calls the copywriter with the subscriber's history, the strategy, and the brand voice guide
5. Supervisor calls the reviewer with the draft and the quality rubric
6. If rejected, supervisor routes the draft back to the copywriter with the reviewer's objections (revision loop)
7. App displays the dashboard: subscribers ranked by risk, each with strategy, final message, and the agent trace

### State Management

- **In-memory** -- Subscriber records, agent outputs, and the orchestration trace live in app memory; write the final plans to a local JSON file (or S3 if chosen)

## Users & Roles

- **Retention manager** -- Uploads the CSV, watches the desk run, reviews and approves the save plans

## Key Workflows

1. User opens the app and clicks "Load sample data" (or uploads their own CSV)
2. User clicks "Run the desk"
3. The trace panel shows the supervisor delegating: analyst first, then strategist, copywriter, and reviewer per subscriber
4. The reviewer rejects at least one draft (for example, it sounds desperate or repeats content the reader already saw); the trace shows the revision loop
5. The dashboard fills in: at-risk subscribers ranked by risk, each with their story, strategy, and final message
6. User expands one subscriber to read the full agent debate, then approves the plans

## Requirements

### Inputs

- **Subscriber engagement CSV** (required): tenure, visit frequency, favorite sections, last visit, newsletter opens. 15-20 rows with obvious planted patterns (a daily reader gone quiet, a loyal opener who stopped opening, a new subscriber who never engaged).
- **Brand voice guide** (required): a short paragraph describing the publication's tone, fed to the copywriter.
- **Quality rubric** (required): 3-5 written rules for the reviewer (no desperation, must reference actual reading history, no repeated recommendations).

### Outputs

- **Save plans**: JSON array, one per high-risk subscriber:
  - `subscriber_id`, `risk_level`, `warning_signs` (array of strings)
  - `strategy` (content-winback | offer | service-recovery | let-go) with `reason`
  - `message` (string, the final approved draft)
  - `review_history` (array: each attempt with the reviewer's verdict and objections)
- **Trace**: array of agent calls (agent name, input summary, output summary)

### UI/UX Notes

- Dashboard-first layout: ranked at-risk list, expandable rows showing strategy, message, and trace
- Make rejections visually distinct in the trace (red) -- the revision loop is the demo moment
- Streamlit or Flask both work; Streamlit is faster to build

## API Integration

### Authentication

AWS sandbox credentials are pre-configured in the environment. No OAuth or token management needed.

### Key API Calls

- Strands `Agent(...)` with `BedrockModel` -- all agent reasoning (supervisor and specialists)
- `s3:PutObject` (optional) -- persist plans and traces

### API Resources

- [Strands Agents: Agents as Tools](https://strandsagents.com/docs/user-guide/concepts/multi-agent/agents-as-tools/)
- [Strands Agents: Amazon Bedrock model provider](https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/)
- [Deploying Strands agents to Bedrock AgentCore Runtime](https://strandsagents.com/docs/user-guide/deploy/deploy_to_bedrock_agentcore/)

## Build Order (important for this idea)

1. Supervisor + analyst only: CSV in, risk assessments out, working locally
2. Add the strategist and copywriter for high-risk subscribers
3. Add the reviewer with its rubric and the revision loop
4. Build the dashboard and trace UI
5. Only then, if time remains: AgentCore deployment (wrap the supervisor with the `bedrock-agentcore` SDK, deploy with the `agentcore` CLI)

## Out of Scope

- Actually sending emails (drafts only, human approves)
- Real subscriber data or CRM/ESP integration
- Payment or offer redemption flows
- Multi-user access or authentication

## Success Criteria

- CSV in, ranked dashboard of save plans out, fully assembled by the agent team
- The trace clearly shows at least 4 distinct agents being orchestrated per subscriber
- The reviewer visibly rejects at least one draft and the revision loop produces a better one
- Each final message references the subscriber's actual reading history from the CSV
- Full run on 15-20 subscribers completes in under 5 minutes

## Judging Alignment (see JUDGING-RUBRIC.md)

- **Business impact:** at 4-5% monthly churn, every saved subscriber is recurring revenue protected at near-zero marginal cost -- and personal beats generic discount
- **Innovation angle:** the agents challenge each other -- a reviewer that rejects the copywriter's draft with reasons is quality control no single-prompt tool can do
- **Demo hook:** expand one subscriber and read the agent debate out loud: the analyst's warning signs, the strategist's call, the rejected first draft, and the better final message
