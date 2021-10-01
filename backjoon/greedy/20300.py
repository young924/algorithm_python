#
# 20300. 서강근육맨
# https://www.acmicpc.net/problem/20300
#

import sys

N = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))
t.sort()

maxSum = 0

if len(t) % 2 != 0: 
    maxSum = t[-1]
    del t[-1]

while len(t) > 0:
    maxSum = max(t[0] + t[-1], maxSum)
    del t[0]
    del t[-1]

print(maxSum)
