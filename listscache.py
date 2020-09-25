import time
from grid import Grid

class ListsCacheSolution :
    def __init__(self, grid: Grid, clues: dict, root_n = 3) :
        self.root_n = root_n
        self.n = root_n**2

        self.grid = grid
        self.clues = clues
        
        self.solved = False
        self.box_map = {}

        # Rows, Cols and Boxes caches
        r = range(self.n)
        self.r_cache = [([None] + [0]*self.n) for _ in r]
        self.c_cache = [([None] + [0]*self.n) for _ in r]
        self.b_cache = [([None] + [0]*self.n) for _ in r]

        self.choose_counter = 0
        self.unchoose_counter = 0


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
        self.choose_counter += 1

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
                    self.unchoose_counter += 1

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
        # pre-processing for initial caches: rows, cols, boxes
        self.fill_caches()
          
        # solve sudoku
        ts = time.time()
        self.solve_cell(0)
        te = time.time()

        return [self.grid.arr, [self.choose_counter, self.unchoose_counter], te - ts]
