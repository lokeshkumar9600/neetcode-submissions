class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        final = 0
        for operation in tokens:
            if operation in ["+","-","*","/"]:
                x = stack.pop()
                y = stack.pop()
                if operation == "+":
                    stack.append(x + y)
                if operation == "-":
                    stack.append(y-x)
                if operation == "*":
                    stack.append(x*y)
                if operation == "/":
                    stack.append(int(y/x))

            else:
                stack.append(int(operation))

        return stack[-1]

        