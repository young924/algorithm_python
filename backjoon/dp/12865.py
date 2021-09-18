#
# 12865. 평범한 배낭
# https://www.acmicpc.net/problem/12865
#

import sys

N, K = map(int, sys.stdin.readline().split())
W = [0]
V = [0]
dp = [ [0] * (K+1) for _ in range(N+1) ]

for i in range(N):
    w, v = list(map(int, sys.stdin.readline().split()))
    W.append(w)
    V.append(v)

for i in range(1, N+1):
    for j in range(1, K+1):
        if (W[i] > j):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max( dp[i-1][j], dp[i-1][j-W[i]] + V[i])

print(dp[N-1][K])
