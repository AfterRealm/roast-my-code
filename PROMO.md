# 🍰 Blunt Cake — Code review that doesn't sugarcoat

You know that friend who'll tell you your outfit looks bad before you leave the house? That's Blunt Cake, but for your code.

**8 modes. 6 personalities. Custom voice creator. Coding challenges. Auto-fix. CI/CD. And it roasts itself to stay sharp.**

## Modes

**🔥 Standard** — fast single-pass. Finds the issues, delivers them straight, gives you the fix.

**👨‍🍳 Panel** — 4 specialist agents tear through your code in parallel (security, performance, architecture, style). Cross-confirmed findings are the real ones.

**📝 Diff Roast** — roast your git diff before you commit. Only judges what you changed.

**🆚 Batter Battle** — two files enter, one leaves. 5-round head-to-head with a declared winner.

**🏫 Roast-a-thon** — roast an entire project directory. File-by-file scores, project GPA, valedictorian and dropout callouts.

**🎯 Skill Roast** — feed it a SKILL.md and it tells you what's missing. 8 categories from trigger design to eval-readiness.

**📊 Eval** — dead serious. Assertions, PASS/FAIL grades, 5 quality dimensions, letter grade. Comedy only in the final verdict.

**🎯🔥 Roast Challenge** — coding katas judged by Blunt Cake. 5 built-in challenges with target scores to beat. Community challenges welcome.

## Personalities

Pick a voice for your roast. Same findings, different delivery.

🧑‍🍳 **Chef** — celebrity chef energy, kitchen metaphors
👵 **Disappointed Grandma** — not mad, just disappointed
😐 **Passive-Aggressive PR Reviewer** — "Interesting choice 🙂"
🎤 **Simon Cowell** — withering pauses, grudging respect
🐕 **Snoop Dogg** — chill but devastating, fo real
🏴‍☠️ **Pirate** — nautical metaphors, walk the plank for CRITICALs
🎨 **Custom** — describe any voice and Blunt Cake generates the personality. Save it, reuse it.

## It fixes what it finds

After any roast, Auto-Fix offers to apply the fixes — all at once, critical only, or pick individually. Then offers a re-roast to check your new score.

## CI/CD

Drop the GitHub Action in your repo. Every PR gets a Diff Roast posted as a comment. Configurable mode and personality.

## Eval-verified

```
9 test cases, 82 assertions
Pass rate:        86% (97% excluding headless-only mode)
Accuracy:         4.4/5
Humor:            4.6/5
Actionability:    4.6/5
```

Ships with a self-improving eval loop — ran its own tests, read its failures, rewrote its own instructions, re-tested.

## Install

```
claude marketplace add AfterRealm/marketplace
claude plugin add afterrealm/blunt-cake
```

Or just grab the skill file:
```
mkdir -p ~/.claude/skills/blunt-cake
curl -o ~/.claude/skills/blunt-cake/SKILL.md https://raw.githubusercontent.com/AfterRealm/blunt-cake/master/SKILL.md
```

**GitHub:** https://github.com/AfterRealm/blunt-cake
**Marketplace:** https://github.com/AfterRealm/marketplace

No frosting. Just cake. 🍰
