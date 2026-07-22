# One Story, Every Format Vision Document

## Vision

Take one article and produce five ready-to-publish formats -- including audio -- in one step.

## Problem

A single article could live as a newsletter, social thread, podcast script, push notification, and SEO summary. But today each format gets rewritten by a different person. That reformatting tax is slow, expensive, and leads to inconsistent messaging across channels.

## Solution

Paste a source article into the app. Bedrock generates five channel-specific versions, each following that channel's conventions (length, tone, structure). Polly renders the audio script into an MP3 with natural-sounding speech. An editorial review step lets a human tweak before publishing.

## Technical Architecture

### AWS Services

- **Amazon Bedrock** -- Converts the source article into five distinct formats (newsletter, social, audio script, push notification, SEO summary)
- **Amazon Polly** -- Renders the audio script into an MP3 using neural text-to-speech (this is what makes the audio output real, Bedrock cannot synthesize speech)
- **Amazon S3** (optional) -- Only needed if you use Polly's async `StartSpeechSynthesisTask` for long scripts (it writes output to S3); for the demo, `SynthesizeSpeech` returns audio directly and a local file is fine

### Data Flow

1. User pastes a source article into the app
2. App sends the article to Bedrock with a prompt specifying five output formats and their rules
3. Bedrock returns five formatted versions
4. App sends the audio script version to Polly for speech synthesis
5. Polly returns the MP3 audio, saved locally (or to S3 for long async jobs)
6. App displays all five outputs with an inline audio player

### State Management

- **In-memory / local files** -- Article text, generated outputs, and the MP3 during the session (S3 only for async Polly jobs)

## Users & Roles

- **Content producer** -- Pastes the source article and reviews the generated formats
- **Editor** (optional) -- Reviews and tweaks outputs before they go live

## Key Workflows

1. User opens the app and clicks "New Article"
2. User pastes a source article (500-2,000 words)
3. User clicks "Generate Formats"
4. System sends the article to Bedrock with format-specific rules
5. System displays five tabs: Newsletter, Social Thread, Audio Script, Push Notification, SEO Summary
6. System sends the audio script to Polly and shows a loading indicator
7. Audio player appears with the rendered MP3
8. User reviews each format and can edit text inline before exporting

## Requirements

### Inputs

- **Source article** (required): Plain text, 500-2,000 words.

### Outputs

Five formatted versions:

- **Newsletter**: 200-400 words, polished tone, clear subject line
- **Social thread**: 5-8 posts, casual tone, each under 280 characters
- **Audio script**: Conversational tone, 2-3 minutes when read aloud, suitable for Polly
- **Push notification**: Under 100 characters, action-oriented
- **SEO summary**: 150-160 character meta description + 300-word summary with keyword focus

Plus:
- **MP3 audio file**: Polly-rendered version of the audio script

### UI/UX Notes

- Single text area for input, tabbed output for each format
- Inline audio player for the MP3
- "Edit" button on each tab for manual tweaks

## API Integration

### Authentication

AWS sandbox credentials are pre-configured. No OAuth needed.

### Key API Calls

- `bedrock-runtime:InvokeModel` -- Convert article to five formats (model: Claude on Bedrock)
- `polly:SynthesizeSpeech` -- Render audio script to MP3 (Engine: "neural", OutputFormat: "mp3", VoiceId: e.g., "Joanna"). Limited to 6,000 characters per call.
- `polly:StartSpeechSynthesisTask` -- For audio scripts longer than 6,000 characters: submit an async synthesis task (up to 200,000 characters) that writes the MP3 to S3. Poll with `GetSpeechSynthesisTask` for completion.

## API Resources

- [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)
- [Amazon Polly SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/dml/API_SynthesizeSpeech.html)
- [Amazon Polly Voice List](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html)

## Out of Scope

- Direct publishing to CMS, social platforms, or email tools
- Scheduling or editorial calendar integration
- A/B testing of format variations
- Batch processing of multiple articles

## Success Criteria

- Paste one article, get five distinct formatted outputs
- Each output follows its channel's conventions (not just a shorter copy of the original)
- At least one output is a playable MP3 audio file
- An editorial review step exists (editable text before export)

## Judging Alignment (see JUDGING-RUBRIC.md)

- **Business impact:** do the math out loud, "four people, four rewrites, four hours per article, times hundreds of articles a week", the reformatting tax is easy to price
- **Innovation angle:** each output respects its channel's conventions (character limits, tone, structure), not just shorter copies, and the audio output makes it multimodal
- **Demo hook:** paste the article, flip through the five tabs, then press play on the audio, ending on sound is memorable
