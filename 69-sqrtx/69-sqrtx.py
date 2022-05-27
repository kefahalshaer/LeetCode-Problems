class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while(i >= 0):
            if(i*i <= x):
                i +=1
            else:
                break
        return i-1