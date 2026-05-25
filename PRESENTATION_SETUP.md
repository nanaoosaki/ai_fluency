# Presentation Setup

This project is a static HTML5 presentation powered by Reveal.js. At this checkpoint, it displays the authored preview/fallback layout. After the image-generation pass, accepted generated full-slide images will replace or be integrated into this viewer.

## Start The Deck

From the repository root:

```powershell
.\.venv\Scripts\python.exe .\start-server.py
```

Or, when opening the page yourself:

```powershell
.\.venv\Scripts\python.exe .\start-server.py --no-browser
```

Then visit:

```text
http://localhost:8080
```

## Presenting

Use extended display mode when presenting on a second screen:

1. Connect the external display.
2. Press `Win + P` and select `Extend`.
3. Move the browser window containing the presentation to the audience display.
4. Use arrow keys or space to move through the presentation.
5. Press `F` for fullscreen or `Esc` for the slide overview.

## Speaker Notes

Speaker notes are intentionally deferred during the current story-and-generation-prompt phase. The active `index.html` does not load the Reveal notes plugin and does not contain presenter-note blocks.

If rehearsal later shows that notes are useful, add succinct `<aside class="notes">` blocks and restore the Reveal notes plugin at that point.

## Pre-Talk Check

- Open all seven screens at the target presentation resolution.
- Confirm preview text is readable without zooming.
- Confirm the static demo slide contains only sanitized content.
- Rehearse the talk from visible text anchors.
- After image generation, verify every generated slide preserves exact text and contains no fake or unreadable additions.
