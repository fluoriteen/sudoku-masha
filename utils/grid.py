import sys
import time
import math

class Grid :
    def __init__(self, values: str, n = 9) :
        self.values = [int(x) for x in values.split(' ')]
        self.arr = self.values

        # size
        n = math.sqrt(len(self.arr)) if len(self.arr) != 0 else n
        self.n = int(n)
        self.root_n = int(math.sqrt(n))

        if n != self.n :
            raise Exception(f'Grid is not square! Test case length: {n}')
        
        # cell values
        self.mapping = [None] * self.n**2
        self.clues = {}
        self.solutions = []
        self.preprocess(self.arr)

        # display configs
        self.span = self.root_n // 2
        self.no_val = (self.span-1)*' ' + '-'
        self.separators = {
            'row': '\n',
            'col': '  ',
            'band': '-' * (self.span * self.n + 2*(self.n - 1) + 3*(self.root_n - 1)) + '\n',
            'pillar': '  |  '
        }
        self.formatters = {
            'header': '\033[95m',
            'blue': '\033[94m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'red': '\033[91m',
            'bold': '\033[1m',
            'underline': '\033[4m',
            'endf': '\033[0m'
        }


    def preprocess(self, values: str) : 
        for idx in range(self.n**2) :
            row = idx // self.n
            col = idx % self.n
            box = row // self.root_n * self.root_n + col // self.root_n

            self.mapping[idx] = [row, col, box]

            if len(values) != 0 and values[idx] != 0:
                self.clues.update({idx: True})


    def format(self, val: str, *args) -> str :
        output = ''

        if len(args) == 0 :
            return val

        for arg in args : 
            output += f"{self.formatters[arg]}"

        output += val
        output += f"{self.formatters['endf']}" * len(args) 

        return output


    def str_value(self, idx: int) -> str : 
        val = f"{self.arr[idx]:>{self.span}d}" 

        if idx in self.clues :
            return self.format(val, 'bold', 'yellow')
        
        return self.format(val, 'bold', 'blue') if self.arr[idx] != 0 else self.no_val


    def str_index(self, show: bool, idx: int) -> str :
        if not show : 
            return ''
        
        return f"{idx:{''}>2d}"


    def str_coord(self, show: bool, row: int, col: int) -> str :
        if not show :
            return ''
            
        return self.format(f"({row},{col})", 'green')
   

    def show_step(self, interval = 0.05) :
        print(self.visual())
        print('\r')
        time.sleep(interval)


    def visual(self, with_coord = False, with_index = False) -> str :
        
        str_res = self.separators['row']

        str_row = ''
        for i in range(self.n**2) :            
            row, col, box = self.mapping[i]
            row += 1
            col += 1

            str_row += self.separators['pillar'] * (col != 1 and (col-1) % self.root_n == 0) 

            value = self.str_value(i)
            index = self.str_index(with_index, i)
            coord = self.str_coord(with_coord, row, col)
            
            str_row += ' '.join( filter(None, [value, coord, index]) )
            str_row += self.separators['col'] * (col % self.root_n != 0)
            
            if col % self.n == 0 :
                row_div = (row % self.root_n == 0) and (row != self.n)
                str_res += f"{str_row}{self.separators['row'] + row_div * self.separators['band']}"
                str_row = ''

        return str_res


    def clear(self) :
        self.arr = self.values