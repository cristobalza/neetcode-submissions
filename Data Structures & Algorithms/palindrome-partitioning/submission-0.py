class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1
            return True
            
        res = []

        def backtrack(i, subset):
            
            if i >= len(s):
                res.append(subset.copy())
                return 

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    subset.append(s[i: j + 1])
                    backtrack(j + 1, subset)
                    subset.pop()
            return

        backtrack(0, [])

        return res

            
        