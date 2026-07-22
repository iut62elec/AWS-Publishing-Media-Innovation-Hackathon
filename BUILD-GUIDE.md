# Build Guide, From Idea to Demo with Claude Code

This is a simple, spec driven way to build your idea. You give Claude Code a clear specification (your vision document), then guide it through six steps: requirements, plan, build, test locally, add AWS and deploy if needed, demo. Each step is one prompt, copy it, paste it, adapt the parts in [BRACKETS].

**The golden rule:** the better your specification, the better your product. Don't just say "build me an app", give Claude Code the vision document and let it ask questions.

**The build order:** get the app working locally first, with sample data and mocked AI responses if needed, then wire in real AWS services (Bedrock, Polly, Textract, ...), and only deploy to AWS infrastructure if your use case actually needs it. A local Streamlit app calling Bedrock is a perfectly great demo.

---

## Before you start

1. Open Claude Code in your browser (we give you access on the day, your AWS sandbox credentials are already configured in the environment)
2. Get your vision document ready:
   - Picked one of the 8 ideas? Copy the matching file from [`vision-docs/`](vision-docs/)
   - Own idea? Fill in [`templates/vision-template.md`](templates/vision-template.md) first
3. Decide as a team what the **minimum demo** is, the smallest thing you can show working end to end. Cut everything else until that works.

> Run each prompt, let it finish, review the output together as a team, then move to the next step. Don't skip the review, two minutes of reading saves an hour of rework.

---

## Step 1, Requirements

Copy this prompt, paste your vision document into it, and send it to Claude Code:

```
Here is the vision document for what we want to build today at a hackathon.
We have about 4 hours to build it and 4 minutes to demo it.

[PASTE YOUR FULL VISION DOCUMENT HERE]

Before writing any code:
1. Ask me up to 5 clarifying questions about anything unclear or ambiguous.
2. Then write a requirements.md file containing:
   - A short list of user stories ("As a [role], I want [action] so that [outcome]")
   - A "minimum demo checklist", the 3 to 5 things that MUST work in the demo
   - A "not today" list, things we are explicitly cutting for time
Keep it to one page. Do not start building yet.
```

**Then answer the questions.** This is the most important moment of the day. Claude Code's questions surface the decisions your team needs to make. Answer them as a team, briefly and decisively.

## Step 2, Plan

```
Read requirements.md. Now create a plan.md file with:
1. A simple architecture: what the app looks like, which AWS services we call and
   how data flows between them (our sandbox AWS account has Bedrock, S3, Lambda,
   Polly, Textract, Translate, and Comprehend available)
2. The tech stack, prefer the simplest thing that works, for example a Python
   Streamlit app calling AWS with boto3, no databases or extra infrastructure
   unless the use case truly needs them
3. An ordered task list in two phases:
   - Phase A, local first: the app runs on this machine with sample data, and
     any AI or AWS calls can start mocked or hardcoded so we can test the flow
   - Phase B, real AWS: replace mocks with real calls to Bedrock and the other
     services, and only if the use case needs deployed infrastructure (for
     example a public URL, S3 event triggers, or a Lambda API), add a final
     deploy task
   Each task should be small enough to build and verify in 15 to 30 minutes.
Do not start building yet. I will review the plan first.
```

**Review the plan as a team.** If it looks too big, say "cut this to the minimum demo checklist only". It is much cheaper to trim the plan than to trim half-built code.

## Step 3, Build locally

```
The plan is approved. Build Phase A now, task by task, in order.
After each task, tell me exactly what you did and give me one command or click
to verify it works before you move to the next task.
Start with a hardcoded happy path and sample data, real AWS calls come in the
next step.
Include 2 or 3 realistic sample inputs (for example sample articles, submissions,
or contracts) so we can test without hunting for data.
```

**While it builds:** verify each task actually works before letting it continue. If something is off, say so immediately, for example "the upload works but the results page is empty, fix that before moving on".

## Step 4, Test locally

```
Run the app locally now and tell me exactly how to open it in the browser.
Then walk through every item on the minimum demo checklist in requirements.md,
step by step, using the sample data, and fix anything that fails.
Do not add new features, just make the local flow solid.
```

**When you hit errors** (you will, everyone does), just paste the full error message back into Claude Code and say "fix this". That is the whole trick.

## Step 5, Add real AWS services, deploy only if needed

Once the local flow works end to end, wire in the real services:

```
The local app works with sample data. Now build Phase B:
1. Replace the mocked or hardcoded AI parts with real calls to Amazon Bedrock
   (and the other AWS services in plan.md) using boto3 and the AWS credentials
   already configured in this environment.
2. After each service is wired in, run the demo flow again and show me it still
   works before moving to the next one.
3. Then tell me honestly: for our demo, do we need to deploy anything to AWS
   infrastructure (for example S3 hosting, Lambda, or an API), or is running
   locally enough? If deployment is genuinely needed for the use case, propose
   the simplest possible deployment and wait for my approval before doing it.
```

**A useful rule:** if your demo works by running the app on your laptop and calling Bedrock directly, ship that. Deploy to AWS infrastructure only when the use case demands it, for example an S3 upload that triggers processing, or a URL that judges can open on their phones.

## Step 6, Demo prep

```
The app works. Now help us prepare a 4 minute demo:
1. Suggest a demo script: what to click, what to say, in what order
2. Add small polish that makes the demo land, a title, clear labels,
   one nice visual touch, nothing risky
3. Create a demo-script.md file with the steps and one backup plan in case
   the live demo fails (for example, screenshots of a successful run)
```

---

## Tips that make the difference

- **Answer, don't ignore.** When Claude Code asks a question, answer it. Vague answers produce vague products.
- **Local first, always.** A flow you can test on your laptop in seconds beats debugging in the cloud. Add AWS services once the flow works.
- **Small scope wins.** A tiny thing that works beats a big thing that almost works. Judges reward working demos.
- **One person drives, everyone reviews.** One keyboard, five brains. Rotate the driver if you like.
- **Paste errors verbatim.** Full error text, not a paraphrase. Claude Code is very good at fixing what it can see.
- **Ask for explanations.** "Explain what this code does in plain English" is a legitimate prompt, use it, this day is about learning.
- **Save your work often.** Ask Claude Code to "commit the current progress with a short message" after each working step.
- **Stuck for more than 10 minutes?** Wave down an AWS expert, that is what we are here for.

## Where things live

| File | What it is |
|------|-----------|
| `vision-docs/` | Ready made specs for the 8 ideas, copy paste into Step 1 |
| `templates/vision-template.md` | Blank spec for your own idea |
| `requirements.md` | Created in Step 1, your user stories and demo checklist |
| `plan.md` | Created in Step 2, architecture and two phase task list |
| `demo-script.md` | Created in Step 6, your 4 minute demo plan |
