class Solution:
    def calculator(self, val1, val2, op):
        res = 0
        if op == '+':
            res = val1 + val2
        elif op == '-':
            res = val1 - val2
        elif op == '*':
            res = val1 * val2
        elif op == '/':
            res = int(val1 / val2)
        return res

    def evalRPN(self, tokens):
        stack = []
        ops = ['+', '-', '*', '/']
        for item in tokens:
            if item not in ops:
                stack.append(item)
                print(f"stack After inserting {item}: {stack}")
            else:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                res = self.calculator(op2, op1, item)
                stack.append(res)
                print(f"stack After inserting {res}: {stack}")
        return res if not stack else stack[-1]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
s = Solution()
print(s.evalRPN(tokens))
