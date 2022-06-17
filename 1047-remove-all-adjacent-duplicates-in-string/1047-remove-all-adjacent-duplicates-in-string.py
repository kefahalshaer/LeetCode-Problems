class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else: 
                stack.append(c)
        return ''.join(stack)
    
    ### O(n) time comp. and space comp. ###
    
    '''
    abbaca
    st = [a]
    ----
    st = [a,b]
    -----
    st = [a]
    -----
    st = []
    ------
    st = [c]
    -------
    st = [c,a]
    
    '''