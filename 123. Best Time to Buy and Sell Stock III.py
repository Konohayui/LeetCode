class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        first_buy = -prices[0]
        first_sold = -float("inf")
        second_buy = -float("inf")
        second_sold = -float("inf")
        
        for price in prices[1:]:
            first_buy = max(first_buy, -price)
            first_sold = max(first_sold, first_buy+price)
            second_buy = max(second_buy, first_sold-price)
            second_sold = max(second_sold, second_buy+price)
            
        return max(0, second_sold)
    
    
