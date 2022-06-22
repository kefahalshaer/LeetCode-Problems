class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = []
        c = 0
        l =  len(nums)
        for i in range(l):  # 0
            for j in range(l): 
                if i == j:
                    continue
                else: # 1
                    if nums[j] < nums[i]: 
                        c +=1
            count.append(c)
            c = 0
        
        return count
                        
            
            
        