from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
           min_price = float('inf')  # 初始化最小價格
           max_profit = 0  # 初始化最大利潤

           for price in prices:
                 min_price = min(min_price, price)  # 更新最小價格
                 max_profit = max(max_profit, price - min_price)
           return max_profit
                 
       







"""
def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for day in range(len(prices)-1):
            if prices[day] < prices[day+1] :
                buy_price = prices[day] 
                for sell_day in range(day + 1, len(prices)):  # 嘗試在未來的某天賣出
                    if prices[sell_day] > buy_price:  # 如果能夠賺錢
                        profit = prices[sell_day] - buy_price
                        max_profit = max(max_profit, profit)  # 更新最大利潤
        return max_profit    
"""
      
        
                            
            






            
