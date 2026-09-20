# 📓 Session Log

> Track all study sessions here. Append after every session.

---

<!-- 
### Session [N] — [YYYY-MM-DD]
- **Pattern:** [Pattern Name]
- **Step Completed:** A / B / C / D
- **Problems Attempted:** [List with LC numbers]
- **Problems Solved Independently:** [List]
- **Hints Used:** [Tier levels for each problem]
- **Key Takeaway:** [One sentence]
- **Weak Area to Revisit:** [If any]
- **Notes Generated:** [Links to pattern/problem notes created]
-->

### Session 1 — 2026-08-14 to 2026-08-17
- **Pattern:** Arrays & Hashing
- **Step Completed:** A (Theory), B (Boilerplate), C (Walkthrough), D (Medium Practice)
- **Problems Attempted:** LC 217 (Contains Duplicate), LC 49 (Group Anagrams)
- **Problems Solved Independently:** LC 217 (Conceptually), LC 49 (with Tier 2 hint)
- **Hints Used:** LC 49 (Tier 2 - Python dictionary/string syntax optimizations)
- **Key Takeaway:** Arrays use contiguous memory for $O(1)$ indexing. Hash Maps use math (hash functions) to achieve $O(1)$ value lookups, trading $O(N)$ space for speed. For anagrams, using a sorted string as a dictionary key is the canonical grouping approach.
- **Notes Generated:** [Pattern 01 Note](file:///d:/sourav/code/DSA/notes/patterns/01_arrays_and_hashing.md), [LC 217 Note](file:///d:/sourav/code/DSA/notes/problems/LC_217_contains_duplicate.md), [LC 49 Note](file:///d:/sourav/code/DSA/notes/problems/LC_049_group_anagrams.md)

### Session 2 — 2026-08-18
- **Pattern:** Two Pointers
- **Step Completed:** A (Theory), D (Medium Practice)
- **Problems Attempted:** LC 11 (Container With Most Water)
- **Problems Solved Independently:** LC 11 (Completely independent)
- **Hints Used:** None
- **Key Takeaway:** For two pointers acting on area/containers, always move the pointer pointing to the shorter line because the shorter line acts as the bottleneck. Moving the taller line is guaranteed to result in a smaller or equal area.
- **Notes Generated:** [Pattern 02 Note](file:///d:/sourav/code/DSA/notes/patterns/02_two_pointers.md), [LC 11 Note](file:///d:/sourav/code/DSA/notes/problems/LC_011_container_with_most_water.md)

### Session 3 — 2026-08-20
- **Pattern:** Sliding Window
- **Step Completed:** A (Theory), B (Boilerplate), C (Walkthrough), D (Medium Practice)
- **Problems Attempted:** LC 121 (Best Time to Buy and Sell Stock), LC 3 (Longest Substring Without Repeating Characters)
- **Problems Solved Independently:** LC 121 (Conceptually), LC 3 (Independently, optimized with minor feedback)
- **Hints Used:** LC 3 (Tier 1 - Time complexity check / string slicing)
- **Key Takeaway:** In a dynamic sliding window, use a `set` to achieve $O(1)$ lookups. The `right` pointer aggressively explores, and the `left` pointer defensively shrinks the window inside a `while` loop whenever a duplicate is found.
- **Notes Generated:** [Pattern 03 Note](file:///d:/sourav/code/DSA/notes/patterns/03_sliding_window.md), [LC 121 Note](file:///d:/sourav/code/DSA/notes/problems/LC_121_best_time_to_buy_and_sell_stock.md), [LC 3 Note](file:///d:/sourav/code/DSA/notes/problems/LC_003_longest_substring_without_repeating_characters.md)

### Session 4 — 2026-09-01
- **Pattern:** Prefix Sum
- **Step Completed:** A (Theory), B (Boilerplate), C (Walkthrough), D (Medium Practice)
- **Problems Attempted:** LC 1480 (Running Sum of 1d Array), LC 560 (Subarray Sum Equals K)
- **Problems Solved Independently:** LC 1480 (Conceptually), LC 560 (Independently, with feedback on frequency tracking)
- **Hints Used:** LC 560 (Tier 1 - Frequency logic bug with `[0, 0, 0]`)
- **Key Takeaway:** Prefix sums allow $O(1)$ range queries. For "Target Sum" problems, track the *frequency* of past prefix sums in a Hash Map so you can count all valid starting points.
- **Notes Generated:** [Pattern 04 Note](file:///d:/sourav/code/DSA/notes/patterns/04_prefix_sum.md), [LC 1480 Note](file:///d:/sourav/code/DSA/notes/problems/LC_1480_running_sum_of_1d_array.md), [LC 560 Note](file:///d:/sourav/code/DSA/notes/problems/LC_0560_subarray_sum_equals_k.md)
