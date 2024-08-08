from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                boxnum = (3*(i//3))+(j//3)
                if(board[i][j] == "."):
                    continue
                if(board[i][j] in rows[i]):
                    return False
                else:
                    rows[i].update(board[i][j])
                if(board[i][j] in columns[j]):
                    return False
                else:
                    columns[j].update(board[i][j])
                if(board[i][j] in boxes[boxnum]):
                    return False
                else:
                    boxes[boxnum].update(board[i][j])
        return True
    
"""
8. Check valid Sudoku
	- Made 3 lists of sets, one for rows 1-9, (0-8 indices), columns 1-9, and boxes 1-9
	- rows is i, columns is j, then boxes is (3*(i//3))+(j//3)
	- Main issue I ran into, doing rows = [set()] * 9 will make the same set listed 9 times
		so inserting 1 element into the set will insert it for all of the sets, because it is all the same set
	- Instead do rows = [set() for i in range(9)], then pretty straightforward
"""