from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # TODO: Implement your Prefix Sum + Hash Map solution here
        prefix_dict = {0:1}
        current_sum = 0
        count = 0

        for num in nums:
            # print(prefix_dict)
            current_sum += num
            if current_sum-k in prefix_dict:
                count += prefix_dict[current_sum-k]
            if current_sum in prefix_dict:
                prefix_dict[current_sum] += 1
            else:
                prefix_dict[current_sum] = 1

        return count

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    print("Test 1:", sol.subarraySum([1, 1, 1], 2))
    # Expected: 2 (indices [0,1] and [1,2])
    
    print("Test 2:", sol.subarraySum([1, 2, 3], 3))
    # Expected: 2 (indices [0,1] and [2])
    
    print("Test 3:", sol.subarraySum([3, 4, 2, -2, 3], 7))
    # Expected: 3
    
    print("Test 4:", sol.subarraySum([-1, -1, 1], 0))
    # Expected: 1 (indices [1,2])

    print("Test 4:", sol.subarraySum([0, 0, 0], 0))
    # Expected: 0
