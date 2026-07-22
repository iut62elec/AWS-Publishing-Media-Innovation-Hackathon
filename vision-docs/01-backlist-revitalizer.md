# AI Backlist Revitalizer Vision Document

## Vision

Match older catalog titles to current trends so publishers can resurface hidden gems.

## Problem

Publishers have thousands of backlist titles sitting idle. Some are one trend away from relevance, but nobody has time to cross-reference the catalog against what's popular right now. Thin metadata (just a title and one-line description) makes it even harder to spot opportunities.

## Solution

Upload a catalog CSV. Bedrock does the whole job in one flow: it enriches thin descriptions with inferred themes, scores each title against a set of trending topics you define, and writes a short marketing pitch for each match. The system returns a ranked list with confidence scores.

## Technical Architecture

### AWS Services

- **Amazon Bedrock** -- Enriches sparse metadata with inferred themes, compares each title against trending topics, scores relevance, and generates a short marketing pitch per title. One model call per batch of titles is enough.
- **Amazon S3** (optional) -- Store the uploaded CSV and results if you want persistence; a local file works fine for the demo

### Data Flow

1. User uploads a CSV file (titles, authors, descriptions)
2. App batches the rows and sends them to Bedrock with the user-provided trending topics
3. Bedrock enriches each title's themes, scores it against the trends, and writes a pitch for top scorers
4. App returns a ranked list as JSON

### State Management

- **In-memory** -- Catalog rows, trending topics, and Bedrock results live in app memory during processing; write the JSON output to a local file (or S3 if you chose it)

## Users & Roles

- **Marketing user** -- Uploads a catalog CSV, provides a list of current trends, and reviews the ranked results

## Key Workflows

1. User opens the app and clicks "Upload Catalog"
2. User selects a CSV file (20-50 rows with title, author, description columns)
3. User types or pastes a list of current trending topics (e.g., "gut health, remote work, AI ethics")
4. User clicks "Analyze"
5. System sends the titles + descriptions + trends to Bedrock, which enriches themes and scores each title
6. System displays a ranked list: title, confidence score, and a one-paragraph pitch
7. User can click any title to see the full pitch and matching trend

## Requirements

### Inputs

- **Catalog CSV** (required): Columns for title, author, description. 20-50 rows for the demo.
- **Trending topics** (required): Comma-separated list of 5-10 current topics.

### Outputs

- **Ranked list**: JSON array of objects, each with:
  - `title` (string)
  - `author` (string)
  - `score` (number, 0-100)
  - `matching_trends` (array of strings)
  - `pitch` (string, 2-3 sentences)

### UI/UX Notes

- Simple form: file upload + text box for trends + "Analyze" button
- Results displayed as a sortable table with expandable rows for the pitch text

## API Integration

### Authentication

AWS sandbox credentials are pre-configured in the environment. No OAuth or token management needed.

### Key API Calls

- `bedrock-runtime:InvokeModel` -- Enrich themes, score titles against trends, and generate pitches in one structured JSON response (model: Claude on Bedrock)
- `comprehend:DetectKeyPhrases` (optional) -- Only if you want a separate quantitative key phrase signal; Bedrock alone handles the demo fine

## API Resources

- [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)
- [Amazon Comprehend DetectKeyPhrases](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectKeyPhrases.html) (optional)

## Out of Scope

- Live trend data feeds (teams define trends manually)
- Real-time dashboards or visualizations beyond the results table
- Production catalog sync or CMS integration
- Multi-user access or authentication

## Success Criteria

- Upload a CSV of 20+ titles and get back a ranked list
- Each result has a confidence score and a short marketing pitch
- At least one title clearly matches a provided trend
- Results return within 60 seconds for a 50-row CSV

## Judging Alignment (see JUDGING-RUBRIC.md)

- **Business impact:** frame the value as found revenue, every resurfaced title is marketing-ready inventory you already own, zero new content cost
- **Innovation angle:** the metadata enrichment step, turning a one-line description into rich themes before matching, is what existing catalog tools don't do
- **Demo hook:** open with one real-feeling example ("this 2019 fermentation cookbook matches today's gut-health trend"), then show the ranked list finding it automatically
