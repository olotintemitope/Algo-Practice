from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) > 0:
            dp = nums
            dp[0] = nums[0]
            count = 1
            for num in range(1, len(nums)):
                dp[count] = dp[count] + dp[count - 1]
                count += 1

            return dp


sol = Solution()
print(sol.runningSum([3, 1, 2, 10, 1]))
