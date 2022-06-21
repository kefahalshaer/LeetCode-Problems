class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        out1, out2 = '', ''
        for w1 in word1:
            out1+= w1
        for w2 in word2:
            out2 += w2
        return out1 == out2