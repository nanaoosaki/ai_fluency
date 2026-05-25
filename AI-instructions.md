# AI Instructions: Beyond Prompting

## Purpose

Create and refine an HTML5-hosted presentation whose intended final slides are generated as full-page images from explicit, text-grounded prompts. The current HTML deck is an authored preview/fallback until those generated images are available. The deck explains how a human-owned context system makes AI work iterative, reviewable, and reusable.

Primary source of truth: `STORYBOARD.md`

Supporting source: `SYNTH_2026-05-25_ai_fluency_demo_context_system_story.md`

Demo source artifacts: `demo_wiki/`

## Audience And Posture

Audience: mixed technical audience including ChatGPT users, coding-agent users, internal-tool users, and AI engineers.

Tone:

- practical;
- thoughtful;
- personal without being confessional;
- technically precise;
- accessible without oversimplifying.

Avoid:

- AI product capability lists;
- deep Agent Notes business or architecture detail;
- claims that the speaker is building or training a model;
- maturity ladders that rank one interface above another;
- presentation language that sounds like hype or generic consulting.

## Thesis

Use this phrasing as the conceptual anchor:

> A model gives capability. A documentation-driven context system makes that capability iterative, reviewable, and reusable.

When describing the speaker's work, prefer:

> I am building the system around the model that lets it work reliably on my problem.

## Authoring Rules

- Start from talking points and exact visible text.
- Put the exact intended words into every generated-slide prompt before rendering.
- Keep one argument per slide.
- Use enough on-slide text to support free-form delivery.
- Do not depend on speaker notes during the current drafting phase.
- Show a sanitized documentation wiki rather than sensitive project records.
- Keep Page 6 concise and inspect generated filenames, prompt wording, result text, and review check for fidelity after generation.

## Image Generation Rules

The image model generates complete final slide candidates.

- Write a full-slide prompt only after a slide claim and on-screen text are accepted.
- Supply the visible copy verbatim and make typography/layout part of the prompt.
- Require accurate, legible text and regenerate slides whose copy is wrong or unreadable.
- Keep the overall deck style consistent, but do not let style exploration precede story clarity.
- Use an image-capable OpenAI model for the render pass in an environment that exposes one; prompt files remain usable if the exact image model changes later.

## Active Slide Sequence

1. Beyond Prompting
2. An Answer Is Not Project Memory
3. The Problem That Forced This Method
4. The Context System
5. A Wiki Grows With The Work
6. AI Uses The Wiki
7. Build The System Around The Model

## Quality Gate

The current checkpoint succeeds when the storyboard and prompts are ready for image generation and the HTML preview communicates the method accurately. The final delivery succeeds when accepted generated slides read clearly at presentation scale and are served cleanly by the static HTML viewer.
