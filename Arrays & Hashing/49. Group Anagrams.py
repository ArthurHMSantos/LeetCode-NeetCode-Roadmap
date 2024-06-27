# essa foi mais complicada, basicamente criei um dicionario vazio, itera sobre a lista para pegar cada string e cria uma string "sorteada" para string, depois adicionada ela como uma chave do dicionario e vai adicionando em formato de lista fim
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict ={}
        for string in strs:
            word = ''.join(sorted(string))
            if word in my_dict:
                my_dict[word].append(string)
            else:
                my_dict[word] = [string]
        return list(my_dict.values())
