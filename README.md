# 🔥 Roast My Code

A Claude Code agent skill that reviews your code with brutal honesty and comedic delivery. Every finding is real, every roast is earned, and every issue comes with a fix.

Think Gordon Ramsay doing code review.

## Install

```bash
claude plugin add AfterRealm/roast-my-code
```

Or manually: copy this repo to `~/.claude/plugins/roast-my-code/`

## Usage

```
/roast                    # roast the current file or recent changes
roast my code             # same thing
roast this function       # scope to a specific function
roast the whole project   # full project review (buckle up)
```

## What It Does

This is a **real code reviewer** that happens to be hilarious. It doesn't manufacture fake issues for laughs — every roast is backed by a genuine finding.

### Review Categories

| Category | What It Catches |
|----------|----------------|
| 🔥 Bugs | Logic errors, off-by-ones, null derefs, race conditions |
| 🔓 Security | Injection, exposed secrets, missing validation, auth gaps |
| 🐌 Performance | O(n²) disasters, memory leaks, unnecessary work |
| 🤡 Style Crimes | God functions, lying variable names, callback hell |
| 💀 Dead Code | Unreachable branches, TODO archaeology, zombie imports |
| 🏗️ Architecture | Wrong abstractions, circular deps, misplaced logic |

### The Roast Scale

| Score | Rating | Meaning |
|:---:|---|---|
| 10 | 👨‍🍳 Chef's Kiss | I came to roast and left humbled |
| 8-9 | 🔥 Well Done | Solid. Minor nitpicks at best |
| 6-7 | 🍳 Medium | Edible but needs seasoning |
| 4-5 | 🥩 Rare | Undercooked. Served too early |
| 2-3 | 🗑️ Dumpster Fire | I've seen better code in a CAPTCHA |
| 0-1 | ☠️ Health Violation | Ship this and someone's going to the hospital |

## Example Output

```
# 🔥 ROAST MY CODE — auth.js

## The Verdict
This authentication module is like a nightclub bouncer who checks IDs
but leaves the back door propped open with a brick. You validated the
JWT perfectly, then stored the session token in localStorage like it's
a grocery list. The password hashing is solid but the rate limiting
is nonexistent — congrats, you built a brute-force playground.

**Score: 4/10 — 🥩 Rare**

---

### 🔓 SECURITY — Session tokens in localStorage
> You hashed the password with bcrypt but stored the session token where
> any XSS script can grab it. That's like locking your front door and
> leaving the key taped to the window.

**What's wrong:** localStorage is accessible to any JavaScript running
on the page. An XSS vulnerability anywhere in the app exposes all
session tokens.
**Severity:** CRITICAL
**Fix:** Use httpOnly cookies for session tokens.
```

## Philosophy

1. **Every roast is backed by a real finding.** No fake issues for comedy.
2. **Roast the code, not the coder.** Never attack intelligence or experience.
3. **Always include the fix.** A roast without a solution is just bullying.
4. **Celebrate the good stuff.** The best roasts acknowledge skill before burning the mistakes.

## Eval

This skill includes an evaluation framework. See `evals/evals.json` for test cases.

```bash
# Run the eval
claude -p "Run the roast-my-code evaluation using evals/evals.json"
```

## License

MIT

## Author

Built by [AfterRealm](https://github.com/AfterRealm) with Claude Code.
