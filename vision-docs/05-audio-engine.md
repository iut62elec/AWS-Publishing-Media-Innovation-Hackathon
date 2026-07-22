# Immersive Audio Engine Vision Document

## Vision

Turn text into multi-voice audio with AI-generated script markup -- in minutes instead of weeks.

## Problem

Audio production costs $5,000+ per finished hour. That prices out most backlist titles and mid-tier content. The European Accessibility Act (in force June 2025) requires accessible formats, and the backlist conversion burden is the acute pain point -- traditional narration is too expensive for the long tail. AI voices are now good enough to close the gap.

## Solution

Paste text into the app. Bedrock analyzes the content, identifies dialogue vs. narration vs. scene changes, and generates a script split by speaker role with SSML markup for pacing and emphasis. The app sends each segment to Polly as a separate `SynthesizeSpeech` call with a different VoiceId (Polly uses one voice per API call — it does not support switching voices mid-request). The app stitches the returned audio clips into one combined MP3. The result is a playable multi-voice audio clip.

## Technical Architecture

### AWS Services

- **Amazon Bedrock** -- Analyzes input text, identifies dialogue/narration/scenes, and generates a script split by speaker role with SSML tags for pacing and emphasis
- **Amazon Polly** -- Renders each segment into audio via separate `SynthesizeSpeech` calls, each with a different VoiceId. Polly uses one voice per call — the app stitches clips together for multi-voice output.
- **Amazon S3** -- Stores the input text, generated SSML script, and final MP3 audio files

### Data Flow

1. User pastes a book chapter, article, or script into the app
2. App sends the text to Bedrock with instructions to generate an SSML script
3. Bedrock returns an SSML script with voice assignments (e.g., "Narrator = Matthew", "Character A = Joanna")
4. App splits the script by voice role
5. App sends each segment to Polly with the assigned voice ID
6. App stitches the audio segments together into one MP3
7. App displays the script markup and an audio player

### State Management

- **S3 bucket** -- Stores input text, SSML script, individual audio segments, and the final combined MP3
- **In-memory** -- SSML parsing and segment routing during processing

## Users & Roles

- **Producer** -- Pastes text, reviews the generated script markup, and plays the audio output
- **Editor** (optional) -- Adjusts voice assignments or SSML tags before re-rendering

## Key Workflows

1. User opens the app and clicks "New Audio Project"
2. User pastes a text passage (500-3,000 words)
3. User clicks "Generate Script"
4. System sends text to Bedrock and displays a loading indicator
5. System shows the SSML script with color-coded voice assignments (e.g., Narrator in blue, Character A in green)
6. User clicks "Render Audio"
7. System sends each segment to Polly and stitches the results
8. Audio player appears with the final MP3
9. User plays at least a 60-second clip for the demo

## Requirements

### Inputs

- **Text passage** (required): Plain text, 500-3,000 words. Can be fiction (with dialogue) or nonfiction.

### Outputs

- **SSML script**: Marked-up text with voice assignments, pauses, emphasis, and prosody tags
- **Voice map**: List of roles and their assigned Polly voice IDs
- **MP3 audio**: Combined multi-voice audio file, at least 60 seconds

### UI/UX Notes

- Text area for input, split-pane for script markup + audio player
- Color-coded voice roles in the script view
- Play/pause controls for the audio output

## API Integration

### Authentication

AWS sandbox credentials are pre-configured. No OAuth needed.

### Key API Calls

- `bedrock-runtime:InvokeModel` -- Generate script split by speaker role with SSML tags (model: Claude on Bedrock)
- `polly:SynthesizeSpeech` -- Render each segment as a separate call (one VoiceId per call, OutputFormat: "mp3"). Limited to 6,000 characters per call. Recommended voices by role:
  - **Long-form (best for narration):** Danielle, Ruth, Gregory, Patrick (engine: "long-form")
  - **Neural (best for dialogue):** Joanna, Matthew, Emma, Brian (engine: "neural")
  - **Generative (most expressive):** 33 voices with emotional range (engine: "generative")
- `polly:StartSpeechSynthesisTask` -- For segments longer than 6,000 characters: async synthesis (up to 200,000 characters, output to S3). Poll with `GetSpeechSynthesisTask` for completion.

## API Resources

- [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)
- [Amazon Polly SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/dml/API_SynthesizeSpeech.html)
- [Amazon Polly SSML Reference](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html)
- [Amazon Polly Voice List](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html)

## Out of Scope

- Ambient soundscapes or background music (stretch goal only)
- Studio-grade audio mastering or mixing
- Real-time streaming playback
- Voice cloning or custom voice training

## Success Criteria

- Paste text and get an SSML script with at least 2 distinct voice roles assigned
- Polly renders a multi-voice MP3 with audibly different speakers
- Play at least a 60-second audio clip in the demo
- Script markup is visible and shows voice assignments
