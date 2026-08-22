# LC 3: Longest Substring Without Repeating Characters
- **Difficulty:** Medium
- **Pattern:** Sliding Window (Dynamic)
- **Date Discussed:** 2026-08-20
- **Solved Independently:** Yes (with minor feedback on time complexity)

## Problem Statement
Given a string `s`, find the length of the **longest substring** without repeating characters.

### Examples
- **Input:** `s = "abcabcbb"` $\rightarrow$ **Output:** `3` ("abc")
- **Input:** `s = "bbbbb"` $\rightarrow$ **Output:** `1` ("b")
- **Input:** `s = "pwwkew"` $\rightarrow$ **Output:** `3` ("wke")

## Approach & Thought Process
1. **Initial Observation:** We need a contiguous block (substring), making it a perfect fit for a Sliding Window.
2. **Data Structure:** We need to know if a character is a duplicate instantly. A `set` provides $O(1)$ lookups.
3. **Dynamic Window Logic:**
   - Expand `right` and add characters to the set.
   - If `s[right]` is already in the set, the window is invalid.
   - Shrink the window from the `left` (removing characters from the set) until `s[right]` is no longer a duplicate.
   - Once valid again, calculate the max length.

## Solution Code
*(Cleanest Boilerplate version using a for-loop)*
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # Shrink until valid
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Now it's valid to add the new character
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
```

## Complexity Analysis
- **Time:** $O(N)$ — The `right` pointer moves forward $N$ times. The `left` pointer can only move forward a maximum of $N$ times over the entire life of the algorithm. Lookups and removals in the set are $O(1)$. Total time is bounded by $2N$, which simplifies to $O(N)$.
- **Space:** $O(K)$ — Where $K$ is the number of unique characters in the string (bounded by the alphabet size, e.g., 26 for English letters or 128 for ASCII). This can also be stated as $O(1)$ if the character set is strictly fixed.

## Edge Cases
- **Empty String (`""`):** Handled gracefully. Loop never runs, returns 0.
- **String with all identical characters (`"bbbbb"`):** `left` constantly chases `right`, keeping max length at 1.

## "If I See This Again" (Quick Revision)
> Sliding Window with a Set. `for right in range(len(s)):` -> `while s[right] in char_set: remove left, left += 1` -> `add right` -> `update max_length`.
