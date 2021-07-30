def isValidChessBoard(board):
    keys = list(board.keys())
    vals = list(board.values())
    countw=0
    countb=0
    
    for i in vals:
        if i[0]=='b':
            countw+=1
        else:
            countb+=1
    
    countbp = 0
    countwp = 0

    for i in vals:
        if i[0:2] == 'bp':
            countbp+=1
        elif i[0:2] == 'wp':
            countwp+=1

    countbk = 0
    countwk = 0
    for i in vals:
        if i[0:2] == 'bk':
            countbk+=1
        elif i[0:2] == 'wk':
            countwk+=1