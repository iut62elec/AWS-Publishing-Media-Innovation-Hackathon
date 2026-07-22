# Real-Time Fact-Checker Vision Document

## Vision

Auto-detect factual claims in text and verify them against your own reference documents.

## Problem

Every nonfiction piece has dozens of factual claims -- dates, statistics, prices, quotes. Checking them is manual, slow, and often squeezed by deadlines. When errors slip through in health or finance content, they erode reader trust and hurt search rankings.

## Solution

Paste an article and provide a reference document (fact sheet, previous edition, or source material). Bedrock extracts every factual claim, then checks each one against your reference. Each claim gets a status: confirmed, disputed, or unverifiable -- with citations to the reference source.

## Technical Architecture

### AWS Services

- **Amazon Bedrock** -- Extracts factual claims from the article, verifies each against the reference document, and returns a status with citations. This is the only service the demo needs.
- **Amazon Comprehend** (optional) -- A separate quantitative entity signal (dates, amounts, organizations) if you want to cross-check that every detected entity was covered by a claim; Bedrock alone handles claim extraction fine
- **Amazon S3** (bonus only) -- Required if you use Bedrock Knowledge Bases for large reference sets, which ingests documents from S3

### Data Flow

**Basic approach (small reference docs):**

1. User pastes an article and a reference document
2. App sends the article + reference to Bedrock in one prompt
3. Bedrock extracts factual claims, verifies each against the reference, and returns a status per claim
4. App displays the claims with color-coded verification status

**Scalable approach (large or multiple reference docs — bonus):**

1. Upload reference documents to S3 and index them with Bedrock Knowledge Bases (managed RAG — automatic chunking, embedding, and indexing)
2. User pastes an article; Bedrock extracts the claims
3. For each claim, use `RetrieveAndGenerate` to semantically retrieve relevant reference chunks and verify the claim — no need to fit the full reference in the prompt
4. App displays results with color-coded verification status

### State Management

- **In-memory** -- Article, reference text, and claim verification results during processing (S3 only for the Knowledge Bases bonus)

## Users & Roles

- **Editor / Reviewer** -- Pastes the article, uploads references, and reviews the verification report
- **Author** (optional) -- Reviews flagged claims and provides corrections

## Key Workflows

1. User opens the app and clicks "New Fact Check"
2. User pastes an article (500-3,000 words)
3. User uploads a reference document (PDF, text, or pasted text)
4. User clicks "Check Facts"
5. System sends article + reference to Bedrock
6. Bedrock returns a list of claims with verification status
7. System displays results: each claim as a row with status badge
   - Green = confirmed against reference
   - Yellow = not found in reference (unverifiable)
   - Red = contradicts reference
9. User clicks any claim to see the supporting or contradicting reference passage

## Requirements

### Inputs

- **Article text** (required): Plain text, 500-3,000 words.
- **Reference document** (required): A fact sheet, previous edition, source document, or similar. Plain text or PDF.

### Outputs

- **Claim report**: JSON array of objects, each with:
  - `claim` (string, the factual statement)
  - `category` (string: "date", "statistic", "quote", "price", "other")
  - `status` (string: "confirmed", "disputed", "unverifiable")
  - `reference_passage` (string, the supporting or contradicting text from the reference, or null)
  - `confidence` (string: "high", "medium", "low")

### UI/UX Notes

- Two-panel layout: article on the left with inline highlights, claim list on the right
- Color-coded status badges (green/yellow/red)
- Click a claim to see the reference passage side by side

## API Integration

### Authentication

AWS sandbox credentials are pre-configured. No OAuth needed.

### Key API Calls

- `bedrock-runtime:InvokeModel` -- Extract claims from article, verify each against reference document (model: Claude on Bedrock)
- `comprehend:DetectEntities` (optional) -- Identify dates, numbers, names, organizations as a separate cross-check signal
- `bedrock-agent-runtime:RetrieveAndGenerate` -- (Bonus) Query Bedrock Knowledge Bases to semantically retrieve relevant reference chunks and verify claims. Scales to large reference sets without fitting everything in the prompt.

## API Resources

- [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)
- [Amazon Comprehend DetectEntities](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectEntities.html) (optional)
- [Amazon Bedrock Knowledge Bases - RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html) (bonus)
- [Amazon Bedrock Guardrails - Automated Reasoning Checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning.html) (bonus — up to 99% verification accuracy against domain knowledge)

## Out of Scope

- Live web verification or internet searches
- Automated corrections (system flags, humans fix)
- Real-time monitoring of published content
- Multi-article batch processing beyond the demo

## Success Criteria

- Paste an article and check at least 5 factual claims
- Each claim has a verification status (confirmed, disputed, or unverifiable)
- At least one claim is flagged as unverifiable or disputed
- Reference passages are cited for confirmed and disputed claims

## Judging Alignment (see JUDGING-RUBRIC.md)

- **Business impact:** a stale fact in a money or health article costs search rankings, affiliate revenue, and reader trust, the credit-card APR story prices the pain
- **Innovation angle:** the honest yellow "unverifiable" status, a fact-checker that never bluffs is the trustworthy kind, and that trust story resonates with publishing executives
- **Demo hook:** run an article with one planted error against the reference doc live, the red flag appearing on the wrong number is the moment
