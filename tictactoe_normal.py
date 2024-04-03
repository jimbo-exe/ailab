# TASK-1: 2 PLAYER GAME. 
# VANIYA TRIPATHI- 102118070, 3BS3

board = [' ' for x in range(10)]

def printBoard(board):
    print('    |     |     ')
    print(' ' + board[1] + '  | ' + board[2] + '   | ' + board[3])
    print('    |     |     ')
    print('----------------')
    print('    |     |     ')
    print(' ' + board[4] + '  | ' + board[5] + '   | ' + board[6])
    print('    |     |     ')
    print('----------------')
    print('    |     |     ')
    print(' ' + board[7] + '  | ' + board[8] + '   | ' + board[9])
    print('    |     |     ')

def IsWinner(b,l):
    return (b[1]== l and b[2]==l and b[3]==l) or (b[4]== l and b[5]==l and b[6]==l) or \
    (b[7]== l and b[8]==l and b[9]==l) or \
    (b[1]== l and b[4]==l and b[7]==l) or (b[3]== l and b[6]==l and b[9]==l) or \
    (b[2]== l and b[5]==l and b[8]==l) or \
    (b[1]== l and b[5]==l and b[9]==l) or (b[3]== l and b[5]==l and b[7]==l)

def spaceIsFree(pos):
    return board[pos]==' '

def insertLetter(letter,pos):
    board[pos]=letter

def playerMove(symbol):
    run = True
    while run:
        move = input("please select a position to enter the {sym} between 1 to 9". format(sym=symbol))
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter(symbol , move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')
        except:
            print('Please type a number')

def main():
    print("starting the game:")

    for turn in range(9):
        current_symbol = 'X' if turn % 2 == 0 else 'O'
        
        printBoard(board)
        playerMove(current_symbol)
        
        #if at last chance, the move doesnt result in a win => tie case.
        if turn==8 and not IsWinner(board, current_symbol):
            printBoard(board)
            print("It's a tie!")
            break

        if IsWinner(board, current_symbol):
            printBoard(board)
            print(f"Player {current_symbol} wins!")
            break

        
if __name__ == "__main__":
    main()


