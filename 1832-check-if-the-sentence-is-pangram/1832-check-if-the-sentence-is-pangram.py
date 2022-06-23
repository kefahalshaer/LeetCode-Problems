class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        list1 = list(map(chr, range(97, 123)))
        alpha = ''.join(list1)
        for char in alpha:
            if sentence.count(char) == 0:
                return False
        return True
        
        
        
        
        
        
        
        
        
        
#         l = len(sentence)
#         if l < 26:  
#             return False
#         list1 = list(map(chr, range(97, 123)))
        
#         list2 = [0]*26
        
#         letters = dict(zip(list1,list2))
        
#         for s in sentence:
#             letters[s] = letters.get(s) + 1
        
#         for v in letters.values():
#             if v == 0:
#                 return False
#                 break
            