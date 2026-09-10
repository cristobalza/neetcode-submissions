class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def dfs(i, subset, sum_subset):
            if sum_subset == target:
                res.append(subset.copy())
                return
            
            if i >= len(nums) or sum_subset > target:
                return

            for j in range(i, len(nums)):
                sum_subset += nums[j]
                subset.append(nums[j])

                dfs(j, subset, sum_subset)

                sum_subset -= nums[j]
                subset.pop()

            return

        res = []

        dfs(0, [], 0)

        return res


            