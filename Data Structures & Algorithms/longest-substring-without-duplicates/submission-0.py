class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """

         Input: s = "zxyzxyz"
                           i

        {
            z:5
            x:4
            y:5
        }

        2 - 0 + 1 = y - x + 1 = 3
        3 - 1 + 1 = 3

        4 - 2 + 1 = 3
        5 - 3 + 1 = 3

        y = max(idx) or max val in the hmap
        x = the val in of the key in the hmap

        then update the val of the hmap to the new idx
                      

        """

        hmap = {}
        max_left = 0
        res = 0

        for i, c in enumerate(s):

            if c in hmap:
                max_left = max(max_left, 1 + hmap.get(c))

            hmap[c] = i

            res = max(res, i - max_left + 1)
    
        return res

    