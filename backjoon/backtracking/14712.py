#
# 14712. 넴모넴모 (Easy)
# https://www.acmicpc.net/problem/14712
#

import sys
    

N, M = map(int, sys.stdin.readline().split())

board = [ [ False for _ in range(M+1) ] for _ in range(N+1) ]
result = 0

def dfs(cnt):
    global result

    if cnt == N*M:
        result += 1
        return
    
    x = cnt // M + 1
    y = cnt % M + 1

    dfs(cnt + 1)

    if not board[x-1][y] or not board[x][y-1] or not board[x-1][y-1]:
        board[x][y] = True
        dfs(cnt + 1)
        board[x][y] = False
    
dfs(0)

print(result)