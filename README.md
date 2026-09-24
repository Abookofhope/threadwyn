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

## Reading the chart

A chart you cannot read square by square is a picture, not a pattern, so the
lines are drawn to be seen rather than to be tasteful.

- **They never turn themselves off.** Every stitch carries a line at every
  zoom. When the stitches get too small to carry one apiece — under about
  three device pixels — the lines thin out to every second, fifth or tenth
  rather than disappearing, which is what the old version did below 4.5x and
  it made the biggest charts unusable.
- **They are snapped to whole device pixels.** A hairline landing across two
  pixels is drawn at half strength into each, and at the alpha the first
  version used that came out invisible. Each line is rounded to a device pixel
  boundary and given a width of exactly one or two of them.
- **Each line carries a halo** of the opposite colour a pixel out, so it reads
  over midnight navy as well as over cream. The halo is dropped when the
  stitches are too small to give it room, and the fine lines give way a little
  as the stitches shrink, so a 100x100 at fit reads as graph paper rather than
  as a wash of grey.
- **Dark grey on a pale chart, pale grey on a dark one**, decided from the
  luminance of the paper token rather than from the theme setting, so it is
  right whichever way the phone's own dark mode is pointing.
- **Three settings** — bold, soft, off — on the *Lines* tile in the chart menu
  and in Settings, remembered between sessions.
- **Rows count from the bottom**, the way crochet does, and the way the written
  pattern and the row-by-row helper always did. The chart used to number them
  from the top, which meant the number under your finger was not the number in
  the pattern.

### Symbols

Every yarn can carry its own mark — twenty of them, the way a printed chart
does. A yarn is given its mark the first time it is worked into a chart, and
the mark is stored with that chart, so it never shuffles under you while you
work. The ink is white or near-black depending on the luminance of the yarn
underneath, so it is legible on any colour.

They are drawn only for the stitches actually on screen, and only above 13x
zoom and under 1400 visible stitches, so turning them on never costs a smooth
pan.

### A sheet to print

**Save a chart sheet to print** draws the whole thing as one page: the grid
heavy enough to follow from a sofa, stitch and row numbers, a mark in every
square so it survives being photocopied in grey, and a legend naming every
yarn with its stitch count and metres. It is a PNG, so it prints, sends and
keeps like any other picture.

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

## Levels

Finishing a piece earns experience — roughly a point per eight stitches, plus a
bonus per colour, so ambitious pieces are worth more. The level curve is
`40 × level^1.55`, which makes the first two levels arrive almost immediately
and every one after that cost noticeably more.

Anyone updating from an earlier version keeps their credit: on first run the
app walks the cabinet, awards the experience those pieces would have earned,
and turns over a letter for each of them.

## Languages

English, French, Spanish and German — every screen, the pattern prompts, the
charm riddles, the level titles and the colour names. The switcher is a chip at
the top of the home screen, and on a first run it starts in the phone's own
language if it is one of the four.

There is no markup to maintain for it: the dictionary is keyed on the English
string itself, and a tree walk translates what is on screen, remembering the
original English on each node — which is what lets it switch back and forth
rather than only forwards. A `MutationObserver` catches anything rendered
afterwards. Strings the app builds by hand use `tf()` with `{braces}`.

To add a language: add its pack to `I18N`, add it to `LANGS`, done.

## Telling colours apart

The starting basket is chosen so every pair of yarns is far apart to the eye,
not merely different by name — the first version had six violet-greys in it and
they were unreadable on a chart.

Three tools back that up:

- **Show me** — pick any yarn in *Yarns in this chart* and everything else
  fades right back, so you can see exactly where that colour went.
- **The dyer warns you** when a colour lands within redmean distance ~65 of one
  already in the basket, and **Push apart** walks it clear — lightness first,
  because that is the difference that survives a small square on a phone, then
  hue.
- Picking a yarn names it, so *Marigold* and *Ochre* are told apart by word as
  well as by eye — and the yarn list, the written pattern, the printed sheet
  and the row-by-row helper all name them too, rather than printing a hex code
  and leaving you to guess.
- **Symbols** settle it for good: two yarns that read alike still carry
  different marks.

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
- **Save a chart sheet to print** exports the printable chart described above.
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
