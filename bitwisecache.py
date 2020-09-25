# import time
from grid import Grid

class BitwiseCacheSolution :
    def __init__(self, clues: dict, metrics: list, root_n = 3) :
        self.root_n = root_n
        self.n = root_n**2

        self.grid = Grid(root_n, clues)
        self.clues = clues
        
        self.idx_map = {}
        self.metrics = [0]*4
        self.is_finished = False

        # integer caches for 1..9 rows, 1..9 cols, 1..9 boxes
        self.r_cache = [0]*self.n
        self.c_cache = [0]*self.n
        self.b_cache = [0]*self.n


    def preprocess(self) :
        for row in range(self.n) :
            for col in range(self.n) :
                coord = f"{row+1} {col+1}"
                idx = row * self.n + col
                box = row // self.root_n * self.root_n + col // self.root_n

                self.idx_map.update({idx: [row, col, box]})

                if coord in self.clues :
                    clue = self.clues[coord]
                    self.grid.arr[idx] = clue
                    self.r_cache[row] |= 1<<(clue-1)
                    self.c_cache[col] |= 1<<(clue-1)
                    self.b_cache[box] |= 1<<(clue-1)

            
    def solve(self, idx: int) :
        self.metrics[2] += 1

        # if we're out of sudoku array - finish and quit recursion
        if idx > self.n**2 - 1 :
            self.is_finished = True
            return self.is_finished

        row, col, box = self.idx_map[idx]

        if self.grid.arr[idx] == 0:
            for k in range(1,self.n+1) :
                p = 1<<(k-1)

                if (self.r_cache[row] & p) + (self.c_cache[col] & p) + (self.b_cache[box] & p) == 0 :
                    
                    # choose
                    self.grid.arr[idx] = k
                    self.r_cache[row] |= p
                    self.c_cache[col] |= p
                    self.b_cache[box] |= p

                    # explore and break if exploring returned True
                    if self.solve(idx+1) : break
                    self.metrics[3] += 1

                    # unchoose
                    self.grid.arr[idx] = 0
                    self.r_cache[row] &= ~p
                    self.c_cache[col] &= ~p
                    self.b_cache[box] &= ~p

            # if all 1..9 numbers were checked return current puzzle state and take step back
            # print(self.grid.visual())
            # print('\r')
            # time.sleep(0.06)
            return self.is_finished

        return self.solve(idx+1)
