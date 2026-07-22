# AI Backlist Revitalizer Vision Document

## Vision

Match older catalog titles to current trends so publishers can resurface hidden gems.

## Problem

Publishers have thousands of backlist titles sitting idle. Some are one trend away from relevance, but nobody has time to cross-reference the catalog against what's popular right now. Thin metadata (just a title and one-line description) makes it even harder to spot opportunities.

## Solution

Upload a catalog CSV to S3. Use Comprehend to pull themes from thin descriptions, then use Bedrock to score each title against a set of trending topics you define. The system returns a ranked list with confidence scores and a short marketing pitch for each match.

## Technical Architecture

### AWS Services

- **Amazon Bedrock** -- Compares each title's metadata against trending topics, scores relevance, and generates a short marketing pitch per title
- **Amazon Comprehend** -- Extracts key phrases and themes from sparse catalog descriptions to give Bedrock more to work with
- **Amazon S3** -- Stores the uploaded CSV and output results

### Data Flow

1. User uploads a CSV file (titles, authors, descriptions) to S3
2. App reads the CSV and sends each description to Comprehend for key phrase extraction
3. App combines the original metadata + extracted themes into a prompt for Bedrock
4. Bedrock scores each title against the user-provided trending topics
5. Bedrock generates a short pitch for top-scoring titles
6. App returns a ranked list as JSON

### State Management

- **S3 bucket** -- Stores the input CSV and the JSON output
- **In-memory** -- Trending topics list and intermediate Comprehend results live in app memory during processing

## Users & Roles

- **Marketing user** -- Uploads a catalog CSV, provides a list of current trends, and reviews the ranked results

## Key Workflows

1. User opens the app and clicks "Upload Catalog"
2. User selects a CSV file (20-50 rows with title, author, description columns)
3. User types or pastes a list of current trending topics (e.g., "gut health, remote work, AI ethics")
4. User clicks "Analyze"
5. System extracts key phrases from each description using Comprehend
6. System sends each title + themes + trends to Bedrock for scoring
7. System displays a ranked list: title, confidence score, and a one-paragraph pitch
8. User can click any title to see the full pitch and matching trend

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

- `comprehend:DetectKeyPhrases` -- Extract themes from each catalog description
- `bedrock-runtime:InvokeModel` -- Score titles against trends and generate pitches (model: Claude on Bedrock)

## API Resources

- [Amazon Comprehend DetectKeyPhrases](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectKeyPhrases.html)
- [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)
- [Amazon S3 PutObject / GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)

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
