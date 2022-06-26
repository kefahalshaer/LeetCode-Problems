class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies = {}
        l  = len(candyType)
        for ctype in candyType:
            candies[ctype] = candies.get(ctype, 0) + 1
        return min(l//2, len(candies))
            
            
            
            
            
            
            
            
            
        