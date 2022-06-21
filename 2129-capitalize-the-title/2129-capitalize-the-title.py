class Solution:
    def capitalizeTitle(self, title: str) -> str:
        out = []
        words = title.split()
        
        '''
        ASCII value of uppercase alphabets – 65 to 90.
        ASCII value of lowercase alphabets – 97 to 122.
        '''
        
        for word in words:
            if len(word)== 1:
                if word.isupper():
                    out.append(chr(ord(word) + 32))
                else: out.append(word)
            elif len(word) == 2:
                for c in word:
                    if c.isupper():            
                        out.append(chr(ord(c) + 32))
                    else: out.append(c)
                
            else:
                for i in range(len(word)):
                    if i == 0:
                        if word[i].islower():
                            out.append(chr(ord(word[i])-32))
                        else:
                            out.append(word[i])
                    else:
                        if word[i].isupper():            
                            out.append(chr(ord(word[i]) + 32))
                        else: out.append(word[i])
            out.append(' ')

        return ''.join(out).strip()
                        
                        
                                        