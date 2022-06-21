class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
        for s in sentences:
            count = s.count(' ') + 1
            max_count = max(max_count,count)
        return max_count
                
            
            
        
        