n = int(input())
board = []
for i in range(n):
    board.append(input())
print(board)
win = '-'
for i in range(n):
    for j in range(n - 2):
        if board[i][j] == board[i][j+1] == board[i][j + 2] != '.':
            win = board[i][j]
        if board[j][i] == board[j + 1][i] == board[j + 2][i] != '.':
            win = board[j][i]

print(win)

