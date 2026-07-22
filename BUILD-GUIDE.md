# Build Guide, From Idea to Demo with Claude Code

This is a lightweight spec driven way to build your idea in about 3 hours. You give Claude Code a clear specification (your vision document), it writes everything important to markdown files (`REQUIREMENTS.md`, `PLAN.md`, `DEMO.md`), and you review and approve each file before it builds. That review loop is the whole method: Claude proposes in writing, your team reads, adjusts, and approves, then Claude executes.

**The golden rule:** the better your specification, the better your product. Don't just say "build me an app", give Claude Code the vision document, answer its questions decisively, and approve in writing at each gate.

**The build order:** get the app working locally first, with sample data and mocked AI responses, then wire in real AWS services (Bedrock, Polly, Textract, ...), and only deploy to AWS infrastructure if your use case actually needs it. A local Streamlit app calling Bedrock is a perfectly great demo.

---

## Before you start

1. Open Claude Code in your browser (we give you access on the day, your AWS sandbox credentials are already configured in the environment)
2. Get your vision document ready:
   - Picked one of the ideas? Copy the matching file from [`vision-docs/`](vision-docs/)
   - Own idea? Fill in [`templates/vision-template.md`](templates/vision-template.md) first
3. Agree as a team on four things before you touch the keyboard: **what** you are building, **why** it matters, **who** it is for, and **what "done" looks like** in the 4 minute demo. If you can say those four sentences out loud, you are ready.

> Copy each prompt below, paste it into Claude Code, adapt the parts in [BRACKETS], and let it finish. Review the markdown file it produces together as a team before approving. Two minutes of reading saves an hour of rework.

---

## Step 1, Requirements (REQUIREMENTS.md)

Copy this prompt, paste your vision document into it, and send it:

```
Here is the vision document for what we want to build today at a hackathon.
We have about 3 hours to build it and 4 minutes to demo it.

[PASTE YOUR FULL VISION DOCUMENT HERE]

Act as a sharp product partner, not an order taker. Before writing anything:

1. Ask me your 3 to 5 most important clarifying questions, one at a time or as
   a short list. Format each question with lettered options (A, B, C) plus a
   final "Other, tell me more" option, so we can answer fast. Challenge any
   vagueness in our vision doc: if it says "users" ask who exactly, if it says
   "simple" ask what is cut. If any of our answers are vague ("maybe",
   "depends"), push back once with a sharper follow-up.

2. After we answer, write REQUIREMENTS.md containing exactly:
   - "What / Why / Who / Done": four single sentences
   - Requirements as a checklist with IDs, like:
     - [ ] REQ-01: User can paste an article and click Analyze
     - [ ] REQ-02: ...
     (5 to 8 requirements maximum, each one demoable)
   - "Minimum demo checklist": the 3 to 5 REQ IDs that MUST work in the demo
   - "Out of scope today": a table with two columns, Item and Reason,
     listing everything we are deliberately NOT building

Do not write any code yet. When REQUIREMENTS.md is ready, tell us to review it
and reply "approve" or request changes. Do not proceed until we approve.
```

**Then answer the questions as a team, briefly and decisively.** This is the most important moment of the day. Vague answers produce vague products. When the file looks right, reply `approve`.

## Step 2, Plan (PLAN.md)

