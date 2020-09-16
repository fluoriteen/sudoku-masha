from grid import Grid
from tests import Test

class SudokuBacktracking :
    def __init__(self, clues = {}) :
        self.grid = Grid(3, clues)
        self.n = 9
        self.clues = clues
        self.solved = False
        self.box_map = {}

        # Index to block number
        for i in range(self.n) :
            for j in range(self.n) :
                index = i*self.n + j%self.n
                self.box_map.update({index: (j // 3 + i // 3 * 3)  })

        # Rows, Cols and Boxes caches
        self.r_cache = [dict() for x in range(self.n)]
        self.c_cache = [dict() for y in range(self.n)]
        self.b_cache = [dict() for z in range(self.n)]

        # Analysis
        self.counter = 0


    def solve_cell(self, i: int) :
        # If we're out of sudoku array - quit recursion
        if i > self.n**2 - 1 :
            self.solved = True
            return True

        row = i // self.n
        col = i % self.n
        box = self.box_map[i]
        key = str(row+1) + ',' + str(col+1)

        if key not in self.clues:
            for j in range(1,10) :
                if j not in self.r_cache[row] and j not in self.c_cache[col] and j not in self.b_cache[box] :
                    
                    # choose
                    self.grid.arr[i] = j
                    self.r_cache[row].update({j: True})
                    self.c_cache[col].update({j: True})
                    self.b_cache[box].update({j: True})

                    # explore // and break if exploring returned True
                    if self.solve_cell(i+1) : break
                    
                    # unchoose
                    self.grid.arr[i] = -1
                    del self.r_cache[row][j]
                    del self.c_cache[col][j] 
                    del self.b_cache[box][j]
            
            # if all 1..9 numbers were checked return current puzzle state and take step back
            return self.solved

        else : 
            self.grid.arr[i] = self.clues[key] 
                
        
        return self.solve_cell(i+1)


    def solve(self) :
        # initial sudoku grid
        self.grid.visualize() 

        # Pre-processing for initial caches
        for coords in self.clues :
            i, j = [(int(c) - 1) for c in coords.split(',')]
            self.r_cache[i].update({self.clues[coords]: True})
            self.c_cache[j].update({self.clues[coords]: True})

            box = self.box_map[i*self.n + j%self.n]
            self.b_cache[box].update({self.clues[coords]: True})


        # solve sudoku
        self.solve_cell(0)

        # show solution
        self.grid.visualize() 




# ==================================================
# ==================================================

s = SudokuBacktracking(Test.case_5)
s.solve()

    