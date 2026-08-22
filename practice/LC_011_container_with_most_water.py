from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # TODO: Implement your Two Pointers solution here
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = min(height[left], height[right])*(right-left)
            max_area = max(area, max_area)

            if height[left]<height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.maxArea([1,8,6,2,5,4,8,3,7]))
    # Expected: 49
    
    print("Test 2:", sol.maxArea([1,1]))
    # Expected: 1
    
    print("Test 3:", sol.maxArea([4,3,2,1,4]))
    # Expected: 16
