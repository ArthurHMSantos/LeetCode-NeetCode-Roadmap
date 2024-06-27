# Reutilizei a função pra colocar o numero que mais aparece e depois fui retirando do dicionario o com maior valor e adicionando numa lista para resposta
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        my_list = []
        for number in nums:
            if number in my_dict:
                my_dict[number] += 1
            else:
                my_dict[number] = 1
        
        for numbers in range(k):
            biggest_key = max(my_dict, key=my_dict.get)
            my_list.append(biggest_key)
            del my_dict[biggest_key]

        return my_list
