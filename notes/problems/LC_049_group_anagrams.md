# LC 49: Group Anagrams
- **Difficulty:** Medium
- **Pattern:** Arrays & Hashing
- **Date Discussed:** 2026-08-17
- **Solved Independently:** Yes (with minor Tier 2 hint on Python syntax)

## Problem Statement
Given an array of strings `strs`, group the **anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Examples
- **Input:** `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- **Output:** `[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]`

## Approach & Thought Process
1. **Initial Observation:** We need a way to group words that have the exact same character frequencies.
2. **Pattern Identified:** Arrays & Hashing (Grouping by Canonical Key).
3. **The Key:** We can use the sorted version of the string as the dictionary key. For example, `"eat"`, `"tea"`, and `"ate"` all sort to `"aet"`.
4. **Data Structure:** We use a `defaultdict(list)` to automatically handle creating a new list for new keys.

## Solution Code
```python
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs: 
            # Canonical key: the sorted string
            sorted_string = "".join(sorted(word))
            anagrams[sorted_string].append(word)

        return list(anagrams.values())
```

## Complexity Analysis
- **Time:** $O(N \times M \log M)$ — Where $N$ is the number of strings, and $M$ is the maximum length of a string. We loop $N$ times, and inside the loop, we sort a string of length $M$, taking $O(M \log M)$ time.
- **Space:** $O(N \times M)$ — To store all the strings in the hash map. (Note: Big-O drops constants, so $O(3N)$ is formally written as $O(N)$, but string length $M$ matters here).

## Edge Cases
- **Empty strings:** Handled automatically. `""` sorts to `""`.
- **Single character strings:** Handled automatically. `"a"` sorts to `"a"`.

## Variations & Follow-ups
- **Follow-up:** "How can we optimize the time complexity to $O(N \times M)$?"
  - **Answer:** Instead of sorting, we can create a character frequency array (or tuple) of size 26 for each word. Example: `[1, 0, 0, 0, 1... 1]`. Tuples are hashable and can be used as keys. This avoids the $O(M \log M)$ sorting cost!

## "If I See This Again" (Quick Revision)
> Use `defaultdict(list)`. Iterate through words, use the **sorted word** (or a **26-char frequency tuple**) as the key, and append the original word to the map's list. Return `list(map.values())`.