```
REQUIREMENTS.md is approved. Now write PLAN.md. Do not write any code yet.

PLAN.md must contain:
1. Architecture: a short description plus a simple text diagram of what the app
   looks like, which AWS services we call and how data flows. Our sandbox AWS
   account has the full range of AWS services available. Choose services in
   this order, and justify each choice in one line:
   a. Amazon Bedrock first: can a Bedrock model solve this step (understanding,
      generation, extraction, classification, structured JSON)? Modern models
      handle most of these directly, prefer one well used Bedrock call over
      extra moving parts.
   b. Specialized AI services where they beat a general model: Polly for
      speech, Textract for PDFs and scans, Translate for baseline translation,
      Comprehend for entity and sentiment analysis at scale.
   c. Everything else (S3, DynamoDB, Lambda, and any other AWS service) only
      when a requirement truly needs it, for example S3 for file storage,
      DynamoDB only if we genuinely need data to survive restarts, Lambda only
      if something must run without the app open. If a Python dict or a local
      file does the job for a demo, use that instead.
   Pick whatever is genuinely best for the requirement, but every service in
   the plan must earn its place, fewer moving parts means more demo.
2. Tech stack: the simplest thing that works, for example a Python Streamlit
   app calling AWS with boto3. No databases or extra infrastructure unless a
   requirement truly needs them. For every AWS service in the plan, look up
   the latest AWS documentation first (use the AWS documentation MCP tools if
   available, otherwise search the current AWS docs) and confirm the API
   names, limits, and the current recommended usage, do not rely on memory
   for AWS specifics.
3. A task checklist in two phases:
   - Phase A, local first: the app runs on this machine end to end with
     sample data, AI and AWS calls mocked or hardcoded
   - Phase B, real AWS: replace mocks with real Bedrock and other service
     calls, one service at a time, and only if a requirement needs deployed
     infrastructure, one final deploy task
   Rules for tasks:
   - Each task is small, 15 to 30 minutes, and ends with something we can see
     or run. Write tasks as checkboxes: - [ ] TASK-01: ...
   - Each task must pass this test: could a different AI instance execute it
     from the text alone, without asking questions? If not, add detail.
   - In the tasks that cover the minimum demo checklist, do not use the words
     "placeholder", "simplified", "for now", or "will be wired later".
     Hardcoding IS allowed in non demo paths, but every hardcoded thing must
     be listed at the bottom of PLAN.md under "Hardcoded shortcuts".
4. A mapping line for each REQ ID from REQUIREMENTS.md showing which tasks
   deliver it, so nothing is silently dropped.

When PLAN.md is ready, tell us to review it and reply "approve" or request
changes. Do not proceed until we approve.
```

**Review the plan as a team.** Check the mapping: is every minimum-demo REQ covered by Phase A tasks? If the plan looks too big, say `cut PLAN.md down to the minimum demo checklist only`. It is much cheaper to trim the plan than to trim half built code. Then reply `approve`.

## Step 3, Build locally (Phase A)

```
PLAN.md is approved. Build Phase A now. Follow the plan exactly, task by task,
in order. Working rules:

1. Mark each task checkbox [x] in PLAN.md in the same turn you complete it,
   so the file always shows true progress.
2. After each task, give us one exact command or click to verify it works.
   Run everything you can run yourself first, only ask us to verify what you
   genuinely cannot check.
3. If you hit a bug or a blocker inside the current task, fix it yourself and
   note it briefly. Only stop and ask us if the fix would change the
   architecture or the requirements.
4. Do not add anything that is not in PLAN.md. If you notice something
   missing, propose it in one sentence and wait for our answer.
5. Include 2 or 3 realistic sample inputs (sample articles, submissions,
   subscriber CSVs, whatever our idea needs) so we can test without hunting
   for data.

Real AWS calls come in Step 5, use mocks or hardcoded responses for now.
```

**While it builds:** watch the checkboxes tick in `PLAN.md`, that is your progress bar. If something looks off, say so immediately, for example "the upload works but the results page is empty, fix that before moving on".

## Step 4, Test locally

```
Phase A is built. Now prove it:

1. Start the app yourself and confirm it runs without errors.
2. Walk through every item on the minimum demo checklist in REQUIREMENTS.md
   yourself, using the sample data, and fix anything that fails.
3. Then hand it to us: give the exact URL to open and the exact steps to
   repeat, one numbered list.
4. Do not add new features, just make the local flow solid.

We will reply "approved" or describe what we see going wrong.
```

**When you hit errors** (you will, everyone does), paste the full error message back into Claude Code and say "fix this". Full text, not a paraphrase, that is the whole trick.

