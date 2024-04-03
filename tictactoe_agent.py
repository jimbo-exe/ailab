# TASK-2: GAME WITH AI PLAYER. 
# VANIYA TRIPATHI- 102118070, 3BS3
import random

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
        move = input("select position to enter {sym} between 1 to 9: ". format(sym=symbol))
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

#AI Move included in main

#MAIN FUNCTION
def main():
    flag1=0
    print("Tic-Tac-Toe Game")
    printBoard(board)
    a1=input("Human Player Symbol: ")
    a2=input("AI Player Symbol: ")
    first=random.randint(0,1)
    if first==1:
        print("Human plays first")
    elif first==0:
        print("AI plays first")
    for count in range(1,10):
        if count%2==first:
            print("Human's turn")
            playerMove(a1)
            printBoard(board)
        else:
            print("AI's turn")
            #WINNING
            l=a2
            f=a2
            if (board[1]== l and board[2]==l and board[3]==' '):
                board[3]=l
            elif( board[2]==l and board[3]==l and board[1]==' '):
                board[1]=l
            elif( board[1]==l and board[3]==l and board[2]==' '):
                board[2]=l
            elif (board[4]== l and board[5]==l and board[6]==' '):
                board[6]=l
            elif (board[4]== l and board[6]==l and board[5]==' '):
                board[5]=l
            elif( board[5]==l and board[6]==l and board[4]==' '):
                board[4]=l
            elif (board[7]== l and board[8]==l and board[9]==' '):
                board[9]=l
            elif (board[7]== l and board[9]==l and board[8]==' '):
                board[8]=l
            elif (board[8]==l and board[9]==l and board[7]==' ') :
                board[7]=l
            elif (board[1]== l and board[4]==l and board[7]==' '):
                board[7]=l
            elif (board[1]==l and board[7]==l and board[4]==' '):
                board[4]=l
            elif (board[4]==l and board[7]==l and board[1]==' '):
                board[1]=l
            elif(board[3]== l and board[6]==l and board[9]==' '):
                board[9]=l
            elif (board[3] == l and board[9]==l and board[6]==' '):
                board[6]=l
            elif (board[6] == l and board[9]==l and board[3]==' '):
                board[3]=l
            elif (board[2]== l and board[5]==l and board[8]==' '):
                board[8]=l
            elif(board[2]==l and board[8]==l and board[5]==' '):
                board[5]=l
            elif (board[5]==l and board[8]==l and board[2]==' '):
                board[2]=l
            elif (board[1]== l and board[5]==l and board[9]==' '):
                board[9]=l
            elif (board[1]==l and board[9]==l and board[5]==' '):
                board[5]=l
            elif (board[5]==l and board[9]==l and board[1]==' '):
                board[1]=l
            elif(board[3]== l and board[5]==l and board[7]==' '):
                board[7]=l
            elif (board[3]==l and board[7]==l and board[5]==' '):
                board[5]=l
            elif (board[5]==l and board[7]==l and board[3]==' '):
                board[3]=l
            #BLOCKING
            
            elif (board[1]== a1 and board[2]==a1 and board[3]==' '):
                board[3]=a2
            elif( board[2]==a1 and board[3]==a1 and board[1]==' '):
                board[1]=f
            elif( board[1]==a1 and board[3]==a1 and board[2]==' '):
                board[2]=f
            elif (board[4]== a1 and board[5]==a1 and board[6]==' '):
                board[6]=f
            elif (board[4]== a1 and board[6]==a1 and board[5]==' '):
                board[5]=f
            elif( board[5]==a1 and board[6]==a1 and board[4]==' '):
                board[4]=f
            elif (board[7]== a1 and board[8]==a1 and board[9]==' '):
                board[9]=f
            elif (board[7]== a1 and board[9]==a1 and board[8]==' '):
                board[8]=f
            elif (board[8]==a1 and board[9]==a1 and board[7]==' ') :
                board[7]=f
            elif (board[1]== a1 and board[4]==a1 and board[7]==' '):
                board[7]=f
            elif (board[1]==a1 and board[7]==a1 and board[4]==' '):
                board[4]=f
            elif (board[4]==a1 and board[7]==a1 and board[1]==' '):
                board[1]=f
            elif(board[3]== a1 and board[6]==a1 and board[9]==' '):
                board[9]=f
            elif (board[3] == a1 and board[9]==a1 and board[6]==' '):
                board[6]=f
            elif (board[6] == a1 and board[9]==a1 and board[3]==' '):
                board[3]=f
            elif (board[2]== a1 and board[5]==a1 and board[8]==' '):
                board[8]=f
            elif(board[2]==a1 and board[8]==a1 and board[5]==' '):
                board[5]=f
            elif (board[5]==a1 and board[8]==a1 and board[2]==' '):
                board[2]=f
            elif (board[1]== a1 and board[5]==a1 and board[9]==' '):
                board[9]=f
            elif (board[1]==a1 and board[9]==a1 and board[5]==' '):
                board[5]=f
            elif (board[5]==a1 and board[9]==a1 and board[1]==' '):
                board[1]=f
            elif(board[3]== a1 and board[5]==a1 and board[7]==' '):
                board[7]=f
            elif (board[3]==a1 and board[7]==a1 and board[5]==' '):
                board[5]=f
            elif (board[5]==a1 and board[7]==a1 and board[3]==' '):
                board[3]=f

            #ELSE
            elif spaceIsFree(5):
                  board[5]=a2
            elif(spaceIsFree(1)):
                 
                 board[1]=a2
            elif (spaceIsFree(3)):
                board[3]=a2
            elif (spaceIsFree(7)):
                board[7]=a2
            elif (spaceIsFree(9)):
                board[9]=a2
            else:
                flag=0
                while(not flag):
                    val=random.randint(1,9)
                    if (spaceIsFree(val)):
                        board[val]=a2
                        flag=1
                           
            printBoard(board)
            if IsWinner(board,a1):
                    print("HUMAN IS THE WINNER")
                    flag1=1
                    break
            elif IsWinner(board,a2):
                print("AI IS THE WINNER")
                flag1=1
                break
    if flag1==0:
        print("THE GAME IS A DRAW")
    
main()
