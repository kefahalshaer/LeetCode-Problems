class Solution:
    def reverseWords(self, s: str) -> str:
        l = [w for w in s.split()]
        return ' '.join(l[::-1])