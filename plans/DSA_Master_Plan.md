# 🎯 DSA Master Plan — Interview Readiness Roadmap

> **Target Audience:** GenAI Engineer preparing for FAANG/top-tier technical interviews  
> **Strategy:** Pattern-first, breadth-before-depth. Master each pattern up to **Medium** difficulty first.  
> **Sources Synthesized:** Grokking the Coding Interview, NeetCode 150, Blind 75, Grind 75, Sean Prashad's LeetCode Patterns, competitive programming heuristics.  
> **Language:** Python (default)

---

## 📊 Overview & Timeline

| Phase | Patterns Covered | Est. Time | Focus |
|-------|-----------------|-----------|-------|
| **Foundation** (Patterns 1–5) | Arrays, Hashing, Two Pointers, Sliding Window, Prefix Sum | ~2 weeks | Core building blocks |
| **Linear Structures** (Patterns 6–8) | Stack, Linked List, Binary Search | ~1.5 weeks | Fundamental data structures |
| **Hierarchical** (Patterns 9–12) | Trees (BFS/DFS), Tries, Heap/Priority Queue, Merge Intervals | ~2 weeks | Recursive thinking |
| **Graph Theory** (Patterns 13–15) | Graph BFS/DFS, Backtracking, Advanced Graphs | ~2 weeks | Traversal & search mastery |
| **Optimization** (Patterns 16–19) | Greedy, 1-D DP, 2-D DP, Knapsack & Sequence DP | ~2.5 weeks | Optimization & decision |
| **Specialized** (Pattern 20) | Bit Manipulation, Math & Geometry, Cyclic Sort | ~1 week | Edge-case patterns |

> **Total Estimated Time: 11–12 weeks** (at ~1.5–2 hours/day, 5–6 days/week)

---

## 🧭 Pattern Recognition Decision Tree

Use this **before** you even think about code. When you read a problem, run it through these filters:

```
START → Read the problem constraints
  │
  ├─ Is the input SORTED (or can be sorted)?
  │    ├─ Looking for a pair/triplet? → TWO POINTERS
  │    ├─ Looking for a target in O(log n)? → BINARY SEARCH
  │    └─ Merging sorted data? → K-WAY MERGE / MERGE INTERVALS
  │
  ├─ Is it about a CONTIGUOUS subarray/substring?
  │    ├─ Fixed window size? → SLIDING WINDOW (fixed)
  │    ├─ Variable window with condition? → SLIDING WINDOW (dynamic)
  │    └─ Cumulative sum/range query? → PREFIX SUM
  │
  ├─ Is it about a LINKED LIST?
  │    ├─ Cycle detection / middle finding? → FAST & SLOW POINTERS
  │    └─ Reversing parts? → IN-PLACE REVERSAL
  │
  ├─ Is it about TREE/GRAPH traversal?
  │    ├─ Level-by-level? → BFS (Queue)
  │    ├─ Path-based / depth exploration? → DFS (Stack/Recursion)
  │    ├─ Shortest path (unweighted)? → BFS
  │    ├─ Shortest path (weighted)? → DIJKSTRA / BELLMAN-FORD
  │    └─ Connectivity / components? → UNION-FIND / DFS
  │
  ├─ "Find top/smallest/largest K elements"? → HEAP (Top K)
  │
  ├─ "Generate all permutations/subsets/combinations"? → BACKTRACKING
  │
  ├─ "Next greater/smaller element"? → MONOTONIC STACK
  │
  ├─ "How many ways..." / "Min/Max cost to reach..."? → DYNAMIC PROGRAMMING
  │    ├─ Choices with weight constraints? → KNAPSACK DP
  │    ├─ Comparing two sequences? → LCS / EDIT DISTANCE
  │    ├─ Finding longest increasing order? → LIS
  │    └─ Grid navigation? → GRID DP
  │
  ├─ "Find missing/duplicate in range [1..n]"? → CYCLIC SORT or XOR
  │
  └─ "Maximize with local optimal choices"? → GREEDY
```

---

## 🔍 Constraint Analysis Cheat Sheet (from Competitive Programming)

The input size `N` in the constraints tells you the **expected time complexity**:

