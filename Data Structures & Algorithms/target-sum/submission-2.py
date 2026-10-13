class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        res = 0

        def backtrack(num, i):
            nonlocal res

            if i == len(nums):
                if num == target:
                    return 1
                else:
                    return 0

            subs = backtrack(num - nums[i], i + 1)
            plus = backtrack(num + nums[i], i + 1)
            return subs + plus

        return backtrack(0, 0)
                
                    

                
        