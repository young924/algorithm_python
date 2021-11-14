#
# 2630. 색종이 만들기
# https://www.acmicpc.net/problem/2630
#

import sys

N = int(sys.stdin.readline())
board = []
blue = 0
white = 0

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

def divide(x, y, size):
    checkAllSame(x, y, size)
    checkAllSame(x, y+size, size)
    checkAllSame(x+size, y, size)
    checkAllSame(x+size, y+size, size)

def checkAllSame(x, y, size):  
    global blue
    global white
    isSameColor = True

    for i in range(x, x+size):
        for j in range(y, y+size):
            if board[i][j] != board[x][y]:
                isSameColor = False
                break
                
        if not isSameColor:
            break
    
    if isSameColor:
        if board[x][y] == 1: blue += 1
        else: white += 1
    else:
        divide(x, y, size//2)


checkAllSame(0, 0, N)

print(white)
print(blue)