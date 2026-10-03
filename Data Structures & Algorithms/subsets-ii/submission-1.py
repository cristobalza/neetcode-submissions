class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()

        def backtrack(i, subset):

            res.append(subset.copy())

            for j in range(i, len(nums)):

                if i < j and nums[j - 1] == nums[j]:
                    continue
                    
                subset.append(nums[j])

                backtrack(j + 1, subset)

                subset.pop()

            return

        backtrack(0, [])

        return res