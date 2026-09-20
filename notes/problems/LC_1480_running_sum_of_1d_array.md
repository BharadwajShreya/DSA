# LC 1480: Running Sum of 1d Array
- **Difficulty:** Easy
- **Pattern:** Prefix Sum
- **Date Discussed:** 2026-09-01
- **Solved Independently:** Walkthrough / Guided

## Problem Statement
Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]...nums[i])`. Return the running sum of `nums`.

### Examples
- **Input:** `nums = [1, 2, 3, 4]`
- **Output:** `[1, 3, 6, 10]`

## Approach & Thought Process
1. **Initial Observation:** We are literally being asked to build a prefix sum array.
2. **Space Optimization:** Creating a new array `res` of size $N$ takes $O(N)$ extra space. However, we can simply overwrite the input array `nums` in-place by adding the previous element's value to the current element.
3. **Algorithm:** Loop from index 1 to $N-1$, executing `nums[i] += nums[i-1]`.

## Solution Code
```python
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Start at index 1 to avoid checking i-1 on index 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        return nums
```

## Complexity Analysis
- **Time:** $O(N)$ — We iterate through the array of size $N$ exactly once.
- **Space:** $O(1)$ — We are modifying the input array in-place, so no auxiliary data structures are used.

## Edge Cases
- **Array of size 1 (`[5]`):** The `range(1, 1)` loop will not execute, and it simply returns `[5]`. Handled correctly.

## "If I See This Again" (Quick Revision)
> Iterate from index 1. Overwrite the array in-place: `nums[i] += nums[i-1]`.
