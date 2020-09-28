import time

from bruteforce import BruteforceSolution
from bitwise import BitwiseSolution
from dlx import DLXSolution

from utils.grid import Grid
from tests.tests import *

class Sudoku :
    def __init__(self, values: str, name = '', n = 9) :
        self.grid = Grid(values)
        self.name = name
        self.is_solved = False

        self.solvers = {
            'bruteforce': BruteforceSolution,
            'bitwise': BitwiseSolution,
            'dlx': DLXSolution
        }

        # analysis
        self.metrics = {
            'preprocessing': 0,
            'solving': 0,
            'total': 0,
            'count_choose': 0,
            'count_unchoose': 0
        }


    def display(self, processor: str, show_result = True) :
        res = ''

        if show_result :
            res = self.grid.visual() if self.is_solved else 'No solution found'

        print(f''' =====================================================
                \r {self.name} / {self.grid.n}x{self.grid.n} / {processor}
                \r number of clues: {len(self.grid.clues)}

                \r preprocessing time: {self.metrics['preprocessing']*1000:.3f}ms 
                \r solving time: {self.metrics['solving']:.3f}s
                \r total time: {self.metrics['total']:.3f}s

                \r count choose: {self.metrics['count_choose']}
                \r count unchoose: {self.metrics['count_unchoose']}
                \r {res}''')


    def solve(self, solver = 'dlx') :
        s = self.solvers[solver](self.grid, self.metrics)
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
        self.is_solved = self.grid.validate()
        
        # record timing
        self.metrics['solving'] = time.time() - ts_solving
        self.metrics['preprocessing'] = ts_solving - ts_preprocessing
        self.metrics['total'] = self.metrics['preprocessing'] + self.metrics['solving'] 

        # show solution
        self.display(solver, False)

        # clear solution
        self.grid.clear()


# ==================================================
# ==================================================
for t in range(len(Tests9x9)):
    game = Sudoku(Tests9x9[t], f"case {t}")
    game.solve()

for t in range(len(Tests16x16)):
    game = Sudoku(Tests16x16[t], f"case {t}")
    game.solve()


# ==================================================
# ==================================================

# game = Sudoku(Tests9x9[0], 'case 13', 9)
# game.solve('dlx')