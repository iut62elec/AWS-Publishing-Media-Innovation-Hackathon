# AI Rights & Permissions Navigator Vision Document

## Vision

Ask your publishing contracts plain-English questions and get answers with clause citations.

## Problem

Rights managers dig through PDFs -- sometimes scanned ones from the '90s -- to answer simple questions like "Can we sell this audiobook in Germany?" The information exists, but it's buried in legal language across hundreds of files. A single rights lookup can take days.

## Solution

Upload a PDF contract. Textract extracts the text (including scanned documents). Paste the extracted text into Bedrock with a plain-English question. Bedrock returns an answer that cites specific contract clauses and flags anything ambiguous as "needs legal review."

## Technical Architecture

### AWS Services

- **Amazon Textract** -- Extracts text from PDF contracts, including scanned/image-based PDFs via OCR (this is where Textract genuinely beats a general model: reliable OCR on scans)
- **Amazon Bedrock** -- Answers plain-English questions about the contract text, citing specific clauses
- **Amazon S3** (conditional) -- Required only for async Textract on contracts longer than 5 pages (async input must come from S3); sync Textract accepts the PDF bytes directly

### Data Flow

1. User uploads 1-2 PDF contracts
2. App sends each PDF to Textract for text extraction (bytes directly for short PDFs, via S3 for long ones)
3. Textract returns the full text of each contract
4. User types a question in plain English
5. App sends the contract text + question to Bedrock
6. Bedrock returns an answer with clause citations and ambiguity flags
7. App displays the answer with highlighted source clauses

### State Management

- **In-memory** -- Extracted contract text and Bedrock conversation history (for follow-up questions); S3 only when async Textract requires it

## Users & Roles

- **Rights manager** -- Uploads contracts, asks questions, and reviews answers
- **Legal reviewer** (optional) -- Reviews clauses flagged as ambiguous

## Key Workflows

1. User opens the app and clicks "Upload Contract"
2. User selects 1-2 PDF files
3. System runs Textract and shows a "Processing..." indicator
4. System displays the extracted text for confirmation
5. User types a question (e.g., "Which titles have open audio rights in Europe?")
6. User clicks "Ask"
7. System sends the full contract text + question to Bedrock
8. System displays the answer with cited clause numbers
9. Clauses flagged as ambiguous show a yellow "Needs Legal Review" badge
10. User can ask follow-up questions in the same session

## Requirements

### Inputs

- **PDF contracts** (required): 1-2 PDF files. Can be digital or scanned. Note: synchronous Textract is limited to 5 pages per call — for longer contracts, use async processing (`StartDocumentAnalysis`).
- **Question** (required): Plain-English question about the contract.

### Outputs

- **Answer**: Plain-English response with:
  - `answer` (string)
  - `cited_clauses` (array of objects: clause number, relevant text, page reference)
  - `ambiguous_flags` (array of clauses marked as unclear or needing legal review)
  - `confidence` (string: "high", "medium", "low")

### UI/UX Notes

- PDF upload area with drag-and-drop
- Text box for questions with a "Ask" button
- Answer panel with cited clauses highlighted
- Yellow badges for ambiguous items

## API Integration

### Authentication

AWS sandbox credentials are pre-configured. No OAuth needed.

### Key API Calls

- `textract:DetectDocumentText` -- Extract text from digital PDFs (sync, up to 5 pages)
- `textract:AnalyzeDocument` -- Extract text from scanned/image PDFs with OCR (sync, up to 5 pages). Supports FeatureTypes: QUERIES (ask specific questions about the doc, e.g., "What is the termination date?"), LAYOUT (preserves reading order), TABLES, FORMS.
- `textract:StartDocumentAnalysis` / `GetDocumentAnalysis` -- Async processing for contracts longer than 5 pages. Required for multi-page PDFs that exceed the sync limit. Input from S3, poll for results.
- `bedrock-runtime:InvokeModel` -- Answer questions about contract text with citations (model: Claude on Bedrock)

## API Resources

- [Amazon Textract DetectDocumentText](https://docs.aws.amazon.com/textract/latest/dg/API_DetectDocumentText.html)
- [Amazon Textract AnalyzeDocument](https://docs.aws.amazon.com/textract/latest/dg/API_AnalyzeDocument.html)
- [Amazon Textract StartDocumentAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_StartDocumentAnalysis.html) (async, for contracts over 5 pages)
- [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)

## Out of Scope

- Contract database or search index (just use Bedrock's context window)
- Automated alerts for expiring rights
- Legal compliance validation
- Multi-user access or permissions

## Success Criteria

- Upload 1-2 PDF contracts and extract text successfully
- Ask at least 3 plain-English questions and get answers with clause citations
- At least one ambiguous clause is flagged as "needs legal review"
- Answers return within 30 seconds per question

## Judging Alignment (see JUDGING-RUBRIC.md)

- **Business impact:** "a rights lookup that takes two days takes thirty seconds", missed rights windows are missed deals, and the film-studio-call story makes it concrete
- **Innovation angle:** clause-level citations and the honest "needs legal review" flag, the system knows what it doesn't know, executives from legal-heavy businesses will notice
- **Demo hook:** ask the contract a question a judge might ask ("can we sell the audiobook in Germany?") and let the cited clause appear on screen
