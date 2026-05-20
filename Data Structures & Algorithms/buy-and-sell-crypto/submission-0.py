class Solution:
    """
    Ok, heres the naive approach, brute force
    """
    def maxProfit(self, prices: List[int]) -> int:
        #store length of prices for later reference
        n = len(prices)

        #store max profit posssible
        profit = 0

        #nested for loop for calculation with EACH stock
        for i in range(n):
            equityPrice = prices[i]
            for j in range(i, n):
                #update max profit to be the best transaction possible
                profit = max(profit, prices[j] - equityPrice)
        
        return profit