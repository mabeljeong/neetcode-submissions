class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stor = {} #num:index (do we need index)

        for i in range(len(nums)): 
            if nums[i] in stor: 
               return True
            else: 
                stor[nums[i]] = i
        return False 