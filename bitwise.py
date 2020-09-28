class BitwiseSolution :
    def __init__(self, grid, metrics: dict) :
        self.root_n = grid.root_n
        self.n = grid.n

        self.grid = grid
        self.metrics = metrics
        self.is_finished = False

        # integer caches for 1..9 rows, 1..9 cols, 1..9 boxes
        self.r_cache = [0]*self.n
        self.c_cache = [0]*self.n
        self.b_cache = [0]*self.n


    def preprocess(self) :
        for idx in self.grid.clues :
            clue = int(self.grid.arr[idx])
            row, col, box = self.grid.mapping[idx]
            self.r_cache[row] |= 1<<(clue-1)
            self.c_cache[col] |= 1<<(clue-1)
            self.b_cache[box] |= 1<<(clue-1)
                    
            
    def solve(self, idx: int) :
        self.metrics['count_choose'] += 1

        # if we're out of sudoku array - finish and quit recursion
        if idx > self.n**2 - 1 :
            self.is_finished = True
            return self.is_finished

        row, col, box = self.grid.mapping[idx]

        if self.grid.arr[idx] == 0:
            for k in range(1,self.n+1) :
                p = 1<<(k-1)
                
                # display iterations of candidate selection
                #
                # self.grid.arr[idx] = k
                # self.grid.show_step()
                # self.grid.arr[idx] = 0

                if (self.r_cache[row] & p) + (self.c_cache[col] & p) + (self.b_cache[box] & p) == 0 :
                    
                    # choose
                    self.grid.arr[idx] = k
                    self.r_cache[row] |= p
                    self.c_cache[col] |= p
                    self.b_cache[box] |= p

                    # explore and break if exploring returned True
                    if self.solve(idx+1) : break
                    self.metrics['count_unchoose'] += 1

                    # unchoose
                    self.grid.arr[idx] = 0
                    self.r_cache[row] &= ~p
                    self.c_cache[col] &= ~p
                    self.b_cache[box] &= ~p

            # if all 1..9 numbers were checked return current puzzle state and take step back
            return self.is_finished

        return self.solve(idx+1)
