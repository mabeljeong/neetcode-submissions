class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, right = 0, 0
        seen = set()
        best_len = 0

        while right < len(s):
            if s[right] not in seen: 
                seen.add(s[right])
                curr_len = right - left + 1 
                best_len = max(curr_len, best_len)
                right+=1 
            else: 
                seen.remove(s[left])
                left += 1 
        return best_len
