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


    def display(self, processor: str) :
        res = 'No solution found'

        if self.is_solved :
            res = self.grid.visual()

        print(f''' 
                \r {self.name} / {processor}
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

        # pre-process
        ts_preprocessing = time.time()
        s.preprocess()

        # show initial sudoku grid
        print(s.grid.visual())
          
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
        self.display(solver)


# ==================================================
# ==================================================

# for name in dir(Tests):
#     if not name.startswith('__') :
#         game = SudokuBacktracking(getattr(Tests, name), name)
#         game.solve()


# ==================================================
# ==================================================

game = Sudoku(Tests9x9[15], 'case 13', 9)
game.solve('bruteforce')