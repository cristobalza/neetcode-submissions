class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        hmap = {} # num in nums: count of that num 
        res = 0

        for num in nums_set:
            count = 1
            curr_num = num

            while curr_num - 1 in nums_set:
                if curr_num - 1 in hmap:
                    count += hmap[curr_num - 1]
                    break
                else:
                    count += 1
                    curr_num -= 1
            
            hmap[num] = count
            res = max(res, count)

        return res

        