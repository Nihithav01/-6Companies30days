
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            stack = []
           
            
            for token in tokens:
                if token == "+" or token == "*" or token  == "-" or token == "/":
                    a = stack.pop()
                    b = stack.pop()
                    
                    if token == "+":
                        res  =  a + b
                    elif token == "-":
                        res = b - a
                    elif token == "*":
                        res = a * b
                    elif token == "/":
                        if abs(b) < abs(a):
                            res = 0
                        else:
                            res = b / a
                    
                    stack.append(int(res)) 
                else:
                    stack.append(int(token))
            return stack.pop()
