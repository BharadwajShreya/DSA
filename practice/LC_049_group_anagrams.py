from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # TODO: Implement your solution here
        anagrams = defaultdict(list)
        # output = []

        for i in strs: 
            sorted_string = str(sorted(i))
            # if sorted_string in anagrams:
            anagrams[sorted_string].append(i)

        # for anagram in anagrams:
        #     output.append(anagrams[anagram])

        return list(anagrams.values())

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # Expected: [["bat"],["nat","tan"],["ate","eat","tea"]] (order doesn't matter)
    
    print("Test 2:", sol.groupAnagrams([""]))
    # Expected: [[""]]
    
    print("Test 3:", sol.groupAnagrams(["a"]))
    # Expected: [["a"]]
