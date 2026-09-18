class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {} # current amount: current answer

        def dfs(target):
            nonlocal res

            if target == 0:
                return 0

            if target in memo:
                return memo[target]

            res = float("inf")
            for j in range(len(coins)):
                if target - coins[j] >= 0:
                    res = min(res, 1 + dfs(target - coins[j]))

            memo[target] = res

            return memo[target]

        res = dfs(amount)

        return res if res != float("inf") else -1
        