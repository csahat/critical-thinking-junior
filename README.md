# Critical Thinking Junior
An AI thinking partner for students aged about 12 to 15. It asks one simple question at a time to help a student test their own ideas, and gives an everyday example for every new idea. It never does the homework.

What it teaches, how it differs from the adult version, and notes for parents and teachers are in the [skill README](skills/critical-thinking-junior/README.md).

## Installing
Download `critical-thinking-junior.zip` from the [latest release](../../releases/latest), or build it yourself with `python build_zip.py` (it lands in `dist/`).

### Gemini (web)
1. Open [gemini.google.com](https://gemini.google.com) and go to the **Skills** page.
2. Choose to create a skill by uploading, and select `critical-thinking-junior.zip`.

Skills can only be uploaded on the web app. To update the skill, upload the whole zip again.

### Claude (claude.ai)
Upload the same zip under **Settings → Capabilities → Skills**.

### Claude Code, Cursor, Codex and other agents
```bash
npx skills add <owner>/critical-thinking-junior
```
Or copy `skills/critical-thinking-junior/` into the agent's skills folder, for example `.claude/skills/` in a project or `~/.claude/skills/` for every project. Copy the whole folder, `references/` included.

### Using it
Start with something like *"Help me think this through: I think our school should ..."* or *"Check my thinking on my History essay argument."*

Check the platform's age rules first. Where a student is below them, run sessions on an adult's account with the adult present.

## Layout
```
skills/critical-thinking-junior/
  SKILL.md        # what the model loads
  README.md       # the human-facing explanation
  references/     # thinking moves, thinking checks, entry points
build_zip.py      # builds dist/critical-thinking-junior.zip
```

## Credit
Adapted from [Critical Thinking](https://github.com/mlevison/agent-thinking-skills/tree/main/skills/critical-thinking) by:
> Mark Levison, [Agile Pain Relief](https://agilepainrelief.com) - [github.com/mlevison/agent-thinking-skills](https://github.com/mlevison/agent-thinking-skills)

The Elements of Reasoning and the Universal Intellectual Standards are the work of Richard Paul and Linda Elder, [Foundation for Critical Thinking](https://www.criticalthinking.org).

## License
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), the same licence as the original, as its share-alike terms require. Full text in [LICENSE](LICENSE).
