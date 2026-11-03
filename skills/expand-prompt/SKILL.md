---
name: expand-prompt
description: Expand a terse creative brief or edit note into the prompt its author would write, in Blake's house shape. For a new brief the order is fixed: first find five images from one aesthetic to ground the visual direction and three moving references to ground the motion (are.na channels, then Pinterest, primary sites, Sketchfab), decide concretely how each one is used in which beat, derive the numbered beats from the motion references, then write the prompt with references and assets attached. A style, brand or medium the user names, or a reference they attach, fences the search: pick the best instance inside it, never a different aesthetic. Use for "/expand-prompt", "expand this prompt", "make this prompt more specific", "what is missing from this prompt", "help me write the prompt for X", or whenever a one-line animation / composition / design brief is about to be handed to an agent.
---

# Expand prompt

Turn a short draft into the brief its author would have written. The drafts are usually
Stewdio composition work (motion, 3D, shaders, footage); the method applies to any
generative brief.

**The author's briefs are references plus beats.** 21 of his 29 real openers attach a
reference; 16 name an aesthetic in the first line; 3 contain a px / ms / hex number.
The idea lives in the thing pointed at (`recreate this <mp4>`, `dancing like in
<youtube>`, `in the texture of embroidery <img>`), and the beats say what turns into
what. Numbers, bans and keep-clauses belong to the edit loop, not the opener.

**Expressive means a committed look, a copied move, a real thing, and a turn.** Not more
words and not more numbers. The voice is the author's own: lowercase, imperative,
numbered, no filler. A new brief stays under ~150 words plus its reference list; an edit
note under ~50.

Files in `references/`:

- `finding-references.md`: roles, seeds, the are.na channel loop, picking, vetting. Read before step 2.
  Target per brief: five images for the visual direction, three moving refs for the motion, each tied to a beat.
- `vocabulary.md`: the author's own words, per slot. Borrow while writing.
- `examples.md`: before / after pairs from real sessions. Read when unsure of the shape.
- `patterns.md`: corpus evidence behind the rules. Optional.

## Procedure

1. **Classify the draft.**

   | mode | signal | output shape |
   |---|---|---|
   | brief | "create", "recreate", a new comp or scene | aesthetic line + numbered beats + frame line + refs + assets |
   | batch | "create N comps", "variations", "fill the gaps" | brief + per-item one-liners + dedupe rule + shared constraints |
   | delta | "make X more/less Y", "get rid of", "fix", "move to" | target + change + magnitude + direction + keep-clause |
   | image feedback | a screenshot / contact sheet is attached | one line per observation, each naming its frame or time |
   | sequence | "at Ns", "after the X exits", beats across time | brief with a time anchor on every beat, duration cap |
   | housekeeping | rename, push, export, "check the render" | leave as is; add the exact format or target |

   Brief, batch and sequence go through steps 2-7. Delta and image feedback skip to
   step 6 (search only when the change brings in a new look or move).

2. **Ground the visual direction: five images.** Before writing a single beat.
   Pick one aesthetic that fits the subject (a nested channel from his umbrellas or
   a CARI aesthetic), sheet it, and keep five stills that together say what the
   piece looks like: the overall look, the palette and texture, the material or
   surface, a composition or framing, a detail or motif. All five from the same
   aesthetic; if a second aesthetic keeps winning tiles, switch to it wholesale,
   never blend. The aesthetic's name goes in the prompt's first line.

   **If the draft says nothing about the look**, choose for being remarkable, not
   for matching the draft's words. **If the draft names a style, a brand or a
   medium, or attaches a reference, that is the fence, and the word is the are.na
   query.** Decode it in one line (what the user pictures when they say it), then
   two queries: `search "<style>"` or `search "<brand domain>"` for the name itself
   (the brand's own artefacts, the style's canon) and `channels "<decoded visual
   word>"` for what curators collect about it (`gradient`, `glow`, `big type`, `stop
   motion`), plus nested umbrella / CARI channels carrying the word. Pick the five
   images there, striking first, homonyms dropped by eye; product-UI channels are a
   `u` source only. Curators' channels hold what is interesting *about* the word,
   which is inside the fence and still a look; the primary site only supplies hex,
   type and one real component, never a frame to copy. The fence constrains
   palette, material, type and components, not layout, scale, camera or the move.
   The first line names a child of the user's word (`in stripe-gradient dark`, not
   `in graphic score`). An attached reference takes its role as-is and the other
   images come from the same look via its channel or `connections`. Two ways this
   has failed (2026-11-02): overriding the word (minimal → a graphic score, stripe
   → a conference sizzle, claymation → clay.com) and screenshotting it (the stripe
   docs page as a4, five settings screens; builds at browser scale).

