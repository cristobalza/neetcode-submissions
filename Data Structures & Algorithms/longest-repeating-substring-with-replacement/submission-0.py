class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Input: s = "XYYX", k = 2
                    l
                      r 
        {
            X: 1
            Y: 2
        
        }

        max_freq = 2

        hmap[l] := freq of current letter different thant s[r]

        max_freq + hmap[l] <= k



        Input: s = "AAABABB", k = 1
                    l
                       r

        {
            A:3
            B:1
        }

        size = 4 = r - l + 1 = 3 - 0 + 1 = 4

        max-freq = 3

        HAS to be this: size - max_freq <= k
        else reset l -> l = r

        update res
        """ 
        res = 0

        hmap = {}

        l = 0

        max_freq = 0

        for r in range(len(s)):

            hmap[s[r]] = 1 + hmap.get(s[r], 0)

            max_freq = max(max_freq, hmap[s[r]])
           
            while (r - l + 1) - max_freq > k:
                # size = r - l + 1
                hmap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


