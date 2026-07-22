# Subscriber Save Engine Vision Document

## Vision

Spot the subscribers about to cancel and win them back with a personal touch, before they reach the cancellation page.

## Problem

Subscriptions are the top revenue focus for about three quarters of publishers, yet the median news publisher loses 4-5% of digital subscribers every month. With acquisition getting harder as search traffic declines, retention is the whole ballgame. Most churn responses are generic -- the same discount email to everyone, sent after the reader has already decided to leave.

## Solution

Upload a CSV of subscriber engagement data. Bedrock analyzes each subscriber, assigns a churn risk level with a plain-English explanation of the warning signs, and for high-risk subscribers generates a personalized retention action: a win-back email tailored to what that reader used to love, content recommendations, or an offer suggestion. Results appear as a ranked dashboard.

## Technical Architecture

### AWS Services

- **Amazon Bedrock** -- Analyzes engagement patterns, assigns churn risk with reasons, and writes personalized win-back emails. This is the only service the demo needs.
- **Amazon S3** (optional) -- Store the CSV and outputs if you want persistence; a local file is fine for the demo

### Data Flow

1. User uploads a subscriber engagement CSV (sample provided)
2. App sends the subscriber records to Bedrock with analysis instructions
3. Bedrock returns structured JSON per subscriber: risk level, warning signs, save plan
4. For high-risk subscribers, Bedrock generates a personalized win-back email
5. App displays a dashboard ranked by risk, each subscriber with their story and save plan

### State Management

- **In-memory** -- Parsed subscriber records, assessments, and emails during processing (add S3 only if you want outputs to persist)

## Users & Roles

- **Audience/retention manager** -- Uploads data, reviews at-risk list, approves win-back emails

## Key Workflows

1. User opens the app and uploads the subscriber CSV (or clicks "Load sample data")
2. User clicks "Analyze"
3. System sends records to Bedrock and receives risk assessments
4. Dashboard shows subscribers ranked by churn risk with color coding (red/yellow/green)
5. User clicks a high-risk subscriber to see warning signs and the personalized win-back email draft
6. User edits or approves the email draft

## Requirements

### Inputs

- **Subscriber CSV** (required): 20-30 rows with columns such as: subscriber_id, tenure_months, visits_per_week, favorite_sections, days_since_last_visit, newsletter_open_rate, plan_type. Sample file with planted patterns provided (a daily reader gone quiet, a loyal opener who stopped opening, a new subscriber who never engaged).

### Outputs

- **Assessment per subscriber**: JSON object with:
  - `subscriber_id` (string)
  - `risk_level` (string: "high", "medium", "low")
  - `warning_signs` (array of strings, plain English)
  - `persona` (string, e.g. "lapsed foodie", bonus)
  - `save_action` (string: "win-back email", "content recommendations", "offer")
  - `winback_email` (object: `subject`, `body` -- only for high risk)

### UI/UX Notes

- Dashboard table ranked by risk with color-coded rows
- Detail view per subscriber: their story in plain English, then the save plan
- The demo moment is reading one genuinely personal, persuasive save email out loud -- make the email view prominent

## API Integration

### Authentication

AWS sandbox credentials are pre-configured. No OAuth needed.

### Key API Calls

- `bedrock-runtime:InvokeModel` -- Send subscriber records, receive structured risk assessments and win-back emails (model: Claude on Bedrock). Use Structured Outputs to guarantee schema-compliant JSON.

## API Resources

- [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)
- [Amazon S3 PutObject / GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)

## Out of Scope

- Real subscriber data or PII (fictional sample data only)
- Actually sending emails
- Integration with subscription management or CDP platforms
- ML churn models trained on historical data (Bedrock reasoning over the CSV is enough for the demo)

## Success Criteria

- Upload the sample CSV and get a risk assessment for every subscriber
- The planted at-risk patterns are correctly flagged as high risk with sensible warning signs
- At least 2 high-risk subscribers get meaningfully different, personalized win-back emails
- Dashboard ranks subscribers by risk with color coding

## Judging Alignment (see JUDGING-RUBRIC.md)

- **Business impact:** the easiest ROI story in the room, publishers lose 4-5% of digital subscribers monthly and retention is the stated top revenue priority, saving even a fraction is real money
- **Innovation angle:** replacing the one-size-fits-all discount email with a save plan built from each reader's actual history, personal beats generic and costs nothing extra to send
- **Demo hook:** click one at-risk subscriber, tell her story from the data ("daily food reader, silent for three weeks"), then read her win-back email out loud, that email is the demo
