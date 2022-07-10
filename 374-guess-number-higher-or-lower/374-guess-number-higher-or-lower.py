# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, n
        while (l <= h):
            md = l +(h - l) // 2
            res = guess(md)
            if res == 0:
                return md
            elif res > 0:
                l = md + 1
            else: 
                h = md - 1
        return -1