class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Input: coins = [1,5,10], amount = 12

            1
        5.              1.                          10

        5.              1....                        coins 3, bc 10+ 1 + 1

        1.             coins 12

coins 4


        If the sum of coins is even and the amount is uneven then -1

        If amount is 0 then guarantee answer

        res = infin

        def dfs(i, target, steps)
        base case: 
            i == len(coins)
                return float('inf')

            target == 0
                return steps

            res = float("inf")
            for j in range(i, len(coins)):
                res = min(res, dfs(j, target - coins[j] , steps + 1))

            return res


        Input: coins = [1,5,10], amount = 12

        dfs(0, 12, 0)
            res = min(inf, dfs(0, 12 - 1, 1))
                                res = min(inf, dfs(0, 11 - 1, 2))

        """

        memo = {}  # (i, target) -> min ADDITIONAL coins needed (path-independent)

        def dfs(i, target, steps):
            if target == 0:
                return steps
            if i == len(coins) or target < 0:
                return float("inf")

            if (i, target) in memo:
                return steps + memo[(i, target)]

            take = dfs(i, target - coins[i], steps + 1)  # use coin i again
            skip = dfs(i + 1, target, steps)             # move to next coin
            best = min(take, skip)

            memo[(i, target)] = best - steps             # inf - steps stays inf

            return best

        res = dfs(0, amount, 0)
        return res if res != float("inf") else -1   
        
