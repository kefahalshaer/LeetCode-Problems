class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ht = {}
        l  = len(arr)
        for n in arr:
            ht[n] = ht.get(n, 0) + 1
        v = ht.values()
        return len(set(v)) == len(list(v))
        
        