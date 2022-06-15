class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using left and right pointers, and if the 
        l = 0
        for r in range(len(nums)):
            if nums[r]:  # if the number is 0 --> ignore it, but if it's 1 --> do that:
                nums[l], nums[r] = nums[r], nums[l] # swapping their values
                l += 1 # updating left pointer by 1 to move to the next value
        return nums
                
        