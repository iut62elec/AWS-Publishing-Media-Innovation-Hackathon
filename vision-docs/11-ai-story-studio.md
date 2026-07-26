# AI Story Studio Vision Document (Advanced, Multi-Agent)

> **Difficulty: Advanced.** This build uses the Strands Agents framework and real multi-agent orchestration. Plan for the full afternoon and make sure at least one teammate is comfortable with Python.

## Vision

An AI newsroom in miniature: an editor-in-chief agent that directs researcher, writer, illustrator, and fact-checker agents to turn one story brief into a finished, illustrated, fact-checked story package.

## Problem

Producing one publishable story is a relay race: research, drafting, artwork, fact-checking, packaging. Each handoff loses time and context. Single-prompt AI tools draft text but can't run the relay -- they don't decide what research is needed, don't commission art, and don't check their own work. Publishers need AI that works the way a newsroom works: specialists coordinated by an editor.

## Solution

The user pastes a story brief. An orchestrator agent (editor-in-chief) built with the Strands Agents framework decides which specialist agents to call and in what order, using the agents-as-tools pattern. The researcher gathers background from provided source material, the writer drafts the piece, the illustrator generates a hero image with an image model on Bedrock, and the fact-checker reviews the draft's claims -- rejecting it back to the writer if claims are unsupported. The UI shows the orchestration trace live, and the output is a complete story package: article, hero image, fact-check report.

## Technical Architecture

### Framework

- **Strands Agents SDK** (`pip install strands-agents`) -- the multi-agent framework. The orchestrator is a Strands `Agent`; each specialist is a Strands `Agent` passed in the orchestrator's `tools` array (agents-as-tools pattern). Strands converts them into callable tools automatically.

### AWS Services

- **Amazon Bedrock (Claude)** -- powers the orchestrator and all text agents (researcher, writer, fact-checker) via the Strands `BedrockModel` provider
- **Amazon Bedrock (Nova Canvas)** -- image generation inside the illustrator agent's custom `@tool`
- **Amazon S3** -- stores generated images (and the story package if you want persistence)
- **Amazon Bedrock AgentCore Runtime** (stretch goal) -- serverless managed deployment of the orchestrator once the local build works

### Agent Roster

| Agent | Role | Implementation |
|-------|------|----------------|
| Editor-in-chief | Orchestrator: reads the brief, plans, calls specialists, assembles the package | Strands `Agent` with sub-agents as tools |
| Researcher | Extracts background, angles, and key facts from provided source material | Strands `Agent` as tool |
| Writer | Drafts the story from the brief plus researcher notes | Strands `Agent` as tool |
| Illustrator | Writes an image prompt matching the story's mood, calls Nova Canvas, returns the image | Custom `@tool` wrapping an `Agent` + `InvokeModel` |
| Fact-checker | Compares the draft's claims against the research notes, approves or rejects with reasons | Strands `Agent` as tool |

### Data Flow

1. User pastes a story brief (topic, length, tone) and optionally source material
2. Orchestrator plans the work and calls the researcher agent
3. Researcher returns structured notes: key facts, angles, quotes
4. Orchestrator calls the writer agent with the brief plus the notes
5. Orchestrator calls the illustrator agent, which generates a Nova Canvas image and stores it in S3
6. Orchestrator calls the fact-checker agent with the draft and the research notes
7. If the fact-checker rejects, the orchestrator sends the draft back to the writer with the objections (one revision loop)
8. App displays the story package and the full agent trace

### State Management

- **In-memory** -- The orchestration trace (which agent, what input, what output, timestamps) lives in app memory and drives the UI; images go to S3

## Users & Roles

- **Editor** -- Pastes the brief, watches the agents work, reviews the finished package

## Key Workflows

1. User opens the app, pastes a brief ("800 words on independent bookstores using BookTok, one hero illustration"), and pastes or uploads 2-3 source articles
2. User clicks "Run the studio"
3. The trace panel shows the editor-in-chief delegating: researcher working, then writer, then illustrator, then fact-checker
4. The fact-checker flags an unsupported claim; the trace shows the draft going back to the writer and returning fixed
5. The finished package appears: article, hero image, fact-check report
6. User reviews and exports

## Requirements

### Inputs

- **Story brief** (required): topic, target length, tone. A few sentences.
- **Source material** (required): 2-3 articles or documents pasted or uploaded, so the researcher and fact-checker have something real to work against.

### Outputs

- **Story package**:
  - `article` (string, markdown)
  - `hero_image_url` (string, S3 URL)
  - `fact_check_report` (array of claims, each with status: supported / unsupported / needs-review)
  - `trace` (array of agent calls: agent name, input summary, output summary)

### UI/UX Notes

- Two-panel layout: story package on the left, live agent trace on the right
- The trace is the demo: make each agent's turn visible and readable
- Streamlit or Flask both work; Streamlit is faster to build

## API Integration

### Authentication

AWS sandbox credentials are pre-configured in the environment. No OAuth or token management needed.

### Key API Calls

- Strands `Agent(...)` with `BedrockModel` -- all agent reasoning (orchestrator and specialists)
- `bedrock-runtime:InvokeModel` with `amazon.nova-canvas-v1:0` -- image generation inside the illustrator tool
- `s3:PutObject` / presigned GET -- store and serve the hero image

### API Resources

- [Strands Agents: Agents as Tools](https://strandsagents.com/docs/user-guide/concepts/multi-agent/agents-as-tools/)
- [Strands Agents: Amazon Bedrock model provider](https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/)
- [Amazon Nova Canvas](https://docs.aws.amazon.com/nova/latest/userguide/image-generation.html)
- [Deploying Strands agents to Bedrock AgentCore Runtime](https://strandsagents.com/docs/user-guide/deploy/deploy_to_bedrock_agentcore/)

## Build Order (important for this idea)

1. Orchestrator + writer only, working end to end locally
2. Add the researcher, then the fact-checker with its revision loop
3. Add the illustrator (custom tool + Nova Canvas + S3)
4. Polish the trace UI
5. Only then, if time remains: AgentCore deployment (wrap the orchestrator with the `bedrock-agentcore` SDK, deploy with the `agentcore` CLI)

## Out of Scope

- CMS integration or real publishing
- Web search or live research (researcher works from provided source material only)
- Video or audio outputs
- Multi-user access or authentication
- Fine-grained cost tracking per agent

## Success Criteria

- One brief in, one complete story package out: article + hero image + fact-check report
- The trace clearly shows at least 4 distinct agents being orchestrated
- The fact-checker visibly rejects at least one draft and the revision loop runs
- The hero image matches the story's subject and mood
- Full run completes in under 5 minutes

## Judging Alignment (see JUDGING-RUBRIC.md)

- **Business impact:** four people and six hours of newsroom relay compressed to minutes per story package, at backlist-content cost
- **Innovation angle:** real multi-agent orchestration with a revision loop -- the agents check and reject each other's work, which single-prompt tools cannot do
- **Demo hook:** the moment the fact-checker rejects the writer's draft on screen and the trace shows the story going back for a fix -- judges watch AI editorial judgment happen live
