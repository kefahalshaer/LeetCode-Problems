class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ht = {}
        l = []
        for num in nums:
            ht[num] = ht.get(num, 0) + 1
        return sorted(nums,key = lambda x : (ht[x], -x))
            
                
            