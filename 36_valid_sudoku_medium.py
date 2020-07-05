def isValidSudoku(board):
    """
    Description:
        Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Idea:
        Store the pairs of (i, item), (item, j), as the positions at which we already encountered the values in set,
        use (i//3, j//3, item) to get the positioning in 3x3 sub-board
    Complexity:
        Time: O(n**2)
        Space: O(n)
    """

    seen = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell != '.':
                if (i, cell) in seen or (cell, j) in seen or (i//3, j//3, cell) in seen:
                    return False
                seen.add((i, cell))
                seen.add((cell, j))
                seen.add((i//3, j//3, cell))
    return True
