# Cultural Adaptation Engine Vision Document

## Vision

Adapt content for culture, not just language -- across multiple locales at once.

## Problem

Translation gets the words right but misses cultural meaning. A Thanksgiving reference confuses readers in Brazil. A baseball metaphor doesn't land in France. Publishers expanding globally need cultural adaptation -- swapping idioms, humor, references, and tone for each audience -- but that requires expensive localization specialists per market.

## Solution

Paste a source article and pick three target locales. Translate produces a baseline translation for each. Then Bedrock layers on cultural adaptation -- swapping culturally specific references, adjusting tone, and converting local conventions. Each change is annotated so local editors can see what was changed and why.

## Technical Architecture

### AWS Services

- **Amazon Translate** -- Produces a baseline word-for-word translation for each target locale
- **Amazon Bedrock** -- Applies cultural adaptation on top of the translation: swaps idioms, references, humor, and tone; generates annotations explaining each change
- **Amazon S3** -- Stores the source text, translations, and adapted versions

### Data Flow

1. User pastes a source article and selects three target locales
2. App sends the article to Translate for each locale
3. Translate returns baseline translations
4. App sends each translation + the original to Bedrock with cultural adaptation instructions
5. Bedrock returns the adapted text + an annotation layer (what changed and why)
6. App displays all three adaptations side by side with annotations

### State Management

- **S3 bucket** -- Stores source text, baseline translations, and adapted versions with annotations
- **In-memory** -- Translation outputs and Bedrock responses during processing

## Users & Roles

- **Content producer** -- Pastes the source article, selects locales, and reviews the adaptations
- **Local editor** (optional) -- Reviews annotations and accepts or rejects individual changes

## Key Workflows

1. User opens the app and clicks "New Adaptation"
2. User pastes a source article (500-2,000 words, English)
3. User selects three target locales from a dropdown (e.g., French/France, Portuguese/Brazil, Japanese/Japan)
4. User clicks "Adapt"
5. System runs Translate for each locale and shows baseline translations
6. System sends each translation to Bedrock for cultural adaptation
7. System displays a three-column view: one column per locale
8. Each adapted section shows the change with an annotation tooltip (e.g., "Swapped 'tailgating' for 'aperitif culture' -- American football culture doesn't exist in France")
9. User can click any annotation to see the original vs. adapted text

## Requirements

### Inputs

- **Source article** (required): Plain text, 500-2,000 words, English.
- **Target locales** (required): Exactly 3 locales from a predefined list (e.g., fr-FR, pt-BR, ja-JP, de-DE, es-MX, ar-SA).

### Outputs

Per locale:
- **Adapted text**: Culturally localized version of the article
- **Annotations**: Array of objects, each with:
  - `original_phrase` (string)
  - `adapted_phrase` (string)
  - `reason` (string, plain-English explanation)
  - `category` (string: "idiom", "cultural reference", "humor", "tone", "convention")

### UI/UX Notes

- Three-column layout for side-by-side comparison
- Highlighted phrases with tooltip annotations
- Toggle to show/hide annotations

## API Integration

### Authentication

AWS sandbox credentials are pre-configured. No OAuth needed.

### Key API Calls

- `translate:TranslateText` -- Translate source text to each target language (SourceLanguageCode: "en", TargetLanguageCode: e.g., "fr"). Supports optional `Settings.Formality` parameter (FORMAL/INFORMAL) for 9 languages to control tone. Supports custom terminology files (`TerminologyNames`) to enforce brand-specific terms.
- `bedrock-runtime:InvokeModel` -- Apply cultural adaptation and generate annotations (model: Claude on Bedrock)

## API Resources

- [Amazon Translate TranslateText](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateText.html)
- [Amazon Translate Supported Languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html)
- [Amazon Translate Formality Setting](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-formality.html) (bonus — supported for 9 languages)
- [Amazon Translate Custom Terminology](https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html) (bonus — enforce brand-specific terms)
- [Amazon Bedrock InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)

## Out of Scope

- Unit, currency, or date format conversion (stretch goal)
- Editorial approval workflows or change tracking
- Translation memory or glossary management
- More than 3 locales per session

## Success Criteria

- Paste one article and get culturally adapted versions for 3 locales
- Each adaptation includes annotations explaining what was changed and why
- Adaptations go beyond translation: idioms, references, and tone are localized
- Side-by-side output is clear and readable
