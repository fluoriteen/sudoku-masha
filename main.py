from grid import Grid
from tests import Tests
from listscache import ListsCacheSolution

class SudokuBacktracking :
    def __init__(self, clues = {}, root_n = 3, name = '') :
        self.root_n = root_n
        self.n = root_n**2

        self.grid = Grid(root_n, clues)
        self.clues = clues
        
        self.name = name
        self.solved = False

        self.processors = {
            'listscache': ListsCacheSolution
        }

    
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
            res = self.grid.visual(False, False)

        print(f''' {self.name}
                \r timing: {self.timing:.2f}s 
                \r number of clues: {len(self.clues)}
                \r number of choose: {self.counters[0]}
                \r number of unchoose: {self.counters[1]}
                \r{res}
            ''')


    def solve(self, processor = 'listscache') :
        # initial sudoku grid
        # print(self.grid.visual())

        s = self.processors[processor](self.grid.arr, self.clues, self.root_n)
        self.grid.arr, self.counters, self.timing = s.solve()

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
game = SudokuBacktracking(Tests.case_3, 3, 'case_3')
game.solve()