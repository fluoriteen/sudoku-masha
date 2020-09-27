import sys
import time
class Grid :
    def __init__(self, root_n: int, values = {}) :
        self.root_n = root_n
        self.n = root_n**2
        self.arr = [0] * root_n**4
        self.values = values

        self.span = self.root_n // 2
        self.no_val = (self.span-1)*' ' + '-'
        
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
    

    def format(self, val: str, *args) -> str :
        output = ''

        if len(args) == 0 :
            return val

        for arg in args : 
            output += f"{self.formatters[arg]}"

        output += val
        output += f"{self.formatters['endf']}" * len(args) 

        return output


    def str_value(self, idx: int, row: int, col: int) -> str :
        key = f"{row} {col}"
        
        if key in self.values :
            return self.format(f"{self.values[key]:>{self.span}d}", 'bold', 'yellow')
        
        return self.format(f"{self.arr[idx]:>{self.span}d}", 'bold', 'blue') if self.arr[idx] != 0 else self.no_val


    def str_index(self, show: bool, idx: int) -> str :
        if not show : 
            return ''
        
        return f"{idx:{''}>2d}"


    def str_coord(self, show: bool, row: int, col: int) -> str :
        if not show :
            return ''
            
        return self.format(f"({row},{col})", 'green')
   

    def show_step(self, interval = 0.2) :
        print(self.visual())
        print('\r')
        time.sleep(interval)


    def visual(self, with_coord = False, with_index = False) -> str :
        str_row_sep = '\n'
        str_col_sep = '     '
        str_val_sep = '  '
        
        str_res = str_row_sep

        str_row = ''
        for i in range(self.n**2) :            
            
            row = i // self.n + 1
            col = i % self.n + 1

            str_row += str_col_sep * (col != 1 and (col-1) % self.root_n == 0) 

            value = self.str_value(i, row, col)
            index = self.str_index(with_index, i)
            coord = self.str_coord(with_coord, row, col)
            
            str_row += ' '.join( filter(None, [value, coord, index]) )
            str_row += str_val_sep * (col % self.root_n != 0)
            
            if col % self.n == 0 :
                row_div = (row % self.root_n == 0)
                str_res += f"{str_row}{str_row_sep * (1 + row_div)}"
                str_row = ''

        return str_res
