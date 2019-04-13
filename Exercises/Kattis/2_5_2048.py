# based on the rules of 2048, input is passed in to simulate a current gamestate
# one final input is the direction to to move the board

#more for my reference than anything, last input is 0/1/2/3 corresponds as such:
direction = {'left','up','right','down'}

#print the board
def print_board(board):
    for x in board:
        print(f'{x[0]} {x[1]} {x[2]} {x[3]}')

#get the inputs
board = []
for _ in range(4):
    board.append(list(map(int, input().split())))

move = int(input())

#do the moving
if move == 0:
    #left
    for row in range(4):
        #run this twice to squish all possible 0's first
        for _ in range(2):
            for col in range(3):
                if board[row][col] == 0 and board[row][col+1] != 0:
                    board[row][col] = board[row][col+1]
                    board[row][col+1] = 0
        #add matching numbers in correct order
        for col in range(3):
            if board[row][col] == board[row][col+1]:
                board[row][col] += board[row][col+1]
                board[row][col+1] = 0
        #squish any 0's made by the addition
        for col in range(3):
            if board[row][col] == 0 and board[row][col+1] != 0:
                board[row][col] = board[row][col+1]
                board[row][col+1] = 0
elif move == 1:
    #up
    for col in range(4):
        #run this twice to squish all possible 0's first
        for _ in range(2):
            for row in range(3):
                if board[row][col] == 0 and board[row+1][col] != 0:
                    board[row][col] = board[row+1][col]
                    board[row+1][col] = 0
        #add matching numbers in correct order
        for row in range(3):
            if board[row][col] == board[row+1][col]:
                board[row][col] += board[row+1][col]
                board[row+1][col] = 0
        #squish any 0's made by the addition
        for row in range(3):
            if board[row][col] == 0 and board[row+1][col] != 0:
                board[row][col] = board[row+1][col]
                board[row+1][col] = 0
elif move == 2:
    #right
    for row in range(4):
        #run this twice to squish all possible 0's first
        for _ in range(2):
            for col in range(3)[::-1]:
                if board[row][col+1] == 0 and board[row][col] != 0:
                    board[row][col+1] = board[row][col]
                    board[row][col] = 0
        #add matching numbers in correct order
        for col in range(3)[::-1]:
            if board[row][col+1] == board[row][col]:
                board[row][col+1] += board[row][col]
                board[row][col] = 0
        #squish any 0's made by the addition
        for col in range(3)[::-1]:
                if board[row][col+1] == 0 and board[row][col] != 0:
                    board[row][col+1] = board[row][col]
                    board[row][col] = 0
elif move == 3:
    #down
    for col in range(4):
        #run this twice to squish all possible 0's first
        for _ in range(2):
            for row in range(3)[::-1]:
                if board[row+1][col] == 0 and board[row][col] != 0:
                    board[row+1][col] = board[row][col]
                    board[row][col] = 0
        #add matching numbers in correct order
        for row in range(3)[::-1]:
            if board[row+1][col] == board[row][col]:
                board[row+1][col] += board[row][col]
                board[row][col] = 0
        #squish any 0's made by the addition
        for row in range(3)[::-1]:
                if board[row+1][col] == 0 and board[row][col] != 0:
                    board[row+1][col] = board[row][col]
                    board[row][col] = 0

#output
print_board(board)