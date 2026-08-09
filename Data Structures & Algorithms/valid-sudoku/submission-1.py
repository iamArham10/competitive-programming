class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = [set()] * 9
        col_map = [set()] * 9
        box_map = [set()] *9

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element == ".":
                    continue
                
                if element in row_map[i]:
                    return False
                else:
                    row_map[i].add(element)
                
                if element in col_map[j]:
                    return False
                else:
                    col_map[j].add(element)
                
                # box check
                if element in col_map[(i//3)*3 + j//3]:
                    return False
                else:
                    box_map[(i//3)*3 + j//3].add(element)
        
        return True
                    
                

        