class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ht = {}
        l = []
        for num1 in set(nums1): 
            ht[num1] = ht.get(num1,0) + 1
        for num2 in set(nums2):
            ht[num2] = ht.get(num2,0) + 1
        for num3 in set(nums3):
            ht[num3] = ht.get(num3,0) + 1
        for k in ht:
            if ht[k] >= 2:
                l.append(k)
        return l
        
                