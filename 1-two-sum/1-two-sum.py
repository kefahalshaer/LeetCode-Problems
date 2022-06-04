class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {} # store the values and its indeices in a hashmap
        for i, n in enumerate(nums):
            y = target - n # try to find the second number 
            if y in mydict:
                return [mydict[y], i] # return the index of the y and recent number ~ n
            mydict[n] = i 
            
        
        

            
            
        
        