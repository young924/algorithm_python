#
# 16987. 계란으로 계란치기
# https://www.acmicpc.net/problem/15649
#

import sys

eggs = []
N = int(sys.stdin.readline())

for _ in range(N):
    eggs.append(list(map(int, sys.stdin.readline().split())))

def hit(i, cnt):
    if i == N:
        return cnt

    if eggs[i][0] <= 0:
        return hit(i+1, cnt)

    maxCnt = cnt

    for j in range(N):
        if i == j: continue
        if eggs[j][0] <= 0: continue

        eggs[i][0] -= eggs[j][1]
        eggs[j][0] -= eggs[i][1]

        if eggs[i][0] <= 0 and eggs[j][0] <= 0:
            maxCnt = max(hit(i+1, cnt+2), maxCnt)
        elif eggs[i][0] <= 0 or eggs[j][0] <= 0:
            maxCnt = max(hit(i+1, cnt+1), maxCnt)
        else:
            maxCnt = max(hit(i+1, cnt), maxCnt)

        eggs[i][0] += eggs[j][1]
        eggs[j][0] += eggs[i][1]
    
    return maxCnt

print(hit(0, 0))