| Constraint | Expected Complexity | Likely Pattern |
|-----------|-------------------|---------------|
| N ≤ 15–20 | O(2^N) or O(N!) | Backtracking, Bitmask DP |
| N ≤ 100 | O(N³) | DP (interval, matrix chain) |
| N ≤ 1,000 | O(N²) | DP (2D), brute force with pruning |
| N ≤ 10,000 | O(N√N) or O(N log²N) | Advanced DS, sqrt decomposition |
| N ≤ 100,000 | O(N log N) | Sorting + greedy, Binary Search, Heap |
| N ≤ 1,000,000 | O(N) | Two Pointers, Sliding Window, Prefix Sum |
| N ≤ 10^9 | O(log N) or O(1) | Binary Search, Math |

---

## ✅ Pattern Checklist & Progress Tracker

### Legend
- `[ ]` = Not started
- `[/]` = In progress
- `[x]` = Mastered (completed Easy + Medium problems)

---

### 🏗️ PHASE 1: Foundation (Patterns 1–5) — *~2 weeks*

---

#### Pattern 1: Arrays & Hashing
- [/] **Status:** In progress
- **Estimated Time:** 3 days
- **Core Concept:** Use hash maps for O(1) lookups to avoid nested loops. Frequency counting, grouping, and deduplication.
- **Triggers:** "Find if X exists," "group similar elements," "count occurrences," "find duplicates"
- **Complexity:** Typically O(N) time, O(N) space

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Two Sum | Easy | 1 | [ ] |
| 2 | Contains Duplicate | Easy | 217 | [x] |
| 3 | Valid Anagram | Easy | 242 | [ ] |
| 4 | Group Anagrams | Medium | 49 | [x] |
| 5 | Top K Frequent Elements | Medium | 347 | [ ] |
| 6 | Product of Array Except Self | Medium | 238 | [ ] |
| 7 | Encode and Decode Strings | Medium | 271 | [ ] |
| 8 | Longest Consecutive Sequence | Medium | 128 | [ ] |

---

#### Pattern 2: Two Pointers
- [/] **Status:** In progress
- **Estimated Time:** 2 days
- **Core Concept:** Use two index variables moving toward each other (or in the same direction) to reduce O(N²) to O(N).
- **Triggers:** "Sorted array + find pair," "palindrome check," "remove duplicates in-place," "container/area problems"
- **Complexity:** O(N) time, O(1) space (usually)

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Valid Palindrome | Easy | 125 | [ ] |
| 2 | Two Sum II (Sorted) | Medium | 167 | [ ] |
| 3 | 3Sum | Medium | 15 | [ ] |
| 4 | Container With Most Water | Medium | 11 | [x] |
| 5 | Trapping Rain Water | Hard* | 42 | [ ] |

> *Hard problem included as a capstone — defer until Medium mastery is solid.

---

#### Pattern 3: Sliding Window
- [/] **Status:** In progress
- **Estimated Time:** 3 days
- **Core Concept:** Maintain a window (subarray/substring) that expands or shrinks based on a condition, avoiding recomputation.
- **Triggers:** "Maximum/minimum subarray of size K," "longest substring with condition," "smallest subarray with sum ≥ X"
- **Complexity:** O(N) time, O(K) or O(1) space

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Best Time to Buy and Sell Stock | Easy | 121 | [x] |
| 2 | Longest Substring Without Repeating Characters | Medium | 3 | [x] |
| 3 | Longest Repeating Character Replacement | Medium | 424 | [ ] |
| 4 | Permutation in String | Medium | 567 | [ ] |
| 5 | Minimum Window Substring | Hard* | 76 | [ ] |

---

#### Pattern 4: Prefix Sum
- [ ] **Status:** Not started
- **Estimated Time:** 1 day
- **Core Concept:** Precompute cumulative sums to answer range-sum queries in O(1). Often combined with hash maps.
- **Triggers:** "Sum of subarray equals K," "range sum query," "equilibrium index"
- **Complexity:** O(N) time, O(N) space (for prefix array)

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Running Sum of 1d Array | Easy | 1480 | [ ] |
| 2 | Find Pivot Index | Easy | 724 | [ ] |
| 3 | Subarray Sum Equals K | Medium | 560 | [ ] |
| 4 | Contiguous Array | Medium | 525 | [ ] |

---

#### Pattern 5: Stack (including Monotonic Stack)
- [ ] **Status:** Not started
- **Estimated Time:** 2 days
- **Core Concept:** LIFO structure for matching pairs, maintaining order, and "next greater/smaller" problems. Monotonic stacks maintain elements in sorted order.
- **Triggers:** "Matching parentheses," "next greater element," "evaluate expression," "histogram problems"
- **Complexity:** O(N) time (amortized), O(N) space

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Valid Parentheses | Easy | 20 | [ ] |
| 2 | Min Stack | Medium | 155 | [ ] |
| 3 | Evaluate Reverse Polish Notation | Medium | 150 | [ ] |
| 4 | Daily Temperatures | Medium | 739 | [ ] |
| 5 | Next Greater Element I | Easy | 496 | [ ] |
| 6 | Car Fleet | Medium | 853 | [ ] |

