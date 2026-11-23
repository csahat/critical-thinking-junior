# Critical Thinking Junior
An AI thinking partner for students aged about 12 to 15. It asks one simple question at a time to help a student test their own ideas, and gives an everyday example for every new idea. It never does the homework.

What it teaches, how it differs from the adult version, and notes for parents and teachers are in the [skill README](skills/critical-thinking-junior/README.md).

## Recommended Platform: Gemini on the Web
For students, I only recommend using this skill with **Google Gemini's web version** ([gemini.google.com](https://gemini.google.com)), on a **teen Google account**.

Set up a Google account for your teenager and enter their birth date correctly. Gemini then applies its standard teen protections on top of the skill's own guardrails:
- stricter content guardrails, which Google describes as ["even stricter content policies"](https://safety.google/products/gemini) for younger users
- limits on some features for under-18 accounts

> [!IMPORTANT]
> **Check your country's minimum age.** Each country sets its own minimum age for creating a Google account ([Google's list by country](https://support.google.com/accounts/answer/1350409)). In Singapore, the minimum age is **13**.

**Use this skill with an adult in the room.** Not hovering over every message, but close enough to notice if the conversation turns, and to talk through what the student found. That matters most in the first few sessions.

> [!WARNING]
> **Common Sense Media rates Gemini with teen protections as "High Risk"** ([assessment, September 2025](https://www.commonsensemedia.org/ai-ratings/gemini-with-teen-protections)). It concluded that the teen version appears to be the adult version of Gemini with some extra safety features, rather than something built for young people. Common Sense recommends that **no one under 18 use Gemini for mental health advice or emotional support**.
>
> This skill stops the exercise and points to a trusted adult when a student seems upset or unsafe, but it cannot fix the underlying model. That is why an adult should be in the room. Check Common Sense Media for newer ratings.

## Installing
Download `critical-thinking-junior.zip` from the [latest release](../../releases/latest), or build it yourself with `python build_zip.py` (it lands in `dist/`).

### Gemini (web)
Uploading a skill needs a **Google AI Plus** subscription and works **only on the web version**, not the mobile app. It works on teen accounts.

1. At [gemini.google.com](https://gemini.google.com), click **Customize** in the left sidebar.
2. Open the **Skills** tab.
3. Click **Create**, choose **Upload**, and select `critical-thinking-junior.zip`.

The skill then appears under **Installed** as *critical-thinking-junior*. To update it, upload the whole zip again.

### Other Platforms (for Adults Trying It Out)
These routes work, but they are not recommended for students. Claude's consumer apps, for example, require users to be 18 or over.

**Claude (claude.ai):** upload the same zip under **Settings → Capabilities → Skills**.

**Claude Code, Cursor, Codex and other agents:**
```bash
npx skills add csahat/critical-thinking-junior
```
Or copy `skills/critical-thinking-junior/` into the agent's skills folder, for example `.claude/skills/` in a project or `~/.claude/skills/` for every project. Copy the whole folder, `references/` included.

## Using It
Start with something like *"Help me think this through: I think our school should ..."* or *"Check my thinking on my History essay argument."*

The reference files in `skills/critical-thinking-junior/references/` are also printable, so you can ask the same questions yourself at the dinner table or over homework.

## TODO
- [ ] **Mental health and emotional support guardrail.** When a student raises a mental health or emotional support topic, the skill should stop and encourage them to talk to a parent or the school counsellor, and give these Singapore services:
  - **National Mindline:** call **1771** or WhatsApp **6669 1771** to talk to a mental health counsellor, available 24/7.
  - **Samaritans of Singapore (SOS):** call the 24-hour hotline at **1767** or WhatsApp **9151 1767**.

  The skill currently gives only the SOS hotline (1767), in its Safety section.

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
