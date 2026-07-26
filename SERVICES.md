# AWS Services You Can Use

Your sandbox account comes with the services below ready to go. You do not need all of them, most winning demos use two or three. Not sure which to pick? Write "TBD, need help choosing" in your vision doc and ask an AWS expert or Claude Code on the day.

## Core AI services

These do the heavy lifting in almost every idea.

| Service | What it does | Good for |
|---------|--------------|----------|
| **Amazon Bedrock** | Access to foundation models (Claude for text and reasoning, Nova Canvas for images) through one API | Every idea, this is your AI engine |
| **Amazon Bedrock Knowledge Bases** | Upload documents and get semantic search with citations, no vector database to manage | Ask Your Archive (#9), Fact-Checker (#6), Rights Navigator (#4) |
| **Amazon Bedrock Guardrails** | Content filtering and automated reasoning checks on model outputs | Fact-Checker (#6), any idea producing reader-facing text |
| **Amazon Polly** | Text to speech, dozens of neural and long-form voices | Audio Engine (#5), One Story Every Format (#3) |
| **Amazon Textract** | Extract text, tables, and answers from PDFs and scans | Rights Navigator (#4), anything starting from documents |
| **Amazon Translate** | Fast baseline translation across 75+ languages | Cultural Adaptation (#7) |
| **Amazon Comprehend** | Detect entities, key phrases, and sentiment in text | Drop-Off Predictor (#8), Fact-Checker (#6), Backlist Revitalizer (#1) |
| **Amazon Transcribe** | Speech to text with speaker labels | Turning podcasts or interviews into text you can work with |
| **Amazon Rekognition** | Detect objects, faces, text, and moderation labels in images and video | Tagging photo archives, checking image content before publishing |

## The agent stack

For the advanced multi-agent ideas (#11 and #12), or to add agents to any idea.

| Tool | What it does |
|------|--------------|
| **Strands Agents SDK** | Open source framework for building agents in Python or TypeScript, one orchestrator agent can call specialist agents as tools |
| **Amazon Bedrock AgentCore** | Serverless runtime for deploying agents to production, build locally with Strands first, then deploy with a small wrapper |

## Media and video services

Publishers are video businesses too. If your idea touches video, these are for you.

| Service | What it does | Good for |
|---------|--------------|----------|
| **AWS Elemental Inference** | Applies AI to video, audio, and image content in real time: smart crop turns landscape video into vertical mobile formats, event clipping finds key moments and cuts highlight clips, smart subtitles generates subtitles from the audio, and contextual metadata classifies what is happening in the stream, including IAB Content Taxonomy output for contextual advertising and brand safety | Auto-creating social clips from video coverage, making video archives searchable, matching ads to video content without cookies |
| **AWS Elemental MediaConvert** | File-based video transcoding | Converting video into web and mobile ready formats |

Interested in Elemental Inference's contextual metadata for your build? Tell an AWS expert on the day and we will help your team get set up.

**Video idea starters:** feed a news clip through Elemental Inference and auto-generate a vertical social cut plus IAB taxonomy tags for ad targeting, or combine it with idea #9 so readers can search your video archive by what happens in the footage.

## App building blocks

| Service | What it does |
|---------|--------------|
| **Amazon S3** | Store uploads, generated audio and images, and results |
| **AWS Lambda** | Run code without servers, good for glue between services |
| **Amazon DynamoDB** | Simple fast database if your demo needs to remember things between sessions |

For the demo itself, a local Streamlit or Flask app calling these services is perfectly fine, you do not need to deploy infrastructure to win.

## AWS partner services

AWS has a large partner ecosystem, and you are welcome to use partner services as a complement to AWS services in your build.

- **Partner models in Amazon Bedrock:** beyond Claude, Bedrock gives you the same API for partner foundation models, including Stability AI for image generation, Luma AI for video generation, TwelveLabs for video understanding, Cohere for embeddings and reranking, and Mistral and Meta Llama for text. Model availability varies by region, check the Bedrock console in your sandbox.
- **AWS Marketplace:** thousands of partner tools (data feeds, analytics, content APIs) that run on or integrate with AWS.
- **Bring your own stack:** if your publishing house already uses a partner CMS, analytics platform, or email service, you can call its API from your app alongside AWS services, that often makes the demo feel real.

Ask an AWS expert on the day if you want help picking or connecting a partner service.

## Rules of thumb

1. Start with Bedrock plus S3, add other services only when they earn their place
2. Mock the AI responses first, get the app working, then wire in the real services
3. One service doing something impressive beats five services doing something shallow
