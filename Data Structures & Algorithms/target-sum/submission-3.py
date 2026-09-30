class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {} #(idx, value)

        def backtrack(num, i):
            if i == len(nums):
                if num == target:
                    return 1
                else:
                    return 0
            
            if (i, num) in memo:
                return memo[(i, num)]

            memo[(i, num)] = backtrack(num + nums[i], i + 1) + backtrack(num - nums[i], i + 1)

            return memo[(i, num)]
        
        return backtrack(0, 0)
                
                    

                
        