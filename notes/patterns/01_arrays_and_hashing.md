# Pattern 01: Arrays & Hashing

## What Is It?
- **Arrays** store elements in contiguous memory blocks. Accessing an element by index takes $O(1)$ time, but searching for a value takes $O(N)$ time. Dynamic arrays (like Python lists) resize automatically under the hood when they run out of space.
- **Hash Tables (Hash Maps / Hash Sets)** use a mathematical hash function to convert a key into an array index. This allows for $O(1)$ average-time insertions, deletions, and lookups. 

### Real-world Analogy
An array is like searching every shelf in a library sequentially ($O(N)$). A hash map is like typing a book title into the library's computer system, which instantly outputs the exact aisle and shelf number ($O(1)$).

## When To Use It (Trigger Table)
| Trigger Signal | Example Problem | Why This Pattern |
|---------------|----------------|------------------|
| "Find if target value / pair exists in unsorted array" | Two Sum | Store complement `target - num` in hash map for $O(1)$ lookup instead of $O(N^2)$ nested loop |
| "Check for duplicates or count frequencies" | Contains Duplicate, Valid Anagram | Use Hash Set for uniqueness or Hash Map for frequency counting |
| "Group items by a shared property / signature" | Group Anagrams | Compute a canonical key (e.g., sorted string) as hash map key |

## Boilerplate Template

### Target Complement Lookup (e.g., Two Sum)
```python
def target_lookup_pattern(nums: list[int], target: int) -> bool:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num 
        if complement in seen:
            return True
        seen[num] = i
    return False
```

### Grouping Pattern (e.g., Anagrams)
```python
from collections import defaultdict

def grouping_pattern(strings: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strings:
        signature = "".join(sorted(s))
        groups[signature].append(s)
    return list(groups.values())
```

## Time & Space Complexity
- **Time:** $O(N)$ for traversing arrays, $O(1)$ for Hash Map lookups/inserts.
- **Space:** $O(N)$ for creating the Hash Map/Set to store values.

## Common Pitfalls
- **Mutable Keys:** In Python, lists or dictionaries cannot be used as dictionary keys because they are mutable. Use tuples or strings instead.
- **Hash Collisions:** While handled automatically, extreme collisions can degrade $O(1)$ lookup to $O(N)$.

## Related Patterns
- **Prerequisites for:** Sliding Window (using a map for frequencies), Graph Traversal (using a `visited` set).
- **Alternative to:** Sorting. You often trade space ($O(N)$ extra memory for a hash map) to save time ($O(N)$ instead of $O(N \log N)$ sorting).

## Key Takeaways
- Hash structures are your primary weapon for turning $O(N^2)$ nested loops into $O(N)$ single passes.
- Always ask yourself: "Is it worth using $O(N)$ extra memory to make my algorithm faster?"
