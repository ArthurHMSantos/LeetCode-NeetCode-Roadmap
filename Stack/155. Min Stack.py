# stack basica e uma que armazena so o menor valor, se pedir o menor retorna o ultimo da min
class MinStack:

    def __init__(self):
        self.my_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.my_stack.append(val)
        if self.min_stack != []:
            val = min(val, self.min_stack[-1])
            self.min_stack.append(val)
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.my_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.my_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
