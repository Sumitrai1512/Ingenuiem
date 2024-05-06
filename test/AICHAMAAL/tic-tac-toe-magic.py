import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*10)

def get_user_move():
    while True:
        user_move=int(input("Please Enter the Position(1-9): "))
        if 1<=user_move<=9:
            break
        else:
            print("Sahi se input daalna bhai")
           
    return user_move
def is_winner(board,player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)


def calculate_computer_move(board,user_symbol,computer_symbol):
    magic_square = [[2,7,6],[9,5,1],[4,3,8]]
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

    for i,j in empty_cells:
        temp_board=[row[:] for row in board]
        temp_board[i][j]=computer_symbol
        if is_winner(temp_board,computer_symbol):
            return i*3+j+1
        
    for i,j in empty_cells:
        temp_board=[row[:] for row in board]
        temp_board[i][j]=user_symbol
        if is_winner(temp_board, user_symbol):
            return i*3+j+1

    return random.choice(empty_cells)[0] * 3 + random.choice(empty_cells)[1] + 1



    return computer_move
    

def play_game():
    board=[[' ' for _ in range(3)]for _ in range(3)]
    user_symbol,computer_symbol='X','O'
    print("Welcome to Tic-Tac-Toe using Magic Square technique!")
    print_board(board)

    for move_num in range(1,10):
        current_player=user_symbol if move_num % 2==1 else computer_symbol


        #Checking WHich Player ki turn and getting their move
        if current_player==user_symbol:
            user_move=get_user_move() 
            row,col=divmod(user_move-1,3)
        else:
            computer_move=calculate_computer_move(board,user_symbol,computer_symbol)
            row,col=divmod(computer_move-1,3)
            print(f"Computer chooses position {computer_move}")

        while board[row][col] !=' ':
            print("ERROR! That position is already taken. Choose a different one.")
            if current_player == user_symbol:
                user_move = get_user_move()
                row, col = divmod(user_move-1, 3)
            else:
                computer_move = calculate_computer_move(board, user_symbol, computer_symbol)
                row, col = divmod(computer_move-1, 3)
                print(f"Computer chooses position {computer_move}")

        #Put the symbol there
        board[row][col] = user_symbol if current_player == user_symbol else computer_symbol
        print_board(board)

        #Check koi winner nikla kya
        if is_winner(board,current_player):
            print(f"{current_player} WINS MKC!!")
            break

        if is_board_full(board):
            print("Tie Ho gaya!!")
            break
        




play_game()
