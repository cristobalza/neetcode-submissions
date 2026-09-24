class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """

        Input: text1 = "cat", text2 = "crabt" 


          * c a t
        * 0 0 0 0
        c 0 1 1 1
        r 1 1 1 1  
        a 1 1 2 2 
        b 2 2 2 2
        t 2 2 2 3



        """

        ROWS = len(text2)
        COLS = len(text1)

        dp = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]

        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                if text2[r - 1] == text1[c - 1]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    dp[r][c] = max(dp[r][c - 1], dp[r - 1][c])
        
        return dp[ROWS][COLS]

        
