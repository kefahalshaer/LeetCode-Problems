class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:     
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
            # else:
            #     nums.remove(nums[i])
        return k

        