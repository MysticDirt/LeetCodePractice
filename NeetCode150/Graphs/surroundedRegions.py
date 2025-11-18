from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Regions touching the border do not get surrounded.
        # It would be easier to check the border, and then move inwards and preserve rather than explore from the middle and reach the border.
        # Check the borders
            # If border is X, continue
            # If border is O, explore time
                # keep track of where the Os are (perhaps in a set of tuples)
        # Then lastly, turn everything into an X except where the indices are in the set
        survivors = set()
        def explore(i, j):
            nonlocal survivors
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if (i, j) not in survivors:
                survivors.add((i, j))
                for direction in directions:
                    x = i + direction[0]
                    y = j + direction[1]
                    if x in range(len(board)) and y in range(len(board[0])):
                        if board[x][y] == 'O':
                            explore(x, y)
        for i in range(len(board)):
            if board[i][0] == 'O':
                explore(i, 0)
            if board[i][-1] == 'O':
                explore(i, len(board[i])-1)
        for j in range(1, len(board[0])-1):
            if board[0][j] == 'O':
                explore(0, j)
            if board[-1][j] == 'O':
                explore(len(board)-1, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in survivors:
                    board[i][j] = 'X'
        
"""
Did not realize it while doing the problem, but explore() is basically just a dfs.
"""