# LC 11: Container With Most Water
- **Difficulty:** Medium
- **Pattern:** Two Pointers
- **Date Discussed:** 2026-08-18
- **Solved Independently:** Yes 

## Problem Statement
You are given an integer array `height` of length $N$. There are $N$ vertical lines drawn such that the two endpoints of the $i^{th}$ line are $(i, 0)$ and $(i, \text{height}[i])$. Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the *maximum amount of water a container can store*.

### Examples
- **Input:** `height = [1,8,6,2,5,4,8,3,7]` $\rightarrow$ **Output:** `49`
- **Input:** `height = [1,1]` $\rightarrow$ **Output:** `1`

## Approach & Thought Process
1. **Initial Observation:** Area is determined by `width * height`. Width is the distance between the two lines (`right - left`). Height is limited by the shorter of the two lines: `min(height[left], height[right])`.
2. **Pattern Identified:** Two Pointers. We want to maximize the area, so it makes sense to start with the maximum possible width (pointers at the opposite ends of the array).
3. **Optimized Approach (The "Bottleneck" Logic):** 
   - Start with `left = 0` and `right = len(height) - 1`.
   - Calculate the area and update `max_area`.
   - To find a potentially larger area, we *must* move the pointer pointing to the shorter line. Moving the taller line inward would only decrease the width without increasing the bottleneck height, guaranteeing a smaller or equal area.
   - If `height[left] < height[right]`, increment `left`. Otherwise, decrement `right`.

## Solution Code
```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

## Complexity Analysis
- **Time:** $O(N)$ — The pointers start at the ends and move inward until they meet. We process each element at most once.
- **Space:** $O(1)$ — Only three integer variables (`max_area`, `left`, `right`) are used, so space remains constant regardless of the input size.

## Edge Cases
- **Array with only two lines (`[1, 1]`):** The loop runs exactly once, calculates area of 1, and exits. Handled perfectly.

## Variations & Follow-ups
- **Follow-up:** "What if we had to return the actual lines (indices) instead of the max area?" 
  - **Answer:** We would simply track `best_left` and `best_right` variables and update them whenever we find a new `max_area`.

## "If I See This Again" (Quick Revision)
> Pointers at opposite ends (max width). Area = `min(height[left], height[right]) * width`. Always move the pointer that points to the shorter line inward, as it is the limiting factor.
