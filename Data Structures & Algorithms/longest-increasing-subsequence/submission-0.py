class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)

        for num in nums_set:
            count = 1
            curr = num

            if curr + 1 not in nums_set:
                while curr - 1 in nums_set:
                    count += 1
                    curr -= 1

            res = max(res, count)

        return res