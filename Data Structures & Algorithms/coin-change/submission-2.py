class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        res = float("inf")
        memo = {} # state := curent amount left to 0, index pair : count

        def dfs(target, i, count):
            nonlocal res

            if target == 0:
                res = min(res, count)
                return

            if i == len(coins) or target < 0 or count >= res:
                return 

            state = (target, i)

            if state in memo and memo[state] <= count:
                return

            memo[state] = count 
            for j in range(i, len(coins)):
                dfs(target - coins[j], j, count + 1)


            return

        dfs(amount, 0, 0)

        return res if res != float("inf") else -1
        