# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def __init__(self) :
        self.n = 9
        self.solved = False
        
        # Rows, Cols and Boxes caches
        self.r_cache = [dict() for x in range(self.n)]
        self.c_cache = [dict() for y in range(self.n)]
        self.b_cache = [dict() for z in range(self.n)]

        
    def solveCell(self, i: int, j: int) :
        if j > self.n - 1 :
            i += 1
            j = 0
            
        # If we're out of sudoku array - quit recursion
        if i*self.n + j%self.n > self.n**2 - 1 :
            self.solved = True
            return True
        

        box = (j // 3) + (i // 3 * 3)

        if self.board[i][j] == '.':
            for k in range(1,10) :
                str_k = str(k)
                if str_k not in self.r_cache[i] and str_k not in self.c_cache[j] and str_k not in self.b_cache[box] :
                    # choose
                    self.board[i][j] = str_k
                    self.r_cache[i].update({str_k: True})
                    self.c_cache[j].update({str_k: True})
                    self.b_cache[box].update({str_k: True})

                    # explore
                    self.solveCell(i, j+1)

                    # out of loop if sudoku solved
                    if self.solved :
                        break

                    # unchoose
                    self.board[i][j] = '.'
                    del self.r_cache[i][str_k]
                    del self.c_cache[j][str_k] 
                    del self.b_cache[box][str_k]
            
            # if none of 1..9 numbers fits conditions take step back 
            return False                
        
        return self.solveCell(i, j+1)

    
    def solveSudoku(self, board: list) -> None:
        self.board = board
        
        for i in range(self.n) :
            for j in range(self.n) :
                box = (j // 3) + (i // 3 * 3)
                
                if self.board[i][j] != '.' :
                    self.r_cache[i].update({self.board[i][j]: True})
                    self.c_cache[j].update({self.board[i][j]: True})
                    self.b_cache[box].update({self.board[i][j]: True})
        
        self.solveCell(0, 0)
        self.visualize()

    def visualize(self) :
        for i in range(self.n) :
            print(self.board[i])
    

s = Solution()
s.solveSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
])