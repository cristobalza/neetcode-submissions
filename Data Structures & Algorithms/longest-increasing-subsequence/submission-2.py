class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """

        Input: nums = [9,1,4,2,3,3,7]


        [9,1,4,2,3,3,7]
           l
                      r

        
        [1,4,2,3,2,2,1]    

        if nums[l] < nums[r]:
            dp[l] = max(dp[r], dp[l] + 1)

        



        """

        dp = [1] * len(nums)

        for l in range(len(nums) - 1,  -1, -1):
            for r in range(l + 1, len(nums)):
                if nums[l] < nums[r]:
                    dp[l] = max(dp[l], dp[r] + 1)

        return max(dp)
        