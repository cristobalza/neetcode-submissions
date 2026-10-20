class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Input: s = "12"
                    i

        dfs(0) -> "1" -> A -> 1 
            dfs(1) -> "2" -> B -> 1
                dfs(3) -> 0
        dfs(2) -> 0

        -> 1 + 1

        """

        def dfs(i):

            if i >= len(s):
                return 1

            if i in memo:
                return memo[i]

            if s[i] == "0":
                return 0

            memo[i] = dfs(i + 1)

            if i + 2 <= len(s):
                if int(s[i: i + 2]) <= 26:
                    memo[i] += dfs(i + 2)

            return memo[i]

        memo = {}

        return dfs(0)


        