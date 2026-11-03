# expand-motion

A skill for Claude Code and Codex, `expand-prompt`, for getting started on a motion piece. The hardest
part of prompting is the blank page: you know roughly what the clip is for, not what it
should look like. Give it a one-liner and it turns that into a full prompt with a look,
references and a sequence of beats, so the first result is already an interesting one.

Good for when you don't know what you want yet, and for when you do but want to explore
directions you wouldn't have thought of.

## Before / after

Each pair starts from the same one-line prompt. Before: the prompt handed to the agent
as typed. After: the prompt run through `/expand-prompt` first.

> 5 sec clip for a payments api: a request leaves the code and comes back as a payment confirmed. dark mode, kind of like stripe’s style

| before | after |
|---|---|
| ![payments api, before](media/payments-api-before.gif) | ![payments api, after](media/payments-api-after.gif) |

> quick 5 second twitter post: our design tool just hit 10,000 users

| before | after |
|---|---|
| ![10,000 users, before](media/10k-users-before.gif) | ![10,000 users, after](media/10k-users-after.gif) |

> 5s looping background for a saas pricing page. it sits behind the plan cards so keep it subtle. soft frosted glass, like apple’s website

| before | after |
|---|---|
| ![pricing glass, before](media/pricing-glass-before.gif) | ![pricing glass, after](media/pricing-glass-after.gif) |

> 5 second clip for a note-taking app launch. you type one search and results pop in from docs, slack and email

| before | after |
|---|---|
| ![notes search, before](media/notes-search-before.gif) | ![notes search, after](media/notes-search-after.gif) |

> 5 second changelog clip for a calendar app. the messy old settings page snaps into clean grouped sections. clean and minimal, lots of white

| before | after |
|---|---|
| ![calendar settings, before](media/calendar-settings-before.gif) | ![calendar settings, after](media/calendar-settings-after.gif) |

## How it works

A one-line prompt gives the agent nothing to aim at, so it falls back on the safest
version of the idea. Instead of asking you to fill in the blanks, the skill goes looking
for references first and builds the prompt around what it finds.

1. **Pick a look.** Five images from one aesthetic on are.na. If you name a style or
   brand, it stays inside it.
2. **Find the motion.** Three gifs or videos with moves worth copying.
3. **Write the beats.** A numbered sequence built from those references, with at least
   one twist: a reveal, a morph, a zoom-out.
4. **Add real assets.** A 3D model, footage or the real UI instead of a hand-built
   stand-in.

You get back the prompt with every reference attached, plus up to three creative
calls it made, so you can swap any of them before handing it to an agent.

Short edit notes ("make it faster") skip the search and come back as a short, precise note.
More examples: [`references/examples.md`](skills/expand-prompt/references/examples.md).

## Layout

```
.claude-plugin/        Claude Code plugin + marketplace manifests
.codex-plugin/         Codex plugin manifest
.agents/plugins/       Codex marketplace manifest
skills/expand-prompt/
  SKILL.md             the procedure (shared by both)
  agents/openai.yaml   Codex display metadata
  references/          finding-references, vocabulary, examples, patterns
  scripts/find_refs.py are.na / Pinterest / Sketchfab search, downloads, contact sheets
media/                 before / after gifs for the README
```

## Install

### Claude Code

As a plugin (skill shows up as `expand-motion:expand-prompt`):

```
/plugin marketplace add blakeshao/expand-motion
/plugin install expand-motion@expand-motion
```

Or as a plain skill (shows up as `/expand-prompt`):

```sh
git clone https://github.com/blakeshao/expand-motion.git
ln -s "$PWD/expand-motion/skills/expand-prompt" ~/.claude/skills/expand-prompt
```

### Codex

As a plugin:

```sh
codex plugin marketplace add blakeshao/expand-motion
codex plugin add expand-motion@expand-motion
```

Or as a plain skill:

```sh
git clone https://github.com/blakeshao/expand-motion.git
ln -s "$PWD/expand-motion/skills/expand-prompt" ~/.agents/skills/expand-prompt
```

For either tool, symlink into a project's `.claude/skills/` or `.agents/skills/` instead
to scope it to one repo.

## Requirements

- `python3` (stdlib only) and `curl`
- `ffmpeg` for contact sheets (`find_refs.py sheet`, `channel <slug> <dir>`)
- web search in the agent, for finding Pinterest pins
- optional `SKETCHFAB_TOKEN` for Sketchfab downloads not in the Objaverse mirror

## Usage

```
/expand-prompt a typing eye made of glb parts, blinking on each keystroke   # Claude Code
$expand-prompt a typing eye made of glb parts, blinking on each keystroke   # Codex
```

Also triggers on "expand this prompt", "make this prompt more specific", "what is
missing from this prompt", or whenever a short brief is about to be handed to an agent.
