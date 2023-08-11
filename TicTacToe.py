import random
def Display(board):
    print("    1   2   3")
    print("  -------------")
    for i in range(3):
        print(f"{i+1} |", end="")
        for j in range(3):
            print("", board[i][j], "|", end="")
        print("\n  -------------")
    

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def is_equal(board):
    for row in board:
        for item in row:
            if item==" ":
                return False
    return True

def next_player(turn):
    if turn == 'X':
        turn = 'O'
    if turn == 'O':
        turn = 'X'
    return turn 

def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    turn = random.choice(['X','O'])
    while True:
        Display(board)
        try:
            row ,col= input(f"turn {turn} Enter (row column): ").split()
            row ,col= int(row)-1 ,int(col)-1
            
            if board[row][col] == " ":
                board[row][col] = turn
                if check_win(board): 
                    Display(board)
                    print(turn, "wins!")
                    break
                elif is_equal(board):
                    Display(board)
                    print("The game equalised.")
                    break
                turn=next_player(turn)
            else:
                print("this if full! Choose another one.")
        except:
            print("Your input is wrong!")
        print("==========================")

tic_tac_toe()