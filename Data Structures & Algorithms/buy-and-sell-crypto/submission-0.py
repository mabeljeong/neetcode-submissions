class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dynamic window 

        #brute force --> o(n^2) get the all combinations 
        #buy price at fixed / sell price when its higher than buy price 
        #compare with the previous max profit 

        cur_max = 0 

        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)): 
                if prices[i] < prices[j]: 
                    profit = prices[j] - prices[i]  
                    if profit > cur_max: 
                        cur_max = profit 
        return cur_max 