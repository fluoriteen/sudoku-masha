# import time
from grid import Grid

class ListsCacheSolution :
    def __init__(self, clues: dict, metrics: list, root_n = 3) :
        self.root_n = root_n
        self.n = root_n**2

        self.grid = Grid(root_n, clues)
        self.clues = clues
        
        self.idx_map = {}
        self.metrics = [0]*4
        self.is_finished = False

        # rows, cols and boxes list caches
        r = range(self.n)
        self.r_cache = [([None] + [0]*self.n) for _ in r]
        self.c_cache = [([None] + [0]*self.n) for _ in r]
        self.b_cache = [([None] + [0]*self.n) for _ in r]


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
                    self.r_cache[row][clue] = 1
                    self.c_cache[col][clue] = 1
                    self.b_cache[box][clue] = 1


    def solve(self, idx: int) :
        self.metrics[2] += 1

        # if we're out of sudoku array - finish and quit recursion
        if idx > self.n**2 - 1 :
            self.is_finished = True
            return self.is_finished

        row, col, box = self.idx_map[idx]

        if self.grid.arr[idx] == 0:
            for k in range(1,self.n+1) :

                if self.r_cache[row][k] + self.c_cache[col][k] + self.b_cache[box][k] == 0 :
                 
                    # choose
                    self.grid.arr[idx] = k
                    self.r_cache[row][k] = 1
                    self.c_cache[col][k] = 1
                    self.b_cache[box][k] = 1

                    # explore and break if exploring returned True
                    if self.solve(idx+1) : break
                    self.metrics[3] += 1

                    # unchoose
                    self.grid.arr[idx] = 0
                    self.r_cache[row][k] = 0
                    self.c_cache[col][k] = 0
                    self.b_cache[box][k] = 0

            # if all 1..9 numbers were checked return current puzzle state and take step back
            # print(self.grid.visual())
            # print('\r')
            # time.sleep(0.05)
            return self.is_finished

        return self.solve(idx+1)
