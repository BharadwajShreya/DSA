# Pattern 02: Two Pointers

## What Is It?
The Two Pointers technique involves using two integer variables (pointers) to traverse a data structure (usually an array or string) simultaneously. 

There are two primary variations:
1. **Opposite Ends (Collision):** One pointer starts at the beginning (`0`), the other at the end (`length - 1`). They move toward each other until they meet.
2. **Same Direction (Slow/Fast):** Both pointers start at the beginning but move at different speeds (e.g., fast pointer moves 2 steps, slow pointer moves 1 step).

## When To Use It (Trigger Table)
| Trigger Signal | Example Problem | Why This Pattern |
|---------------|----------------|------------------|
| "The input array is SORTED and you need a pair" | Two Sum II | Move pointers inward based on whether the current sum is too large or too small |
| "Check if a string is a Palindrome" | Valid Palindrome | Compare characters at `left` and `right`, move inward |
| "Remove duplicates IN-PLACE" | Remove Duplicates from Sorted Array | Use a slow pointer to track the unique elements and a fast pointer to scan |
| "Find maximum area / container" | Container With Most Water | Pointers at ends, always move the pointer with the smaller bottleneck |

## Boilerplate Template

### Opposite Ends (Collision)
```python
def two_pointers_opposite(arr: list[int]) -> bool:
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # 1. Check condition
        # if arr[left] + arr[right] == target:
        #     return True
        
        # 2. Decide which pointer to move
        if condition_to_move_left:
            left += 1
        else:
            right -= 1
            
    return False
```

## Time & Space Complexity
- **Time:** $O(N)$ — In most cases, each element is visited at most once as the pointers sweep across the array.
- **Space:** $O(1)$ — We are only storing two integer variables (the indices), meaning no extra memory is needed regardless of array size.

## Common Pitfalls
- **Index Out of Bounds:** Forgetting to subtract 1 when initializing the right pointer (`right = len(arr) - 1`).
- **While Loop Condition:** Using `while left <= right` when you shouldn't, or `while left < right` when you actually need to check the middle element. Always think about what happens when they cross.
- **Infinite Loops:** Forgetting to increment `left` or decrement `right` inside the while loop.

## Related Patterns
- **Prerequisites for:** Sliding Window (which is essentially a specific application of two pointers moving in the same direction).
- **Alternative to:** Hashing. If an array is already sorted, Two Pointers gives you $O(N)$ time with $O(1)$ space, whereas Hashing gives you $O(N)$ time but uses $O(N)$ extra space!

## Key Takeaways
- The Two Pointers pattern is fundamentally a **space optimization** technique (getting $O(1)$ space) or a way to take advantage of sorted data to avoid $O(N^2)$ brute force loops.
