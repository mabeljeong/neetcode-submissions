class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #nums are already sorted
        #find the num in the middle, if thats greater than target then it's on the right side / if that's less than the target then its on the left side  

        
        front = 0
        end = len(nums) - 1  

        while front <= end:
            mid = (front + end) // 2
            if nums[mid] == target: 
                return mid 
            if nums[mid] > target: 
                end = mid - 1
            else: 
                front = mid + 1
        return -1
