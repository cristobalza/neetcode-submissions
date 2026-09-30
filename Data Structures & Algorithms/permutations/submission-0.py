class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """

        Input: nums = [1,2,3]
                       i
                           j
        """

        res = []

        def backtrack(i, subset):
            if i == len(nums) :
                print(subset)
                res.append(subset.copy())
                return

            for j in range(i, len(subset)):

                subset[i], subset[j] = subset[j], subset[i]

                backtrack(i + 1, subset)

                subset[i], subset[j] = subset[j], subset[i]



            return 

        subset = nums.copy()



        backtrack(0, subset)

        return res

            

        