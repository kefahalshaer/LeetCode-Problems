class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0        
        for i in range(len(s)):
            temp = [s[i]]
            for j in range(i+1, len(s)):
                if s[j] not in temp:
                    temp.append(s[j])
                else: break
            if max_len < len(temp):
                max_len = len(temp)
        return max_len
             