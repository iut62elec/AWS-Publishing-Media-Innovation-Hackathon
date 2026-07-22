# Intelligent Content Triage Vision Document

## Vision

Let AI do the first read on submissions so editors can focus on the good stuff.

## Problem

Editors get buried in submissions -- thousands of manuscripts, pitches, and drafts per year. Most won't make the cut, but someone still has to read every one. That first-pass screening eats time that should go toward actual editing.

## Solution

Paste or upload 2-3 sample submissions. Send each to Bedrock along with your editorial standards. Bedrock returns a structured JSON assessment for each submission: quality score, topic fit, strengths, concerns, and a recommendation (pass, consider, reject).

## Technical Architecture

### AWS Services

- **Amazon Bedrock** -- Reads each submission, evaluates it against your editorial standards, and returns a structured JSON assessment. This is the only service the demo needs.
- **Amazon S3** (optional) -- Store submissions and assessments if you want persistence; pasted text and in-memory results are fine for the demo

### Data Flow

1. User pastes or uploads 2-3 submissions (plain text)
2. User provides a short description of their editorial standards
3. App sends each submission + standards to Bedrock in a single prompt
4. Bedrock returns a JSON assessment per submission
5. App displays the assessments side by side

### State Management

- **In-memory** -- Submissions, editorial standards, and Bedrock responses during processing (add S3 only if you want assessments to persist)

## Users & Roles

- **Editor** -- Uploads submissions, defines editorial standards, and reviews the AI assessments

## Key Workflows

1. User opens the app and clicks "New Triage Session"
2. User pastes or uploads 2-3 submissions
3. User types a short description of editorial standards (e.g., "We publish long-form tech journalism. We value original reporting, clear structure, and no listicles.")
4. User clicks "Evaluate"
5. System sends each submission + standards to Bedrock
6. System displays a side-by-side comparison: each submission gets a score, strengths, concerns, and recommendation
7. User clicks any submission to see the full assessment

## Requirements

### Inputs

- **Submissions** (required): 2-3 text files or pasted text. Each 500-5,000 words.
- **Editorial standards** (required): Free-text description, 1-3 sentences.

### Outputs

- **Assessment per submission**: JSON object with:
  - `title` (string, extracted or "Untitled")
  - `quality_score` (number, 1-10)
  - `topic_fit` (string: "strong", "moderate", "weak")
  - `strengths` (array of strings)
  - `concerns` (array of strings)
  - `recommendation` (string: "pass", "consider", "reject")
  - `summary` (string, 2-3 sentences)

### UI/UX Notes

- Text areas for pasting submissions + a standards text box
- Results as cards: one card per submission with color-coded recommendation (green/yellow/red)
- This is the simplest hackathon idea -- good for teams new to Bedrock

## API Integration

### Authentication

AWS sandbox credentials are pre-configured. No OAuth needed.

### Key API Calls

- `bedrock-runtime:InvokeModel` -- Send submission + standards, receive JSON assessment (model: Claude on Bedrock). Use Bedrock's Structured Outputs (constrained decoding) to guarantee schema-compliant JSON without prompt engineering — available for Claude models on Bedrock.

## API Resources

- [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)

## Out of Scope

- CMS or editorial workflow integration
- Email notifications or rejection letter sending
- Multi-reviewer workflows or role-based access
- Batch processing beyond 2-3 submissions

## Success Criteria

- Upload at least 2 submissions and get a structured assessment for each
- Assessments are meaningfully different (a strong submission scores higher than a weak one)
- Each assessment includes scores, strengths, concerns, and a recommendation
- Output is valid JSON

## Judging Alignment (see JUDGING-RUBRIC.md)

- **Business impact:** quantify the time saved, "an editor spends half a day on 30 pitches every Monday, this returns a pre-sorted queue in two minutes"
- **Innovation angle:** the assessments adapt to *your* editorial standards typed in plain English, not a fixed rubric, show two different standards producing different verdicts on the same submission
- **Demo hook:** feed it one strong and one weak submission live, the meaningfully different assessments are the moment that lands
