class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expressions = []

        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                res = self.arithmetic(expressions.pop(), expressions.pop(), token)
                expressions.append(res)
            else:
                expressions.append(int(token))
        return expressions.pop()

    def arithmetic(self, a, b, op) -> int:
        if op == '+':
            return a + b
        elif op == '-':
            return b - a
        elif op == '*':
            return a * b
        else:
            return int(b / a)