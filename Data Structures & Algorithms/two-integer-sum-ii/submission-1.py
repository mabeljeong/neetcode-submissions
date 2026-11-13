class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #brute force --> compare all combinations / n^2
        
        #two pointers
        right = len(numbers) - 1 

        for i in range(len(numbers)): 
            while i < right:
                if numbers[i] + numbers[right] > target: 
                    right -= 1 
                elif numbers[i] + numbers[right] == target: 
                    return [i+1, right+1] 
                else: 
                    break


