import time
from tests import Tests

from listscache import BruteforceSolution
from bitwisecache import BitwiseSolution
from dlx import DLXSolution

class Sudoku :
    def __init__(self, clues: dict, name = '', root_n = 3) :
        self.root_n = root_n
        self.n = root_n**2

        self.name = name
        self.clues = clues
        self.is_solved = False

        self.processors = {
            'bruteforce': BruteforceSolution,
            'bitwise': BitwiseSolution,
            'dlx': DLXSolution
        }

        # analysis
        # - preprocessing timing
        # - solving timing
        # - count choose (recursive calls)
        # - count unchoose
        self.metrics = {
            'preprocessing': 0,
            'solving': 0,
            'total': 0,
            'count_choose': 0,
            'count_unchoose': 0
        }


    def display(self, processor: str) :
        res = 'No solution found'

        if self.is_solved :
            res = self.grid.visual()

        print(f''' 
                \r {self.name} / {processor}
                \r number of clues: {len(self.clues)}

                \r preprocessing time: {self.metrics['preprocessing']*1000:.3f}ms 
                \r solving time: {self.metrics['solving']:.3f}s
                \r total time: {self.metrics['total']:.3f}s

                \r count choose: {self.metrics['count_choose']}
                \r count unchoose: {self.metrics['count_unchoose']}
                \r {res}''')

    
    def validate(self) :
        # referral sum is the sum of all candidates appearing in each row (col, box)
        # it's the sum of first n items of arithmetic progression: 1..n 
        ref_sum = int(0.5 * (1 + self.n) * self.n)

        for i in range(self.n) :
            row_sum = 0
            for j in range(self.n) :
                row_sum += self.grid.arr[(i * self.n) + j]
            
            if row_sum != ref_sum :
                ref_sum = row_sum
                break

        if 0 not in self.grid.arr and ref_sum == 45 :
            self.is_solved = True


    def solve(self, processor = 'dlx') :
        s = self.processors[processor](self.clues, self.metrics, self.root_n)
        self.grid, self.metrics = s.grid, s.metrics

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
        self.metrics['solving'] = time.time() - ts_solving
        self.metrics['preprocessing'] = ts_solving - ts_preprocessing
        self.metrics['total'] = self.metrics['preprocessing'] + self.metrics['solving'] 

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

game = Sudoku(Tests.case_5, 'case 3', 3)
# game.solve()
game.solve('bruteforce')