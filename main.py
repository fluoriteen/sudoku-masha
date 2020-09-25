import time
import sys
from grid import Grid
from tests import Tests

class SudokuBacktracking :
    def __init__(self, clues = {}, root_n = 3, name = '') :
        self.name = name
        self.root_n = root_n
        self.grid = Grid(root_n, clues)
        self.n = root_n**2
        self.clues = clues
        self.solved = False
        self.box_map = {}

        # Rows, Cols and Boxes caches
        r = range(self.n)
        self.r_cache = [([None] + [0]*self.n) for _ in r]
        self.c_cache = [([None] + [0]*self.n) for _ in r]
        self.b_cache = [([None] + [0]*self.n) for _ in r]

        # Analysis 
        self.start_time = time.time()
        self.recursive_counter = 0

    
    def output_result(self) :
        res = 'No solution found'

        ref_sum = 45

        for i in range(self.n) :
            row_sum = 0
            for j in range(self.n) :
                row_sum += self.grid.arr[(i * self.n) + j]
            
            if row_sum != ref_sum :
                ref_sum = row_sum
                break

        if 0 not in self.grid.arr and ref_sum == 45 :
            res = self.grid.visual()

        print(f''' {self.name}
                \r timing: {time.time() - self.start_time:.2f}s 
                \r number of clues: {len(self.clues)}
                \r number of recursive calls: {self.recursive_counter}
                \r{res}
            ''')


    def fill_caches(self) :
        for row in range(self.n) :
            for col in range(self.n) :
                coord = f"{row+1} {col+1}"
                box = row // self.root_n + col // self.root_n * self.root_n

                self.box_map.update({coord: box})

                if coord in self.clues :
                    clue = self.clues[coord]
                    self.grid.arr[(row * self.n) + col] = clue
                    self.r_cache[row][clue] = 1
                    self.c_cache[col][clue] = 1
                    self.b_cache[box][clue] = 1


    def solve_cell(self, idx: int) :
        self.recursive_counter += 1

        # If we're out of sudoku array - quit recursion
        if idx > self.n**2 - 1 :
            self.solved = True
            return self.solved

        row = idx // self.n
        col = idx % self.n
        box = self.box_map[f"{row+1} {col+1}"]

        if self.grid.arr[idx] == 0:
            for k in range(1,self.n+1) :

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
            # print(self.grid.visual())
            # print('\r')
            # time.sleep(0.05)
            return self.solved

        
        return self.solve_cell(idx+1)


    def solve(self) :
        # initial sudoku grid
        print(self.grid.visual())
        
        # pre-processing for initial caches: rows, cols, boxes
        self.fill_caches()
          
        # solve sudoku
        self.solve_cell(0)

        # show solution
        self.output_result()


# ==================================================
# ==================================================

# for name in dir(Tests):
#     if not name.startswith('__') :
#         game = SudokuBacktracking(getattr(Tests, name), 3, name)
#         game.solve()


# ==================================================
# ==================================================
game = SudokuBacktracking(Tests.case_5, 3, 'case_5')
game.solve()