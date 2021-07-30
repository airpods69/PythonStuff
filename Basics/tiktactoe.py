board = {'1':'1' , '2':'2' , '3':'3' ,
         '4':'4' , '5':'5' , '6':'6' ,
         '7':'7' , '8':'8' , '9':'9' }

def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' +  board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' +  board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' +  board['9'])

print_board(board)

def check(board):
    L = list(board.values())
    if (L[0]==L[4]==L[8] or L[2]==L[4]==L[9]):
        return True
    elif (row_checker==True):
        return True
    elif (column_checker==True):
        return True
    else:
        return False

def column_checker(board):
    L = board.values()
    for i in range(3):
        if (L[i]==L[i+3]==L[i+6]):
            return True
    return False

def row_checker(board):
    L = board.values()
    for i in range(3):
        if (L[i]==L[i+1]==L[i+2]):
            return True
    return False

turn = 'X'

while(check(board)==False):

    print_board(board)
    print("turn of " + turn)
    
    move = str(input())
    
    board[move] = turn
    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
