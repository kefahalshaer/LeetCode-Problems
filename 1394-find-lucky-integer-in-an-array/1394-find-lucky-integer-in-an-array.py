class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l = len(arr)
        ht = {}
        l = []
        for num in arr:
            ht[num] = ht.get(num, 0) + 1
        for k,v in ht.items():
            if k == v:
                l.append(v)
        if l:
            return max(l)
        else: return -1
        
        
        