3. **Ground the motion: three moving references.** gif / mp4 from the motion
   channels, each a move worth copying ("would he put this in mo-graph?"). Aim for
   three different jobs: the entrance or main mechanic, the transition or turn, the
   exit or the camera. Sheet each and read its timings. **The fence never applies
   here**: a named style fences the images, the move stays free and striking, and
   UI micro-interaction channels are a ui source, not an m source.

   Then, as the beats need them: a copy reference or asset for anything recognisable
   (a real UI, a real product, a named artwork, a model from Sketchfab), a ui
   reference for interfaces. Assign roles to user-attached references too; a user
   attachment fills its slot. Method and seeds: `finding-references.md`. Look at
   every candidate before it gets a role.

4. **Decide how each reference is used, concretely.** For every one of the eight:
   which beat it feeds and exactly what is taken from it. Images: "a3's wet-stone
   texture is the canvas surface", "a5's bead row is the end state", "a2's palette
   for the ink, nothing else". Motion: "m1 0.0-1.6s is beat 1 at 1.5x slower, the
   subject swapped for cards", "m2's grow-and-invert is the turn at ~5s", "m3's
   camera pull-back is beat 4". A reference that cannot be tied to a beat is
   dropped, not kept for atmosphere. Then write the beats: the motion refs give
   their order and timings, the images sit on the beat where their quality first
   shows. Add the turn: at least one beat where something is revealed, changes
   medium or texture, zooms out to show a larger whole, or becomes something else.
   His sequences are chains of these (`the wave washes the scene into a shanshui
   painting`, `the painting unravels into a single thread which becomes a running
   silhouette`, `the camera zooms out to reveal all ~100 carousels`). A piece that
   only enters, animates and holds is not finished. **When the draft already holds a
   transformation** (`snaps into`, `comes back as`, `checks off on the other`), that
   verb *is* the turn: make it the biggest beat and do not stack a second metaphor
   on it (a ribbon coil, a whip-pan contraption, staves becoming brackets). In a
   ≤5 s product clip there is room for exactly one idea; added ideas go into the
   material and the camera, not the plot.

5. **Add ideas.** Welcome and expected on a bare draft: a look, a twist, a prop that
   makes the subject specific, a real asset, a camera move tied to a reveal, a second
   beat that answers the first. Write them as beats, not as options. Mark the one or
   two that are real forks with `[? ...]`. What stays out: annotation text, UI
   chrome, guiding lines, drop shadows, a fade where a cut would do, anything the
   author's standing bans cover.

6. **Fill the slots** (checklist below). Inferable from the file, the previous comp,
   an attachment or the conversation: silently. Missing and creative: a
   `[? best default]` placeholder inside the prompt. Missing and routine (duration,
   aspect): default it inline, no marker.

7. **Rewrite in the house shape** (templates below). Keep the author's wording
   where it exists; reorder; close with `refs:` and `assets:`, every entry carrying
   its concrete use from step 4.

