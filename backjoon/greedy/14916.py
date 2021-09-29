
#
# 14916. 거스름돈
# https://www.acmicpc.net/problem/14916
#

import sys

def coin(n):
    num5 = n // 5
    rest = n % 5
    if rest % 2 == 1:
        num5 -= 1
        rest += 5
        if num5 < 0: return -1
    num2 = rest // 2
    return num5 + num2

n = int(sys.stdin.readline())

print(coin(n))
