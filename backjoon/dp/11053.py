#
# 11053. 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
#

import sys

N = sys.stdin.readline()
A = list(map(int, sys.stdin.readline().split()))

dp = [ ]

for i in range(len(A)):
    dp.append(1)

    for j in range(i):
        if A[j] < A[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))