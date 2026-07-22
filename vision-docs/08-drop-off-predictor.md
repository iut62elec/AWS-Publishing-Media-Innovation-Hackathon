# Reader Drop-Off Predictor Vision Document

## Vision

Predict where readers lose interest in your content -- before you publish.

## Problem

Publishers don't know where readers stop reading until after publication. For digital, you see scroll depth and bounce rates only after the damage is done. A 3,000-word article where 60% of readers bail before the call-to-action means lost conversions and declining search rankings. Predicting drop-off points before publishing gives editors a new tool for tightening content.

## Solution

Upload a text passage. The app splits it into sections (each under 5KB for Comprehend's per-call limit), then runs Comprehend to extract raw signals per section — key phrase density (DetectKeyPhrases), entity count (DetectEntities), and sentiment (DetectSentiment). Note: Comprehend provides raw signals, not readability scores — Bedrock interprets them. The app sends the text and Comprehend signals to Bedrock. Bedrock predicts engagement levels, identifies drop-off factors (pacing issues, complexity spikes, topic shifts, sentiment shifts), and suggests concrete revisions. Results are shown as a heatmap.

## Technical Architecture

### AWS Services

- **Amazon Comprehend** -- Extracts consistent quantitative signals per section: key phrase density (DetectKeyPhrases), entity count (DetectEntities), sentiment polarity and shifts (DetectSentiment). These give the prediction a repeatable numeric backbone that a general model would score inconsistently. Each call is limited to 5KB of text, so process section by section.
- **Amazon Bedrock** -- Interprets the Comprehend signals alongside the text, predicts per-section engagement, identifies drop-off factors, and suggests revisions. A simpler Bedrock-only version (skip Comprehend, let the model score sections directly) is a valid starting point, add Comprehend signals when the basic flow works.

### Data Flow

1. User uploads or pastes a long-form text passage
2. App splits the text into logical sections (by paragraph or heading)
3. App sends each section to Comprehend for key phrase detection (DetectKeyPhrases), entity counting (DetectEntities), and sentiment analysis (DetectSentiment). Each section must be under 5KB.
4. App bundles the text + Comprehend signals and sends them to Bedrock
5. Bedrock returns per-section engagement scores, drop-off factors, and revision suggestions
6. App renders the results as a color-coded heatmap

### State Management

- **In-memory** -- Section splits, Comprehend metrics, and scores during processing (no storage service needed for the demo)

## Users & Roles

- **Content strategist / Editor** -- Uploads text, reviews the engagement heatmap, and uses revision suggestions to improve the piece

## Key Workflows

1. User opens the app and clicks "Analyze Content"
2. User pastes or uploads a text passage (1,000-5,000 words)
3. User clicks "Predict Engagement"
4. System splits text into sections and runs Comprehend on each
5. System sends text + metrics to Bedrock for engagement analysis
6. System displays a heatmap: each section color-coded by predicted engagement
   - Green = high engagement (readers stay)
   - Yellow = moderate (readers may skim)
   - Red = low (likely drop-off point)
7. User clicks any section to see:
   - Drop-off factors (e.g., "complexity spike," "topic shift," "dense paragraph")
   - Specific revision suggestions
8. User can apply a suggestion and re-analyze to see improvement

## Requirements

### Inputs

- **Text passage** (required): Plain text, 1,000-5,000 words. Articles, blog posts, or long-form content.

### Outputs

- **Engagement heatmap**: Per-section scores rendered visually
- **Section analysis**: JSON array of objects, each with:
  - `section_number` (number)
  - `text_preview` (string, first 50 characters)
  - `engagement_score` (number, 1-10)
  - `readability_metrics` (object: sentence_complexity, entity_density, key_phrase_count)
  - `drop_off_factors` (array of strings)
  - `revision_suggestions` (array of strings)

### UI/UX Notes

- Single text area for input
- Vertical heatmap alongside the text, with clickable sections
- Detail panel showing factors and suggestions for the selected section

## API Integration

### Authentication

AWS sandbox credentials are pre-configured. No OAuth needed.

### Key API Calls

- `comprehend:DetectKeyPhrases` -- Extract key phrases per section (density signal). Limited to 5KB per call.
- `comprehend:DetectEntities` -- Count and classify entities per section (density signal). Limited to 5KB per call.
- `comprehend:DetectSentiment` -- Returns POSITIVE/NEGATIVE/NEUTRAL/MIXED with confidence scores per section. Tracking sentiment shifts between sections is a useful engagement signal. Limited to 5KB per call.
- `comprehend:DetectSyntax` (optional) -- Part-of-speech tags per token if you want a complexity signal; note it does NOT compute readability scores. Limited to 5KB per call, 6 languages.
- `bedrock-runtime:InvokeModel` -- Interpret Comprehend signals, predict engagement, identify drop-off factors, and generate revision suggestions (model: Claude on Bedrock)

## API Resources

- [Amazon Comprehend DetectKeyPhrases](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectKeyPhrases.html)
- [Amazon Comprehend DetectEntities](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectEntities.html)
- [Amazon Comprehend DetectSentiment](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectSentiment.html)
- [Amazon Comprehend DetectSyntax](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectSyntax.html)
- [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)

## Out of Scope

- Integration with real analytics platforms or scroll tracking
- A/B testing of revisions
- Historical performance benchmarks
- Multi-article pattern analysis beyond a single piece

## Success Criteria

- Upload a text passage and get a per-section engagement prediction
- Results display as a visual heatmap with at least 3 color levels
- At least one section is flagged as a likely drop-off point with specific factors
- Revision suggestions are concrete and actionable (not generic advice)

## Judging Alignment (see JUDGING-RUBRIC.md)

- **Business impact:** "60% of readers bail before the call-to-action" is lost conversion revenue, and this moves the fix from post-mortem analytics to pre-publication editing
- **Innovation angle:** predicting engagement *before* publication is a genuinely new editorial tool, analytics tell you what happened, this tells you what will happen
- **Demo hook:** analyze a deliberately baggy article, point at the red section, apply the suggested fix, re-analyze, and watch the section turn green, the before/after is the demo
