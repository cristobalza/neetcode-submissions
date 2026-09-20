class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        prices = [10,1,5,6,7,1]
                             i
                     j

        1 - 10 < 0
        5 - 1 > 0 = 4 
        6  - 1 = 5
        7 - 1 = 6

        1 - 1 = 0

        prices = [10,8,7,5,2]
                           i 
                   j

                   10 - 10 = 0
                   8-10


        """

        res = 0
        j = 0

        for i in range(len(prices)):

            sell_price = prices[i] - prices[j]
            if sell_price <= 0:
                j = i

            res = max(res, sell_price)

        return res

            