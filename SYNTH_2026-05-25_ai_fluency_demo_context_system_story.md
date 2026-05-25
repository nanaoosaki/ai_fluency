# AI Fluency Demo: A Context System for Collaboration

Date: 2026-05-25
Project: `context_infrastructure_design`
Status: Layer 2 synthesis for presentation planning

## Source Inputs

- `contexts/layer1/PLAN_05-25-2026_AI_fluency_demo.md`
- `contexts/layer2/context_infrastructure_design/SYNTH_2026-04-29_layer_model_and_skill_runtime.md`
- `contexts/INDEX.md`
- `rules/WORKSPACE.md`
- Discussion on 2026-05-25 refining the showcase from Agent Notes implementation details to the documentation wiki and context lifecycle.

## Core Recommendation

The ten-minute presentation should not primarily explain Agent Notes architecture or list AI product capabilities. It should demonstrate a more portable idea:

> AI becomes a reliable collaborator when you build a human-owned context system around it: source material, organized synthesis, usable outputs, and reusable operating rules.

Agent Notes can remain the project backdrop, but the showcase should be the documentation wiki itself. The wiki is easier to understand, safer to show, and more directly demonstrates the behavior the audience can adopt in their own work.

## What This Story Is Really About

The differentiator is not that one AI can produce code or answer a question. Most of the audience has already seen that.

The differentiator is that documentation becomes a shared working surface between the human and the AI:

- the human records goals, constraints, discoveries, and corrections;
- the AI reads that context before acting;
- generated work is reviewed against that context;
- failures and new knowledge are documented back into the system;
- another AI can critique the same work because the context is externalized rather than trapped inside one chat.

This is not model training. It is building an inspectable collaboration environment around interchangeable models.

## Challenge To The Original Framing

### Do Not Reduce The Topic To Context Window Management

Prompt engineering and context-window management are parts of the story, but they are not sufficient descriptions of the system.

The wiki also defines:

- what sources are authoritative;
- how raw notes become synthesis;
- which instructions govern action;
- how output is reviewed;
- how decisions and revisions are preserved;
- how multiple AI tools can work against the same contract.

For this audience, use **context system** or **documentation-driven AI collaboration** as the primary term. Mention context engineering as the broader industry concept only if needed.

### Do Not Say You Are Building The Model

Say:

> I am building the system around the model that lets it work reliably on my problem.

That wording is technically precise and makes the method accessible to people who do not build models themselves.

### Do Not Overload The Demo With The Business Problem

Agent Notes may require explanation of Latitude, consultant notes, Cortex, extraction schemas, data precedence, and pilot constraints. That consumes the time needed to teach the transferable idea.

Use Agent Notes as a one-sentence origin:

> While building Agent Notes, I needed AI to keep up with an evolving project, not just answer isolated questions. That forced me to build a documentation wiki the AI could work from.

Then move directly to the wiki lifecycle.

## Proposed Presentation Thesis

Title option:

> Beyond Prompting: Building a Context System That Lets AI Work With You

Short thesis:

> A model gives capability. A documentation-driven context system makes that capability iterative, reviewable, and reusable.

Practical audience takeaway:

> Start documenting one recurring project in a way an AI can read, critique, and execute against. Organize it only when repetition and inconsistency appear.

## The Showcase: Documentation Wiki Evolution

The demo should show one project wiki evolving across three recognizable stages.

### Stage 1: One Document

You begin with one document that answers:

- What problem am I trying to solve?
- What do I know?
- What remains uncertain?
- What should the AI help me do next?

Message to audience:

> This is already more reliable than an isolated prompt because the project context persists outside the chat.

Possible screen visual:

```text
agent_notes_overview.md
  - problem
  - users
  - initial assumptions
  - next questions
```

### Stage 2: Scattered Expansion

As the work evolves, new documents appear:

```text
agent_notes_overview.md
data_sources.md
cortex_experiments.md
meeting_feedback.md
tooling_notes.md
open_questions.md
```

At this point, the documentation is useful but imperfect:

- content overlaps;
- some assumptions conflict;
- operational learnings are mixed with stable design;
- AI can help create more notes faster than the system can remain coherent.

Message to audience:

