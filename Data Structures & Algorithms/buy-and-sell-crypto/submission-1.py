class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for num in prices:
            minPrice = min(minPrice,num)
            maxProfit = max(maxProfit, num - minPrice)
        return maxProfit