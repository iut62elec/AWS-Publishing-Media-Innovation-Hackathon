# Ask Your Archive Vision Document

## Vision

Give readers a publisher-owned AI chat experience over your own content, so they get answers on your site instead of a chatbot's.

## Problem

AI Overviews and chatbots are answering readers' questions before they ever reach the publisher. Click-through rates drop from roughly 15% to 8% when an AI Overview appears, and publishers expect search traffic to keep falling. Leading publishers (Washington Post's "Ask The Post AI", FT's "Ask FT") are responding by owning the AI experience — conversational search over their own archive, grounded in their own journalism. Most publishers don't have this yet.

## Solution

Upload 10-20 articles to S3. A chat interface lets readers ask questions in plain English. Bedrock answers using only the uploaded archive, cites the specific source articles for every claim, and honestly says "our archive doesn't cover this" when the answer isn't there. Every citation links back to an article — a pageview the publisher would otherwise have lost.

## Technical Architecture

### AWS Services

- **Amazon Bedrock** -- Answers questions grounded in the uploaded articles, with per-claim citations; refuses questions the archive can't answer
- **Amazon S3** -- Stores the article archive

### Data Flow

1. User uploads 10-20 articles (or uses provided samples) to S3
2. Reader types a question in the chat interface
3. App loads the articles plus the question into a single Bedrock prompt with strict grounding instructions
4. Bedrock returns an answer with cited article titles, or a "not covered" response
5. App renders the answer with clickable citations and the chat history

### State Management

- **S3 bucket** -- Stores the article archive
- **In-memory** -- Chat history and loaded article text during the session

## Users & Roles

- **Reader** -- Asks questions and follows citations to full articles
- **Editor (bonus)** -- Reviews which questions had no good answer, as an editorial gap report

## Key Workflows

1. User opens the app and sees a chat box with 3-4 suggested starter questions
2. Reader clicks a starter question or types their own
3. System sends the archive + question to Bedrock
4. Answer appears with citations listing each source article title
5. Reader asks a follow-up; the conversation continues with context
6. Reader asks something outside the archive; the system says the archive doesn't cover it

## Requirements

### Inputs

- **Article archive** (required): 10-20 articles, plain text or markdown, 300-2,000 words each. Sample articles provided.
- **Reader question** (required): Free-text chat input.

### Outputs

- **Grounded answer**: JSON object with:
  - `answer` (string, the synthesized response)
  - `citations` (array of objects: `article_title`, `relevance` string)
  - `covered` (boolean, false when the archive cannot answer)
  - `suggested_followups` (array of strings, optional)

### UI/UX Notes

- Chat layout with message history, citations rendered as distinct chips or links under each answer
- Show suggested starter questions -- real publisher chatbots found readers struggle with a blank prompt box
- A visible "not covered by our archive" state builds trust; never let it invent an answer

## API Integration

### Authentication

AWS sandbox credentials are pre-configured. No OAuth needed.

### Key API Calls

- `bedrock-runtime:InvokeModel` -- Send archive + question with grounding instructions, receive answer with citations (model: Claude on Bedrock)
- `bedrock-agent-runtime:RetrieveAndGenerate` (bonus) -- Bedrock Knowledge Bases for semantic retrieval when the archive outgrows the context window

## API Resources

- [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)
- [Bedrock Knowledge Bases RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html)
- [Amazon S3 PutObject / GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)

## Out of Scope

- User accounts, paywall, or subscription integration
- Crawling or ingesting live websites
- Vector database setup beyond Bedrock Knowledge Bases (bonus only)
- Moderation of reader questions

## Success Criteria

- Ask at least 3 questions: one answered from a single article, one synthesized across multiple articles, one the archive can't answer
- Every answer cites the source article titles
- The out-of-archive question gets an honest "not covered" response, not a hallucination
- Follow-up questions keep conversational context
