class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  
        idx = None  
        while(r >= l):
            md = (l + r) // 2 
            if target > nums[md]:   
               l = md + 1
            else:
                idx = md
                r = md - 1 
        if idx != None:
            return  idx
        else: return len(nums)  # when the number is larger than the whole no. in `nums`  

        