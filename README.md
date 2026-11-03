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
