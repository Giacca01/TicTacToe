# Defining Global Variables and Data Structures
players_names = {
    "X": "Computer",
    "O": "Human",
    "Tie": "No One"
}
players = ["X", "O"]
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
ai = "X"
human = "O"
current_player = human
scores = {
  "X": 10,
  "O": -10,
  "Tie": 0
}


# Main Function Implementation
def main():
    """
    Simple Tic Tac Toe game that implements the Minimax algorithm in order to create a simple artificial challenger
    """
    print_board()
    best_move()


# Function that prints the game board
def print_board():

    for i in range(3):
        for j in range(3):
            spot = board[i][j]
            if spot == human:
                print(f" {human} |", end="")
            elif spot == ai:
                print(f" {ai} |", end="")
            else:
                print(f"   |", end="")
        print("\n")

    # Check the board's state to determine if a player has won
    result = check_winner()

    # Print Winner if available otherwise go ahead to play a new turn
    if result is not None:
        print(f"The Winner is {players_names[result]}")
        exit()
    else:
        next_turn()


# Function that prompts the human player for his move
def next_turn():
    global current_player
    i = -1
    j = -1

    if current_player == human:
        # Check input validity
        while i < 0 or i > 2 or j < 0 or j > 2:
            move = input("\nMove (row col) ==> ")
            i = int(move.split(" ")[0])
            j = int(move.split(" ")[1])
        # If the place selected by the player is free insert his placeholder otherwise ask for the input again
        if board[i][j] == " ":
            board[i][j] = human
            current_player = ai
            best_move()
        else:
            next_turn()


# Check possible combinations to determine whether there is a winner
def check_winner():
    winner = None
    result = ""

    # horizontal
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != " ":
            winner = board[i][0]

    # vertical
    for j in range(3):
        if board[0][j] == board[1][j] and board[0][j] == board[2][j] and board[0][j] != " ":
            winner = board[0][j]

    # Diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != " ":
        winner = board[0][0]
    if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] != " ":
        winner = board[2][0]

    # Loop through the board to count the number of free cells (required to detect draws)
    open_spots = 0
    for k in range(3):
        for y in range(3):
            if board[k][y] == " ":
                open_spots += 1

    if winner is None and open_spots == 0:
        result = "Tie"
    else:
        result = winner

    return result


# Compute best move available using Minimax algorithm
def best_move():
    global current_player
    best_score = -500
    move = tuple()
    check_winner()

    # Count the score for each available cell and make the AI's move in the cell with the highest score (the most favorable one)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if len(move) != 0:
        board[move[0]][move[1]] = ai

    current_player = human
    print_board()
    next_turn()


# Calculate the score of each scenario with a recursive implementation
# Minimax explanation ==> https://en.wikipedia.org/wiki/Minimax
def minimax(board_minimax, depth, is_max):
    # Look for possible winners
    result = check_winner()
    if result is not None:
        return scores[result]

    # Determine if the move has to maximise the score (AI) or to minimise it (Human)
    if is_max:
        best_score = -500
        for i in range(3):
            for j in range(3):
                if board_minimax[i][j] == " ":
                    board_minimax[i][j] = ai
                    score = minimax(board_minimax, depth + 1, False)
                    board_minimax[i][j] = " "
                    best_score = max(score, best_score)
    else:
        best_score = 500
        for i in range(3):
            for j in range(3):
                if board_minimax[i][j] == " ":
                    board_minimax[i][j] = human
                    score = minimax(board_minimax, depth + 1, True)
                    board_minimax[i][j] = " "
                    best_score = min(score, best_score)

    return best_score


main()
