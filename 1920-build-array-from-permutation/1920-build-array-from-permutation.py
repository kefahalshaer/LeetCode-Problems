class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        out = []
        l = len(nums)
        for i in range(l):
            out.append(nums[nums[i]])
        return out
        
        