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

### Shapes

The block tool lays four shapes, and tapping it again while it is already the
chosen tool moves it on to the next: **block**, **frame**, **ring**, **disc**.
Four shapes for one slot, in a tool tray with no room for three more buttons.
The icon changes to whichever is loaded, the choice is remembered, and the
round ones keep only the cells with a neighbour outside the ellipse, which
gives an even one-stitch line at any size instead of the gaps a naive plot
leaves.

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

## The Cabinet

It opens on the work. The ribbons sit under it, and the ones still to earn are
one chip reading *"n still to earn"* rather than twenty-two greyed badges
filling the screen before a single finished piece is in sight.

Thumbnails lay one even cloth behind a piece rather than the woven check the
chart itself uses: at thumbnail size a check reads as the transparency pattern
from an image editor, which is the last thing a framed piece should look like.

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

Every string the app builds by hand goes through `t()` or `tf()` too — the
toasts, the questions it asks, the notes under buttons, the guide templates and
the whole written pattern, down to RS/WS and the yarn units. A translation that
covers the markup and not the messages is not a translation; for a long time
this one only covered the markup.

`audit.py` in the scratchpad keeps it honest: it strips the dictionary blocks
out of the source, scans what is left for sentence-shaped literals, and reports
any that no pack has a key for. It reads zero.

To add a language: add its pack to `I18N`, add it to `LANGS`, done.

## Recolour

**Try other colours** shows the chart as it would be in every set of yarns you
have — the basket and each unlocked skein set — each one previewed live before
you pick it, and applied as a single undoable change.

It maps by **tone, not by hue**: both sides are sorted by lightness and rank is
mapped to rank, with each target taken at most once while spares remain. That
is what keeps a picture readable in a set that shares none of its colours —
mapping to the nearest hue would flatten a night palette into one grey.

The dyer also offers five colours that go with the one you are making: the
opposite, the two neighbours, a tint and a deeper shade, all recomputed as you
drag, with one button to drop the lot in the basket. Choosing the first colour
is the hard part; the other five should not be.

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
- The dyer names the colour while you drag it, so you know what you are making
  before you keep it.
- A colour we only have a near name for is set in *italics* rather than
  prefixed with a tilde: a tilde in front of a colour name reads as a typo, and
  in four languages a punctuation mark explains nothing.
- Picking a yarn names it, so *Marigold* and *Ochre* are told apart by word as
  well as by eye — and the yarn list, the written pattern, the printed sheet
  and the row-by-row helper all name them too, rather than printing a hex code
  and leaving you to guess.
- **Symbols** settle it for good: two yarns that read alike still carry
  different marks.

## Read aloud

Every control that is only a picture carries a name, in whatever language the
app is set to, so a phone reading the screen aloud says *Undo* rather than
*button*. The chart is a canvas, which announces nothing at all on its own, so
it carries a live description instead — the chart's name and size, where the
cursor is, and how much is worked — rebuilt with the row and stitch readout.

`i18n_audit.py` checks the control names alongside everything else: it reads
the `aria-label`, `placeholder` and `title` attributes out of the markup and
reports any with no key in any pack.

If the phone asks for less movement, the sheets and the buttons stop sliding.

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
