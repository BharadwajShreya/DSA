# 🧠 DSA Preparation — Agent Context File

> **Read this file first if you are a new agent session continuing this DSA preparation journey.**

---

## Who Is The User?

A **GenAI Engineer** preparing for FAANG/top-tier technical interviews. They need systematic, pattern-based DSA mastery with a focus on **Medium** difficulty first for breadth and speed.

## What Is This Project?

An interactive, agent-guided DSA interview preparation system. The agent acts as both **instructor** (teaching patterns) and **mock interviewer** (during practice). All learning artifacts are persisted in this folder so progress survives across chat sessions.

## Folder Structure

```
d:\sourav\code\DSA\
│
├── CONTEXT.md                  ← YOU ARE HERE. Read this first.
│
├── plans\
│   ├── DSA_Master_Plan.md      ← The master roadmap: 20 patterns, ~150 problems,
│   │                              ordered by prerequisites with progress checkboxes.
│   │                              UPDATE this as patterns are completed.
│   │
│   └── Learning_Execution_Guide.md  ← The 4-step protocol for each pattern:
│                                       Step A (Theory) → B (Boilerplate) →
│                                       C (Easy Walkthrough) → D (Medium Practice).
│                                       Includes hint tier system & mastery criteria.
│
├── notes\
│   ├── patterns\               ← One .md file per pattern (e.g., 01_arrays_and_hashing.md)
│   │                              Contains: theory summary, triggers, templates,
│   │                              pitfalls, and complexity cheat sheet.
│   │                              Created after completing Steps A+B for a pattern.
│   │
│   └── problems\               ← One .md file per problem discussed (e.g., LC_001_two_sum.md)
│                                  Contains: problem statement, approach, code,
│                                  complexity analysis, edge cases, and interviewer notes.
│                                  Created after each problem walkthrough/practice.
│
└── session_log.md              ← Running log of all sessions: date, pattern,
                                   problems attempted, hints used, takeaways.
                                   Append to this after every session.
```

## How To Resume

1. **Check `plans/DSA_Master_Plan.md`** — look at the progress checkboxes to see which patterns are `[x]` (done), `[/]` (in progress), or `[ ]` (not started).
2. **Check `session_log.md`** — read the last few entries to understand where the user left off.
3. **Check `notes/patterns/`** — see which pattern notes exist (these are completed theory).
4. **Check `notes/problems/`** — see which problems have been discussed.
5. **Resume from the last `[/]` pattern** or ask the user which pattern to continue with.
6. **Follow the protocol** in `plans/Learning_Execution_Guide.md` exactly.

## Key Rules

- **No Code Dumping:** Never give full solutions unless user explicitly asks or has exhausted all hint tiers.
- **Language:** Python (default), unless user specifies otherwise.
- **Pattern Triggers Are King:** The most valuable thing to teach is *how to recognize which pattern applies*.
- **Medium First:** Hard problems are strictly deferred until all Mediums in a pattern are mastered.
- **Always Generate Notes:** After every theory session and problem discussion, create/update the corresponding note file.
- **Update Progress:** After every session, update both the Master Plan checkboxes and the session log.
