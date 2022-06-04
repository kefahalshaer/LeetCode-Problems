class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        h1, h2 = {}, {}
        for ls in s:
            h1[ls] = h1.get(ls, 0) + 1
        for lt in t:
            h2[lt] = h2.get(lt, 0) + 1
        return h1 == h2