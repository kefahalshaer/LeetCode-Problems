class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        1- left, right pointer 
        2- left at the first, right at the end of the list
        3- add left to right
        4- check if left + right > target?
        5- shift right point to left,
        elif left + right < target: shift left to right
        else: return[left+1, right+1]
               
        '''
        l = len(numbers) 
        left = 0      # first number
        right = l-1   # last number
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -=1

            elif numbers[left] + numbers[right] < target:
                left += 1
        
            else: return [left+1 , right+1]
        return []


            
                
                
                
                    
                
        