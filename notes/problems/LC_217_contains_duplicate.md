# LC 217: Contains Duplicate
- **Difficulty:** Easy
- **Pattern:** Arrays & Hashing
- **Date Discussed:** 2026-08-14
- **Solved Independently:** Yes (Guided conceptually)

## Problem Statement
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

### Examples
- **Input:** `nums = [1, 2, 3, 1]` $\rightarrow$ **Output:** `true`
- **Input:** `nums = [1, 2, 3, 4]` $\rightarrow$ **Output:** `false`

## Approach & Thought Process
1. **Initial Observation:** We need to track elements we've seen so far.
2. **Pattern Identified:** Arrays & Hashing. A hash structure gives us $O(1)$ lookups to check if an element was already encountered.
3. **Optimized Approach:** Iterate through the array. Use a **Hash Set** (instead of a Hash Map) because we only care about the *existence* of a value, not mapping it to an index or frequency.
4. Check if the current number is in the set. If yes, return `True`. If no, add it to the set and continue.

## Solution Code
```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

## Complexity Analysis
- **Time:** $O(N)$ — We loop through the array of size $N$ exactly once. Checking `if num in seen` takes $O(1)$ time on average.
- **Space:** $O(N)$ — In the worst-case scenario (all numbers are unique), our hash set will store all $N$ elements.

## Edge Cases
- **Single element array (`[1]`):** The loop runs once, adds the element to the set, finishes, and returns `False`. Handled perfectly.
- **Empty array (`[]`):** Loop doesn't run, returns `False`.

## Variations & Follow-ups
- **Follow-up:** "What if you can't use extra memory?" 
  - **Answer:** Sort the array first ($O(N \log N)$ time), then do a linear scan checking if `nums[i] == nums[i-1]` ($O(1)$ space).

## "If I See This Again" (Quick Revision)
> Use a Hash Set to track seen numbers in a single pass. Early return `True` on the first collision to optimize time.
