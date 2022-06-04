class Solution:
    def frequencySort(self, s: str) -> str:
        h = {} # hash map of frequensies
        for l in s:
            h[l] = h.get(l, 0) + 1
        res = []  
        l = sorted(h, key = lambda v : h[v], reverse = True)
        for char in l: 
            (res.append(char*h[char]))
        return ''.join((res))
        
        