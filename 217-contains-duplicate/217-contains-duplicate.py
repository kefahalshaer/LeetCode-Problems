class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 908 ms	26 MB
        # return len(nums) != len(set(nums))  
        
        # 464 ms  25.9 MB
        # solve it by counting them in a hashmap
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1 
            else: return True
        return False  
            
            
     # slower solution        
        #     hashMap[num] = hashMap.get(num, 0) + 1 # return 0 when the number is not found
        # for k,v in hashMap.items():
        #     if v > 1: # check dublicates
        #         return True
        # return False
     
        
            