class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for l in range(len(nums)):
            if 0 < l and nums[l - 1] == nums[l]:
                continue 

            m = l + 1
            r = len(nums) - 1

            while m < r:

                if nums[l] + nums[m] + nums[r] < 0:
                    m += 1
                elif nums[l] + nums[m] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1

                    while m < r and nums[m - 1] == nums[m]:
                        m += 1

        return res