class Solution:
    def isValid(self, s: str) -> bool:
    # valid open and closed parentheses
        openp = "{(["
        closep = "})]"
        
        # valid paren dict
        valid_paren = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        
        # stack
        st = []
        
        # iterate through the string
        for c in s:
            # condition 1 character is a open bracket
            if c in openp:
                st.append(c)
            # condition 2 character is a closed bracket
            elif c in closep:
                if st == []:
                    return False
                t = st.pop()
                if (valid_paren[t] != c):
                    return False
            # condition 3 it's not a bracket of any type
            else:
                return False
            
        # finally if the stack is not empty the the parentheses are invalid
        return st == []