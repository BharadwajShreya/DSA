# Pattern 03: Sliding Window

## What Is It?
The Sliding Window pattern is an extension of the Two Pointers technique. It uses two pointers (`left` and `right`) to create a "window" that evaluates a contiguous subarray or substring. 

Instead of re-evaluating the entire window from scratch on every step ($O(N^2)$), you simply subtract the element that is falling out of the window and add the element that is entering the window. This reduces the time complexity to $O(N)$.

There are two types:
1. **Fixed Window:** The distance between `left` and `right` stays constant. The whole window just shifts one step at a time.
2. **Dynamic Window:** The `right` pointer expands to add new elements, and the `left` pointer shrinks the window when a specific condition is violated.

## When To Use It (Trigger Table)
| Trigger Signal | Example Problem | Why This Pattern |
|---------------|----------------|------------------|
| "Find maximum/minimum contiguous subarray" | Best Time to Buy/Sell Stock | Moving `left` to the lowest price seen so far as `right` explores future prices |
| "Longest substring without repeating characters" | Longest Substring | Expand `right` until a duplicate is found, then shrink `left` until it's removed |
| "Smallest subarray with sum >= target" | Minimum Size Subarray Sum | Expand `right` until sum is large enough, then shrink `left` to find the smallest length |

## Boilerplate Template (Dynamic Window)

```python
def dynamic_sliding_window(arr: list[int]) -> int:
    left = 0
    max_result = 0 
    
    for right in range(len(arr)):
        # 1. Add arr[right] to window state
        
        # 2. While window violates the condition, shrink it
        while window_is_invalid():
            # Remove arr[left] from window state
            left += 1
            
        # 3. Update the best result seen so far
        # max_result = max(max_result, right - left + 1)
        
    return max_result
```

## Time & Space Complexity
- **Time:** $O(N)$ — Both `left` and `right` pointers only ever move forward. Each element is processed at most twice (once added by `right`, once removed by `left`).
- **Space:** $O(1)$ (if just tracking sums/lengths) or $O(K)$ (if tracking frequencies in a map, where $K$ is the character set size).

## Common Pitfalls
- **While vs If:** In dynamic windows, always use a `while` loop for shrinking the `left` side, because a single move of `right` might require `left` to shrink multiple times to restore validity.
- **Updating Result:** Be careful about *when* you update your `max_result` or `min_result`. Usually, you update it right *after* the `while` loop makes the window valid again.

## Key Takeaways
- If the problem says **"Contiguous"**, **"Subarray"**, or **"Substring"**, your brain should immediately yell "Sliding Window!"
