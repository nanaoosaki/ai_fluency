# Presentation Setup Guide

This repo uses **Reveal.js** for presentation playback.

The important separation is:

*   `index.html` is the audience-facing deck
*   `<aside class="notes">...</aside>` inside `index.html` contains the speaker notes
*   speaker notes are visible in Reveal's presenter view, not on the projected audience screen

## 1. Start The Deck Locally

From the repo root, run:

```powershell
.\.venv\Scripts\python.exe .\start-server.py
```

Then open:

```text
http://localhost:8080
```

Do not rely on opening `file:///.../index.html` directly. Use the local server.

## 2. Open Speaker Notes View

Once the deck is open in the browser:

1. Focus the main deck window
2. Press `S`

Reveal.js will open the presenter window.

That presenter window typically shows:

*   current slide
*   next slide
*   speaker notes
*   timer

## 3. Recommended Display Setup

Use **extended display mode**, not mirrored display.

Recommended arrangement:

*   external monitor / projector / TV: audience deck
*   laptop screen: speaker notes window

This way:

*   the audience only sees the slide deck
*   you see the notes, next slide, and timer on your own screen

## 4. Windows Display Setup

On Windows:

1. Connect your projector or second display
2. Press `Win + P`
3. Choose `Extend`

Then place windows like this:

*   drag the main deck browser window to the audience display
*   keep the speaker notes window on your laptop

If the wrong screen gets the wrong window:

1. Press `Win + Shift + Left/Right Arrow` to move the focused window between displays
2. Or drag the browser windows manually

## 5. How To Present

Suggested workflow:

1. Start the local server
2. Open `http://localhost:8080`
3. Press `S` to open presenter view
4. Put the main deck on the projector screen
5. Keep the presenter notes window on your laptop
6. Navigate slides from either window

Common navigation keys:

*   `Right Arrow` or `Space`: next slide
*   `Left Arrow`: previous slide
*   `Esc`: overview mode
*   `F`: fullscreen

## 6. Where Notes Come From

Reveal does **not** read notes directly from `speak_notes.md`.

Presenter notes come from the `<aside class="notes">...</aside>` blocks in:

*   `index.html`

So if you update:

*   `speak_notes.md`

and want those changes to appear in presenter view, you must also sync the notes in:

*   `index.html`

## 7. Troubleshooting

### I pressed `S` and nothing happened

Check:

*   you opened the deck through `http://localhost:8080`
*   the deck window has keyboard focus
*   pop-up blocking is not preventing the speaker window

### The audience can see the notes

That usually means:

*   you put the presenter window on the projector instead of the main deck

Fix:

*   move the presenter notes window back to your laptop
*   keep only the main slide deck on the audience display

### The deck is blank

Check:

*   the slide images exist under `generated_slides/`
*   `index.html` points to the correct file extensions (`.jpg` vs `.png`)
*   you are loading through the local server

### I changed `speak_notes.md`, but presenter notes did not update

That is expected until `index.html` is updated too.

## 8. Pre-Talk Checklist

Before presenting:

*   `generated_slides/` contains the final slide images
*   `index.html` points to the correct generated filenames
*   `index.html` speaker notes match your latest speaking draft
*   local server starts successfully
*   `S` opens presenter view
*   projector is in `Extend` mode
*   audience display shows the main deck only
