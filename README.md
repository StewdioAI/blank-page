# expand-motion

A Claude Code skill, `expand-prompt`, that turns a one-line animation / composition /
design brief into the prompt its author would have written: one committed aesthetic,
five images grounding the look, three moving references grounding the motion, and
numbered beats derived from them.

Built in Stewdio composition work (motion, 3D, shaders, footage); the method applies
to any generative brief.

## Before / after

Each pair starts from the same one-line prompt. Before: the prompt handed to the agent
as typed. After: the prompt run through `/expand-prompt` first.

> 5 second clip for a note-taking app launch. you type one search and results pop in from docs, slack and email

| before | after |
|---|---|
| ![notes search, before](media/notes-search-before.gif) | ![notes search, after](media/notes-search-after.gif) |

> quick 5 second twitter post: our design tool just hit 10,000 users

| before | after |
|---|---|
| ![10,000 users, before](media/10k-users-before.gif) | ![10,000 users, after](media/10k-users-after.gif) |

> 5s looping background for a saas pricing page. it sits behind the plan cards so keep it subtle. soft frosted glass, like apple’s website

| before | after |
|---|---|
| ![pricing glass, before](media/pricing-glass-before.gif) | ![pricing glass, after](media/pricing-glass-after.gif) |

> 5 sec clip for a payments api: a request leaves the code and comes back as a payment confirmed. dark mode, kind of like stripe’s style

| before | after |
|---|---|
| ![payments api, before](media/payments-api-before.gif) | ![payments api, after](media/payments-api-after.gif) |

> 5 second changelog clip for a calendar app. the messy old settings page snaps into clean grouped sections. clean and minimal, lots of white

| before | after |
|---|---|
| ![calendar settings, before](media/calendar-settings-before.gif) | ![calendar settings, after](media/calendar-settings-after.gif) |

## How it works

A capable agent already picks sensible easing and staggers. What it does not do on its
own is commit to a look, copy a striking move, use a real asset and add a turn. The skill
makes it do those four things, in a fixed order: references first, beats second.

1. **Classify the draft.** A new brief, a batch of variations, a timed sequence, an edit
   ("make X more Y"), or feedback on a screenshot. Edits and feedback skip the search
   and come back as short, targeted notes with a keep-clause.
2. **Pick one aesthetic and ground it in five images.** Overall look, palette, material,
   composition, detail, all from one aesthetic (an are.na channel). A style, brand or medium named
   in the draft fences the search: the best instance inside it, never a different look.
3. **Find three moving references.** gifs / mp4s from motion channels, one each for the
   entrance or main mechanic, the turn, and the exit or camera. Each is cut into a
   contact sheet so its timing can be read. The fence does not apply here; the move stays
   free.
4. **Tie every reference to a beat.** Which beat it feeds and exactly what is taken
   ("m1 0.0-1.6s is beat 1 at 1.5x slower, subject swapped"). A reference that feeds no
   beat is dropped. The beats take their order and timing from the motion refs, and at
   least one is a turn: a reveal, a morph, a zoom-out, a change of medium.
5. **Add ideas, fill the gaps.** A prop, a real asset (a Sketchfab model, real footage,
   the real UI), a camera move tied to the reveal. Routine gaps get defaults inline;
   creative forks get a `[? ...]` placeholder.
6. **Write it in the house shape.** Lowercase, imperative, numbered, under ~150 words,
   closing with `refs:` and `assets:`.

The output is the prompt in a fenced block, up to three fill-ins (the creative forks,
each with the choice made and one alternative), and a pointer to
`.context/refs/<topic>/` with the contact sheets so you can veto a pick. Handing the
prompt to the agent is up to you.

```
in stewdio, <file>, create the following, in <aesthetic>:

1. <subject at 0s> enters like m1
2. <main action from m1, subject swapped> at ~2s, on a3's <material>
3. <the turn: reveals / turns into / zooms out to show ...>
4. <end state>

<pace>; <camera>; ~5s
expose params for <list>

refs:
- a1 .context/refs/<topic>/a1.jpg: look, sets beat 1's frame (are.na/block/<id>, channel <slug>)
- m1 .context/refs/<topic>/m1.gif: motion, beat 1: <mechanic, 0.0-1.6s at 1.5x slower>, subject swapped
- ...
assets:
- <sketchfab page> (<author>, <licence>): <object>, one-to-one
```

`skills/expand-prompt/references/examples.md` has real before / after prompt pairs.

## Layout

```
.claude-plugin/
  plugin.json          plugin manifest
  marketplace.json     single-plugin marketplace, so the repo installs with /plugin
skills/expand-prompt/
  SKILL.md             the procedure
  references/          finding-references, vocabulary, examples, patterns
  scripts/find_refs.py are.na / Pinterest / Sketchfab search, downloads, contact sheets
media/                 before / after gifs for the README
```

## Install

As a plugin (skill shows up as `expand-motion:expand-prompt`):

```
/plugin marketplace add blakeshao/expand-motion
/plugin install expand-motion@expand-motion
```

Or as a plain user skill (shows up as `/expand-prompt`):

```sh
git clone https://github.com/blakeshao/expand-motion.git
ln -s "$PWD/expand-motion/skills/expand-prompt" ~/.claude/skills/expand-prompt
```

Use a project-level `.claude/skills/expand-prompt` symlink instead to scope it to one repo.

## Requirements

- `python3` (stdlib only) and `curl`
- `ffmpeg` for contact sheets (`find_refs.py sheet`, `channel <slug> <dir>`)
- WebSearch, for finding Pinterest pins
- optional `SKETCHFAB_TOKEN` for Sketchfab downloads not in the Objaverse mirror

## Usage

```
/expand-prompt a typing eye made of glb parts, blinking on each keystroke
```

Also triggers on "expand this prompt", "make this prompt more specific", "what is
missing from this prompt", or whenever a short brief is about to be handed to an agent.
