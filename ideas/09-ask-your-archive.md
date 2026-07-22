## 9. Ask Your Archive
*Your own AI chat experience, built on your content, keeping readers on your site*

**The Problem:** Readers are getting answers from AI chatbots instead of clicking through to publishers. Google's AI Overviews cut click-through rates nearly in half when they appear, and publishers expect search traffic to keep falling. The industry's answer: own the AI experience yourself. The Washington Post launched "Ask The Post AI," the Financial Times launched "Ask FT" — conversational search over their own journalism, with answers grounded in their own articles. Most publishers don't have this yet.

**Real-Life Example:** A reader wants to understand a developing story your newsroom has covered in twelve articles over three months. Today they either dig through your archive page by page, or they ask ChatGPT and never visit your site at all. With your own archive chat, they ask one question on *your* site, get a synthesized answer built only from *your* reporting, with citations linking back to each article — and every citation is a pageview you would have lost.

**What You'll Build:**
- Upload 10–20 of your articles (or sample articles we provide) to S3
- A chat interface where readers ask questions in plain English
- Bedrock answers using ONLY your uploaded content — every answer cites the specific source articles with titles and links
- If the archive doesn't cover the question, the system says so instead of making something up
- Demo at least 3 questions: one answered from a single article, one synthesized across multiple articles, and one the archive can't answer

**AWS Services:** Amazon Bedrock, Amazon S3

**Bonus Points:**
- Use Bedrock Knowledge Bases for semantic retrieval so it scales past what fits in a prompt
- Show "related articles you might like" alongside each answer to drive further reading
- Add suggested starter questions so readers don't face a blank box (real publisher chatbots found users struggle with prompting)
- Track which questions had no good answer — that's an editorial gap report, story ideas your audience is asking for
- Match answers to your publication's voice and style

**Quick-Start Hint:** For the demo, skip the vector database — load 10–20 articles into the prompt directly (Bedrock's context window can take them) and instruct: "Answer only from these articles, cite the article title for every claim, and say 'our archive doesn't cover this' if the answer isn't there." For the scalable version, upload articles to S3 and use Bedrock Knowledge Bases (`RetrieveAndGenerate`), which handles chunking, embeddings, and citations for you.

---
