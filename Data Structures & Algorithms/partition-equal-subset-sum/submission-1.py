class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """

        Input: nums = [1,2,3,4]
                           i
                              

        full_sum = 10 - 6
        curr_sum = 6



        """
        if sum(nums) % 2 != 0:
            return False
        
        total_sum = sum(nums) # o(n)

        memo = {}

        def dfs(i, curr_sum):
            if i >= len(nums) or curr_sum > total_sum // 2:
                return False

            if (i, curr_sum) in memo:
                return memo[i]

            if total_sum // 2 == curr_sum:
                return True
            
            return (
                dfs(i + 1, curr_sum + nums[i]) or dfs(i + 1, curr_sum)
            )

            return memo[(i, curr_sum)]

        return dfs(0, 0)
        
        