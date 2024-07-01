# usar set pq é bom pra exclusividade mas da pra fazer com lista tbm!
# rule 3 verifica se existem numeros de apenas um a 9 naquele grid
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #rule 1
        for row in range(9):
            seen_set = set()
            for column in range(9):
                element = board[row][column]
                if element != '.':
                    if element in seen_set:
                        return False
                    seen_set.add(element)
        
        #rule 2
        for column in range(9):
            seen_set = set()
            for row in range(9):
                element = board[row][column]
                if element != '.':
                    if element in seen_set:
                        return False
                    seen_set.add(element)
        
        #rule 3
        for grid_row in range(3):
            for grid_col in range(3):
                seen_set = set()
                for i in range(3):
                    for j in range(3):
                        num = board[grid_row * 3 + i][grid_col * 3 + j]
                        if num != '.':
                            if num in seen_set:
                                return False
                            seen_set.add(num)
        return True
