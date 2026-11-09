class Solution:
    def isHappy(self, n: int) -> bool:
         
        seen = set()

        while n!= 1:
            result = 0 
            for c in str(n): 
                squared = int(c)*int(c)
                result+= squared 

            if result not in seen: 
                seen.add(result) 
                n= result 
            else:
                return False 
        return True