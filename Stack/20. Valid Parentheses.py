# ideia simples, vai adicionando no auxiliar o bracket, se o proximo for um fechamento ele excluir da lista, se não adiciona
class Solution:
    def isValid(self, s: str) -> bool:
        my_map = {"}": "{", ")": "(", "]": "["}

        aux = []

        for char in s:
            if not char in my_map:
                aux.append(char)
                continue
            
            if not aux or aux[-1] != my_map[char]:
                return False
            aux.pop()
        return not aux
