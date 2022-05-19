class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localSum = 0
        globalSum = nums[0]
        
        for i in range(len(nums)):
            localSum = max(localSum + nums[i], nums[i])
            globalSum = max(globalSum , localSum)
        return globalSum 
        
        