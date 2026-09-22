class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for ch in s:
            if ch.isalnum():
                lst.append(ch.lower())

        s = "".join(lst)

        l, r = 0, len(s) - 1

        while l < r: 
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True