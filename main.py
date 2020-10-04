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


    def validate(self) -> bool:
        # referral sum is the sum of all candidates appearing in each row (col, box)
        # it's the sum of first n items of arithmetic progression: 1..n 
        n = self.grid.n
        ref_sum = int(0.5 * (1 + n) * n)
        

        for solution in self.solutions :
            for i in range(n) :
                row_sum = 0
                for j in range(n) :
                    row_sum += solution[(i * n) + j]
                
                if row_sum != ref_sum :
                    self.solutions.remove(solution)


    def display(self, processor: str, show_result = True) :
        count_solutions = len(self.solutions)

        print(f''' =====================================================
                \r {self.grid.n}x{self.grid.n} / {processor}
                \r number of clues: {len(self.grid.clues)}
                \r total time: {self.metrics['total']:.3f}s
                \r count choose: {self.metrics['count_choose']}''')

        if count_solutions == 0 :
            print('No solution found')
        
        else :
            counter_msg = f'\n There are {count_solutions} solutions' if count_solutions > 1 else f' There is {count_solutions} solution'
            print(counter_msg)
            
            self.grid.arr = self.solutions[0]
            print(self.grid.visual())
                


    def solve(self, solver = 'dlx', show_iteration = False) :
        s = self.solvers[solver](self.grid, self.metrics, show_iteration)
        self.metrics = s.metrics
        self.solutions = s.solutions

        # show initial sudoku grid
        # print(s.grid.visual())

        # pre-process
        ts_preprocessing = time.time()
        s.preprocess()
          
        # solve sudoku
        ts_solving = time.time()
        s.solve(0)

        # check solution
        self.is_solved = len(self.solutions) > 0
        
        # record timing
        self.metrics['solving'] = time.time() - ts_solving
        self.metrics['preprocessing'] = ts_solving - ts_preprocessing
        self.metrics['total'] = self.metrics['preprocessing'] + self.metrics['solving'] 

        # show solution
        self.display(solver)

        # clear solution
        self.grid.clear()


# ==================================================
# ==================================================

# for t in range(len(Tests9x9_2)):
#     game = Sudoku(Tests9x9_2[t], f"case {t}")
#     game.solve()


# dlx_results_file = open('tests/bruteforce_results.txt', 'w')
# [dlx_results_file.writelines(result) for result in results]
# dlx_results_file.close()


# ==================================================
# ==================================================

game = Sudoku(Tests9x9[1], '9x9')
game.solve('bitwise', False)