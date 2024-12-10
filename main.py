def print_board(board):
    print("---------")
    for row in board:
        print("|".join(row))
        print("---------")


def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)


def tic_tac_toe():
    board = [[' ' for a in range(3)] for a in range(3)]
    players = ['X', 'O']
    current_player = 0
    player1_number = 0
    player2_number = 0
    position_player1 = []
    position_player2 = []

    while True:

        print_board(board)
        print(f"Player {players[current_player]}'s turn")
        if current_player == 0:
            if player1_number >= 3:
                a = player1_number % 3
                print(f"Attention Player {players[current_player]}! Your pawn at the position of {position_player1[a][0]} row and {position_player1[a][1]} col will be replaced with the new move.")
        else:
            if player2_number >= 3:
                a = player2_number % 3
                print(f"Attention Player {players[current_player]}! Your pawn at the position of {position_player2[a][0]} row and {position_player2[a][1]} col will be replaced with the new move.")

        try:
            row, col = map(int, input("Enter row and column (0, 1, 2) by adding one blank between them: ").split())
        except ValueError:
            print("Please enter valid numbers for row and column.")
            continue

        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid move! Choose a row and column between 0 and 2.")
            continue

        if board[row][col] != ' ':
            print("Cell already taken! Choose another one.")
            continue

        board[row][col] = players[current_player]

        if players[current_player] == players[0]:
            player1_number = player1_number + 1
            if player1_number <= 3:
                position_player1.append([row, col])
            if player1_number > 3:
                a = player1_number %3 - 1
                if a == -1:
                    a = 2
                board[position_player1[a][0]][position_player1[a][1]] = ' '
                position_player1[a] = [row, col]

        else:
            player2_number = player2_number + 1
            if player2_number <= 3:
                position_player2.append([row, col])
            if player2_number > 3:
                a = player2_number %3 - 1
                if a == -1:
                    a = 2
                board[position_player2[a][0]][position_player2[a][1]] = ' '
                position_player2[a] = [row, col]


        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 1 - current_player  # Switch player

if __name__ == "__main__":
    tic_tac_toe()