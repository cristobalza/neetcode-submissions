class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        lst = sorted(nums1 + nums2)

        print(lst)

        if len(lst) % 2 == 0:
            return (lst[(len(lst) // 2) - 1] + lst[len(lst) // 2]) / 2.0
        else:
            return lst[len(lst) // 2] 


        