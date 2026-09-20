class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

        Input: nums = [1,2,4,6]


        i=0 - 2*4*6 = 48
        i=1 - 1*4*6 = 20
        i=2 - 1*2*6 = 12
        i=3 - 1*2*4 = 8


        Input: nums = [1,2,4,6]

        [1, 1, 1 * 2, 1 * 2 * 4] = [1, 1, 2, 8]

        [2 * 4 * 6 , 4*6 , 6, 1] = [48, 24, 6, 1]

        multiply each other

        [1, 1, 2, 8] * [48, 24, 6, 1] = [1* 48, 1* 24, 2* 6, 8 * 1] = [48, 24, 12, 8]

        -----

        


        """


        n = len(nums)

        res = [1] * n
        fwd = [1] * n
        back = [1] * n

        for i in range(1, n):
            fwd[i] = nums[i - 1] * fwd[i - 1]

        for i in range(n - 2, -1, -1):
            back[i] = nums[i + 1] * back[i + 1]

        # multiply each other
        for i in range(n):
            res[i] = fwd[i] * back[i]

        return res

        # Time: O(n)
        # Space: O(n)

        