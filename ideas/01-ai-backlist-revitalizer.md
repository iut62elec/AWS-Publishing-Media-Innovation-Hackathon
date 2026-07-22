## 1. AI Backlist Revitalizer
*Find hidden gems in your catalog that match what people are searching for right now*

**The Problem:** Every publisher has thousands of older titles or articles gathering dust. Some of that content is one trend away from being relevant again — but nobody has time to manually cross-reference the catalog against what's trending today. Thin metadata makes it even harder: many backlist titles have only a title, author, and one-line description.

**Real-Life Example:** A 2019 cookbook on fermentation is sitting in your backlist with flat sales. Meanwhile, "gut health" is blowing up on TikTok and search volume for "fermented foods" is at an all-time high. Your team won't notice until the moment has passed — unless something connects the dots automatically.

**What You'll Build:**
- Upload a small CSV of titles (20–50 rows with titles, descriptions, and whatever metadata you have) to S3
- Bedrock analyzes each title against a set of current trending topics you define and returns a ranked list with resurgence potential
- Each recommendation includes a short pitch: why this title is timely *right now*
- Confidence score so your team knows where to focus first

**AWS Services:** Amazon Bedrock, Amazon S3, Amazon Comprehend

**Bonus Points:**
- Auto-enrich sparse catalog metadata (themes, audience, reading level, comp titles) using Bedrock before matching
- Auto-generate a one-paragraph marketing pitch for the top recommendations
- Show results in a dashboard or visual ranking view
- Support both book catalogs and article/URL inventories

**Quick-Start Hint:** Start with a small CSV of titles and descriptions. Use Bedrock to compare each title against a set of current trend keywords, then rank by relevance. Use Comprehend to extract key themes from thin descriptions before matching.

---

