class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # med = 0
        nums3=[]
        nums3 += nums1
        nums3 += nums2
        nums3.sort()
        median = None
        mid = None
        mid = int(len(nums3)/2)
        
        if len(nums3) % 2 != 0:
            median = nums3[mid]
        else:
            median = float((nums3[mid-1] + nums3[mid])/2.0)
        return median