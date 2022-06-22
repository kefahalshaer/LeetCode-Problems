class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            if nums.count(num) == 1:
                sum += num
        return sum
            
        