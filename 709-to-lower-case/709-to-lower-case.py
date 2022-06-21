class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()
        '''
        ASCII value of uppercase alphabets – 65 to 90.
        ASCII value of lowercase alphabets – 97 to 122.
        '''
    
        out = ''
        for c in s:
            if c.isupper():
                out+= chr(ord(c) + 32)

            else: 
                out+= c
        return out