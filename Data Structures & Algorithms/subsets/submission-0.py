class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        backtrack
        1. mark candidate
        2. explore further
        3. rm candidate

        candidate: if subset == n
        use a set to store values and faster lookup

        explore:
        add 1
        dfs([1])
        rm 1
        

        """

        def dfs(i):
            if i == len(nums):
                res.append(subset[::])

                return 

            subset.append(nums[i])

            dfs(i+1)

            subset.pop()

            dfs(i + 1)

            return 

        res = []
        subset = []

        dfs(0)
        
        return res