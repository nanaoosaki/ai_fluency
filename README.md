# Nano Banana Pro Slide Deck Generator

This repository contains the **Generative Kernel** slide-generation workflow and an active deck source that you can swap for your own theme and topic.

**使用Nano Banana Pro生成整套PPT：疯狂，挑战和工作流 (Generating a Full Slide Deck with Nano Banana Pro: Madness, Challenges, and Workflow)**

Read the full article here:
*   [中文版 (Chinese)](https://yage.ai/nano-banana-pro.html)
*   [English Version](https://yage.ai/nano-banana-pro-en.html)

This project demonstrates a workflow to generate a complete, professional-grade slide deck using AI image generation. The currently active content files are the canonical filenames at the repo root:

*   `AI-instructions.md`
*   `outline_visual.md`
*   `speak_notes.md`
*   `visual_guideline.md`

The original Nano Banana deck sources have been archived under `archive/original_nano_banana_deck/`.

## The Generative Kernel Philosophy

This project implements the **Generative Kernel** philosophy: instead of manually assembling slides, we inject raw assets and prompts into a generative model to render the final presentation layer.

*   **Beyond DRY**: Don't just repeat yourself; generate yourself.
*   **Asset Injection**: The core technique. We take raw functional assets (QR codes, logos, diagrams) and "inject" them into the generative process. The model renders the lighting, texture, and environment *around* the asset, creating a seamless organic integration.
*   **The Glass Garden**: Our visual language. Translucent interfaces, matte ceramic accents, and soft, diffused lighting.

## Workflow

The system is designed for an AI-assisted loop:

### 1. Define the Context
Edit `outline_visual.md`. This is the source of truth.
*   **Structure**: Markdown headers define slides.
*   **Prompts**: Self-contained visual descriptions for each slide.
*   **Assets**: Paths to local images (e.g., `imgs/qrcode.png`) to be injected.

Also make sure the shared visual anchor exists at `imgs/style_matrix_0.jpg` if your outline references it.

### 2. Generate (Draft Mode)
Run the generator to create 1K previews. This is fast and cheap for iteration.
```bash
python tools/generate_slides.py
```
This parses the outline, calls the Gemini 3.1 Flash Image Preview API by default, and saves images to `generated_slides/`.

### 3. Refine & Upscale (Production Mode)
Once specific slides are approved, upscale them to 4K resolution using the generative upscaler.
```bash
# Upscale everything
python tools/generate_slides.py --enlarge

# Upscale specific slides
python tools/generate_slides.py --enlarge --slides 8 11
```

### 4. Present
Open `index.html`.
The presentation uses **Reveal.js** to display the generated "Mega-Images" as full-screen backgrounds. It is simple, robust, and visually stunning.

## Adapting This Repo To A New Theme

To reuse this repo for a different talk, you should treat the repo root as the **active deck contract**. The generator and viewer expect these canonical files:

*   `AI-instructions.md`
*   `outline_visual.md`
*   `visual_guideline.md`
*   `speak_notes.md`

If you are starting a new deck, the cleanest workflow is:

1.  Archive or rename the current active deck files.
2.  Prepare your new theme/topic artifacts.
3.  Promote your new artifacts to the canonical filenames above.
4.  Generate slides into `generated_slides/`.
5.  Update `index.html` speaker notes if your deck length or notes changed.

### Required Artifacts For A New Deck

At minimum, prepare the following files yourself:

*   `AI-instructions.md`: The AI workflow, tone, and deck-specific generation rules. This should explain what kind of deck is being made, what quality bar to aim for, and how the AI should interpret the project.
*   `visual_guideline.md`: The visual system for the deck. This should define the visual metaphor, materials, lighting, color palette, typography tone, forbidden styles, and rendering rules.
*   `outline_visual.md`: The actual slide-by-slide deck specification. This is the most important artifact. Each slide should include a heading like `## Slide 1: ...` or `#### Slide 1: ...`, plus a `Layout`, `Scene`, and `Asset` section.
*   `speak_notes.md`: Your speaker script or note draft. This is not used by the Python generator, but it is the source material for notes you may want to paste into `index.html`.

### Recommended Additional Artifacts

These are not always mandatory, but in practice they are usually needed for good results:

*   `imgs/style_matrix_0.jpg`: The main style anchor. This is the most important visual reference for consistency across slides.
*   Slide-specific assets in `imgs/`: logos, screenshots, diagrams, QR codes, profile images, UI captures, or any other pixels the model should not hallucinate.
*   Existing generated slides in `generated_slides/`: useful when iterating on only a few slides instead of regenerating everything.

### What Each Artifact Should Contain

`visual_guideline.md` should answer:

*   What visual world are we in?
*   What materials, lighting, and palette define this deck?
*   What visual motifs should repeat across slides?
*   What styles are explicitly forbidden?

`outline_visual.md` should answer, slide by slide:

*   What is the purpose of this slide?
*   What layout pattern should it use?
*   What scene should be rendered?
*   What text should appear in the scene?
*   What assets need to be injected?

`AI-instructions.md` should answer:

*   What kind of talk is this?
*   Who is the audience?
*   What tone should the deck have?
*   How should the AI make tradeoffs between clarity, style, and fidelity?

`speak_notes.md` should answer:

*   What will the speaker actually say on each slide?
*   What details are spoken but not shown visually?
*   What notes should be transferred into `index.html`?

### Visual Anchors And Asset Preparation

The most important asset for a new theme is usually `imgs/style_matrix_0.jpg`.
It should define the deck's visual language, not just show topic-related content.

A good style anchor usually establishes:

*   Material language
*   Lighting direction
*   Background atmosphere
*   Color palette
*   The overall emotional tone of the deck

Then add slide-specific assets only where fidelity matters, such as:

*   logos
*   screenshots
*   QR codes
*   diagrams
*   product UI
*   profile pages

### Minimal Checklist Before Generation

Before you run the generator, verify:

*   `outline_visual.md` exists and has valid slide headings
*   `visual_guideline.md` exists
*   `.env` contains a valid `GEMINI_API_KEY` or `GOOGLE_API_KEY`
*   `imgs/style_matrix_0.jpg` exists if referenced by the outline
*   Any other files listed under each slide's `Asset` section actually exist
*   Your Python environment has the dependencies in `requirements.txt`

### Notes On The Viewer

`tools/generate_slides.py` reads from `outline_visual.md` and `visual_guideline.md`.
`index.html` is separate from generation:

*   it displays the rendered slide images from `generated_slides/`
*   it contains the Reveal.js presentation shell
*   it contains speaker notes in `<aside class="notes">...</aside>`

If your new deck has a different number of slides, you should update `index.html` accordingly so the viewer and notes match the generated outputs.

## Setup

1.  **Environment**:
    ```bash
    uv venv  # using uv is recommended
    # macOS / Linux
    source .venv/bin/activate
    # Windows PowerShell
    .venv\Scripts\Activate.ps1
    uv pip install -r requirements.txt
    ```
2.  **Credentials**:
    Create a `.env` file with your API key:
    ```
    GOOGLE_API_KEY=your_key_here
    ```
    `GEMINI_API_KEY=your_key_here` also works.

## Detailed Setup

### 1. Install Dependencies

```bash
uv venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
uv pip install -r requirements.txt
```

### 2. Prepare Credentials

Create `.env` in the project root with either:

```env
GEMINI_API_KEY=your_key_here
```

or:

```env
GOOGLE_API_KEY=your_key_here
```

### 3. Prepare The Active Deck Files

Make sure these files exist in the repo root and represent the deck you want to render:

*   `AI-instructions.md`
*   `outline_visual.md`
*   `visual_guideline.md`
*   `speak_notes.md`

### 4. Prepare Assets

Create or populate `imgs/` with:

*   `style_matrix_0.jpg` for shared style consistency
*   any additional assets referenced in `outline_visual.md`

### 5. Generate Draft Slides

Use the virtualenv Python to avoid dependency/path issues:

```bash
.venv\Scripts\python.exe tools\generate_slides.py
```

This creates draft images in `generated_slides/`.

### 6. Upscale Approved Slides

```bash
.venv\Scripts\python.exe tools\generate_slides.py --enlarge
```

Or upscale only selected slides:

```bash
.venv\Scripts\python.exe tools\generate_slides.py --enlarge --slides 1 3 6
```

### 7. Present Or Review

Open `index.html` directly, or run the local server:

```bash
.venv\Scripts\python.exe start-server.py
```

## Project Structure

*   `AI-instructions.md`: The workflow and prompting guidance for the active deck.
*   `outline_visual.md`: The "Source Code" of the presentation.
*   `visual_guideline.md`: The visual language definition for the active deck.
*   `speak_notes.md`: The speaker notes for the active deck.
*   `archive/original_nano_banana_deck/`: Archived source files from the original sample deck.
*   `tools/`: Python scripts for generation and upscaling.
    *   `generate_slides.py`: Main orchestrator.
    *   `gemini_generate_image.py`: API wrapper for generation.
    *   `gemini_enlarge_image.py`: API wrapper for upscaling.
*   `imgs/`: Local asset inputs such as `style_matrix_0.jpg`, logos, screenshots, or QR codes.
*   `generated_slides/`: The render targets.
*   `index.html`: The viewer.
*   `PRESENTATION_SETUP.md`: How to present the deck with private speaker notes.
