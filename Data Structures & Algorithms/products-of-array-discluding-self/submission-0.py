class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

        Input: nums = [1,2,4,6]


        i=0 - 2*4*6 = 48
        i=1 - 1*4*6 = 20
        i=2 - 1*2*6 = 12
        i=3 - 1*2*4 = 8

        Brute force:

        for i in range(n)
            temp1, temp2 = 1, 1
            for back in range(0, i)
                temp1 *= nums[back]

            for fwd in range(i + 1, n)
                temp2*=nums[fwd]

            res[i] = temp1 * temp2


        """

        n = len(nums)

        res = [0] * n

        for i in range(n):
            temp1, temp2 = 1, 1
            for back in range(0, i):
                temp1 *= nums[back]

            for fwd in range(i + 1, n):
                temp2*=nums[fwd]

            res[i] = temp1 * temp2

        return res
        