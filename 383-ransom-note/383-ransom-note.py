class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dm = Counter(magazine)
        dr = Counter(ransomNote)
        
        for key , value in dr.items():
            
            if  value > dm[key]:
                return False
            
        return True
        # ht1 = {}
        # ht2 = {}
        # for r in ransomNote:
        #     ht1[r] = ht1.get(r, 0) + 1 
        # for m in magazine:
        #     ht2[m] = ht2.get(m, 0) + 1
        # res = []
        # for k in ht1:
        #     if k in ht2 and ht1[k] <= ht2[k]:
        #         res.append(True)
        #     else: res.append(False)
        # return all(res)
        