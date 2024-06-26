# funciona assim: pega um numero, verifica quanto falta para o target e depois ve se o que falta está no hash
# se está, retorna o elemento e o hash como resposta, senão adiciona o elemento atual no hash
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        size = len(nums)

        for i in range(size):
            subtract = target - nums[i]
            if subtract in hash:
                return [hash[subtract], i]
            hash[nums[i]] = i
            
