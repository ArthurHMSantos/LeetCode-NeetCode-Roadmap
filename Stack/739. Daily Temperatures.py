# essa não pensei numa solução O(n) sozinho. Vai verificando quanto demorou pra achar um maior e vai dando pop  da stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [] 

        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                aux = stack.pop()
                answer[aux] = index - aux
            stack.append(index)
        return answer
