class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0

        area = lambda h, w: h * w

        l, r = 0, len(heights) - 1

        while l < r:

            curr_area = area(min(heights[l], heights[r]), r - l)

            res = max(res, curr_area)

            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1

        return res


        