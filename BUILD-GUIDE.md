# Build Guide, From Idea to Demo with Claude Code

This is a simple, spec driven way to build your idea. You give Claude Code a clear specification (your vision document), then guide it through five steps: requirements, plan, build, test, demo. Each step is one prompt you copy, paste, and adapt.

**The golden rule:** the better your specification, the better your product. Don't just say "build me an app", give Claude Code the vision document and let it ask questions.

---

## Before you start

1. Open Claude Code in your browser (we give you access on the day)
2. Have your vision document ready:
   - Picked one of the 8 ideas? Use its file from [`vision-docs/`](vision-docs/)
   - Own idea? Fill in [`templates/vision-template.md`](templates/vision-template.md) first
3. Decide as a team what the **minimum demo** is, the smallest thing you can show working end to end. Cut everything else until that works.

> Run each prompt, let it finish, review the output together as a team, then move to the next step. Don't skip the review, two minutes of reading saves an hour of rework.

---

## Step 1, Requirements

Paste your vision document into Claude Code with this prompt:

```
Here is the vision document for what we want to build today at a hackathon.
We have about 4 hours to build it and 4 minutes to demo it.

[PASTE YOUR VISION DOCUMENT HERE]

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
1. A simple architecture: what AWS services we use and how data flows between them
   (we have a sandbox AWS account with Bedrock, S3, Lambda, Polly, Textract,
   Translate, and Comprehend available)
2. The tech stack, prefer the simplest thing that works, for example a Python
   Streamlit app calling AWS with boto3, no databases or infrastructure unless
   the idea truly needs them
3. An ordered task list, smallest working version first, each task small enough
   to build and verify in 15 to 30 minutes
Do not start building yet. I will review the plan first.
```

**Review the plan as a team.** If it looks too big, say "cut this to the minimum demo checklist only". It is much cheaper to trim the plan than to trim half-built code.

## Step 3, Build

```
The plan is approved. Build it task by task, in order.
After each task, tell me what you did and how I can verify it works before
moving to the next task.
Start with a hardcoded happy path first, real data and edge cases later.
Use the AWS credentials already configured in this environment.
```

**While it builds:** verify each task actually works before letting it continue. If something is off, say so immediately, for example "the upload works but the results page is empty, fix that before moving on".

## Step 4, Test and run

```
Run the app now and walk me through how to open it.
Then test the full demo flow from requirements.md's minimum demo checklist,
step by step, and fix anything that fails.
```

**When you hit errors** (you will, everyone does), just paste the full error message back into Claude Code and say "fix this". That is the whole trick.

## Step 5, Demo prep

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
- **Small scope wins.** A tiny thing that works beats a big thing that almost works. Judges reward working demos.
- **One person drives, everyone reviews.** One keyboard, five brains. Rotate the driver if you like.
- **Paste errors verbatim.** Full error text, not a paraphrase. Claude Code is very good at fixing what it can see.
- **Ask for explanations.** "Explain what this code does in plain English" is a legitimate prompt, use it, this day is about learning.
- **Save your work often.** Ask Claude Code to "commit the current progress with a short message" after each working step.
- **Stuck for more than 10 minutes?** Wave down an AWS expert, that is what we are here for.

## Where things live

| File | What it is |
|------|-----------|
| `vision-docs/` | Ready made specs for the 8 ideas |
| `templates/vision-template.md` | Blank spec for your own idea |
| `requirements.md` | Created in Step 1, your user stories and demo checklist |
| `plan.md` | Created in Step 2, architecture and task list |
| `demo-script.md` | Created in Step 5, your 4 minute demo plan |
