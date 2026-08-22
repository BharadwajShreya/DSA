class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TODO: Implement your Sliding Window solution here
        max_length = 0
        left = 0
        right = 1
        char_set = set()
        if len(s)>0:
            char_set.add(s[left])
            max_length = 1

        while right < len(s):
            if s[right] not in char_set:
                max_length = max((right+1-left), max_length)
                char_set.add(s[right])
                right += 1
            else:
                char_set.remove(s[left])
                left += 1

        return max_length
            


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    print("Test 1:", sol.lengthOfLongestSubstring("abcabcbb"))
    # Expected: 3
    
    print("Test 2:", sol.lengthOfLongestSubstring("bbbbb"))
    # Expected: 1
    
    print("Test 3:", sol.lengthOfLongestSubstring("pwwkew"))
    # Expected: 3
    
    print("Test 4:", sol.lengthOfLongestSubstring(" "))
    # Expected: 1
