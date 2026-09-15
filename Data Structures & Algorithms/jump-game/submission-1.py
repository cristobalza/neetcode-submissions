class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """

                        i= 0
                        1

                    i=1.     
                    2           


        i=2.      i=3
        0.        1


                  i=4
                  true


        """
        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return True

            if nums[i] == 0:
                return False

            if i in memo:
                return memo[i]

            for j in range(i + 1, nums[i] + i + 1):
                if dfs(j):
                    memo[j] = True
                    return memo[j]
            
            memo[i] = False
            return False

        return dfs(0)
        