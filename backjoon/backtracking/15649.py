#
# 15649. N과 M (1)
# https://www.acmicpc.net/problem/15649
#

import sys

N, M = map(int, sys.stdin.readline().split())

def dfs(result, cnt):
    if cnt == M:
        print(" ".join(map(str, result)))
        return

    for n in range(1, N+1):
        if not n in result:
            dfs(result + [n], cnt+1)

for n in range(1, N+1):
    dfs([n], 1)
