class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}
        
        def dfs(i, j):
            """
            i for word1
            j for word2

            """

            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1)) + 1

            return memo[(i, j)]

        return dfs(0, 0)