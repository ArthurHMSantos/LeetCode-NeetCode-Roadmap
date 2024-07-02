# inicialmente eu fiz usando o metodo sort que era o metodo mais obvio, porem fica com O(nlogn) e precisa ser no máximo log(n), enfim. A solução usa set (não queremos repetidos) e vai verificando se existe o anterior do num no set, se tiver adicionar um na contagem, se não reseta e armazena o maior valor, bem simples. log (n)

class Solution: 
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        biggest = 0

        for num in nums:
            if (num - 1) not in nums_set:
                counter = 0
                while (num + counter) in nums_set:
                    counter += 1
                    if counter > biggest:
                        biggest = counter
        return biggest

"""
Solução com sorting que por algum motivo é mais rapida:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        nums.sort()
        size = len(nums)
        biggest = 1
        counter = 1
        
        for i in range(1, size):
            if nums[i] != nums[i - 1]:  
                if nums[i] == nums[i - 1] + 1:
                    counter += 1
                else:
                    if counter > biggest:
                        biggest = counter
                    counter = 1
        
        if counter > biggest:  
            biggest = counter
        
        return biggest
"""
