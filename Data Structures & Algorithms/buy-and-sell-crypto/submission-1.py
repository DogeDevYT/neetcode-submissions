class Solution:
    """
    Ok, for this solution, we need to leverage minimum ask to consistantly
    move our buy pointer forward

    for example: [5, 10, 2, 20]

    we start off with buy at 5 and sell at 10 which results in PnL of $5

    then we move sell to 2 which results in PnL of $-3 which means we 
    have to move our buy pointer to 2 since we are guarenteed to not find
    a better buy price (buying at 10 would make no sense), and then we just
    iterate to end of day
    """
    def maxProfit(self, prices: List[int]) -> int:
        #set length variable of n
        n = len(prices)

        #initialize buy/sell pointers to move
        buy, sell = 0, 0

        #initialize max profit
        profit = 0

        while sell < n:
            spread = prices[sell] - prices[buy]

            """
            We have 2 outcomes here: one where we have a >= spread which
            means we have to check for new max profit or a situation where
            we have a < 0 spread which means we have to move our buy pointer            
            """
            if spread < 0:
                buy = sell
            else:
                profit = max(profit, spread)
            sell += 1
        
        return profit
        