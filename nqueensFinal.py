from queue import Queue

class NQueen:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_safe(self, board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i] == col:
                return False

            # Check diagonals
            if abs(board[i] - col) == row - i:
                return False

        return True

    def solve(self):
        # Initialize an empty board (1D array)
        board = [-1] * self.n # for example, board[0] = 2 means queen is placed in row 0, column 2

        # Initialize a queue for BFS
        queue = Queue()
        queue.put((board, 0))  # Tuple: (board, row)

        while not queue.empty():
            current_board, row = queue.get()

            # If all queens are placed (last row reached), add solution
            if row == self.n:
                self.solutions.append(current_board)
                continue

            # Try placing queen in each column of the current row
            for col in range(self.n):
                if self.is_safe(current_board, row, col):
                    # Create a new board with the queen placed in the current position
                    new_board = current_board[:] # copy the current board
                    new_board[row] = col
                    # Add the new board and the next row to the queue
                    queue.put((new_board, row + 1))

    def print_solutions(self):
        for solution in self.solutions:
            for row in range(self.n):
                line = ""
                for col in range(self.n):
                    if solution[row] == col:
                        line += "Q "
                    else:
                        line += ". "
                print(line)
            print()

def main():
    n = 4
    q1 = NQueen(n)
    q1.solve()
    q1.print_solutions()


main()