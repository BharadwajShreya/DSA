# LC 121: Best Time to Buy and Sell Stock
- **Difficulty:** Easy
- **Pattern:** Sliding Window / Two Pointers
- **Date Discussed:** 2026-08-20
- **Solved Independently:** Walkthrough / Guided

## Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{th}$ day. You want to maximize your profit by choosing a single day to buy and a different day in the future to sell. Return the maximum profit.

### Examples
- **Input:** `prices = [7, 1, 5, 3, 6, 4]` $\rightarrow$ **Output:** `5` (Buy at 1, sell at 6)
- **Input:** `prices = [7, 6, 4, 3, 1]` $\rightarrow$ **Output:** `0` (No profit possible)

## Approach & Thought Process
1. **Initial Observation:** We must buy before we sell, so order matters. We want to find the maximum difference `prices[sell] - prices[buy]`.
2. **Pattern Identified:** Sliding Window (Dynamic). `left` is the buy day, `right` is the sell day.
3. **Condition to Shrink/Move:** If we ever find a day where the stock is cheaper than our current buy day (`prices[left] > prices[right]`), that new day is strictly better for buying. So we jump our `left` pointer all the way to `right`.

## Solution Code
```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # Buy
        right = 1 # Sell
        max_profit = 0

        while right < len(prices):
            # Is this a profitable transaction?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # We found a completely new low point, shift our buy day here!
                left = right
            
            # Time marches forward, check the next day to sell
            right += 1

        return max_profit
```

## Complexity Analysis
- **Time:** $O(N)$ — We traverse the `prices` array exactly once with the `right` pointer.
- **Space:** $O(1)$ — Only tracking `left`, `right`, and `max_profit`.

## Edge Cases
- **Descending Array (`[7, 6, 4, 3, 1]`):** `prices[left] < prices[right]` is never true. `max_profit` remains 0. `left` shifts every day. Correct behavior.

## "If I See This Again" (Quick Revision)
> `left` = buy, `right` = sell. Slide `right` across the array. If `prices[left] > prices[right]`, we found a new absolute low, so jump `left` to `right`. Otherwise, calculate `profit` and update `max_profit`.
