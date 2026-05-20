use std::cmp;

impl Solution {
    /*
    Ok, for this solution, we need to leverage minimum ask to consistantly
    move our buy pointer forward

    for example: [5, 10, 2, 20]

    we start off with buy at 5 and sell at 10 which results in PnL of $5

    then we move sell to 2 which results in PnL of $-3 which means we 
    have to move our buy pointer to 2 since we are guarenteed to not find
    a better buy price (buying at 10 would make no sense), and then we just
    iterate to end of day
    */
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let n: usize = prices.len();

        let mut buy: usize = 0;
        let mut sell: usize = 0;

        let mut profit: i32 = 0;

        while sell < n 
        {
            let spread: i32 = prices[sell] - prices[buy];

            if spread < 0 
            {
                buy = sell;
            } else 
            {
                profit = cmp::max(profit, spread);
            }
            sell += 1
        }
        profit
    }
}
