from grid import Grid
from tests import Test

class Sudoku :
    def __init__(self, clues = {}) :
        self.grid = Grid(3, clues)
        self.n = 9
        self.clues = clues
        self.solved = False

        # Rows, Cols and Boxes caches
        self.r_cache = [dict() for x in range(self.n)]
        self.c_cache = [dict() for y in range(self.n)]
        self.b_cache = [dict() for z in range(self.n)]

        # Analysis
        self.counter = 0


    def solve_cell(self, i: int) :
        
        if i > self.n**2 - 1 :
            self.solved = True
            return True

        row = i // self.n
        col = i % self.n
        box = self.grid.box_map[i]

        key = str(row+1) + ',' + str(col+1)

        if key not in self.clues:
            for j in range(1,10) :
                if j not in self.r_cache[row] and j not in self.c_cache[col] and j not in self.b_cache[box] :
                    # choose
                    self.grid.arr[i] = j
                    self.r_cache[row].update({j: True})
                    self.c_cache[col].update({j: True})
                    self.b_cache[box].update({j: True})

                    # explore
                    self.solve_cell(i+1)

                    # out of loop if sudoku solved
                    if self.solved :
                        break

                    # unchoose
                    self.grid.arr[i] = -1
                    del self.r_cache[row][j]
                    del self.c_cache[col][j] 
                    del self.b_cache[box][j]
            
            # if none of 1..9 numbers fits conditions take step back
            return False

        else : 
            self.grid.arr[i] = self.clues[key] 
                
        
        return self.solve_cell(i+1)


    def solve(self) :
        # Pre-processing for initial cache
        for coords in self.clues :
            i, j = [(int(c) - 1) for c in coords.split(',')]
            self.r_cache[i].update({self.clues[coords]: True})
            self.c_cache[j].update({self.clues[coords]: True})

            box = self.grid.box_map[i*self.n + j%self.n]
            self.b_cache[box].update({self.clues[coords]: True})

        # show initial sudoku
        # self.visualize()

        # solve sudoku
        self.solve_cell(0)

        # show solution
        self.visualize()
        print('================================================' * 6)


    def visualize(self, show_coords = False, show_indices = False) :
        self.grid.visualize(show_coords, show_indices)



# ==================================================
# ==================================================
s1 = Sudoku(Test.case_1)
s = Sudoku(Test.case_3)

s.solve()

    