8. **Output** three things and nothing else: the prompt in a fenced block; a
   "fill-ins" list (max three) naming the creative forks, each with the choice made
   and the one alternative worth considering; one line pointing at
   `.context/refs/<topic>/` with the contact sheets so the user can veto a pick.
   Never ask about duration, loop or aspect in the fill-ins. No technique, no
   advice. If a real thing is needed and absent (the user's own app, product, logo),
   say so in one line above the prompt and still deliver the prompt with the best
   stand-in named.

## Slot checklist

Opener slots first; they decide the result. Edit-loop slots after; they decide the
second round.

| slot | ask | house form |
|---|---|---|
| where | tool, file, comp; for sequences the time or beat it attaches to | `in stewdio, <file>, <comp>, at 3.5s:` / `after the sticker exits:` |
| look | one aesthetic, named, from the visual reference; a child of the user's own style word or attachment when there is one | `in frutiger aero style` / `in the style of a 16bit dungeon crawler game` / `everything in riso` |
| medium / technique | photo or footage, 3D rebuild, vector, shader, real model | `using threejs or 3d framework` / `illustrator vector animation` / `real 3d texture and train models` |
| move | the mechanic, copied from the motion reference, subject swapped | `recreate this animation, but make it nyc subway` / `only the spiral form factor and the scroll animation` |
| subject | the real thing, by name, with its source | `the famous ukiyo-e painting <img>` / `the orb in liquid orb composition` |
| beats | numbered; each = subject + action + what it reveals or becomes | `2. then at around 2s, a big wave splats across the screen, turning the entire screen into a new texture` |
| turn | the reveal / morph / zoom-out / medium switch | `the camera zooms out to reveal that ...` / `unravels into a single thread which eventually becomes ...` |
| realism | fidelity demand when it matters | `it should be very realistic` / `very realistic liquid simulation` / `loyal to the og` |
| camera | move + easing + what it lands on | `camera zooms fast into the pupil, steep quadratic ease-in` / `camera stays still` |
| pace | the feel in his words, seconds only for anchors | `very snappy, ease-in-out` / `one continuous motion from the start` / `the whole sequence should be under 15s` |
| frame | bg, aspect, duration, loop | `white bg, 1:1, ~5s loop` (state only what differs from the standing defaults) |
| params | values to expose when the comp will be tuned | `expose params for plumpness, sheen, glow` |
| keep | what must not change when editing something that works | `keep the old entrance speed` / `keep the rest the same` |
| magnitude + direction | deltas only: multiplier, phase, axis and sense | `2x faster at top speed` / `30 degree clockwise` |
| scope fence | deltas only: which comps the edit touches | `only for 23` / `unrelated: also ...` |

**Standing defaults**, left implicit when they apply: white bg (black for the
math-graph family); no fade, no drop shadow, no rounded corners, no annotation text,
no UI chrome, no guiding lines; 1:1 for social posts, 16:9 for the graph and carousel
families; ~5 s for a loop, 3-4 s for an inserted beat, under 15-20 s for a sequence;
real assets for recognisable objects, stylised on top. Do not write these out.

## Templates

**Brief**

```
in stewdio, <file>, [<comp>,] [at <N>s / after <beat>,] create the following, in <aesthetic from a1>[, using <technique>]:

1. <subject (c1 / asset), its state at 0s> <enters like m1: mechanic>
2. <main action from m1, subject swapped> [at ~<N>s]
3. <the turn: reveals / turns into / zooms out to show ...> <a1 or d1 if the new look needs one>
4. <exit or end state>

<realism demand if it matters>; <camera if it moves>; <pace in his words>
<frame only where it differs from the defaults>; the whole thing ~<N>s
[expose params for <list>]

refs:
- a1 <path>: look, <what it sets: overall look, framing of beat 1> (<url>, channel <slug>)
- a2 <path>: palette, <used where> (<url>, channel <slug>)
- a3 <path>: texture / material, <which surface in which beat> (<url>, channel <slug>)
- a4 <path>: composition, <which beat's frame> (<url>, channel <slug>)
- a5 <path>: detail / motif, <which element, which beat> (<url>, channel <slug>)
- m1 <path>: motion, beat <n>: <mechanic + the time range taken, scale factor>, subject swapped, not the look (<url>, channel <slug>)
- m2 <path>: motion, beat <n> (the turn): <what is taken> (<url>, channel <slug>)
- m3 <path>: motion, beat <n>: <camera / exit taken> (<url>, channel <slug>)
- c1 <path>: copy, <subject>, one-to-one (<url>)
assets:
- <path or url>: use as-is for <what>
- <sketchfab page> (<author>, <licence>, <faces>): <object>, one-to-one, <parts that must move> [? download]
```

Beats cite handles inline: `2. the sticker peels from the lower-left corner like m1
(curl, then lift), on a3's wet stone`. Every handle in `refs:` appears in a beat.

**Batch**

```
in <file>, create <N> <things>, <one-line shared description>, using <channel> as reference:

1. <item: mechanic + orientation + layout>
2. ...

for all of them: <shared constraints>; keep each ~<N>s
no overlap with <existing set>; a valid variation changes the mechanic, orientation, layout or treatment, not just direction or mirror
name them "<Prefix>: [<k> word description]"
```

**Delta**

```
[for <comp>,] make <element> <change> <magnitude> [<direction with axis>] [at <N>s]
[get rid of <element>]
keep <what must stay>
```

Several deltas: a numbered list, one change per line, each naming its target;
"unrelated:" marks a change to a different comp.

**Image feedback**

```
<frame or time it points at>: <one observation, quantified>
```

## Rules

- **References before beats, always.** A brief written first and decorated with
  matching references afterwards reads like a spec. The motion reference supplies
  the mechanic and its timing; the visual reference supplies the aesthetic; the beats
  are what happens when the draft's subject goes through that move in that look.
- **Pick for quality, not for match.** The best motion reference is the most
  striking move that could carry the subject, found in a curated channel; a keyword
  hit that merely shows the right object is a weak pick. Three channels per role,
  then widen through `connections`.
- **A named style or an attached reference is the fence, and the fence is a query.**
  The images are picked, striking first, from are.na channels named for the word;
  the primary site gives hex, type and one component. The chosen look must read as
  the user's word to the person who typed it and still be a look, not a
  screenshot. The fence covers palette, material, type and components; the move,
  the scale and the camera stay free.
- **A film frame, not a web page.** One hero element takes ≥40% of the frame height
  at the beat it matters; the smallest text is ≥24 px at 1080p; nothing is rebuilt
  at 1:1 browser scale. A settings page in a fifth of the frame and a docs page
  with 11 px code both read as screenshots. Judge the sheet at thumbnail size.
- **The action fills the clip.** In ≤5 s the end hold is under 1 s. A turn that is
  over by 1.6 s means compressed beats or a missing second half.
- **Five images, three moves, each with a job.** The images are one aesthetic seen
  five ways (look, palette, material, composition, detail), not five moods. The
  moves cover different beats (mechanic, turn, camera or exit). Every reference in
  `refs:` names the beat it feeds and what is taken; one that feeds nothing is cut.
- **One reference, one job, with a fidelity word.** Moving media for motion, stills
  for look. A motion ref implies a subject swap. Never one file for two roles unscoped.
- **Assets are used, references are read.** Real footage, a real GLB, the real UI
  screenshot, the real painting, stylised on top. A hand-built brain was "very bad";
  a real model fixed it. Procedural only for primitives, orbs, blobs, extrusions,
  noise fields and things that must grow or morph.
- **Treat each thing as a contraption.** Animate its special mechanism (a lid
  closes, a folder's papers jump out, an envelope seals, a checkbox ticks), not a
  default draw-in. Transformations are in-process morphs, not a deconstruction then
  a reconstruction; a shape morph, not a tracing play.
- **Describe the mechanism, not the adjective.** What moves, from where, revealing
  what. "editorial page-drag" was read as a slide-in; "the current image is peeled
  from a corner to reveal the new one already underneath" was built once.
- **Numbers where he uses them.** Seconds for anchors and total length, multipliers
  and degrees in deltas, a hex only when the colour is the point (klein blue
  #002FA7). No ms staggers, px rises or pixelRatio checks in an opener.
- **Direction has an axis and a sense; magnitude names its phase.** Edit-loop rules:
  "the other way" is not a direction; "entrance 5x faster" needs "the fastest
  entrance we have had, constant roll speed afterwards".
- **Keep the voice.** "get rid of", "tho", "~5s", "plz" are fine. No greetings,
  rationale or headings inside the prompt.
- **Batches need a dedupe rule and a naming format.** Backward and mirror are not
  variations.

## Scripts

- `scripts/find_refs.py`: are.na channels / umbrellas / contact sheets, Pinterest
  pin resolution, Sketchfab search + download, file downloads, video contact sheets.
  Run it with no arguments for the command list.
- `scripts/extract_prompts.py <out.md>`: rebuilds the prompt corpus from every
  transcript under `~/.claude/projects`. Re-run when the author's habits drift and
  re-check `patterns.md`.
