class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        res = 0

        def backtrack(num, i):
            nonlocal res

            if i == len(nums):
                if num == target:
                    res += 1
                return

            num += nums[i]
            backtrack(num, i + 1)
            num -= nums[i]
            num -= nums[i]
            backtrack(num, i + 1)

            return 
        
        backtrack(0, 0)

        return res
                
                    

                
        