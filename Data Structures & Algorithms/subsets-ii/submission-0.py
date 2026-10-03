class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()

        nums.sort()

        def backtrack(i, subset):
            if i >= len(nums):
                res.add(tuple(subset.copy()))
                return

            for j in range(i, len(nums)):
                    
                subset.append(nums[j])

                backtrack(j + 1, subset)

                subset.pop()

                backtrack(j + 1, subset)

            return

        backtrack(0, [])

        return list(res)