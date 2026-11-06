class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = []
        s = s.lower()
        for i in range(len(s)): 
            if s[i].isalnum(): 
                clean_s.append(s[i])
        clean_s = "".join(clean_s)
        print(clean_s)
        left = 0 
        right = len(clean_s) - 1 

        while left <= right:
            if clean_s[left] == clean_s[right]: 
                left += 1
                right -= 1 
            else: 
                return False 
        return True 