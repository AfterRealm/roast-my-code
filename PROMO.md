# 🔥 Roast My Code — a Claude Code Agent Skill

Your code review called. It said it's tired of being boring.

**Roast My Code** is an agent skill that does real code review — bugs, security holes, performance issues, architectural crimes — but delivers every finding like a standup set. Every roast is backed by a real finding. Every finding comes with a fix. If your code is actually good, it'll tell you that too. And then roast you for making its job boring.

## What it catches
```
🔥 Bugs         — off-by-ones, null derefs, race conditions
🔓 Security     — injection, exposed secrets, auth gaps
🐌 Performance  — O(n²) disasters, memory leaks
🤡 Style Crimes — god functions, lying variable names
💀 Dead Code    — zombie imports, TODO archaeology
🏗️ Architecture — circular deps, business logic in the view layer
```

## Sample roast
> *"You hashed the password with bcrypt but stored the session token in localStorage. That's like locking your front door and leaving the key taped to the window."*

> *"`proc()` takes 8 parameters, handles 7 modes, and has a default behavior for when you pass no mode at all. It's not a function — it's a microservice disguised as a `def`."*

> *"These JWTs live forever. You've issued immortal credentials. If one leaks, it's valid until the heat death of the universe."*

## Scores your code on the Roast Scale
| Score | Rating |
|:---:|---|
| 10 | 👨‍🍳 Chef's Kiss — I came to roast and left humbled |
| 6-7 | 🍳 Medium — Edible but needs seasoning |
| 2-3 | 🗑️ Dumpster Fire — I've seen better code in a CAPTCHA |
| 0-1 | ☠️ Health Violation — Ship this and someone's going to the hospital |

## Ships with a real eval
Not just vibes — actual proof it works. 3 test files, 28 assertions, automated eval runner with Opus as judge.

**First run: 93% assertion pass rate. 5/5 humor. 5/5 actionability.**

The spaghetti monster test file (a 150-line god function with global mutable state and recursive retry) scored 10/10 assertions. It caught everything.

## Install
```
claude plugin add AfterRealm/roast-my-code
```

**GitHub:** https://github.com/AfterRealm/roast-my-code

Your code's been talking behind your back. Time to find out what it's saying. 🔥
