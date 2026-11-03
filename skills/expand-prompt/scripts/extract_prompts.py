#!/usr/bin/env python3
"""Dump every human-typed prompt from all Claude Code transcripts into one markdown corpus.
Handles: opening prompt glued after </system_instruction>, mid-turn queue-operation enqueues,
image placeholders, sidechain (subagent) turns excluded."""
import json, os, re, glob, sys
from datetime import datetime
NOISE_BLOCKS = [
    re.compile(r"<system-reminder>.*?</system-reminder>", re.S),
    re.compile(r"<system_instruction>.*?</system_instruction>", re.S),
    re.compile(r"<local-command-stdout>.*?</local-command-stdout>", re.S),
    re.compile(r"<command-(?:name|message|args)>.*?</command-(?:name|message|args)>", re.S),
    re.compile(r"<task-notification>.*?</task-notification>", re.S),
    re.compile(r"<ide_opened_file>.*?</ide_opened_file>", re.S),
]
NOISE_PREFIXES = ("Caveat:", "<local-command-stdout>", "<command-name>", "[Request interrupted", "Base directory for this skill")
def clean(t):
    for p in NOISE_BLOCKS: t = p.sub("", t)
    t = t.strip()
    if not t or t.startswith(NOISE_PREFIXES): return None
    return t
def user_text(msg):
    c = msg.get("content")
    if isinstance(c, str): return clean(c), 0
    if isinstance(c, list):
        parts, imgs = [], 0
        for b in c:
            if not isinstance(b, dict): continue
            if b.get("type") == "text": parts.append(b.get("text", ""))
            elif b.get("type") == "image": imgs += 1
            elif b.get("type") == "tool_result": return None, 0
        return clean("\n".join(parts)), imgs
    return None, 0
roots = glob.glob(os.path.expanduser("~/.claude/projects/*/*.jsonl"))
sessions = []
for path in roots:
    title, prompts, seen = None, [], set()
    for line in open(path, errors="replace"):
        try: r = json.loads(line)
        except ValueError: continue
        t = r.get("type")
        if t == "ai-title" and r.get("aiTitle"): title = r["aiTitle"]
        elif t == "user" and not r.get("isSidechain"):
            txt, imgs = user_text(r.get("message", {}))
            if txt and txt not in seen:
                seen.add(txt); prompts.append((r.get("timestamp") or "", txt, imgs))
        elif t == "queue-operation" and r.get("operation") == "enqueue":
            txt = clean(r.get("content") or "")
            if txt and txt not in seen:
                seen.add(txt); prompts.append((r.get("timestamp") or "", txt, 0))
    if prompts:
        prompts.sort(key=lambda p: p[0])
        sessions.append((prompts[0][0], os.path.basename(path)[:-6], title, prompts))
sessions.sort()
out = ["# Prompt corpus", ""]
total = 0
for ts0, sid, title, prompts in sessions:
    out += [f"## {ts0[:10]} · {title or '(untitled)'} · `{sid[:8]}` · {len(prompts)} prompts", ""]
    for ts, txt, imgs in prompts:
        total += 1
        tag = f" [+{imgs} image{'s' if imgs>1 else ''}]" if imgs else ""
        out += [f"**{ts[11:16]}**{tag}", "", txt, "", "---", ""]
open(sys.argv[1], "w").write("\n".join(out))
print(len(sessions), "sessions", total, "prompts", "->", sys.argv[1])