---

### 🔗 PHASE 2: Linear Structures (Patterns 6–8) — *~1.5 weeks*

---

#### Pattern 6: Linked List (Including Fast & Slow Pointers)
- [ ] **Status:** Not started
- **Estimated Time:** 3 days
- **Core Concept:** Pointer manipulation, in-place reversal, cycle detection (Floyd's algorithm). Fast pointer moves 2x speed of slow.
- **Triggers:** "Reverse a linked list," "detect cycle," "find middle node," "merge two lists," "remove nth from end"
- **Complexity:** O(N) time, O(1) space (for in-place operations)

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Reverse Linked List | Easy | 206 | [ ] |
| 2 | Merge Two Sorted Lists | Easy | 21 | [ ] |
| 3 | Linked List Cycle | Easy | 141 | [ ] |
| 4 | Reorder List | Medium | 143 | [ ] |
| 5 | Remove Nth Node From End of List | Medium | 19 | [ ] |
| 6 | Add Two Numbers | Medium | 2 | [ ] |
| 7 | Find the Duplicate Number | Medium | 287 | [ ] |

---

#### Pattern 7: Binary Search
- [ ] **Status:** Not started
- **Estimated Time:** 3 days
- **Core Concept:** Divide the search space in half each step. Applies beyond sorted arrays — any problem where you can binary search on the answer.
- **Triggers:** "Sorted array + find target," "minimize the maximum," "find boundary/insertion point," "rotated sorted array"
- **Complexity:** O(log N) time, O(1) space

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Binary Search | Easy | 704 | [ ] |
| 2 | Search a 2D Matrix | Medium | 74 | [ ] |
| 3 | Koko Eating Bananas | Medium | 875 | [ ] |
| 4 | Find Minimum in Rotated Sorted Array | Medium | 153 | [ ] |
| 5 | Search in Rotated Sorted Array | Medium | 33 | [ ] |
| 6 | Time Based Key-Value Store | Medium | 981 | [ ] |

---

#### Pattern 8: Merge Intervals
- [ ] **Status:** Not started
- **Estimated Time:** 1.5 days
- **Core Concept:** Sort intervals by start time, then iterate and merge overlapping ones. Key: compare `current.end` with `next.start`.
- **Triggers:** "Overlapping intervals," "meeting rooms," "insert interval," "free time"
- **Complexity:** O(N log N) time (sorting), O(N) space

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Meeting Rooms | Easy | 252 | [ ] |
| 2 | Merge Intervals | Medium | 56 | [ ] |
| 3 | Insert Interval | Medium | 57 | [ ] |
| 4 | Non-overlapping Intervals | Medium | 435 | [ ] |
| 5 | Meeting Rooms II | Medium | 253 | [ ] |

---

### 🌳 PHASE 3: Hierarchical Structures (Patterns 9–12) — *~2 weeks*

---

#### Pattern 9: Tree — Depth-First Search (DFS)
- [ ] **Status:** Not started
- **Estimated Time:** 3 days
- **Core Concept:** Recursive or stack-based traversal exploring depth before breadth. Three orderings: pre-order, in-order, post-order. Core skill: passing state down/up the tree.
- **Triggers:** "Path sum," "validate BST," "tree diameter," "lowest common ancestor," "serialize tree"
- **Complexity:** O(N) time, O(H) space (H = height, worst case O(N))

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Invert Binary Tree | Easy | 226 | [ ] |
| 2 | Maximum Depth of Binary Tree | Easy | 104 | [ ] |
| 3 | Same Tree | Easy | 100 | [ ] |
| 4 | Subtree of Another Tree | Easy | 572 | [ ] |
| 5 | Lowest Common Ancestor of a BST | Medium | 235 | [ ] |
| 6 | Binary Tree Right Side View | Medium | 199 | [ ] |
| 7 | Count Good Nodes in Binary Tree | Medium | 1448 | [ ] |
| 8 | Validate Binary Search Tree | Medium | 98 | [ ] |
| 9 | Kth Smallest Element in a BST | Medium | 230 | [ ] |
| 10 | Construct Binary Tree from Preorder and Inorder Traversal | Medium | 105 | [ ] |

---

#### Pattern 10: Tree — Breadth-First Search (BFS)
- [ ] **Status:** Not started
- **Estimated Time:** 2 days
- **Core Concept:** Level-by-level traversal using a queue. Essential for "level order" problems and shortest path in unweighted graphs.
- **Triggers:** "Level order traversal," "minimum depth," "right side view," "zigzag traversal"
- **Complexity:** O(N) time, O(W) space (W = max width of tree)

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Binary Tree Level Order Traversal | Medium | 102 | [ ] |
| 2 | Average of Levels in Binary Tree | Easy | 637 | [ ] |
| 3 | Minimum Depth of Binary Tree | Easy | 111 | [ ] |
| 4 | Binary Tree Zigzag Level Order Traversal | Medium | 103 | [ ] |
| 5 | Populating Next Right Pointers | Medium | 116 | [ ] |

---

#### Pattern 11: Tries (Prefix Trees)
- [ ] **Status:** Not started
- **Estimated Time:** 1.5 days
- **Core Concept:** Tree-like data structure for efficient prefix-based string operations. Each node represents a character.
- **Triggers:** "Autocomplete," "word search," "prefix matching," "dictionary-based problems"
- **Complexity:** O(L) per operation (L = word length)

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Implement Trie (Prefix Tree) | Medium | 208 | [ ] |
| 2 | Design Add and Search Words | Medium | 211 | [ ] |
| 3 | Word Search II | Hard* | 212 | [ ] |

---

#### Pattern 12: Heap / Priority Queue (Top K Elements)
- [ ] **Status:** Not started
- **Estimated Time:** 2 days
- **Core Concept:** Efficiently track the K largest/smallest elements using a min/max heap. Also used for K-way merge of sorted lists.
- **Triggers:** "Kth largest/smallest," "top K frequent," "merge K sorted lists," "median of stream"
- **Complexity:** O(N log K) time, O(K) space

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Kth Largest Element in a Stream | Easy | 703 | [ ] |
| 2 | Last Stone Weight | Easy | 1046 | [ ] |
| 3 | K Closest Points to Origin | Medium | 973 | [ ] |
| 4 | Task Scheduler | Medium | 621 | [ ] |
| 5 | Design Twitter | Medium | 355 | [ ] |
| 6 | Find Median from Data Stream | Hard* | 295 | [ ] |

---

### 🕸️ PHASE 4: Graph Theory (Patterns 13–15) — *~2 weeks*

---

#### Pattern 13: Graph BFS & DFS
- [ ] **Status:** Not started
- **Estimated Time:** 4 days
- **Core Concept:** Represent problems as nodes + edges. BFS for shortest path (unweighted), DFS for connectivity, cycle detection, topological sort.
- **Triggers:** "Number of islands," "connected components," "shortest path," "course prerequisites," "clone graph"
- **Complexity:** O(V + E) time, O(V) space

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Number of Islands | Medium | 200 | [ ] |
| 2 | Clone Graph | Medium | 133 | [ ] |
| 3 | Pacific Atlantic Water Flow | Medium | 417 | [ ] |
| 4 | Course Schedule | Medium | 207 | [ ] |
| 5 | Course Schedule II | Medium | 210 | [ ] |
| 6 | Rotting Oranges | Medium | 994 | [ ] |
| 7 | Surrounded Regions | Medium | 130 | [ ] |
| 8 | Graph Valid Tree | Medium | 261 | [ ] |

---

#### Pattern 14: Backtracking
- [ ] **Status:** Not started
- **Estimated Time:** 3 days
- **Core Concept:** Systematically explore all candidates and abandon ("backtrack") paths that violate constraints. Template: choose → explore → un-choose.
- **Triggers:** "Generate all permutations/combinations/subsets," "N-Queens," "Sudoku solver," "word search," "partition"
- **Complexity:** O(2^N) or O(N!) depending on problem

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Subsets | Medium | 78 | [ ] |
| 2 | Combination Sum | Medium | 39 | [ ] |
| 3 | Permutations | Medium | 46 | [ ] |
| 4 | Subsets II | Medium | 90 | [ ] |
| 5 | Combination Sum II | Medium | 40 | [ ] |
| 6 | Word Search | Medium | 79 | [ ] |
| 7 | Palindrome Partitioning | Medium | 131 | [ ] |
| 8 | Letter Combinations of a Phone Number | Medium | 17 | [ ] |

---

#### Pattern 15: Advanced Graphs
- [ ] **Status:** Not started
- **Estimated Time:** 3 days
- **Core Concept:** Union-Find (Disjoint Set Union), Dijkstra's algorithm, topological sort (Kahn's algorithm), Minimum Spanning Tree.
- **Triggers:** "Redundant connection," "network delay time," "cheapest flights," "alien dictionary"
- **Complexity:** Varies — Dijkstra O(E log V), Union-Find O(α(N)) per operation

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Redundant Connection | Medium | 684 | [ ] |
| 2 | Number of Connected Components | Medium | 323 | [ ] |
| 3 | Network Delay Time | Medium | 743 | [ ] |
| 4 | Cheapest Flights Within K Stops | Medium | 787 | [ ] |
| 5 | Alien Dictionary | Hard* | 269 | [ ] |
| 6 | Min Cost to Connect All Points | Medium | 1584 | [ ] |

