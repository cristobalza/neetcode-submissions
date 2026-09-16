class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def fwd():
            dp = [0] * len(nums)

            dp[1] = nums[1]
            dp[2] = max(nums[1], nums[2])

            for i in range(3, len(nums)):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])

            return dp[len(nums) - 1]

        def bwd():
            dp = [0] * len(nums)

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums) - 1):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])

            return dp[len(nums) - 2]

        if len(nums) < 4:
            return max(nums)

        return max(fwd(), bwd())

        
        