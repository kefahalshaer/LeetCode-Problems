class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for s in stones:
            if s in jewels:
                count+=1
        return count