class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        count = 0

        for i in range(len(s)):
            # odd
            l = i
            r = i

            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > count:
                    res = s[l: r + 1]
                    count = r - l + 1

                r += 1
                l -= 1

            # even
            l = i
            r = i + 1

            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > count:
                    res = s[l: r + 1]
                    count = r - l + 1

                r += 1
                l -= 1

        return res

