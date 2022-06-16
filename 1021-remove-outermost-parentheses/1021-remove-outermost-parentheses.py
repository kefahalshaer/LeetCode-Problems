class Solution:

    def removeOuterParentheses(self, s: str) -> str:
        a,t, l = 0,0, []        
        for i in range(len(s)):
            t = t + 1 if s[i] is '(' else t - 1
            if t == 0:
                l.append(s[a:i+1])
                a = i + 1
        return ''.join(sub[1:-1] for sub in l)



              

            
        