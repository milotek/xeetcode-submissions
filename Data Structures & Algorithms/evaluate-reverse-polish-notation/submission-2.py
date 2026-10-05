class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = s.pop()
                a = s.pop()
                if token == "+":
                    s.append(a + b)
                elif token == "-":
                    s.append(a - b)
                elif token == "*":
                    s.append(a * b)
                elif token == "/":
                    s.append(int(a / b))
            else:
                s.append(int(token))
        return s[0]