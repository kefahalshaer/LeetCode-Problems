class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        idx = None
        while(r >= l):
            md = (l+r) // 2
            if letters[md] > target:
                idx = md 
                r = md - 1
            else:
                l = md + 1 
        if idx != None:
            return letters[idx]
        else: return letters[0]