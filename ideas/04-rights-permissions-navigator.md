## 4. AI Rights & Permissions Navigator
*Ask your contracts a question and get a straight answer with citations*

**The Problem:** Publishing runs on contracts, and nobody can find anything in them. Rights managers dig through PDFs — sometimes scanned ones from the '90s — to answer simple questions like "Can we sell this audiobook in Germany?" or "When does this license expire?" The information exists, it's just buried in legal language across hundreds of files.

**Real-Life Example:** A film studio calls asking about adaptation rights for one of your titles. Your rights manager spends two days pulling the original contract, checking amendments, and emailing legal — only to discover the option expired six months ago. With a searchable contract system, that answer takes thirty seconds.

**What You'll Build:**
- Upload 1–2 sample contracts (PDFs) and extract the text using Textract
- Paste the extracted text into Bedrock with plain-English questions like "Which titles have open audio rights in Europe?"
- Get answers that cite specific contract clauses — not just summaries
- Flag ambiguous clauses as "needs legal review" instead of guessing

**AWS Services:** Amazon Bedrock, Amazon Textract, Amazon S3

**Bonus Points:**
- Handle scanned PDFs using Textract's OCR capabilities
- Support conversational follow-up questions ("What about the sequel?")
- Show a timeline view of rights windows and expiration dates
- Extract and compare terms across multiple contracts at once
- Use Textract Queries to ask specific questions about the contract directly (e.g., "What is the termination date?")

**Quick-Start Hint:** Extract text from a PDF with Textract, paste it into Bedrock with your question, and ask for answers with clause citations. Bedrock's large context window can handle full contracts — no need to build a search index for the demo. Note: synchronous Textract (`DetectDocumentText` / `AnalyzeDocument`) is limited to 5 pages — for longer contracts, use async processing (`StartDocumentAnalysis` / `GetDocumentAnalysis`).

---