---

### ⚡ PHASE 5: Optimization (Patterns 16–19) — *~2.5 weeks*

---

#### Pattern 16: Greedy Algorithms
- [ ] **Status:** Not started
- **Estimated Time:** 2 days
- **Core Concept:** Make the locally optimal choice at each step, hoping to find the global optimum. Prove greedy works by showing the "exchange argument" or "greedy stays ahead."
- **Triggers:** "Minimum number of X to cover Y," "maximum events to attend," "jump game," "gas station"
- **Complexity:** Usually O(N log N) (sorting) or O(N)

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Maximum Subarray | Medium | 53 | [ ] |
| 2 | Jump Game | Medium | 55 | [ ] |
| 3 | Jump Game II | Medium | 45 | [ ] |
| 4 | Gas Station | Medium | 134 | [ ] |
| 5 | Hand of Straights | Medium | 846 | [ ] |
| 6 | Partition Labels | Medium | 763 | [ ] |

---

#### Pattern 17: 1-D Dynamic Programming
- [ ] **Status:** Not started
- **Estimated Time:** 4 days
- **Core Concept:** Break a problem into overlapping subproblems; store results to avoid recomputation. Start with recursive + memo, then convert to tabulation.
- **Triggers:** "Count ways to reach X," "minimum cost to do Y," "can you partition Z," "longest increasing subsequence"
- **Complexity:** O(N) to O(N²) time, O(N) space

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Climbing Stairs | Easy | 70 | [ ] |
| 2 | Min Cost Climbing Stairs | Easy | 746 | [ ] |
| 3 | House Robber | Medium | 198 | [ ] |
| 4 | House Robber II | Medium | 213 | [ ] |
| 5 | Longest Palindromic Substring | Medium | 5 | [ ] |
| 6 | Palindromic Substrings | Medium | 647 | [ ] |
| 7 | Decode Ways | Medium | 91 | [ ] |
| 8 | Coin Change | Medium | 322 | [ ] |
| 9 | Maximum Product Subarray | Medium | 152 | [ ] |
| 10 | Word Break | Medium | 139 | [ ] |
| 11 | Longest Increasing Subsequence | Medium | 300 | [ ] |

