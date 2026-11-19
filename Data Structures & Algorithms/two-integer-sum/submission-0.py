class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        stor = {} #key - second_num: val: index of i  

        for i in range(len(nums)): 
            
            if nums[i] in stor: 
                return[stor[nums[i]], i]
        
            second_num = target - nums[i]  
            stor[second_num] = i 
            
        

        