## Step 5, Add real AWS services, deploy only if needed (Phase B)

```
The local app is approved. Build Phase B from PLAN.md:

1. Replace the mocked AI parts with real calls to Amazon Bedrock (and the
   other AWS services in PLAN.md) using boto3 and the AWS credentials already
   configured in this environment. Before writing each integration, check the
   latest AWS documentation for that service (use the AWS documentation MCP
   tools if available, otherwise search the current AWS docs) and use the
   current API, model IDs, and limits, do not rely on memory for AWS
   specifics. One service at a time, and after each one, run the minimum
   demo flow yourself and show us it still works before moving to the next.
   Keep ticking the PLAN.md checkboxes.
2. Then answer honestly in two sentences: for our 4 minute demo, do we need
   to deploy anything to AWS infrastructure (S3 hosting, Lambda, an API), or
   is running locally enough? If deployment is genuinely needed for a
   requirement, propose the simplest possible deployment and wait for our
   "approve" before doing it.
```

**A useful rule:** if your demo works by running the app on your laptop and calling Bedrock directly, ship that. Deploy only when the use case demands it, for example an S3 upload that triggers processing, or a URL the judges can open on their phones.

## Step 6, Demo prep (DEMO.md)

```
The app works end to end. Now write DEMO.md and do the final polish:

1. DEMO.md contains a 4 minute demo script: what to click, what to say, in
   what order. Open with the problem in one sentence (who feels this pain and
   what it costs them), close with the value in one sentence (time saved,
   revenue protected, readers retained).
2. DEMO.md also contains one backup plan in case the live demo fails, for
   example screenshots of a successful run, take those screenshots now and
   save them in a demo-assets folder.
3. Add small polish that makes the demo land, a title, clear labels, one nice
   visual touch. Nothing risky, do not touch working logic.
4. Finally, run the whole demo script yourself once, top to bottom, and
   confirm every step works.
```

---

## Tips that make the difference

- **Answer, don't ignore.** When Claude Code asks a question, answer it. Push it to ask, "what are your top 3 open questions?" is always a legitimate prompt.
- **Approve in writing.** The `approve` replies at each gate are what keep the build on rails. If you skip the reading, you approve a plan you haven't seen.
- **The md files are the memory.** If the session gets confused or restarts, say "read REQUIREMENTS.md and PLAN.md and continue from the first unchecked task".
- **Local first, always.** A flow you can test on your laptop in seconds beats debugging in the cloud. Add AWS services once the flow works.
- **Latest docs, not memory.** AWS APIs, model IDs, and limits change fast. Any time Claude Code writes AWS code, tell it to check the latest AWS documentation first, "look up the current Bedrock API for this in the AWS docs before writing the code" is always a legitimate prompt.
- **Small scope wins.** A tiny thing that works beats a big thing that almost works. Judges reward working demos, see the [Judging Rubric](JUDGING-RUBRIC.md).
- **One person drives, everyone reviews.** One keyboard, five brains. Rotate the driver if you like.
- **Paste errors verbatim.** Full error text, not a paraphrase. Claude Code is very good at fixing what it can see.
- **Ask for explanations.** "Explain what this code does in plain English" is a legitimate prompt, use it, this day is about learning.
- **Save your work often.** Ask Claude Code to "commit the current progress with a short message" after each working step.
- **Stuck for more than 10 minutes?** Wave down an AWS expert, that is what we are here for.

## Where things live

| File | What it is |
|------|-----------|
| `vision-docs/` | Ready made specs for the ideas, copy paste into Step 1 |
| `templates/vision-template.md` | Blank spec for your own idea |
| `REQUIREMENTS.md` | Created in Step 1, what/why/who/done, REQ checklist, out of scope table |
| `PLAN.md` | Created in Step 2, architecture and two phase task checklist, your live progress bar |
| `DEMO.md` | Created in Step 6, your 4 minute demo script and backup plan |