---

#### Pattern 18: 2-D Dynamic Programming
- [ ] **Status:** Not started
- **Estimated Time:** 3 days
- **Core Concept:** DP on grids or when state depends on two changing dimensions (e.g., two string indices). Common: `dp[i][j]` represents answer for prefix `s[0..i]` and `t[0..j]`.
- **Triggers:** "Unique paths in grid," "edit distance," "longest common subsequence," "interleaving strings"
- **Complexity:** O(N × M) time and space

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Unique Paths | Medium | 62 | [ ] |
| 2 | Longest Common Subsequence | Medium | 1143 | [ ] |
| 3 | Best Time to Buy and Sell Stock with Cooldown | Medium | 309 | [ ] |
| 4 | Coin Change II | Medium | 518 | [ ] |
| 5 | Target Sum | Medium | 494 | [ ] |
| 6 | Interleaving String | Medium | 97 | [ ] |
| 7 | Edit Distance | Medium | 72 | [ ] |

---

#### Pattern 19: Knapsack & Sequence DP (Deep Dive)
- [ ] **Status:** Not started
- **Estimated Time:** 3 days
- **Core Concept:** Specialized DP families: 0/1 Knapsack (choose or skip each item), Unbounded Knapsack (unlimited copies), Palindromic Subsequence, State Machine DP (buy/sell stocks).
- **Triggers:** "Subset sum," "partition into equal halves," "coin change (unlimited)," "buy and sell stock with constraints"
- **Complexity:** O(N × W) for knapsack, O(N²) for LCS/palindromes

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Partition Equal Subset Sum | Medium | 416 | [ ] |
| 2 | Last Stone Weight II | Medium | 1049 | [ ] |
| 3 | Ones and Zeroes | Medium | 474 | [ ] |
| 4 | Best Time to Buy and Sell Stock with Transaction Fee | Medium | 714 | [ ] |
| 5 | Longest Palindromic Subsequence | Medium | 516 | [ ] |

