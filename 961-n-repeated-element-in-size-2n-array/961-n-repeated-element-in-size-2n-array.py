class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > 1:
                return num
                break
            
        
        