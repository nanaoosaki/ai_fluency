# Beyond Prompting: AI Fluency HTML5 Presentation

This repository prepares a ten-minute presentation about documentation-driven AI collaboration:

> A model gives capability. A maintained context system makes it iterative, reviewable, and reusable.

The intended final delivery is a Reveal.js viewer for full-slide images generated from exact, text-grounded prompts. At this checkpoint, the repository contains:

- the story and on-slide copy;
- full-slide image-generation prompts;
- a sanitized demonstration wiki;
- an authored HTML preview/fallback for narrative review;
- tooling for prompt export and an OpenAI image-render adapter.

No AI-generated full-slide images are committed yet. The OpenAI API project available in this workspace was checked on `2026-05-25` and does not expose an image-generation model. Rendering is intended to continue in the company OpenAI environment that has image-model access.

## Current Story

The seven-screen deck tells this story:

1. Beyond Prompting
2. An Answer Is Not Project Memory
3. The Problem That Forced This Method
4. The Context System
5. A Wiki Grows With The Work
6. AI Uses The Wiki
7. Build The System Around The Model

Primary planning documents:

- `PLAN_2026-05-25_text_first_html_visual_workflow.md`: workflow decision and delivery checkpoint.
- `STORYBOARD.md`: narrative and exact visible content contract.
- `SYNTH_2026-05-25_ai_fluency_demo_context_system_story.md`: source synthesis for the talk.

## Repository Contract

```text
STORYBOARD.md               slide story and exact visible content
AI-instructions.md          AI-assisted authoring constraints
visual_guideline.md         generated-slide design rules
outline_visual.md           compact prompt index
visual_prompts/             full-slide generation prompts
generated_prompts/          compiled provider-ready prompts
generated_slides/           target location for approved generated slide images
demo_wiki/                  sanitized demonstration artifacts
index.html                  current HTML preview/fallback viewer
css/deck.css                current preview/fallback styling
tools/generate_visuals.py   prompt compiler and rendering orchestrator
tools/image_provider.py     OpenAI image adapter for image-enabled credentials
archive/ds_career_active/   preserved prior career-talk deck
```

## Workflow

### 1. Refine The Story

Edit `STORYBOARD.md` first. The talk is developed from visible content rather than speaker notes.

### 2. Refine Full-Slide Prompts

Each `visual_prompts/slide_*.md` file includes:

- slide purpose;
- exact text to render;
- layout instructions;
- visual direction;
- text-fidelity requirements.

These prompts intentionally request finished slide images, including the approved text. Rendered output must be visually inspected, because any image model can still make spelling or typography errors.

### 3. Export Provider-Ready Prompts

```powershell
python .\tools\generate_visuals.py
```

This compiles all prompts into `generated_prompts/` without invoking an image model.

To compile selected slides:

```powershell
python .\tools\generate_visuals.py --slides 1 4 7
```

### 4. Render In An Image-Enabled Environment

The adapter defaults to `gpt-image-2` and can be configured using `OPENAI_IMAGE_MODEL`:

```powershell
$env:OPENAI_IMAGE_MODEL = "gpt-image-2"
python .\tools\generate_visuals.py --render --slides 1 4 7
```

Required:

- `OPENAI_API_KEY` in `.env` or the environment;
- project access to the configured image model;
- Codex's bundled `imagegen/scripts/image_gen.py` CLI, used by `tools/image_provider.py`.

The local key currently in this workspace cannot perform this rendering because its model catalog contains no image-generation model.

### 5. Review And Integrate Generated Slides

For each generated slide:

1. inspect all rendered text against its `visual_prompts/slide_*.md` exact-text block;
2. reject output with misspellings, invented copy, unreadable labels, or weak layout;
3. regenerate affected slides;
4. after acceptance, update `index.html` to display the generated slide images.

Until that integration step, `index.html` remains the authored HTML preview/fallback.

## Sanitized Demo Artifacts

`demo_wiki/` contains the source material for the demonstration slide:

```text
overview.md
decisions.md
operational_learnings.md
open_questions.md
tools/text_exploration_workbench.md
```

The files are intentionally compact and contain no proprietary project records.

## Preview The Current HTML Fallback

Install the local viewer dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Start the viewer:

```powershell
python .\start-server.py --no-browser
```

Open `http://localhost:8080`.

## Notes

- Speaker notes are intentionally deferred.
- The previous career-focused generated deck is preserved under `archive/ds_career_active/`.
- Legacy source material and unused legacy slide modules are kept under `archive/` rather than part of the active presentation.
- `references.md` and the supplied `imgs/codex_*.png` assets are retained as source material for the future visual-generation pass.
