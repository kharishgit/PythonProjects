# from typing import  List
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit =0
#         for i in range (len(prices)):
#             for j in range(i+1,len(prices)):
#                 # print((prices[j]-prices[i]))
#                 if profit < prices[j]-prices[i]:
#                     profit = prices[j]-prices[i]
#
#         return profit
# s= Solution()
# print(s.maxProfit([7,1,5,3,6,4]))

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = float('inf')
        print(min_price)
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
                # print(min_price,price)
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


# Example usage
s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))