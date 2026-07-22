## 3. One Story, Every Format
*One article goes in, five ready-to-publish formats come out (with audio)*

**The Problem:** A single article could live as a newsletter, a social thread, a podcast script, a push notification, and an SEO summary — but today, each format gets rewritten by a different person. When you publish hundreds of pieces a week, that reformatting tax adds up fast. The result: slow distribution and inconsistent messaging across channels.

**Real-Life Example:** Your newsroom publishes a 1,200-word feature on remote work trends. The social team needs a thread, the newsletter editor needs a summary, the podcast producer needs a script, and the app team needs a push notification. Four people, four rewrites, four hours — for content that already exists.

**What You'll Build:**
- Paste one source article and get at least five channel-specific outputs (newsletter, social thread, audio script, push notification, SEO summary)
- Each output respects its format's conventions — not just a shorter version of the original
- Include at least one audio output rendered with Polly
- An editorial review step so a human can tweak before publishing

**AWS Services:** Amazon Bedrock, Amazon Polly, Amazon S3

**Bonus Points:**
- Tailor the newsletter version to different reader segments (e.g., executive summary vs. practitioner deep-dive)
- Adjust tone and style per platform (casual for social, polished for newsletter)
- Add an editorial approval workflow with one-click publish
- Support multiple source articles in a batch

**Quick-Start Hint:** Start with a single article and a Bedrock prompt that specifies each output format's rules (character limits, tone, structure). Use Polly for the audio version — `SynthesizeSpeech` handles up to 6,000 characters; for longer scripts, use `StartSpeechSynthesisTask` (up to 200,000 characters, output to S3).

---

