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

## Carry or cut

In colour-work the cost of a picture is not its stitches, it is its colour
*changes*: every one is a yarn end to weave in, and weaving in ends is the part
everyone dreads. A drawing app would show a stitch count. This one shows the
work.

**Effort** (in the chart menu) counts the colour changes, then the ends you
would face two ways: cutting at every change, or **carrying** the yarn along the
back where the colour returns within six stitches. Rows turn, so the colour a
row ends in is the colour the next starts with, and that join costs nothing.
It turns the ends into a rough weaving time and says how big a job the whole
chart is, from *gentle* to *an epic*.

**Strays** are single stitches surrounded on three or four sides by other
colours; each costs a change and two ends for almost nothing on the finished
piece. Effort rings them on the chart, and one tap matches each to the commonest
colour round it, as a single undo. A lone dot on bare ground is left alone, as
is an edge stitch with only two worked neighbours: those are deliberate.

And when you work the pattern row by row, it says what to **reach for next**
and whether to **carry the yarn behind or cut it** — the decision a crocheter
actually makes at the end of every run, answered at the moment it comes up.

## Reach for it

Following a pattern, the thing you need to know is not a number, it is *which
yarn*. Two thumb-sized swatches show the colour in your hand and the one to
reach for next, so you match them by eye against the skeins in the basket
without reading a word. The next one pulses gently. At the end of a row it
looks across the turn to the first yarn of the following row, because rows turn
and that yarn is wanted straight away. In **Hands busy** they grow to 62 px.

## Where did it go wrong?

The app cannot see your crochet, so it cannot compare it with the chart. What it
can do is ask the question a person actually has to answer, and ask it
cleverly. If the rows are right up to some point and drifted after it, the
first bad row can be found by halving: it asks about the most recent row, then
the middle, then the middle of whichever half is left, showing the piece as it
should look at that row with the row boxed. A hundred rows takes seven answers,
where counting back takes up to a hundred. It is `git bisect` for a blanket.

When it finds the row it says what fixing it costs — how many rows, about how
many stitches — and puts the row-by-row helper back at that row. Checked
exhaustively: every count of finished rows from 1 to 22 against every possible
first-bad row, 253 cases, found correctly every time in at most six questions.

## The basket looks ahead

A guide layer says what each square should be, but you still hunt the basket
for the right yarn every time the colour changes. Crochet works a row in one
direction and turns at the end, so the next stitch owed is knowable: it is the
first square, going the way this row runs (odd rows right to left), that the
guide wants and the chart does not yet have. Its skein is ringed and wears a
count of how many stitches in that yarn come together; a dot marks colours that
are still to come in the row. When the row is finished the ring is already on
the yarn the next row begins with — the turn. If the pattern wants a colour that
is not in the basket, the dye button is ringed instead and it says so once.
The basket scrolls the wanted skein into view but never fights your thumb.
There is a switch in Settings (*The basket looks ahead*).

## Which yarn and hook?

Every pattern site tells you the yarn it was written in. The Worked-up screen
goes the other way: say how wide you want the picture and it shows what each yarn
weight, from fingering to super bulky, would make of it — the finished size, the
hook that usually goes with it, the metres you would need — and marks the closest
fit. Single-crochet gauges are the Craft Yarn Council's, per 10 cm. Your hands do
not change with the yarn, so each weight is read at the tension inside its usual
range that is **nearest to yours**: a weight whose range holds your tension shows
exactly the size the rest of the app already gives you, and the others show where
your hands would sit at the edge of theirs. The picture keeps your own
stitch-to-row proportion, and yarn per stitch scales from the number you
measured, so the metres agree with *What to buy* to the metre. *Use this* adopts
a weight's tension; with more than one colour carried it also reminds you that
most makers go down a hook size.

## A tag to go with it

Handmade things go out with a tag on a loop of yarn. **Make a gift tag** (on any
piece in the cabinet) draws one: a hole punched through the top with the loop
threaded through it, in the first of the piece's yarns that is not near-black;
the piece framed; who it is for and who made it; a line of your own; a row of
running stitches; the **true finished size in centimetres** from your own
tension; the yarns by name; a care label for the fibre (cotton, acrylic, wool,
or "not sure", which gives the safe answer for any yarn); and, once the app has
learned your pace, how many hours of crocheting went into it. It is written in
the language the app is set to, shared through the phone's own share sheet where
there is one, and saved as a picture where there is not.

## What I already have

A shopping list that says "buy 40 m of teal" when there are 60 m of it in a
drawer is asking for a wasted trip. Tell the app how many metres of each yarn
are really in the basket at home and the list changes: colours you have enough
of are marked **you have it**, the rest say how many metres you are *short*,
and nothing else changes. It is kept on the phone with everything else.

## Hands busy

Following a pattern with a hook in one hand and yarn in the other, a small
button is the wrong target. **Hands busy** turns the whole panel into the
button and sets the run you are on at 30–46 px, readable from a lap, with the
chart and the run list out of the way and the screen held awake.

## Your own pace

It times how long you actually take between marking one run done and the next,
divides by the stitches in it, and keeps the **median** — so putting the work
down for an hour does not make every estimate an hour long. Once it has a few
samples, the worked-up screen says how long a chart will take *you*, rather
than how long it would take somebody else.

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
