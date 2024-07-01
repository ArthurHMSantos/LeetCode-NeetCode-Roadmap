# Essa foi bem dificil pois não pode usar /, basicamente fiz uma lista armazenando os produtos de x com o produto anterior (prefix) ex: p = x, p2 = p * x2, p3 = p2 *x3,... e depois uma lista fazendo isso de trás pra frente (suffix) ex: p4 = x4, p3 = p4 * x3... p = p2 * x.. 
#Depois é so armazenar a multiplicação entre os elementos de cada lista e fim:
#Vi a melhoria de espaço contudo não pensei em implementar
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = [1] * size
        suffix = [1] * size
        result = [1] * size

        for i in range(1, size):
            prefix[i] = prefix[i - 1] * nums[i-1]

        for i in range(size - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(size):
            result[i] = suffix[i] * prefix[i]

        return result