---

### 🧩 PHASE 6: Specialized Patterns (Pattern 20) — *~1 week*

---

#### Pattern 20: Bit Manipulation, Math & Geometry, Cyclic Sort
- [ ] **Status:** Not started
- **Estimated Time:** 3 days
- **Core Concept:** XOR for finding missing/duplicate numbers, bit shifting for multiplication/division, modular arithmetic. Cyclic sort places each number at its "correct" index.
- **Triggers:** "Find the missing number," "single number," "power of two," "counting bits," "numbers in range [1, N]"
- **Complexity:** O(N) time, O(1) space (typically)

| # | Problem | Difficulty | LeetCode # | Status |
|---|---------|-----------|------------|--------|
| 1 | Single Number | Easy | 136 | [ ] |
| 2 | Number of 1 Bits | Easy | 191 | [ ] |
| 3 | Missing Number | Easy | 268 | [ ] |
| 4 | Counting Bits | Easy | 338 | [ ] |
| 5 | Reverse Bits | Easy | 190 | [ ] |
| 6 | Sum of Two Integers | Medium | 371 | [ ] |
| 7 | Rotate Image | Medium | 48 | [ ] |
| 8 | Spiral Matrix | Medium | 54 | [ ] |
| 9 | Set Matrix Zeroes | Medium | 73 | [ ] |
| 10 | Find All Numbers Disappeared in an Array | Easy | 448 | [ ] |
| 11 | Find All Duplicates in an Array | Medium | 442 | [ ] |

---

## 🧠 Mental Models for Interview Performance

### 1. Reverse Thinking
When stuck going forward from input → output, flip it. Start from the desired output and work backward asking: *"What must be true immediately before this final state?"*

### 2. Constraint-First Analysis
Always read constraints **before** thinking about algorithms. The input size `N` narrows down viable approaches instantly (see Constraint Analysis table above).

### 3. Externalize Everything
Write down: inputs, outputs, edge cases, examples. Drawing the problem **prevents** the "blank stare" paralysis.

### 4. The "Dumb Solution First" Rule
Always articulate the brute force O(N²) or O(2^N) solution first. Then ask: *"What repeated work can I eliminate?"* This naturally leads to the optimized pattern.

### 5. Recursion Tree Visualization
For any recursive/DP problem, draw 3–4 levels of the recursion tree. This reveals:
- Overlapping subproblems → memoization
- Independent subproblems → divide & conquer
- Pruning opportunities → backtracking

### 6. State Machine Thinking
For problems with rules about transitions (stock trading, state changes), model as a finite state machine. Define states, transitions, and the DP table tracks the best value at each state.

---

## 📈 Progress Summary

| Phase | Patterns | Easy Problems | Medium Problems | Hard Problems | Status |
|-------|----------|--------------|----------------|--------------|--------|
| Foundation | 5 | 14 | 22 | 2 | [ ] |
| Linear Structures | 3 | 6 | 14 | 0 | [ ] |
| Hierarchical | 4 | 9 | 16 | 2 | [ ] |
| Graph Theory | 3 | 0 | 22 | 1 | [ ] |
| Optimization | 4 | 3 | 28 | 0 | [ ] |
| Specialized | 1 | 6 | 5 | 0 | [ ] |
| **TOTAL** | **20** | **38** | **107** | **5** | **[ ]** |

> **Total: ~150 problems** covering 20 patterns. This aligns with NeetCode 150's proven scope.  
> Hard problems (marked with *) are **strictly deferred** until all Medium problems in that pattern are mastered.

---

## 📅 Weekly Schedule Template

| Day | Activity | Duration |
|-----|----------|----------|
| Mon–Fri | Pattern theory (20 min) + Problem solving (60–80 min) | ~1.5–2 hrs |
| Sat | Review weak areas, re-attempt failed problems | ~1.5 hrs |
| Sun | Rest or light review of upcoming pattern | Optional |
