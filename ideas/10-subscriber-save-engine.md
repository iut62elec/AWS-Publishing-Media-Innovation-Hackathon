## 10. Subscriber Save Engine
*Spot the subscribers about to leave, and win them back with a personal touch*

**The Problem:** Subscriptions are the top revenue focus for roughly three quarters of publishers, but the median news publisher loses around 4–5% of digital subscribers every month. With new-reader acquisition getting harder as search traffic declines, retention is the whole ballgame. Yet most churn responses are generic: the same discount email to everyone, sent after the reader has already decided to leave.

**Real-Life Example:** A subscriber who read your food coverage daily has gone quiet for three weeks — she's a cancellation waiting to happen. Today, nobody notices until the cancellation survey. A save engine flags her this week, sees *what she used to love*, and drafts a personal win-back email: "We noticed you enjoyed our restaurant guides — here are three new ones, plus our new weekly food newsletter." Personal beats generic discount, and it costs nothing to send.

**What You'll Build:**
- Upload a CSV of subscriber engagement data (we provide a realistic sample: tenure, visit frequency, favorite sections, last visit, newsletter opens)
- Bedrock analyzes each subscriber and assigns a churn risk level (high, medium, low) with a plain-English explanation of the warning signs
- For each high-risk subscriber, generate a personalized retention action: a win-back email draft tailored to their reading history, a content recommendation set, or an offer suggestion
- A dashboard view: at-risk subscribers ranked by risk, each with their story and their save plan

**AWS Services:** Amazon Bedrock, Amazon S3

**Bonus Points:**
- Segment at-risk subscribers into personas (the lapsed foodie, the headline skimmer, the weekend-only reader) with a different save strategy per persona
- Generate the win-back emails in the publication's brand voice
- Predict which retention action is most likely to work for each subscriber, and say why
- Show an aggregate view: what the top churn drivers are across the whole file, as editorial and product feedback
- A/B variant generation: two different win-back emails per subscriber, ready to test

**Quick-Start Hint:** Start with a CSV of 20–30 fictional subscribers with obvious patterns planted (a daily reader gone quiet, a loyal opener who stopped opening, a new subscriber who never engaged). Send the CSV to Bedrock and ask for structured JSON: risk level, warning signs, and a personalized win-back email per subscriber. Render it as a ranked dashboard. The demo moment is reading one genuinely personal, persuasive save email out loud.

---
