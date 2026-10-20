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

        def dfs(i, curr_sum):
            if i >= len(nums) or curr_sum > total_sum // 2:
                return False

            if total_sum // 2 == curr_sum:
                return True
            
            return (
                dfs(i + 1, curr_sum + nums[i]) or dfs(i + 1, curr_sum)
            )

        return dfs(0, 0)
        
        