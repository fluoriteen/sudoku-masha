from grid import Grid
from tests import Test

class Sudoku :
    def __init__(self, clues = {}) :
        self.grid = Grid(3, clues)
        self.clues = clues
        self.n = 9

    def solve_cell(self, i: int, rows_cache: list, cols_cache: list) :
        row = i // self.n + 1
        col = i % self.n + 1

        if row > self.n :
            return False

        row_cache = rows_cache[row]
        col_cache = cols_cache[col]

        if self.grid.arr[i] == -1:
            for j in range(1,10) :
                if j not in row_cache and j not in col_cache :
                    # choose
                    self.grid.arr[i] = j
                    row_cache.update({j: True})
                    col_cache.update({j: True})

                    # explore
                    self.solve_cell(i+1, rows_cache, cols_cache)

                    # unchoose
                    self.grid.arr[i] = -1
                    del row_cache[j]
                    del col_cache[j]
            
            self.visualize()
            return False
                
        
        self.visualize()    
        return self.solve_cell(i+1, rows_cache, cols_cache)

    def solve(self) :
        # todo: +1 empty dict here
        rows_cache = [dict() for x in range(self.n+1)]
        cols_cache = [dict() for y in range(self.n+1)]

        # Pre-processing for initial cache
        for coords in self.clues :
            i, j = [int(i) for i in coords.split(',')]
            rows_cache[i].update({self.clues[coords]: True})
            cols_cache[j].update({self.clues[coords]: True})

        self.solve_cell(0, rows_cache, cols_cache)
        self.visualize()


    def visualize(self) :
        self.grid.visualize()

# ==================================================
# ==================================================
s = Sudoku(Test.case_1)
s.solve()

    