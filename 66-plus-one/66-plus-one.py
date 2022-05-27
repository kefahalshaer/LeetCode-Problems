class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l1 = [str(i) for i in digits] #covert to str list
        s1 = ''.join(l1)
        n1 = int(s1) + 1
        l3 = [i for i in str(n1)]
        return [int(i) for i in l3]
    
        
        
        