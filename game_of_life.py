import time
import os
import boards

class GameOfLife:

    def __init__(self, board):
        self.board = board

        rows, cols = len(self.board), len(self.board[0])
        self.cycle = [[0] * cols for _ in range(rows)]

    def game_of_life(self):
        rows, cols = len(self.board), len(self.board[0])

        cycle = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                state = self.board[r][c]
                adjacent = self.adjacent_tiles(r, c, rows, cols)
                if adjacent == 3:
                    cycle[r][c] = 1
                elif adjacent == 2 and state == 1:
                    cycle[r][c] = 1
                else:
                    cycle[r][c] = 0
                    
        self.board = cycle     

        return     
    

    def adjacent_tiles(self, r: int, c: int, rows: int, cols: int) -> int:
        count = 0

        # Loop through adjacent tiles
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1,-1), (-1,-1), (-1, 1)]:
            nr, nc = r + dr, c + dc

            # Check bounds
            if nr in range(rows) and nc in range(cols):
        
                # Increment count if alive
                if self.board[nr][nc] == 0:
                    continue
                count += 1
        
        return count
    
    def print_board(self):

        for row in self.board:
            print(" ".join('⬜' if cell == 1 else '⬛' for cell in row))
    
    def board_status(self):
        if self.cycle == self.board:
            return True
        return False

game = GameOfLife(boards.board)

while True:
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    game.game_of_life()
    game.print_board()
    
    if game.board_status():
        break
