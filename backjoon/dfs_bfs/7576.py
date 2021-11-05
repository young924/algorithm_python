#
# 7576. 토마토
# https://www.acmicpc.net/problem/7576
#

import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

box = []
ripe_tomatos = []

def bfs(starts):
    level = -1
    queue = deque(starts)

    while queue:
        #print(box)
        queue_size = len(queue)

        while (queue_size > 0):
            tomato = queue.popleft()

            for d in range(4):
                nx = tomato[0] + dx[d]
                ny = tomato[1] + dy[d]

                if nx >= 0 and nx < N and ny >= 0 and ny < M:
                    if box[nx][ny] == 0:
                        box[nx][ny] = 1
                        queue.append((nx, ny))

            queue_size -= 1
        
        level += 1

    for row in box:
        if 0 in row:
            return -1
    
    return level

M, N = map(int, sys.stdin.readline().split())

for i in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))

for x in range(N):
    for y in range(M):
        if box[x][y] == 1:
            ripe_tomatos.append((x, y))

print(bfs(ripe_tomatos))
