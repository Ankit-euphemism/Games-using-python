def print_board(board):
    for row in board:
        print("\n")
        print(" | ".join(row))
        print("-"*5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] !=" ":
            return True
        if board[0][i] == board[1][i] == board[2][i]!=" ":
            return True
    if board[0][0]==board[1][1]==board[2][2]!=" ":
        return True
    if board[0][2]==board[1][1]==board[2][0]!=" ":
        return True
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell != " ":
                print("Game is draw")
                return False
    return True

def tic_tac_toe():
    board=[[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        try:
        #User Input
            move=input(f"Player {current_player}, Enter a number between (1-9)or type 'exit' to quit: ")
            if (move.lower()=="exit"):
                print("Exiting the game!")
                break
        
            
            move=int(move)-1
            if move<0 and move>8 or board[move//3][move%3]!=" ":
                print("Invalid move! Try Again.")
                continue
            #Update Board
            board[move//3][move%3]=current_player
        
            if (check_winner(board)):
                print_board(board)
                print(f"Player {current_player} wins the match")
                break
            if(check_draw(board)):
                print_board(board)
                break
            current_player ="O" if current_player=="X" else "X"
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9 or type 'exit'.")
if __name__=="__main__":
    tic_tac_toe()