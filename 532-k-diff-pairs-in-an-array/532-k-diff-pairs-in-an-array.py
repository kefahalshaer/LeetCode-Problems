class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        l = len(nums)
        ht = {}
        count = 0
        for num in nums:
            ht[num] = ht.get(num,0) + 1
        for key,v in ht.items():
            if k == 0:
                if v > 1:
                    count+= 1
            else: 
                if key+k in ht:
                    count+= 1
        return count
                    
        
            
                
        
        
        
        
        
        
        
        
#         l = len(nums)
#         count = 0
#         ht = {}
#         for i in range(l):
#             ht[nums[i]] = ht.get(nums[i], 0) + 1  # make counter for how many times 
#                                                  # each elemnts in `nums` appear
#         for num in ht:
#             if (num & num + k in ht.keys()):
#                 count += (ht[num] * ht[num + k])
#         return count 
            