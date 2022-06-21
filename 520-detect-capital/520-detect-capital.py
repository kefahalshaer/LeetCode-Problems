class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        l = len(word)
        if word.isupper():
            return True
        elif word.islower():
            return True
        else: 
            for i in range(l):
                if word[i].isupper() and word[i+1:].islower():
                    return True
                else: return False
        return False 
            