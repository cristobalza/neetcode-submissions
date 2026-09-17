class Solution:
    def countSubstrings(self, s: str) -> int:
        """

        Input: s = "aaa"
                      l
                      r

        res = 6

        sliding window

        iterate once 
            create second idx
            check if that slice is palindrome
            if so
                move forward
            else
                stop 


        ---

        two pointers

        start left and right
            check if it palidrome


        """

        def check_palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1
            return True

        res = 0

        # two pointers + window

        for i in range(len(s)):

            # even
            l = i
            r = i

            while 0 <= l and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # odd
            l = i
            r = i + 1

            while 0 <= l and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res 
            

                


        return res
            
