# Changelog

## v1.0.0 — 2026-04-05

> *Your code had it coming.*

### The Skill
- Full code review engine with 6 review categories: Bugs, Security, Performance, Style Crimes, Dead Code, Architecture
- Every finding includes a roast, a real explanation, severity rating, AND a concrete fix
- Roast Scale scoring system (0-10): Health Violation → Dumpster Fire → Rare → Medium → Well Done → Chef's Kiss
- Structured output format: Verdict, Findings, Scoreboard, Final Words
- Rules: roast the code not the coder, every roast backed by a real finding, celebrate what's done right

### The Eval
- 3 hand-crafted test files covering the full spectrum:
  - `bad_auth.js` — auth module with 6 security vulnerabilities (hardcoded secret, query param admin escalation, no rate limiting)
  - `decent_api.py` — competent Flask API with real but non-critical issues (tests that good code doesn't get over-roasted)
  - `spaghetti.py` — 150-line god function with 8 parameters, recursive retry, global mutable state, string dispatch (the ultimate roast target)
- Automated eval runner (`evals/run_eval.py`) — runs each test with and without the skill, Opus judges assertions + quality
- 28 total assertions across test cases
- Iteration tracking in `evals/iteration-N/`
- Markdown report output (`--markdown` flag)

### First Eval Results
- **93% assertion pass rate**
- **Accuracy: 4.7/5** — catches real issues
- **Humor: 5.0/5** — actually funny
- **Actionability: 5.0/5** — every finding has a fix
- **Format compliance: 5.0/5** — follows the template
- Spaghetti monster test: 10/10 assertions, perfect score
