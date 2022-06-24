class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        l = len(nums)
        count = 0
        for i in range(l):
            for j in range(i+1,l):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count
                
        
        
            
        
            
            
                    