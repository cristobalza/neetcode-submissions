class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
              0 1 2 3 4 5
        nums=[3,4,5,6,1,2]
              l.        r
                  m

            3 < 5
            
            is sorted? yes

                  l.    r
                    m

            5 < 6
             
                    l   r
                      m
            6< 1
                    l r
        """
        # binary search

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[l] <= nums[m]:
                if nums[m] <= nums[r]:
                    r = m
                else:
                    l = m + 1

            elif nums[m] <= nums[r]:
                if nums[l] <= nums[r]:
                    l = m + 1
                else:
                    r = m

        return nums[l]