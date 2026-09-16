class Solution:
    def rob(self, nums: List[int]) -> int:
        """

        nums=[2,1,1,2]
              

        dp = [2,2,3,4]

        """

        if len(nums) < 3:
            return max(nums)
        
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i - 2])

        return dp[len(nums) - 1]