class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = prices[0]
        profit = 0
        for price in prices:
            profit = max(profit, price - buy_price)
            if price < buy_price:
                buy_price = price
        return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
