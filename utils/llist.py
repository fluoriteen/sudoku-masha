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

  