# expand-motion

A Claude Code skill, `expand-prompt`, that turns a one-line animation / composition /
design brief into the prompt its author would have written: one committed aesthetic,
five images grounding the look, three moving references grounding the motion, and
numbered beats derived from them.

Built in Stewdio composition work (motion, 3D, shaders, footage); the method applies
to any generative brief.

## Layout

```
.claude-plugin/
  plugin.json          plugin manifest
  marketplace.json     single-plugin marketplace, so the repo installs with /plugin
skills/expand-prompt/
  SKILL.md             the procedure
  references/          finding-references, vocabulary, examples, patterns
  scripts/
    find_refs.py       are.na / Pinterest / Sketchfab search, downloads, contact sheets
    extract_prompts.py dump human-typed prompts from Claude Code transcripts (corpus building)
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
