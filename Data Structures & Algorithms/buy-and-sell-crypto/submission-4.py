class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #quick sliding window chud mode

        buy_price = prices[0]

        profit = 0

        for i in range(len(prices)):
            if prices[i] < buy_price:
                #we can automatically slide the window here because 
                #we can gauarentee we can make more profit buying later on for less
                #than selling later for more profit
                buy_price = prices[i]
            
            #consistantly get the maximum profit availible
            profit = max(profit, prices[i] - buy_price) 
        
        return profit
            
