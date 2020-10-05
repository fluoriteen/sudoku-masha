# https://norvig.com/sudoku.html
path = 'tests/'
Tests9x9 = open(path+'9x9.txt', 'r').read().split('\n')
Tests16x16 = open(path+'16x16.txt', 'r').read().split('\n')

# same pattern of clues
Tests9x9_2 = open(path+'9x9-2.txt', 'r').read().split('\n')