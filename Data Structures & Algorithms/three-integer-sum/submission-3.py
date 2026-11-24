class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #so for two sum -> u save {second num: first num index} 
        #does it work same as the two sum way? 
        
        nums.sort() 
        output = set()

        for i in range(len(nums)): 
            stor = {} 
            for j in range(i+1, len(nums)): 
                if nums[j] in stor: 
                    output.add(tuple(stor[nums[j]]+ [nums[j]]))
                else: 
                    two_sum = nums[i] + nums[j] 
                                        
                    third = 0 - two_sum  
                    stor[third] = [nums[i], nums[j]] 

        return [list(t) for t in output]

#1: [-1, 0]
        
            