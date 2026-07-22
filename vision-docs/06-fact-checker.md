# Real-Time Fact-Checker Vision Document

## Vision

Auto-detect factual claims in text and verify them against your own reference documents.

## Problem

Every nonfiction piece has dozens of factual claims -- dates, statistics, prices, quotes. Checking them is manual, slow, and often squeezed by deadlines. When errors slip through in health or finance content, they erode reader trust and hurt search rankings.

## Solution

Paste an article and upload a reference document (fact sheet, previous edition, or source material). Comprehend identifies key entities. Bedrock extracts every factual claim, then checks each one against your reference. Each claim gets a status: confirmed, disputed, or unverifiable -- with citations to the reference source.

## Technical Architecture

### AWS Services

- **Amazon Bedrock** -- Extracts factual claims from the article, then verifies each against the reference document and returns a status with citations
- **Amazon Comprehend** -- Detects and classifies entities (dates, amounts, organizations, people) to help focus the fact-checking
- **Amazon S3** -- Stores the article text, reference documents, and verification results

### Data Flow

**Basic approach (small reference docs):**

1. User pastes an article and uploads a reference document to S3
2. App sends the article to Comprehend for entity detection
3. Comprehend returns classified entities (dates, numbers, names, organizations)
4. App sends the article + reference doc + entity list to Bedrock
5. Bedrock extracts factual claims, verifies each against the reference, and returns a status per claim
6. App displays the claims with color-coded verification status

**Scalable approach (large or multiple reference docs — bonus):**

1. Upload reference documents to S3 and index them with Bedrock Knowledge Bases (managed RAG — automatic chunking, embedding, and indexing)
2. User pastes an article; app sends it to Comprehend for entity detection
3. For each claim, use `RetrieveAndGenerate` to semantically retrieve relevant reference chunks and verify the claim — no need to fit the full reference in the prompt
4. App displays results with color-coded verification status

### State Management

- **S3 bucket** -- Stores article text, reference documents, and JSON results
- **In-memory** -- Entity list and claim verification results during processing

## Users & Roles

- **Editor / Reviewer** -- Pastes the article, uploads references, and reviews the verification report
- **Author** (optional) -- Reviews flagged claims and provides corrections

## Key Workflows

1. User opens the app and clicks "New Fact Check"
2. User pastes an article (500-3,000 words)
3. User uploads a reference document (PDF, text, or pasted text)
4. User clicks "Check Facts"
5. System runs Comprehend to identify entities
6. System sends article + reference + entities to Bedrock
7. Bedrock returns a list of claims with verification status
8. System displays results: each claim as a row with status badge
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

- `comprehend:DetectEntities` -- Identify dates, numbers, names, organizations in the article
- `bedrock-runtime:InvokeModel` -- Extract claims from article, verify each against reference document (model: Claude on Bedrock)
- `bedrock-agent-runtime:RetrieveAndGenerate` -- (Bonus) Query Bedrock Knowledge Bases to semantically retrieve relevant reference chunks and verify claims. Scales to large reference sets without fitting everything in the prompt.

## API Resources

- [Amazon Comprehend DetectEntities](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectEntities.html)
- [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)
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
