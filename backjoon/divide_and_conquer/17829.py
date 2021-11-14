#
# 17829. 222-풀링
# https://www.acmicpc.net/problem/17829
#

import sys

N = int(sys.stdin.readline())
board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

while len(board) > 1:
    newBoard = []

    for i in range(0, len(board), 2):
        newRow = []

        for j in range(0, len(board), 2):
            square = []
            square.append(board[i][j])
            square.append(board[i+1][j])
            square.append(board[i][j+1])
            square.append(board[i+1][j+1])
            newRow.append(sorted(square)[2])

        newBoard.append(newRow)

    board = newBoard

print(board[0][0])