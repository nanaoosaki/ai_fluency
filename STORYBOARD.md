# Storyboard: Beyond Prompting

## Deck Intent

Audience: mixed technical audience already familiar with AI tools at some level.

Decision to unlock: move from using AI as a one-off answer engine to maintaining reusable project context that AI can execute and be reviewed against.

Tone: clear, personal, practical, technically precise.

Viewing context: a ten-minute live HTML5 presentation intended to present generated full-slide images; the current authored HTML preview is used to refine the story until those images are available.

## Narrative Arc

```text
AI can answer a prompt
  -> evolving work requires memory and rules
  -> a documentation wiki becomes the shared context
  -> AI performs bounded work against that context
  -> review updates the context for the next task
```

## Slide 1: Beyond Prompting

Purpose: Open with the transferable thesis.

Visible text:

```text
AI FLUENCY / CONTEXT SYSTEMS

Beyond Prompting
Building a context system that lets AI work with you

CORE THESIS
A model gives capability.
A maintained context system makes it iterative, reviewable, and reusable.
```

Delivery cue: Most people have seen AI answer a question. This talk is about getting AI to follow an evolving project.

Visual job: Type-led generated cover with a quiet documentation/workbench atmosphere.

## Slide 2: An Answer Is Not Project Memory

Purpose: Establish the limitation of isolated prompting.

Visible text:

```text
THE GAP

An answer is not project memory.

One-off assistance
Question -> Prompt -> Answer

Iterative collaboration
Problem -> Context -> AI work -> Review -> Update

The harder problem is not getting an answer.
It is keeping the work aligned as understanding changes.
```

Delivery cue: A useful answer can still become obsolete as assumptions, terminology, and constraints change.

Visual job: Generated comparison infographic with clear, verified labels.

## Slide 3: The Problem That Forced This Method

Purpose: Establish personal origin without spending the talk on Agent Notes architecture.

Visible text:

```text
THE ORIGIN

The project changed faster than a prompt could hold it.

While building Agent Notes, I needed AI to follow an evolving problem,
not just answer isolated questions.

01  Definitions changed.
02  Experiments produced new evidence.
03  Decisions replaced assumptions.
04  Tools acquired operating rules.

One clever prompt was not enough.
The missing piece was persistent, inspectable context.
```

Delivery cue: Agent Notes is the origin; the documentation method is the subject.

Visual job: Light editorial framing around a progression of project discoveries.

## Slide 4: The Context System

Purpose: Name the method and show its mechanics.

Visible text:

```text
THE METHOD

A context system turns documentation into a working contract.

Sources       Synthesis       Protocol       Execution       Feedback
notes         meaning         decisions      analysis        review
schemas       structure       constraints    drafts          corrections
tests         priorities      rules          code            updated context

Documentation is not storage.
It is the working contract between human judgment and AI capability.
```

Delivery cue: The system externalizes what is known, what governs action, and how outputs get checked.

Visual job: Generated system diagram with precise five-stage labeling and text QA.

## Slide 5: A Wiki Grows With The Work

Purpose: Make the method feel adoptable rather than architected in advance.

Visible text:

```text
THE EVOLUTION

A useful wiki is built gradually.

01 / CAPTURE                02 / ACCUMULATE            03 / ORGANIZE
One document                Scattered growth           Maintained context

overview.md                 overview.md                overview.md
                            experiments.md             decisions.md
                            meeting_feedback.md        operational_learnings.md
                            tooling_notes.md           open_questions.md
                            open_questions.md          tools/
                                                       text_exploration_workbench.md

Capture while learning.
Refactor context when inconsistency begins to slow collaboration.
```

Delivery cue: The organized system appears because fragmentation becomes costly, not because documentation must be perfect on day one.

Visual job: Generated file-tree evolution infographic; filenames require post-render inspection.

## Slide 6: AI Uses The Wiki

Purpose: Demonstrate the behavioral difference created by maintained context.

Visible text:

```text
THE DEMONSTRATION

AI performs a bounded task against named context.

REQUEST
Read overview.md, decisions.md, and operational_learnings.md.
Recommend the next experiment without contradicting current decisions.

GROUNDED RESPONSE
Decision: Keep human review before downstream action.
Uncertainty: Which evidence fields are consistently reliable?
Next test: Evaluate a fixed sample and log failure types.

Sources: overview.md / decisions.md / operational_learnings.md
Review pass: No contradiction found. The experiment is reversible.
```

Delivery cue: The value is not blind trust in the output; it is a bounded task and a review pass against shared artifacts.

Visual job: Generated artifact-style slide. Keep copy concise and reject output if any critical text is incorrect.

## Slide 7: Build The System Around The Model

Purpose: End with a practical, portable action.

Visible text:

```text
THE PRACTICE

Build the system around the model.

01  Start with one persistent project document.
02  Add what you learn as the work changes.
03  Separate decisions from open questions.
04  Ask AI to work against maintained context.
05  Review the result and write learning back.

The model supplies capability.
The context system turns it into collaboration.
```

Delivery cue: The exact folder structure is not the product; the reusable habit is.

Visual job: Type-led generated close with a restrained loop marker.
