class Colors:
    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


class Grid :
    def __init__(self, root_n: int, values = {}) :
        self.root_n = root_n
        self.n = root_n**2
        self.values = values
        self.arr = [-1] * root_n**4
        self.matrix = [[-1] * root_n**2] * root_n**2

        for i in range(self.n) :
            for j in range(self.n) :
                key = str(i+1) + ',' + str(j+1)

                if key in self.values  :
                    self.matrix[i][j] = self.values[key]
                    self.arr[i*self.n + j%self.n] = self.values[key]
    

    def format(self, val: str, *args) -> str :
        output = ''
        
        if val == '0':
            return ''

        if len(args) == 0 :
            return val

        for arg in args : 
            output += f"{getattr(Colors, arg)}"

        output += val
        output += f"{Colors.endc}" * len(args) 

        return output


    def str_val(self, i: int, p: int, q: int) -> str :
        key = str(p) + ',' + str(q)

        if key in self.values :
            return self.format(f"{self.values[key]}", 'bold', 'yellow')
        
        return self.format(f"{self.arr[i] if self.arr[i] != -1 else '-'}", 'bold', 'green')


    def str_index(self, show: bool, i: int) -> str :
        if not show : 
            return ''
        
        return f"{i+1}"


    def str_coordinate(self, show: bool, p: int, q: int) -> str :
        if not show :
            return ''
        return self.format(f"({p},{q})", 'blue')
   

    def visualize(self, w_coord = False, w_indices = False) :
        str_row_sep = '\n'
        str_col_sep = '\t\t'
        str_val_sep = '\t'
        
        print(str_row_sep)

        str_row = ''
        for i in range(self.n**2) :            
            
            row = i // self.n + 1
            col = i % self.n + 1

            str_row += str_col_sep * (col != 1 and (col-1) % self.root_n == 0) 

            val   = self.str_val(i, row, col)
            index = self.str_index(w_indices, i)
            coord = self.str_coordinate(w_coord, row, col)
            
            str_row += ' '.join( filter(None, [val, coord, index]) )
            str_row += str_val_sep * (col % self.root_n != 0)
            
            if col % self.n == 0 :
                print(f"{str_row}{str_row_sep * (row % self.root_n == 0)}")
                str_row = ''
