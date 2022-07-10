# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            md = l + (r - l) // 2
            if isBadVersion(md):
                r = md
            else: 
                l = md + 1
        return l
    
        