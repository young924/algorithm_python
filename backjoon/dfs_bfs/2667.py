#
# 2667. 단지번호붙이기
# https://www.acmicpc.net/problem/2667
#

import sys

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

map = []
visited = []
counts = []

def dfs(x, y, idx, cnt):
    visited.append((x, y))
    cnt += 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if map[nx][ny] == 1 and (nx, ny) not in visited:
                map[nx][ny] = idx
                cnt = dfs(nx, ny, idx, cnt)
    return cnt

N = int(sys.stdin.readline())

for i in range(N):
    map.append( [ int(x) for x in list(sys.stdin.readline().rstrip()) ] )

idx = 1

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and (i, j) not in visited:
            counts.append(dfs(i, j, idx, 0))
            idx += 1

print(idx - 1)

for e in sorted(counts):
    print(e)
    