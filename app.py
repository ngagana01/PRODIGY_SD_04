

def print_board(board):
    print("\nSolved Sudoku:\n")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()
    print()


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, num, pos):
    row, col = pos

   
    for j in range(9):
        if board[row][j] == num and col != j:
            return False

    
    for i in range(9):
        if board[i][col] == num and row != i:
            return False

    
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


def get_user_input():
    print("Enter the Sudoku puzzle row by row.")
    print("You can enter digits without spaces (530070000)")
    print("OR with spaces (5 3 0 0 7 0 0 0 0)")
    print("Use 0 for empty cells.\n")

    board = []

    for i in range(9):
        while True:
            row = input(f"Enter row {i+1}: ").strip()

           
            if " " in row:
                parts = row.split()
            else:
                parts = list(row)

            if len(parts) != 9:
                print("Invalid input! Enter exactly 9 numbers.")
                continue

            try:
                row_data = [int(num) for num in parts]

                if any(num < 0 or num > 9 for num in row_data):
                    print("Numbers must be between 0 and 9.")
                    continue

                board.append(row_data)
                break

            except ValueError:
                print("Invalid input! Enter only numbers.")

    return board



print("==== Sudoku Solver ====\n")

board = get_user_input()

print("\nSolving Sudoku...\n")

if solve(board):
    print_board(board)
else:
    print("No solution exists for this Sudoku puzzle.")
