# 📘 Learning Execution Guide — The Pattern Mastery Protocol

> **Purpose:** This document defines the exact protocol for learning each DSA pattern identified in [DSA_Master_Plan.md](file:///d:/sourav/code/DSA/plans/DSA_Master_Plan.md).  
> **Core Constraint:** Master each pattern up to **Medium** difficulty first for speed and breadth. Hard problems are strictly deferred.  
> **Language:** Python (default)  
> **Notes Location:** `d:\sourav\code\DSA\notes\` — All pattern theories and problem discussions are persisted here for revision.

---

## 🔄 The Learning Loop (Overview)

For **each pattern** in the Master Plan, you will execute this 4-step protocol in strict order:

```
┌───────────────────────────────────────────────────┐
│            THE PATTERN MASTERY LOOP               │
│                                                   │
│  Step A: Concept Theory                           │
│    ↓  Agent explains the pattern                  │
│  Step B: Boilerplate Code                         │
│    ↓  Agent provides code template                │
│  ★ GENERATE PATTERN NOTE → notes/patterns/        │
│    ↓                                              │
│  Step C: Easy Problem Walkthrough                 │
│    ↓  Agent walks through 1-2 Easy problems       │
│  ★ GENERATE PROBLEM NOTE → notes/problems/        │
│    ↓                                              │
│  Step D: Medium Problem Practice                  │
│    ↓  User solves; Agent acts as interviewer      │
│  ★ GENERATE PROBLEM NOTE → notes/problems/        │
│                                                   │
│  ✓ Pattern Mastered → Update Master Plan → Next   │
└───────────────────────────────────────────────────┘
```

---

## 📋 Step A: Concept Theory

**Who acts:** Agent (Instructor Mode)

**What happens:**
The agent delivers a focused theory session covering:

### A.1 — What is this pattern?
- Clear, jargon-free definition of the pattern
- Real-world analogy to build intuition
- Visual diagram or ASCII art showing the pattern in action

### A.2 — When does this pattern apply? (Trigger Recognition)
This is the **most valuable section**. The agent provides:

| Trigger Signal | Example Problem Statement | Why This Pattern |
|---------------|--------------------------|-----------------|
| *Exact phrases or structural cues in problem statements that indicate this pattern is applicable* | *A concrete example problem* | *Brief reasoning* |

> [!IMPORTANT]
> **The #1 skill in interviews is recognizing which pattern applies.** Memorizing this trigger table is more valuable than memorizing any solution.

### A.3 — Time & Space Complexity
- Typical time complexity of the pattern
- Typical space complexity
- When/why it degrades (edge cases)

### A.4 — Common Pitfalls & Edge Cases
- Off-by-one errors specific to this pattern
- Empty input handling
- Boundary conditions
- Mistakes beginners make

### A.5 — Relationship to Other Patterns
- Prerequisites: "You need to understand X before this"
- Siblings: "This is similar to Y, but differs because..."
- Evolutions: "This pattern forms the basis for Z"

> [!NOTE]
> **After completing Steps A + B**, the agent **must** generate a pattern note file at:
> `notes/patterns/XX_pattern_name.md` (e.g., `01_arrays_and_hashing.md`)
> This note consolidates everything from Steps A and B into a self-contained revision document.
> See the [Pattern Note Template](#-pattern-note-template) below.

---

## 📋 Step B: Boilerplate Code

**Who acts:** Agent (Instructor Mode)

**What happens:**
The agent provides **two artifacts** for each pattern:

### B.1 — The Skeleton Template
A reusable code template with:
- Clear variable naming conventions
- Comments marking the "fill in the logic here" points
- Standard import statements
- The canonical data structure setup

```python
# TEMPLATE: [Pattern Name]
# Time:  O(?)
# Space: O(?)

def solve(input_params):
    # 1. Initialize data structures
    # ____________________________
    
    # 2. Core loop / recursion
    # ____________________________
    
    # 3. Process / return result
    # ____________________________
    pass
```

### B.2 — A Fully Annotated Reference Implementation
One complete, well-commented solution to the simplest problem in this pattern, showing:
- Every line explained with inline comments
- The "why" behind each decision, not just the "what"
- Time and space complexity analysis at the end

> [!NOTE]
> The reference implementation is for **learning only**. During Step D (practice), you should reconstruct the solution from the skeleton template, not by memorizing this reference.

---

## 📋 Step C: Easy Problem Walkthrough

**Who acts:** Agent (Instructor Mode, Guided)

**What happens:**
The agent walks through **1–2 Easy** problems from the pattern's problem list, step by step.

### The Walkthrough Protocol:

#### C.1 — Problem Statement
Agent presents the problem clearly with:
- Input/output format
- Constraints
- 2–3 examples (including edge cases)

#### C.2 — Thought Process (Think Aloud)
Agent demonstrates the **exact thinking process** an experienced engineer would use:

1. **Read & Restate:** "In my own words, this problem is asking..."
2. **Identify Triggers:** "I notice [trigger], which tells me to try [pattern]"
3. **Brute Force First:** "The naive approach would be... with O(?) complexity"
4. **Optimize:** "I can improve this by using [pattern] because..."
5. **Dry Run:** Walk through the algorithm on Example 1 with a trace table

#### C.3 — Code Implementation
Full code with inline comments explaining each block.

#### C.4 — Complexity Analysis
- Time complexity with justification
- Space complexity with justification

#### C.5 — Variations & Follow-ups
- "What if the input were sorted/unsorted?"
- "What if we needed to return indices instead of values?"
- "How would this change if duplicates were allowed?"

> [!TIP]
> **After each Easy walkthrough, pause and ask yourself:** "Could I solve a slight variation of this from scratch in under 10 minutes?" If yes, proceed to Step D. If not, re-study Steps A and B.

#### C.6 — Generate Problem Note ★
After each Easy walkthrough, the agent **must** generate a problem note file at:
`notes/problems/LC_XXX_problem_name.md` (e.g., `LC_001_two_sum.md`)

This note captures:
- The complete problem statement and constraints
- The full thought process and approach discussed
- The final code with inline comments
- Complexity analysis
- Edge cases and variations
- **Interviewer tips:** What a real interviewer expects to hear, common follow-ups

> Companies frequently pick these exact problems in interviews. Having detailed discussion notes means you can revise the *reasoning*, not just re-read code.

---

## 📋 Step D: Medium Problem Practice

**Who acts:** User (with Agent as Interviewer/Tutor)

**What happens:**
The user attempts **Medium** problems from the pattern's problem list. The agent transitions from instructor to **mock interviewer**.

### The Practice Protocol:

#### D.1 — Problem Presentation
Agent presents the Medium problem with:
- Full problem statement
- Constraints
- Examples
- **No hints at this stage**

#### D.2 — User Attempts Solution
The user works on the problem. The agent monitors and provides **tiered hints** only when needed:

##### Hint Tier System

| Tier | When to Give | What to Say | Example |
|------|-------------|-------------|---------|
| **Tier 0: Nudge** | User is silent for 3+ minutes or asks "where do I start?" | A directional question, not an answer | *"What data structure would let you check membership in O(1)?"* |
| **Tier 1: Pattern Hint** | User is going down a wrong path | Reveal which pattern applies | *"This problem has a sliding window structure. What would your window represent?"* |
| **Tier 2: Approach Hint** | User has the right pattern but is stuck on implementation | Describe the high-level approach | *"Try maintaining a frequency map of characters in your window and compare it to..."* |
| **Tier 3: Pseudocode** | User has been stuck for 15+ minutes after Tier 2 | Provide pseudocode (not Python) | *"1. Initialize left=0, freq={}. 2. For each right... 3. While window invalid..."* |
| **Tier 4: Full Solution** | User explicitly gives up or has spent 30+ minutes | Provide full annotated solution | *(Full code with explanation)* |

> [!CAUTION]
> **Rule: Never jump to Tier 4 unless the user explicitly requests it or has exhausted all tiers.** The struggle is where learning happens.

#### D.3 — Post-Solution Review
After the user solves (or reviews) the problem:

1. **Complexity Check:** "What's your time and space complexity? Can you prove it?"
2. **Optimality Check:** "Is there a more optimal solution? Why or why not?"
3. **Edge Case Audit:** "What happens with empty input? Single element? All duplicates?"
4. **Pattern Reinforcement:** "What were the trigger signals that told you to use [pattern]?"

#### D.4 — Generate Problem Note ★
After each Medium problem (whether solved independently or with hints), the agent **must** generate a problem note at:
`notes/problems/LC_XXX_problem_name.md`

For Medium problems, the note additionally captures:
- **Hint trail:** Which hint tiers were used (important for tracking growth)
- **User's initial approach:** What the user tried first, even if wrong (shows thinking evolution)
- **Optimal vs. user solution comparison:** If different, document both
- **"If I see this again" summary:** A 2–3 sentence cheat sheet the user can scan before an interview
- **Related problems:** Other problems that use the same core technique

> [!IMPORTANT]
> Problem notes are your **interview quick-revision deck**. Before any interview, scan the `notes/problems/` folder to refresh approaches for the most commonly asked problems.

#### D.5 — Mastery Assessment

After completing all Medium problems for a pattern, the agent evaluates:

| Criteria | ✅ Mastered | ⚠️ Needs Review |
|----------|-----------|-----------------|
| Can identify the pattern from a problem statement within 2 minutes | Yes | No |
| Can write the boilerplate template from memory | Yes | No |
| Can solve a Medium problem in ≤ 25 minutes | Yes | No |
| Can explain time/space complexity accurately | Yes | No |
| Can handle edge cases without prompting | Yes | No |

- **If all ✅:** Mark pattern as `[x]` in the Master Plan. Move to next pattern.
- **If any ⚠️:** Revisit the weak area. Agent provides 1 additional problem targeting the gap.

---

## 🎯 Session Structure

Each study session should follow this structure:

```
┌─────────────────────────────────────────────────┐
│              DAILY SESSION (~90-120 min)         │
│                                                  │
│  00:00 – 05:00  │ Warm-up: Review yesterday's    │
│                 │ pattern triggers from memory    │
│                 │                                 │
│  05:00 – 25:00  │ Step A: Theory for new pattern  │
│                 │ (skip if continuing a pattern)  │
│                 │                                 │
│  25:00 – 35:00  │ Step B: Study boilerplate code  │
│                 │ (skip if continuing a pattern)  │
│                 │                                 │
│  35:00 – 55:00  │ Step C: Easy walkthrough        │
│                 │ (1 problem, guided)             │
│                 │                                 │
│  55:00 – 110:00 │ Step D: Medium practice         │
│                 │ (1-2 problems, interviewer mode) │
│                 │                                 │
│  110:00 – 120:00│ Cooldown: Log what you learned, │
│                 │ update Master Plan checklist     │
└─────────────────────────────────────────────────┘
```

---

## 📊 Progress Tracking Protocol

After each session, the agent **must** update these files:

1. **[DSA_Master_Plan.md](file:///d:/sourav/code/DSA/plans/DSA_Master_Plan.md):**
   - Pattern status: `[ ]` → `[/]` → `[x]`
   - Individual problem checkboxes
2. **[session_log.md](file:///d:/sourav/code/DSA/session_log.md):**
   - Append a new session entry (see template below)
3. **Pattern & Problem Notes:**
   - Create/update the relevant files in `notes/patterns/` and `notes/problems/`

### Session Log Entry Format

Append to [session_log.md](file:///d:/sourav/code/DSA/session_log.md):

```
### Session [N] — [YYYY-MM-DD]
- **Pattern:** [Pattern Name]
- **Step Completed:** A / B / C / D
- **Problems Attempted:** [List with LC numbers]
- **Problems Solved Independently:** [List]
- **Hints Used:** [Tier levels for each problem]
- **Key Takeaway:** [One sentence]
- **Weak Area to Revisit:** [If any]
- **Notes Generated:** [Links to pattern/problem notes created this session]
```

---

## 🏁 Mastery Milestones

### Milestone 1: Foundation Complete (Patterns 1–5)
- [ ] Can solve any Easy array/string problem in < 10 minutes
- [ ] Can recognize Two Pointers vs. Sliding Window vs. Prefix Sum triggers instantly
- [ ] Can write Stack/Monotonic Stack templates from memory

### Milestone 2: Core DS Complete (Patterns 6–12)
- [ ] Can reverse a linked list in 3 minutes (both iterative and recursive)
- [ ] Can implement binary search with correct boundary handling every time
- [ ] Can traverse a tree using BFS and DFS, choosing the right one based on the problem
- [ ] Can implement a Trie and use a heap for Top-K problems

### Milestone 3: Graphs & Backtracking Complete (Patterns 13–15)
- [ ] Can model a problem as a graph (adjacency list) and choose BFS vs. DFS
- [ ] Can implement topological sort (both DFS and Kahn's)
- [ ] Can write the backtracking template and prune effectively

### Milestone 4: DP & Optimization Complete (Patterns 16–19)
- [ ] Can identify if a problem is Greedy vs. DP
- [ ] Can define DP state, transition, and base cases for 1D and 2D problems
- [ ] Can convert top-down memoization to bottom-up tabulation
- [ ] Can recognize Knapsack, LCS, LIS, and State Machine DP variants

### Milestone 5: Full Mastery (All 20 Patterns)
- [ ] Can solve 80%+ of Medium LeetCode problems within 25 minutes
- [ ] Can identify the correct pattern for any problem within 2 minutes
- [ ] Can clearly communicate approach and trade-offs during a mock interview
- [ ] Ready to tackle Hard problems as a deep-dive phase

---

## 🚨 Rules of Engagement

### For the Agent (Instructor/Interviewer):

1. **No Code Dumping:** Never output a full solution unless the user explicitly requests it or has given up after all hint tiers.
2. **Pattern Triggers First:** When introducing a problem, always ask the user to identify the pattern before writing any code.
3. **Socratic Method:** Prefer questions over statements. Guide the user to discover the solution.
4. **Code & Style Review:** ALWAYS thoroughly examine the user's final code. Suggest Pythonic improvements, variable naming fixes, and stylistic better practices, even if the code already passes all tests.
5. **Celebrate Progress:** Acknowledge when the user correctly identifies a pattern or solves a problem independently.
6. **Be Honest:** If the user's solution works but is suboptimal, say so clearly and explain why.

### For the User (Learner):

1. **Don't Peek:** Resist looking at solutions before attempting the problem for at least 20 minutes.
2. **Speak Your Thoughts:** Practice explaining your approach out loud (or in text) — this is the interview skill.
3. **Time Yourself:** Use a timer. Interviews are 45 minutes. Medium problems should be solvable in 20–25 minutes.
4. **Track Honestly:** If you needed a Tier 3+ hint, that problem is not "solved" — revisit it in 3 days.
5. **Review Triggers Daily:** Spend 5 minutes each morning reviewing the trigger table for patterns you've covered.

---

## 🔄 The Spaced Repetition Schedule

Problems you struggled with should be revisited on this schedule:

| Review | When | What to Do |
|--------|------|-----------|
| Review 1 | 1 day after | Re-solve from scratch without looking at notes |
| Review 2 | 3 days after | Re-solve and explain the approach out loud |
| Review 3 | 7 days after | Re-solve under time pressure (25 min max) |
| Review 4 | 14 days after | If solved in < 15 min, mark as mastered. Otherwise, restart the cycle. |

---

## 📝 Pattern Note Template

Saved to: `notes/patterns/XX_pattern_name.md`

```markdown
# Pattern [N]: [Pattern Name]

## What Is It?
[Clear definition + real-world analogy]

## When To Use It (Trigger Table)
| Trigger Signal | Example Problem | Why This Pattern |
|---------------|----------------|------------------|
| ... | ... | ... |

## Boilerplate Template
```python
# [code template]
```

## Time & Space Complexity
- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls
- [list of gotchas]

## Related Patterns
- [prerequisites, siblings, evolutions]

## Key Takeaways
- [bullet points from the discussion]
```

---

## 📝 Problem Note Template

Saved to: `notes/problems/LC_XXX_problem_name.md`

```markdown
# LC [Number]: [Problem Name]
- **Difficulty:** Easy / Medium / Hard
- **Pattern:** [Pattern Name]
- **Date Discussed:** [YYYY-MM-DD]
- **Solved Independently:** Yes / No (Tier [X] hint used)

## Problem Statement
[Full problem statement with constraints and examples]

## Approach & Thought Process
1. **Initial Observation:** [What I noticed first]
2. **Pattern Identified:** [Why this pattern applies]
3. **Brute Force:** [Naive approach and its complexity]
4. **Optimized Approach:** [Step-by-step logic]

## Solution Code
```python
# [Full annotated solution]
```

## Complexity Analysis
- **Time:** O(?) — [justification]
- **Space:** O(?) — [justification]

## Edge Cases
- [List of edge cases and how they're handled]

## Variations & Follow-ups
- [What if the input changes? Common interviewer follow-ups]

## "If I See This Again" (Quick Revision)
> [2-3 sentence cheat sheet: the core insight + approach in plain English]

## Related Problems
- [LC numbers and names of similar problems]
```

---

> [!IMPORTANT]
> ## Ready to Begin?
> 
> Once both `DSA_Master_Plan.md` and this `Learning_Execution_Guide.md` are approved, the agent will transition from **Planner** to **Interviewer/Tutor** mode.
> 
> Read [CONTEXT.md](file:///d:/sourav/code/DSA/CONTEXT.md) for the full folder structure and resumption protocol.
> 
> **Action Required:** Tell the agent which pattern from the Master Plan you want to start with, and the learning loop begins!
