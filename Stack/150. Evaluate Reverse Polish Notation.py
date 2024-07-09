# se numero adiciona na stack, se for operador pega os dois ultimos da stack e faz a operaação substituindo valores, usei um dicionariozinho pq acho feio um milhão de if (ficariam 5 no maximo)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b) 
        }

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                
                result = operators[token](a, b)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]
