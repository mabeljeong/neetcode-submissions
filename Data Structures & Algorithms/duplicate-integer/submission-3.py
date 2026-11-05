class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stor = set() 

        for num in nums: 
            if num in stor: 
               return True
            else: 
                stor.add(num)
        return False 