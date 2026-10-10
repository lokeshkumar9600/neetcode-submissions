class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) <= 1):
            return False
        stack = []
        pairs  = {'}':'{' ,']':'[' ,')':'('}
        for chars in s:
            if chars in pairs.values():
                stack.append(chars)
            
            if chars in pairs.keys():
                top = ''
                if len(stack) > 0:
                    top = stack[-1]
                
                if top != pairs[chars]:
                    return False
                
                if top == pairs[chars]:
                    stack.pop()
        
        
        if len(stack) == 0:
            return True
        else:
            return False
        