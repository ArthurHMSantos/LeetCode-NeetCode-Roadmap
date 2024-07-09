# essa foi dificil, tive que apelar para as dicas admito. Inicia uma lista vazka e uma função recursiva com fechador e abridor, se os dois for zero retorna
# se tiver mais abridorr volta a função adicionando um abridor, se tiver mais fechador volta a função adicionando um fechador e assim por diante vai!!
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def recursive_parent(current, opener, closer):
            if opener == 0 and closer == 0:
                result.append(current)
                return
            if opener > 0:
                recursive_parent(current + '(', opener -1, closer)
            if closer > opener:
                recursive_parent(current + ')', opener, closer - 1)
            
        recursive_parent('',n,n)
        return result
