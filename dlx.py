import time
import sys
import copy
from grid import Grid
from tests import Tests

class Node: 
    def __init__(self) :
        self.up = None
        self.down = None
        self.left = None
        self.right = None


class Header(Node):
    def __init__(self, name: str) :
        self.name = name
        self.size = 0


class Cell(Node):
    def __init__(self) :
        self.col = None


class DoubleLinkedList: 
    def __init__(self, values) :
        self.head = Header('root')
        self.head.up, self.head.down = self.head, self.head
        self.tail = self.head
        self.rows = []


    def add_header(self, name: str) :
        new = Header(name)

        # update new header links
        new.up = new
        new.down = new
        new.left = self.tail
        new.right = self.head

        # update head and tail left and right links
        new.left.right = new
        self.head.left = new
        self.tail = new


    def add_cell(self, col_name: str) -> Cell :
        new = Cell()

        # find column for new cell
        col = self.head
        while col.name != col_name :
            col = col.right

        col.size += 1
        new.col = col

        # integrate new cell in a column
        new.up = col.up
        new.down = col
        new.up.down = new
        new.down.up = new
        return new
    
    
    def add_circular_links(self, period: int) :
        period -= 1
        i = 0
        while i < len(self.rows) - 1 :
            # go through every group of constraints (period) and link them in circle
            left = self.rows[i + period]
            
            for j in range(period) :
                current = self.rows[i + j]
                current.left, current.right = left, self.rows[i + j + 1]
                left = current

            current = self.rows[i + period]
            current.left, current.right = left, self.rows[i]

            i += period + 1

        
class DLXSolution :
    def __init__(self, clues = {}, root_n = 3) :
        self.root_n = root_n
        self.n = root_n**2

        self.grid = Grid(root_n, clues)
        self.clues = clues
        self.is_finished = False


    def cover(self, col: Header) :
        # hide current col
        col.right.left = col.left
        col.left.right = col.right

        # move down
        pointer = col.down
        while pointer != col :

            # move right
            pointer = pointer.right
            while pointer.col != col :
                # hide all node's links to up and down nodes
                pointer.down.up = pointer.up
                pointer.up.down = pointer.down
                pointer.col.size -= 1
                pointer = pointer.right

            pointer = pointer.down


    def uncover(self, col: Header) :
        # move up
        pointer = col.up

        # bring back column links to closest columns
        col.right.left = col
        col.left.right = col

        while pointer != col :

            #move left
            pointer = pointer.left
            while pointer.col != col :
                pointer.col.size += 1

                # bring back node links to its up and down closest nodes
                pointer.down.up = pointer
                pointer.up.down = pointer
                
                pointer = pointer.left

            pointer = pointer.up

        
    def choose_col(self) -> Header :
        size = float('inf')
        header = self.cache.head.right
        col = None

        while header != self.cache.head :
            if header.size < size :
                col = header
                size = col.size
            
            header = header.right

        return col


    def get_token(self, col: Header) -> dict:
        constraint, tokens = col.name.split(':')
        return {constraint: [int(x) for x in tokens.split(' ')]}
    

    def show_step(self) :
        # uncomment time import in order to create time delay between steps
        print(self.grid.visual())
        print('\r')
        time.sleep(0.1)


    def preprocess(self) :
        # rows, cols, boxes and positions list caches
        rng = range(self.n)
        rng1 = range(1, self.n + 1)
        r_cache = [[False]*(self.n+1) for _ in rng]
        c_cache = [[False]*(self.n+1) for _ in rng]
        b_cache = [[False]*(self.n+1) for _ in rng]

        self.cache = DoubleLinkedList(self.clues)
        self.idx_map = {}

        # fill caches
        for row in rng :
            i = row * self.n
            b = row // self.root_n * self.root_n
            for col in rng :
                idx = i + col
                box = b + col // self.root_n
                coord = f"{row+1} {col+1}"

                self.idx_map.update({idx: [row, col, box]})

                if coord in self.clues :
                    clue = self.clues[coord]
                    self.grid.arr[idx] = clue
                    r_cache[row][clue] = True
                    c_cache[col][clue] = True
                    b_cache[box][clue] = True
                    
                else :
                    self.cache.add_header(f"p:{idx}")
                    
        # generate headers for rows, cols, boxes
        for digit in rng :
            for clue in rng1 :
                if not r_cache[digit][clue] :
                    self.cache.add_header(f"r:{digit} {clue}")
                if not c_cache[digit][clue] :
                    self.cache.add_header(f"c:{digit} {clue}")
                if not b_cache[digit][clue] :
                    self.cache.add_header(f"b:{digit} {clue}")
  
        # generate rows
        for idx in range(self.n**2) :
            if not self.grid.arr[idx] :
                for clue in rng1 :
                    row, col, box = self.idx_map[idx]
                    if (r_cache[row][clue] or c_cache[col][clue] or b_cache[box][clue]) == False :
                        self.cache.rows += [
                            self.cache.add_cell(f"p:{idx}"),
                            self.cache.add_cell(f"r:{row} {clue}"),
                            self.cache.add_cell(f"c:{col} {clue}"),
                            self.cache.add_cell(f"b:{box} {clue}")
                        ]

        # link circles inside rows
        self.cache.add_circular_links(4)


    def solve(self, depth: int) :
        if self.cache.head.right == self.cache.head :
            self.is_finished = True
            return True
        
        else :
            col = self.choose_col()
            self.cover(col)

            # move down 
            pointer = col.down
            while pointer != col :
                state = {}
                state.update(self.get_token(col))

                # move right
                pointer = pointer.right
                while pointer.col != col :
                    self.cover(pointer.col)
                    state.update(self.get_token(pointer.col))
                    pointer = pointer.right

                # choose // add current state to solution
                idx = state['p'][0]
                self.grid.arr[idx] = state['r'][1]
                self.show_step()
                
                # explore further, increasing depth
                if self.solve(depth + 1) : break
                
                # unchoose // remove current state from solution
                self.grid.arr[idx] = 0
                self.show_step()

                # move left
                pointer = pointer.left
                while pointer.col != col :
                    self.uncover(pointer.col)
                    pointer = pointer.left

                # move down
                pointer = pointer.down

        self.uncover(col)
        return self.is_finished
