from grid import Grid
from tests import Test

class Sudoku :
    def __init__(self, clues = {}) :
        self.grid = Grid(3, clues)
        self.clues = clues
        self.n = 9
        self.solved = False

    def check_col_sum(self, i: int) :
        counter = 0

        while i > 0 :
            counter += self.grid.arr[i]
            i -= 9            

        return True if counter == 45 else False

    def solve_cell(self, i: int, rows_cache: list, cols_cache: list, boxs_cache: list) :
        #if row == self.n and col > 1 : 
        #    check = self.check_col_sum(i-1)
        #    if not check :
        #        return False

        if i > self.n**2 - 1 :
            self.solved = True
            return self.grid.arr

        row = i // self.n + 1
        col = i % self.n + 1
        box = self.grid.box_map[i]

        if self.grid.arr[i] == -1:
            for j in range(1,10) :
                if j not in rows_cache[row] and j not in cols_cache[col] and j not in boxs_cache[box] :
                    # choose
                    self.grid.arr[i] = j
                    rows_cache[row].update({j: True})
                    cols_cache[col].update({j: True})
                    boxs_cache[box].update({j: True})

                    # explore
                    self.solve_cell(i+1, rows_cache, cols_cache, boxs_cache)

                    # out of loop if sudoku solved
                    if self.solved :
                        break

                    # unchoose
                    self.grid.arr[i] = -1
                    del rows_cache[row][j]
                    del cols_cache[col][j] 
                    del boxs_cache[box][j]
            
            # if none of 1..9 numbers fits conditions take step back
            return False
                
        
        return self.solve_cell(i+1, rows_cache, cols_cache, boxs_cache)

    def solve(self) :
        # todo: +1 empty dict here
        rows_cache = [dict() for x in range(self.n+1)]
        cols_cache = [dict() for y in range(self.n+1)]
        boxs_cache = [dict() for z in range(self.n+1)]

        # Pre-processing for initial cache
        for coords in self.clues :
            i, j = [int(i) for i in coords.split(',')]
            rows_cache[i].update({self.clues[coords]: True})
            cols_cache[j].update({self.clues[coords]: True})
            box = self.grid.box_map[(i-1)*self.n + (j-1)%self.n]
            boxs_cache[box].update({self.clues[coords]: True})

        # show initial sudoku
        # self.visualize()

        # solve sudoku
        self.solve_cell(0, rows_cache, cols_cache, boxs_cache)

        # show solution
        self.visualize() 
        print('================================================' * 6)


    def visualize(self, show_coords = False, show_indices = False) :
        self.grid.visualize(show_coords, show_indices)



# ==================================================
# ==================================================
s = Sudoku(Test.case_1)
s.solve()

    