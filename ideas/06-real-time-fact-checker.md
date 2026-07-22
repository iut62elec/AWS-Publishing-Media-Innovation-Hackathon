## 6. Real-Time Fact-Checker
*Catch factual errors before your readers do*

**The Problem:** Every nonfiction book, product review, and health article contains dozens of factual claims — dates, statistics, prices, quotes. Fact-checking is manual, slow, and often squeezed by deadlines. For content about health, money, or safety, errors don't just embarrass you — they tank search rankings and erode the audience trust that drives revenue.

**Real-Life Example:** Your team publishes a "Best Credit Cards of 2026" roundup. Two weeks later, a reader points out that one card's APR changed before you even published. The article drops in search rankings, and your affiliate revenue takes a hit. A fact-checker that flagged the stale data before publication would have saved thousands of dollars.

**What You'll Build:**
- Paste a text passage and have the system automatically identify factual claims (statistics, dates, prices, quotes)
- Upload a reference knowledge base (fact sheet, previous edition, or source document) to check claims against
- Each claim gets a verification status: confirmed, disputed, or unverifiable against your sources
- Flag uncertain or outdated claims for human review — no false confidence
- Show at least 5 claims checked, with at least one flagged as unverifiable or outdated

**AWS Services:** Amazon Bedrock, Amazon Comprehend, Amazon S3

**Bonus Points:**
- Auto-expand thin claims with supporting context pulled from your reference documents
- Display results as inline color-coded highlights (green = verified, yellow = uncertain, red = wrong)
- Use Comprehend to extract and classify entity types (dates, amounts, organizations) before verification
- Support batch checking of multiple articles
- Use Bedrock Knowledge Bases to index your reference documents for semantic retrieval instead of pasting the full text into the prompt — scales to large reference sets
- Use Bedrock Guardrails Automated Reasoning Checks for up to 99% verification accuracy against domain knowledge

**Quick-Start Hint:** Use Bedrock to extract factual claims from a passage as structured data. Then verify each claim against a reference document you provide in the same prompt — "Here are my sources, here is the article, which claims are supported?" Use Comprehend to identify key entities first. For a more scalable approach, upload reference docs to S3 and use Bedrock Knowledge Bases for semantic retrieval (`RetrieveAndGenerate`) instead of fitting everything in the prompt.

---

