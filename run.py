from random import randint

# Represents boards that are currently empty
board = []
hidden_board = []
users_board = []


# Will make a grid of 8x8 and append to list above
for i in range(8):
    users_board.append(["U"] * 8)
for i in range(8):
    hidden_board.append(["H"] * 8)
for i in range(8):
    board.append(["O"] * 8)


def print_board(board):
    """Removes all quotes and instead adds blank space."""

    for row in board:
        print(" ".join(row))


def create_ships(board):
    """Generates 5 ships in random locations."""

    for ship in range(5):
        ship_row, ship_col = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_col] == "X":
            ship_row, ship_col = randint(0, 7), randint(0, 7)
        board[ship_row][ship_col] = "X"


def create_user_ships(board):
    """Generates 5 ships in random locations."""

    for ship in range(5):
        ship_row, ship_col = randint(0, 7), randint(0, 7)
        while users_board[ship_row][ship_col] == "X":
            ship_row, ship_col = randint(0, 7), randint(0, 7)
        users_board[ship_row][ship_col] = "X"


def computer_guess():
    """Randomly guesses a row and col."""

    computer_row, computer_col = randint(1, 8), randint(1, 8)
    print("The computer guessed")
    print("row " + str(computer_row) + " "  "col " + str(computer_col))
    return int(computer_row) - 1, int(computer_col) - 1


def get_ship_location():
    """Asks user input for row,col."""

    row = input("Please enter a row between 1-8:\n")
    while row not in '1, 2, 3, 4, 5, 6, 7, 8':
        print("Error enter a number between 1-8")
        row = input("Please enter a row between 1-8:\n")
    col = input("Please enter a column between 1-8:\n")
    while col not in '1, 2, 3, 4, 5, 6, 7, 8':
        print("Error enter a number between 1-8")
        col = input("Please enter a number between 1-8:\n")
    return int(row) - 1, int(col) - 1


def count_hit_ships(board):
    """Iterates through the board to find "X"s"""

    count = 0
    for row in board:
        for col in row:
            if col == "X":
                count += 1
    return count


def count_hit_user_ships(users_board):
    """Iterates through the board to find "X"s"""

    user_count = 0
    for row in users_board:
        for col in row:
            if col == "@":
                user_count += 1
    return user_count


def did_computer_hit():
    """Tells the user if the computer's guess hit them """

    computer_row, computer_col = computer_guess()
    if users_board[computer_row][computer_col] == "X":
        print("Computer hit a battleship")
        users_board[computer_row][computer_col] = "@"
    if users_board[computer_row][computer_col] == "U":
        print("computer missed ")
        users_board[computer_row][computer_col] = "-"
    if count_hit_user_ships(users_board) == 5:
        print("You lost all your battleships are destroyed")
        
         
create_user_ships(users_board)
create_ships(hidden_board)
turns = 9
print("Welcome to battleship")
print("Hit 5 ships within " + str(turns) + " turns")
while turns > 0:
    print("Users board")
    print_board(users_board)
    print("---------------------")
    print("Computer's board")
    print_board(board)
    print("---------------------")
    row, col = get_ship_location()
    if board[row][col] == '-':
        print("You guessed that already")
    elif hidden_board[row][col] == "X":
        print("You hit the battleship you have " + str(turns) + " turns left")
        board[row][col] = "X"
        turns -= 1
        computer_guess()
        did_computer_hit()
    else:
        print("Sorry, you missed you have " + str(turns) + " turns left")
        board[row][col] = '-'
        turns -= 1
        computer_guess()
        did_computer_hit()
    if count_hit_ships(board) == 5:
        print("Well done you sunk all the battleships")
        break
    if turns == 0:
        print("Game over your out of turns!")
    
