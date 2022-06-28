class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""
        
        for i in s:
            res += str(ord(i)-96)
        
        while k > 0:
            s = 0
            
            for i in res:
                s += int(i)
            
            res = str(s)
            k -= 1
        
        return int(res)
#         c = [' abcdefghijklmnopqrstuvwxyz']
#         ht = {}
#         for i in  range(1,len(c)):
#             ht[c[i]] = i
#         out1 = ""
#         # l = len(s)
#         for ltr in s: # first transform
#             out1 += ht[ltr]  # out is ready
#         out2 = ""
#         for j in range[1:k]: # next transforms
#             sum = 0   
#             for c in out:
#                 sum += c
#                 out2 = sum
#         return int(out2) 
                
                
            
        
            
            
            
            
            
            
         
        
        