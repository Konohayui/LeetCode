class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        total_profit = 0
        current_price = float("inf")
        
        for price in prices:
            profit = price - current_price
            if profit > 0:
                total_profit += profit
            current_price = price
            
        return total_profit
    
    
