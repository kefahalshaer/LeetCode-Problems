class Solution:
    def interpret(self, command: str) -> str:
        res =[]
        p = 0
        while(p < len(command)):
            if command[p] == 'G':
                res.append(command[p])
                p+=1 # 1
            elif command[p] == '(' and command[p+1] == ')':
                res.append('o')
                p+= 2 # 3
            elif command[p] == '(' and command[p+1]  == 'a':
                res.append('al')
                p += 4

        return ''.join(res)
                
            
                
        
        