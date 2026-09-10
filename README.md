# Threadwyn

**thread·wyn** *(n.)* — thread, and *wyn*, the old word for joy: the quiet
pleasure of a pattern coming out even.

A pixel picture creator for crochet charts, built for a phone. Work a chart
square by square, trace a photo into it, mirror it along a crease you place,
then follow it row by row with the hook in your hand.

One HTML file. No build step for the app itself, no server, no account, no
tracking. Everything anyone makes is saved on their own device and is never
uploaded anywhere.

## What it does

- **The chart** — up to 100×100. A loupe floats above your fingertip so your
  thumb never hides the square you're aiming at; an aim pad places one stitch
  at a time; pinch, pan and double-tap to zoom.
- **Mirror & fold lines** — live symmetry across, down, quartered or turned,
  with a crease you can move a *half* stitch at a time, so it can sit between
  two stitches or straight down the middle of one. Or work half and press
  **Fold** to reflect what's already there.
- **Trace a photo** — an image is reduced to whole stitches at the chart's
  gauge (k-means, 2–16 yarns, from the photo or from your own basket). Trace
  over it, or stitch it straight in.
- **Yarn** — a full colour dyer, five skein sets, and a live census of the
  chart that can swap one yarn for another everywhere at once.
- **Written patterns** — any chart becomes real row-by-row instructions, with
  a yarn legend, RS/WS direction and metre estimates.
- **Working mode** — walks those rows while you crochet, and remembers where
  you got to.
- **The Cabinet** — finished pieces, framed, with ribbons; lay them out into
  blankets before sewing a seam.
- **Charm codes** — words that unlock skein sets, bigger looms and extra tools.

## Shortcuts worth knowing

| Gesture | What it does |
|---|---|
| Two-finger tap on the chart | Undo. Pinching never triggers it — it requires both fingers to stay put and leave quickly. |
| Hold a tool, or a corner-rail button | Says what it does, without setting it off. |
| Hold a yarn in the basket | Opens the dyer on that colour, to change it. |
| Hold the dye button | Snaps back to the yarn you were using before. |
| Hold a chart in Works in progress | Open, rename, duplicate, copy as a code, or throw away. |
| Pull a sheet down | Puts it away. |
| Double-tap the chart | Zooms in on that stitch, without leaving a mark. |

## Install it

Open the site in a browser and choose **Install** on the Share & backup screen,
or use the browser's own *Add to Home screen*. It then opens full screen with
its own icon and **works with no signal**.

## Your work is yours

Saved in your browser's local storage, on that device only. Nothing leaves it.

- **Save a backup file** writes every chart, piece and blanket to a `.json`
  you can keep or move to another phone.
- **Save the picture** exports a finished piece as a PNG.
- **Chart codes** share a single chart as a short line of text.
- **Settings → Protect my work from cleanup** asks the browser to keep the data
  when the phone is short of space.

## Developing

`src/index.html` is the whole app and the source of truth. `build.py` wraps it
for a plain web server and writes `site/`; pushing to `main` publishes it via
GitHub Pages.

```
python3 build.py && python3 -m http.server -d site 8000
```
