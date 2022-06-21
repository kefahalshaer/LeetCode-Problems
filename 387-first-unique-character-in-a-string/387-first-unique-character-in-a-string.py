class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = len(s)
        for i in range(l):
            if s.count(s[i]) == 1:
                return i
                break
            
        return -1
                
            