class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:            
        out_s, out_t = [], []
        
        for char in s:
            if char is '#':
                if out_s: out_s.pop()
            else: 
                out_s.append(char)
        
        for char in t:
            if char is '#':
                if out_t: out_t.pop()
            else: 
                out_t.append(char)   
        if out_s == out_t:
            return True 
        else: return False

        
        