> More context is not automatically better context. Accumulated documentation eventually needs architecture.

### Stage 3: Organized Context System

You review the accumulated notes with AI and separate the documentation by purpose:

```text
overview.md
  - what the system is
  - current architecture
  - where to start

operational_learnings.md
  - findings from experiments
  - limitations
  - decisions still being tested

tools/
  - cortex_workflow.md
  - text_exploration_workbench.md

decisions.md
  - key changes and rationale

open_questions.md
  - what the next iteration must resolve
```

Message to audience:

> The AI is now no longer working from a pile of notes. It is working from a maintained contract.

## Ten-Minute Flow

Recommended duration: four pages with one compact visual/example per page.

| Time | Page | Purpose |
| ---: | --- | --- |
| 0:00-2:00 | 1. From Prompt To Partnership | Establish the gap between chat usage and iterative project work |
| 2:00-4:00 | 2. The Context System | Show the reusable model: inputs, protocol, execution, feedback |
| 4:00-6:30 | 3. A Wiki That Grows With The Work | Demonstrate one document becoming a maintained documentation system |
| 6:30-10:00 | 4. Showcase: AI Uses The Wiki | Show the system in action and end with the takeaway |

## Page 1: From Prompt To Partnership

### Main Message

> I do not only ask AI questions; I build a place where the AI can learn the project with me.

### Visual

```text
One-off assistance
Question -> Prompt -> Answer

Iterative collaboration
Problem -> Documentation -> AI work -> Review -> Updated documentation -> Next task
```

### Talking Points

- People at different levels already use AI: ChatGPT, Copilot, coding agents, or internal tools.
- The hard case is not drafting an email or generating a function.
- The hard case is an ambiguous project where your understanding changes over time.
- My solution is to keep the context outside the chat, in documentation that I and the AI can both inspect and improve.

### What Not To Say Yet

- Avoid naming every tool or framework.
- Avoid defining prompt engineering, context engineering, and harness engineering separately.
- Avoid beginning with Agent Notes data complexity.

## Page 2: The Context System

### Main Message

> The durable asset is the context-and-feedback loop, not one model or one conversation.

### Visual

```text
Inputs                 Protocol                 Execution              Feedback
Problem statement      Scope and constraints    Any AI/tool            Review notes
Data definitions       Documentation structure  Analysis/code          Decision log
Meeting learning       Output expectations      Drafts/prototypes      Updated context
```

### Talking Points

- Context includes more than prompt text: requirements, meeting notes, schemas, decisions, examples, tool instructions, and failure records.
- Documentation is a protocol: it tells the AI what the system means and tells me what I agreed to.
- Metadata and revision history help track how thinking and plans evolve.
- Multiple AI tools can critique or extend the work because they can read the same documented contract.
- Models can change; maintained context survives model changes.

### Optional Phrase

> This is documentation-driven AI collaboration: I externalize what the AI needs to know, what it should do, and how I will review it.

## Page 3: A Wiki That Grows With The Work

### Main Message

> A context system is built gradually: capture first, organize when fragmentation becomes costly.

### Visual

Use three panels, not an implementation architecture diagram:

```text
1. Initial
   overview.md

2. Expansion
   overview.md
   meeting_feedback.md
   experiments.md
   tools.md
   open_questions.md

3. Refinement
   overview.md
   operational_learnings.md
   decisions.md
   open_questions.md
   tools/<one doc per tool>
```

### Talking Points

- I did not design the entire documentation system on day one.
- I first documented new problems and discoveries as they appeared.
- The system became fragmented: overlapping documents, inconsistent wording, repeated instructions.
- I then asked AI to help audit the documentation: identify redundancy, clarify document scope, and reorganize it into a coherent wiki.
- The organization is not cosmetic. It changes the quality of AI work because the AI can find stable definitions, current decisions, and unresolved questions.

### Important Nuance

Do not imply that perfect documentation should come before project work. The actual method is:

> Capture while learning; refactor context when inconsistency begins to slow collaboration.

## Page 4: Showcase - AI Uses The Wiki

### Main Message

> A useful context system changes an AI request from “guess what I mean” to “perform this task within an understood project.”

### Recommended Demonstration

