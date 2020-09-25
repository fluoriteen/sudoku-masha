import time
from tests import Tests

from listscache import ListsCacheSolution
from bitwisecache import BitwiseCacheSolution

class SudokuBacktracking :
    def __init__(self, clues: dict, name = '', root_n = 3) :
        self.root_n = root_n
        self.n = root_n**2

        self.name = name
        self.clues = clues
        self.is_solved = False

        self.processors = {
            'listscache': ListsCacheSolution,
            'bitwisecache': BitwiseCacheSolution
        }

        # analysis
        # - preprocessing timing
        # - solving timing
        # - count choose (recursive calls)
        # - count unchoose
        self.metrics = [0, 0, 0, 0]


    def display(self, processor: str) :
        res = 'No solution found'

        if self.is_solved :
            res = self.grid.visual(False, False)

        print(f''' 
                \r {self.name} / {processor}
                \r number of clues: {len(self.clues)}

                \r preprocessing time: {self.metrics[0]*1000:.3f}ms 
                \r solving time: {self.metrics[1]:.3f}s

                \r count choose: {self.metrics[2]}
                \r count unchoose: {self.metrics[3]}
                \r {res}''')

    
    def validate(self) :
        ref_sum = 45

        for i in range(self.n) :
            row_sum = 0
            for j in range(self.n) :
                row_sum += self.grid.arr[(i * self.n) + j]
            
            if row_sum != ref_sum :
                ref_sum = row_sum
                break

        if 0 not in self.grid.arr and ref_sum == 45 :
            self.is_solved = True


    def solve(self, processor = 'bitwisecache') :
        s = self.processors[processor](self.clues, self.root_n)
        self.grid = s.grid
        self.metrics = s.metrics

        # show initial sudoku grid
        # print(s.grid.visual())

        # pre-process
        ts_preprocessing = time.time()
        s.preprocess()
          
        # solve sudoku
        ts_solving = time.time()
        s.solve(0)

        # check solution
        self.validate()
        
        # record timing
        self.metrics[1] = time.time() - ts_solving
        self.metrics[0] = ts_solving - ts_preprocessing

        # show solution
        self.display(processor)


# ==================================================
# ==================================================

# for name in dir(Tests):
#     if not name.startswith('__') :
#         game = SudokuBacktracking(getattr(Tests, name), name)
#         game.solve()


# ==================================================
# ==================================================

game = SudokuBacktracking(Tests.case_5)
game.solve('listscache')
game.solve('bitwisecache')