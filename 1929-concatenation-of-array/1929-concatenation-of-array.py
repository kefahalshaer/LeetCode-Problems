class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
        
        # 8.36%  - 63.71%
        # n = len(nums)
        # for i in range(n):
        #     nums.append(nums[i])
        # return nums
            
        