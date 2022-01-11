'''
CSE 210: Programming with classes 
W02 Prove: Tic Tac Toe 
Author: Miguel Secades García
'''


def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    if is_a_draw(board):
        print("Draw")
    if has_winner(board):
        print(f"{next_player(player)}'s won!")

    print("Good game. Thanks for playing!")


def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board


def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()


def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True


def has_winner(board):
    print()
    print("Welcome to the Tic Tac Toe game")
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])


def make_move(player, board):
    square = 0
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    while square < 1 or square > 9:
        print("Incorrect selected position. It must be between 1 and 9")
        print()
        square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player


def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"


if __name__ == "__main__":
    main()
