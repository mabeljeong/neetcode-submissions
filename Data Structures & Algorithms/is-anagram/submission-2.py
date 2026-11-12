class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt = {} 

        for c in s:
            cnt[c] = cnt.get(c, 0)
            cnt[c] += 1
        print(cnt)

        for c in t: 
            if not c in cnt:
                return False
            cnt[c] -= 1 
        print(cnt)

        for i in cnt.values(): 
            if i != 0: 
                return False
        return True