class Solution:
    def climbStairs(self, n: int) -> int:
        stor = {}

        def helper(n): 
            if n == 1:
                return 1 
            if n == 0: 
                return 1 
            
            if n in stor: 
                res = stor[n] 
                return res
            
            stor[n] = helper(n-1) + helper(n-2)
            return stor[n]
        

        return helper(n)