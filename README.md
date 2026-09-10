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

## Worked up

Any chart can be seen as **actual fabric**. Every square is drawn as a
procedural single crochet — a rounded body, light falling across it, the V of
its two top loops, and the bar of the row below tucking underneath. Rows lean
alternately because right-side and wrong-side rows really do, they overlap the
row beneath so the fabric looks layered rather than tiled, and each stitch
carries a fixed sliver of colour variation so it reads as worked rather than
printed.

It is drawn once into an offscreen canvas, so a 100×100 costs no more to look
at than a coaster.

Set your own tension (stitches and rows per 10 cm — work a swatch and count)
and the screen tells you the **true finished size in centimetres**, plus a
shopping list: every colour named in plain words, with its stitch count and
roughly how many metres of it you need.

## Version

The home screen carries a build stamp in the bottom right, like `v1.6 · 34c8c93`.
Tap it for the version, the build date, whether a newer one is waiting, and a
button to go and fetch it.

Nothing about it is hand-maintained. `build.py` sets the version from the
commit count, so it climbs by itself on every deploy and cannot be forgotten,
and the build id is a hash of the page, so identical pages always read the
same. Opened straight from `src/`, it reads `0.0.0-dev`.

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
