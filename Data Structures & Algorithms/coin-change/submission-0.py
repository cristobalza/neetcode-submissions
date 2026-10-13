class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        res = float("inf")

        def dfs(target, i, count):
            nonlocal res
            
            if target == 0:
                res = min(res, count)
                return

            if i == len(coins) or target < 0:
                return 

            for j in range(i, len(coins)):
                dfs(target - coins[j], j, count + 1)

            return

        dfs(amount, 0, 0)

        return res if res != float("inf") else -1
        