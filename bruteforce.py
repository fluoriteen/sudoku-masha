class BruteforceSolution :
    def __init__(self, grid, metrics: dict, play: bool) :
        self.root_n = grid.root_n
        self.n = grid.n
 
        self.grid = grid
        self.metrics = metrics
        self.is_finished = False

        # rows, cols and boxes list caches
        r = range(self.n)
        self.r_cache = [[False]*(self.n+1) for _ in r]
        self.c_cache = [[False]*(self.n+1) for _ in r]
        self.b_cache = [[False]*(self.n+1) for _ in r]

        # print iteratively
        self.play = play


    def preprocess(self) :
        for idx in self.grid.clues :
            clue = int(self.grid.arr[idx])
            row, col, box = self.grid.mapping[idx]
            self.r_cache[row][clue] = True
            self.c_cache[col][clue] = True
            self.b_cache[box][clue] = True
                

    def solve(self, idx: int) :
        self.metrics['count_choose'] += 1

        # if we're out of sudoku array - finish and quit recursion
        if idx > self.n**2 - 1 :
            self.is_finished = True
            return self.is_finished

        row, col, box = self.grid.mapping[idx]

        if self.grid.arr[idx] == 0:
            for k in range(1,self.n+1) :

                # display iterations of candidate selection
                if self.play :
                    self.grid.arr[idx] = k
                    self.grid.show_step()
                    self.grid.arr[idx] = 0

                if (self.r_cache[row][k] or self.c_cache[col][k] or self.b_cache[box][k]) == False :
                 
                    # choose
                    self.grid.arr[idx] = k
                    self.r_cache[row][k] = True
                    self.c_cache[col][k] = True
                    self.b_cache[box][k] = True

                    # explore and break if exploring returned True
                    if self.solve(idx+1) : break
                    self.metrics['count_unchoose'] += 1

                    # unchoose
                    self.grid.arr[idx] = 0
                    self.r_cache[row][k] = False
                    self.c_cache[col][k] = False
                    self.b_cache[box][k] = False

            # if all 1..9 numbers were checked return current puzzle state and take step back
            return self.is_finished

        return self.solve(idx+1)
