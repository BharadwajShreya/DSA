# LC 560: Subarray Sum Equals K
- **Difficulty:** Medium
- **Pattern:** Prefix Sum + Hash Map
- **Date Discussed:** 2026-09-05
- **Solved Independently:** Yes (with feedback on tracking frequencies)

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

### Examples
- **Input:** `nums = [1, 1, 1], k = 2` $\rightarrow$ **Output:** `2`
- **Input:** `nums = [1, 2, 3], k = 3` $\rightarrow$ **Output:** `2`
- **Input:** `nums = [0, 0, 0], k = 0` $\rightarrow$ **Output:** `6`

## Approach & Thought Process
1. **Why not Sliding Window?** The array can contain negative numbers and zeroes. Expanding the window doesn't guarantee the sum strictly increases, making the sliding window condition impossible to maintain.
2. **The Equation:** If we are currently at `current_sum`, and we want a subarray that sums to `k`, we need to find an old prefix sum equal to `current_sum - k`. If we chop off that old prefix, the remaining subarray equals `k`.
3. **Data Structure:** We use a Hash Map to track the frequencies of every prefix sum we've seen so far.
4. **Why Frequencies?** If `current_sum - k` has occurred 3 times in the past (e.g., due to zeroes or negative numbers), it means there are 3 distinct valid subarrays ending at the current index. We must add the *frequency*, not just `1`.

## Solution Code
```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary stores: {prefix_sum: frequency}
        # Base case: A prefix sum of 0 has occurred exactly 1 time before the array starts
        prefix_dict = {0: 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            
            # If we've seen (current_sum - k) before, we found valid subarrays!
            if (current_sum - k) in prefix_dict:
                count += prefix_dict[current_sum - k]
                
            # Add the current_sum to our dictionary for future elements
            if current_sum in prefix_dict:
                prefix_dict[current_sum] += 1
            else:
                prefix_dict[current_sum] = 1

        return count
```

## Complexity Analysis
- **Time:** $O(N)$ — We loop through the array exactly once. Hash map lookups and insertions are $O(1)$.
- **Space:** $O(N)$ — In the worst-case scenario (all positive numbers), every prefix sum is unique, so the hash map will store $N$ distinct entries.

## Edge Cases
- **Negative numbers & Zeroes:** Handled flawlessly by the frequency counter.
- **Array size 1:** Handled perfectly, assuming `prefix_dict` is initialized with `{0: 1}`.

## "If I See This Again" (Quick Revision)
> **Target Sums = Prefix Sum + Hash Map.** Equation: `Target = Current - Old`. Keep a dictionary of `{prefix_sum : frequency}` starting with `{0:1}`. For each num, add `dict[current - k]` to your total count, then increment `dict[current]`.
