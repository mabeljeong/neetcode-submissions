class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        running_sum = nums[0]  
        best_sum = nums[0]

        for i in range(1, len(nums)):
            running_sum += nums[i]
            if running_sum < nums[i]:
                running_sum = nums[i]
            if running_sum >= best_sum:
                    best_sum = running_sum
        return best_sum 

