# Python program for a Tic Tac Toe game

# Function to display the game board
def display_board(board):
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("-+-+-")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("-+-+-")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])

# Function to check if a player has won
def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to play the game
def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    players = ["X", "O"]
    current_player = players[0]

    display_board(board)

    while True:
        row = int(input("Enter row (0-2) for " + current_player + ": "))
        col = int(input("Enter column (0-2) for " + current_player + ": "))

        # Check that row and column are in range (0-2)
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Numbers must be 0, 1 or 2. Try again.")
            continue

        if board[row][col] != " ":
            print("Position already taken. Try again.")
            continue

        board[row][col] = current_player
        display_board(board)

        if check_win(board, current_player):
            print(current_player + " wins!")
            break

        if " " not in [pos for row in board for pos in row]:
            print("It's a tie!")
            break

        current_player = players[(players.index(current_player) + 1) % 2]

# Call the main function to start the game
if __name__ == "__main__":
    play_game()