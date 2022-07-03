class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return [num for num in nums1 if num in nums2] 
        res = []
        nums1 = sorted(nums1)
        # nums2 = set(nums2)
        for i in nums2:
            l,r = 0,len(nums1)-1
            while l <=  r:
                m = (l+r) // 2
                if nums1[m] == i:
                    res.append(i)
                    nums1.pop(m)
                    break
                else:
                    if nums1[m] < i:
                        l = m + 1
                    else:
                        r = m - 1
        return res