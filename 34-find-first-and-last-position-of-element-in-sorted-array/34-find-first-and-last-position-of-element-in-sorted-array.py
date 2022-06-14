class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.bias(nums, target, True)
        right = self.bias(nums, target, False)
        return [left, right]    
 
    # leftbias if `leftbias` is true, if it is false make rightbias
    def bias(self, nums, target, leftbias): 
        l, r = 0, len(nums) - 1 
        i = -1
        while (l <= r):
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else: 
                i = m
                if leftbias:
                    r = m - 1
                else:
                    l = m + 1
        return i
    
                
        
        
        