Use a sanitized or non-confidential miniature of the documentation wiki. Do not show raw consultant notes, candidate details, transcripts, or proprietary system data.

Show:

1. A small wiki index or folder:

```text
overview.md
operational_learnings.md
decisions.md
tools/text_exploration_workbench.md
open_questions.md
```

2. A bounded request:

```text
Read the project overview, current decisions, and operational learnings.
Summarize what the current system does, what is still uncertain,
and recommend the next experiment without contradicting existing decisions.
```

3. A result that references documentation:

```text
Current system: ...
Confirmed decisions: ...
Open uncertainty: ...
Recommended next experiment: ...
Sources reviewed: overview.md, decisions.md, operational_learnings.md
```

4. A brief critique step:

```text
Review this recommendation against decisions.md.
Flag contradictions or unsupported assumptions.
```

### Talking Points

- The first AI output is not the final truth.
- I use the documentation to ground the task and a review pass to check it.
- This is how different AIs can collaborate: not by trusting each other, but by reviewing against shared artifacts.
- This workflow applies whether the AI is ChatGPT, Copilot, Cortex, a coding agent, or a future internal platform.

### Ending The Showcase

End the demo on the transformation, not an internal architecture:

```text
One persistent document
    -> accumulated project context
    -> organized wiki
    -> grounded AI task
    -> reviewed recommendation
    -> updated documentation for the next task
```

Closing talking points:

- Start with one persistent project document rather than a perfect system.
- Add context as your understanding evolves.
- When documentation becomes fragmented, reorganize it into clear scopes, decisions, operational learnings, and tool instructions.
- Use AI to execute against that wiki and to critique work against the same wiki.
- That is how individual AI use becomes an iterative, inspectable working system.

## Suggested Spoken Flow

### Opening: 45 Seconds

```text
Most of us have used AI for a prompt: write something, summarize something,
or help with code. But in my work, the harder problem is when I am still
learning what the problem is.

While working on Agent Notes, I realized I did not need one clever prompt.
I needed a system where the AI could follow the project as my own
understanding evolved. That system became a documentation wiki.
```

### Transition Into Page 2

```text
What I mean by context is not just the text I paste into a chat window.
It is the full working contract: what problem we are solving, what we have
learned, what decisions are current, which tools exist, and what remains open.
```

### Transition Into The Wiki Evolution

```text
I did not begin with an elegant wiki. I began with one document. Then,
as the project grew, I created notes as problems appeared. Eventually the
context itself needed to be organized, because inconsistent context produces
inconsistent AI work.
```

### Transition Into Demo

```text
Now instead of asking an AI to infer the project from one prompt, I can
give it a bounded task against the maintained project context and ask it
to show its sources and critique its own recommendation.
```

### Closing: Final 45 Seconds Of Page 4

```text
The lesson is not that everyone needs my exact wiki structure. The lesson
is that AI fluency includes designing the relationship between your work and
the model: what context persists, how outputs are checked, and how learning
gets reused.

The model supplies capability. The context system turns that capability into
reliable collaboration.
```

## Audience Design

The mixed technical audience is a reason to show documentation rather than code.

| Audience Experience | What They Should Recognize |
| --- | --- |
| ChatGPT users | Persistent documents make prompts less repetitive and outputs more grounded |
| Copilot/internal-tool users | Context is not tied to one product; their working documents can still be the anchor |
| Coders/AI engineers | The wiki is an inspectable context layer with provenance, evaluation, and model portability |

Avoid positioning this as a maturity ladder where code users are advanced and chat users are behind. The differentiator is whether work context is explicit and reusable, not which interface someone uses.

## Demo Preparation Checklist

Before creating slides or presenting:

- Build a sanitized mini-wiki with four to five markdown files.
- Remove confidential project data, names, candidate information, and internal system details from screenshots.
- Capture the initial single-document state and the reorganized wiki state.
- Prepare one exact AI task and one critique prompt.
- Run the demo in advance and keep screenshots as fallback in case live execution is slow.
- Keep page 3 visual simple: document evolution, not technical pipeline architecture.

## Recommended Next Artifact

Next create a presentation draft and demo runbook containing the final page text, speaker notes, exact demo prompt, redacted screenshots/assets list, and timing rehearsal notes.
