#
# 1003. 피보나치 함수
# https://www.acmicpc.net/problem/1003
#

import sys

fibonacci = [ [1, 0], [0, 1] ]

def dp(n):
    if n == 0: return fibonacci[0]
    if n == 1: return fibonacci[1]

    for i in range(len(fibonacci), n+1):
        fibonacci.append([ fibonacci[i-1][0] + fibonacci[i-2][0], fibonacci[i-1][1] + fibonacci[i-2][1] ])
    
    return fibonacci[n]

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    result = dp(N)
    print(result[0], result[1])
