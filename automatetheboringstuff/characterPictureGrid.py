# characterPictureGrid.py (idea from automatetheboringstuffwithpython)
# Print the list of lists of one-character strings

grids = [['.', '.', '.', '.', '.', '.'], # example of list of lists
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for i in range(len(grids)):
    for grid in grids:
        if i <= len(grid) - 1:
            print(grid[i], end = '')
    if i < len(grid):
        print('\n', end = '')
