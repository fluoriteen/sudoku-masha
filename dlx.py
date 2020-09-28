from utils.llist import Header, DoubleLinkedList
      
class DLXSolution :
    def __init__(self, grid, metrics: dict) :
        self.root_n = grid.root_n
        self.n = grid.n

        self.grid = grid
        self.metrics = metrics
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
                # re-link node's up and down neighbors
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


    def get_value(self, col: Header) -> dict:
        constraint, tokens = col.name.split(':')
        return {constraint: [int(x) for x in tokens.split(' ')]}
    

    def preprocess(self) :
        # rows, cols, boxes and positions list caches
        rng = range(self.n)
        rng1 = range(1, self.n + 1)
        r_cache = [[False]*(self.n+1) for _ in rng]
        c_cache = [[False]*(self.n+1) for _ in rng]
        b_cache = [[False]*(self.n+1) for _ in rng]

        self.cache = DoubleLinkedList()

        # fill caches
        for idx in range(self.n**2) :
            row, col, box = self.grid.mapping[idx]

            if idx in self.grid.clues:
                clue = int(self.grid.arr[idx])
                if r_cache[row][clue] or c_cache[col][clue] or b_cache[box][clue] :
                    raise Exception(f'Duplicates found. Conflict at: {row} {col}')

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
                    row, col, box = self.grid.mapping[idx]
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
                state.update(self.get_value(col))

                # move right
                pointer = pointer.right
                while pointer.col != col :
                    self.cover(pointer.col)
                    state.update(self.get_value(pointer.col))
                    pointer = pointer.right

                idx = state['p'][0]

                # choose // add current state to solution
                self.metrics['count_choose'] += 1
                self.grid.arr[idx] = state['r'][1]
                # self.grid.show_step()
                
                # explore further, increasing depth
                if self.solve(depth + 1) : break

                # unchoose // remove current state from solution
                self.metrics['count_unchoose'] += 1
                self.grid.arr[idx] = 0
                # self.grid.show_step()

                # move left
                pointer = pointer.left
                while pointer.col != col :
                    self.uncover(pointer.col)
                    pointer = pointer.left

                # move down
                pointer = pointer.down

        self.uncover(col)
        return self.is_finished
