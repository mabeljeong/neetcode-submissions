class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dynamic window 

        max_profit= 0 
        lowest_buy = prices[0]

        for i in range(len(prices)): 
            lowest_buy = min(lowest_buy, prices[i]) 
            profit = prices[i] - lowest_buy 
            max_profit = max(max_profit, profit)
        return max_profit




        '''
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
        '''