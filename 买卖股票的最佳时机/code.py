class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = int(1e9)
        maxProfit=0
        for price in prices:
           maxProfit = max(price - minprice,maxProfit)
           minprice = min(price,minprice)

        return maxProfit
