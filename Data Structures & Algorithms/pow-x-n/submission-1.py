class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        pow(x, n) -> pow(2, 1) = 2 

        2^1 x^n

        num = 2

        power = 5

        2*2*2*2*2 -> 2^2 * 2^2 * 2
                    ----------
                    O(logN)

        n // 2 = 5 // 2 = 2

        if n is even:
            res = res * res

        



        """
        def dfs(num, power):
            if power == 0:
                return 1
            if num == 0:
                return 0

            res = dfs(num * num, power // 2)

            return num * res if power % 2 != 0 else res
        
        res = dfs(x, abs(n))
        return res if n > 0 else 1/res

        