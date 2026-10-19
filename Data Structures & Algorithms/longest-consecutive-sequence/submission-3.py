class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0

        hs = set(nums)

        for num in nums:

            curr_res = 1

            if num + 1 not in hs:

                while num - 1 in hs:
                    num -= 1
                    curr_res += 1

            res = max(res, curr_res)

        return res
        