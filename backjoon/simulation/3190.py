#
# 3190. 뱀
# https://www.acmicpc.net/problem/3190
#

import sys

# 오른쪽부터 시계 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
board = [ [0] * N for _ in range(N)]
board[0][0] = -1
snake = [[0, 0]]

for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    board[x][y] = 1

L = int(sys.stdin.readline())
dirTable = []
for i in range(L):
    t, c = map(str, sys.stdin.readline().rstrip().split())
    dirTable.append([int(t), c])

time = 1
x = 0
y = 0

while True:
    # 머리 늘리기
    x = x + dx[dir]
    y = y + dy[dir]

    # 게임 종료 조건 체크
    if x < 0 or y < 0 or x >= N or y >= N or board[x][y] < 0 or x == snake[0][0] and y == snake[0][1]:
        break

    # 머리 늘리기
    snake.append([x, y])

    # 꼬리 자르기
    if board[x][y] == 0:
        board[snake[0][0]][snake[0][1]] = 0
        del snake[0]
        
    board[x][y] = -1

    # 방향 전환
    if len(dirTable) > 0 and dirTable[0][0] == time:
        dir = (dir + 1) % 4 if dirTable[0][1] == 'D' else (dir - 1) % 4
        del dirTable[0]
    
    time += 1
    
print(time)
