# Pattern 04: Prefix Sum

## What Is It?
Prefix Sum is an array (or list) where each element at index `i` represents the cumulative sum of all elements from the start of the original array up to index `i`. 
By pre-calculating this, you can answer questions about the sum of any continuous range in $O(1)$ time, turning $O(N)$ scanning operations into instant math.

Formula for the sum between index `L` and `R`:
`Sum(L, R) = Prefix[R] - Prefix[L-1]`

## When To Use It (Trigger Table)
| Trigger Signal | Example Problem | Why This Pattern |
|---------------|----------------|------------------|
| "Range sum queries" | Range Sum Query - Immutable | Calculate sum of `arr[i...j]` in $O(1)$ time after an $O(N)$ setup |
| "Subarrays that sum to exactly K" | Subarray Sum Equals K | Use a Hash Map to track frequencies of prefix sums seen so far |
| "Equilibrium Index" / "Pivot Index" | Find Pivot Index | `Total Sum - Left Sum - Current = Right Sum` |

## Boilerplate Template

### Pure Prefix Sum (For Range Queries)
```python
def range_queries(arr: list[int], queries: list[list[int]]) -> list[int]:
    # It's highly recommended to pad the prefix array with a leading 0
    # to avoid out-of-bounds errors when querying from index 0.
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
        
    results = []
    for L, R in queries:
        results.append(prefix[R + 1] - prefix[L])
    return results
```

### Prefix Sum + Hash Map (Target Sums)
```python
def subarray_sum_count(arr: list[int], k: int) -> int:
    prefix_counts = {0: 1} # Initialize to handle subarrays starting at index 0
    current_sum = 0
    count = 0
    
    for num in arr:
        current_sum += num
        # If we've seen (current - target) before, that means the subarray 
        # between that past index and our current index equals target!
        if (current_sum - k) in prefix_counts:
            count += prefix_counts[current_sum - k]
            
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
        
    return count
```

> **Why track frequencies (`count += prefix_counts[...]`) instead of just `True`/`False`?**
> If an array has zeroes or negative numbers (like `[0, 0, 0]`), a prefix sum can occur multiple times at different indices. If `current_sum - k` has happened 3 times in the past, it means there are 3 *different* valid starting indices for your subarray! You must add the *frequency* of that past sum to capture all possible subarrays.

## Time & Space Complexity
- **Time:** $O(N)$ to build the prefix sum array. After that, range queries are $O(1)$.
- **Space:** $O(N)$ to store the new array or Hash Map. (Can be $O(1)$ if you are allowed to modify the input array in-place).

## Common Pitfalls
- **Negative Numbers:** Sliding Window does NOT work if the array contains negative numbers (because expanding the window might decrease the sum). Prefix Sum + Hash Map works flawlessly with negative numbers!
- **Index Out of Bounds:** When calculating `prefix[R] - prefix[L-1]`, if `L` is `0`, `L-1` is `-1`. Adding a leading `0` to the prefix array avoids this annoying edge case.

## Key Takeaways
- Prefix Sum is your go-to pattern whenever a problem asks about the sum (or product) of a continuous range (subarray). 
- If a problem asks "how many subarrays sum to K?" immediately use Prefix Sum + Hash Map.

---

## 🎨 Visualizing Prefix Sums: The "Chop Off" Analogy

The absolute best way to understand Prefix Sum target searching is to stop thinking about numbers, and start thinking about **lengths of string**.

Imagine you are unrolling a ball of string.
- The `Current_Prefix_Sum` is the **total length** of string you have unrolled so far.
- `K` is the exact length of string you want to cut off from the end.

### The Core Question
If you have unrolled **10 inches** of string, and you want to cut off exactly **7 inches** from the end... how much string do you need to "chop off" and throw away from the beginning?
You need to chop off **3 inches**! (Because `10 - 7 = 3`).

### Step-by-step Visualization

**Target `K = 7`**  
**Array:** `[3, 4, 2, -2, 3]`

#### 1. Index 0 (Value = 3)
```text
Total Unrolled (Prefix Sum): 3

[ 3 ]
```
- We want 7. We only have 3. 
- *Hash Map remembers: We had a length of 3 at Index 0.*

#### 2. Index 1 (Value = 4)
```text
Total Unrolled (Prefix Sum): 7

[ 3 ] [ 4 ]
|---- 7 ----|
```
- We want 7. We have exactly 7! 
- *Hash Map remembers: We had a length of 7 at Index 1.*

#### 3. Index 2 (Value = 2)
```text
Total Unrolled (Prefix Sum): 9

[ 3 ] [ 4 ] [ 2 ]
|------- 9 -------|
```
- We want a chunk of 7 at the end. 
- To get 7 from 9, we need to chop off 2 from the beginning (`9 - 7 = 2`).
- Do we have a prefix of exactly 2 that we can chop off? No.
- *Hash Map remembers: We had a length of 9 at Index 2.*

#### 4. Index 3 (Value = -2)
```text
Total Unrolled (Prefix Sum): 7

[ 3 ] [ 4 ] [ 2 ] [-2 ]
|--------- 7 ---------|
```
- We want 7. We have exactly 7 again!
- *Hash Map remembers: We had a length of 7 at Index 3.*

#### 5. Index 4 (Value = 3)
```text
Total Unrolled (Prefix Sum): 10

[ 3 ] [ 4 ] [ 2 ] [-2 ] [ 3 ]
|------------ 10 ------------|
```
- We want a chunk of 7 at the end. 
- To get 7 from a total of 10, we must chop off exactly **3** from the beginning (`10 - 7 = 3`).
- We ask the Hash Map: *"Did we ever have a length of exactly 3 that we can chop off?"*
- Hash Map says: *"YES! At Index 0, the length was 3!"*

Look what happens if we take the total length of 10, and visually "chop off" that initial chunk of 3:

```text
Chop this off! | Keep this! (This is our subarray!)
[ 3 ]          | [ 4 ] [ 2 ] [-2 ] [ 3 ]
-- 3 --        | --------- 7 -----------
```
By chopping off the old prefix sum of 3, the remaining subarray **must** perfectly equal 7. 

**This is why `Current_Sum - K = Old_Prefix_Sum`.**
We are just asking the Hash Map if a "choppable" prefix exists so that the remainder perfectly matches `K`!
