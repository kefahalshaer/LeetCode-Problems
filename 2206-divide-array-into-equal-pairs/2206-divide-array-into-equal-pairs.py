class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ht = {}
        l = []
        for num in nums:
            ht[num] = ht.get(num, 0) + 1
        for k,v in ht.items():
            if v % 2 != 0:
                l.append(False)
            else: l.append(True)
        return all(l)
        
        
        