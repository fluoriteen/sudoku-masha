from grid import Grid
from tests import Test

class SudokuBacktracking :
    def __init__(self, clues = {}) :
        self.grid = Grid(3, clues)
        self.n = 9
        self.clues = clues
        self.solved = False
        self.box_map = {}

        # Rows, Cols and Boxes caches
        r = range(self.n)
        self.r_cache = [[0]*(self.n+1) for _ in r]
        self.c_cache = [[0]*(self.n+1) for _ in r]
        self.b_cache = [[0]*(self.n+1) for _ in r]


    def fill_caches(self) :
        for row in range(self.n) :
            for col in range(self.n) :
                coord = f"{row+1}{col+1}"
                box = row // 3 + col // 3 * 3

                self.box_map.update({coord: box})

                if coord in self.clues :
                    clue = self.clues[coord]
                    self.grid.arr[(row * self.n) + col] = clue
                    self.r_cache[row][clue] = 1
                    self.c_cache[col][clue] = 1
                    self.b_cache[box][clue] = 1


    def solve_cell(self, idx: int) :
        # If we're out of sudoku array - quit recursion
        if idx > self.n**2 - 1 :
            self.solved = True
            return True

        row = idx // self.n
        col = idx % self.n
        box = self.box_map[f"{row+1}{col+1}"]

        if self.grid.arr[idx] == 0:
            for k in range(1,10) :
                if self.r_cache[row][k] + self.c_cache[col][k] + self.b_cache[box][k] == 0 :
                    
                    # choose
                    self.grid.arr[idx] = k
                    self.r_cache[row][k] = 1
                    self.c_cache[col][k] = 1
                    self.b_cache[box][k] = 1

                    # explore and break if exploring returned True
                    if self.solve_cell(idx+1) : break
                    
                    # unchoose
                    self.grid.arr[idx] = 0
                    self.r_cache[row][k] = 0
                    self.c_cache[col][k] = 0
                    self.b_cache[box][k] = 0
            
            # if all 1..9 numbers were checked return current puzzle state and take step back
            # print('=======================================================================================================')
            # self.grid.visualize() 
            return self.solved

        
        return self.solve_cell(idx+1)


    def solve(self) :
        # initial sudoku grid
        self.grid.visualize() 

        # pre-processing for initial caches: rows, cols, boxes
        self.fill_caches()
          
        # solve sudoku
        self.solve_cell(0)

        # show solution
        self.grid.visualize() 


# ==================================================
# ==================================================
game = SudokuBacktracking(Test.case_7)
game.solve()

    