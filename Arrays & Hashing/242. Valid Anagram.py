# Nessa solução utilizei 2 dicionarios e adicionei a cada dicionario os elementos das strings, então comparei ambos
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        my_dict2 = {}

        for char in s:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        for char in t:
            if char in my_dict2:
                my_dict2[char] += 1
            else:
                my_dict2[char] = 1
        
        return my_dict == my_dict2
