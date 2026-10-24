class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Set two pointers at the begining and end of the height list (l, r)
        Calculate the distance between maxL or maxR against its respective height[l] or height[r]

        max_L, max_R = height[l], height[r]

        So, if height[l] <= heigth[r]:
            calculate area of maxL - height[l]
            l ++
            update maxL
        else
            maxR - height[r]
            r --
            update maxR

        Test:          0 1 2 3 4 5 6 7 8 9
             height = [0,2,0,3,1,0,1,3,2,1]
                             l               
                                       r

            res = 2

            maxL - height[l] = 2 - 0
            maxL = max(2, 0) = 3

            maxR - height[r] = 1 - 1
            maxR = max(2, 1) = 2


        """

        l, r = 0, len(height) - 1

        maxL, maxR = height[l], height[r]

        res = 0

        while l < r:
            if height[l] <= height[r]:
                res += maxL - height[l]
                l += 1
                maxL = max(maxL, height[l])
            else:
                res += maxR - height[r]
                r -= 1
                maxR = max(maxR, height[r])

        return res

        