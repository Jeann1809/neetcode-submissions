class Solution:
    def isValid(self, s: str) -> bool:
        keys = { ')' : '(',']' : '[','}' : '{'}
        stack = []
        
        for char in s:
            if char in keys.keys():
                if len(stack)>0 and stack[-1] == keys[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack:
            return False
        else:
            return True
                
