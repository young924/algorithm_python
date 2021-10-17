#
# 2493. 탑
# https://www.acmicpc.net/problem/2493
#

import sys

N = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
valueStack = []  # stack에 들어가는 애들은 decreasing
indexStack = []
result = [ 0 ] * N

for i in range(N-1, 0, -1):
    if towers[i-1] < towers[i]:
        valueStack.append(towers[i])
        indexStack.append(i)
    elif towers[i-1] > towers[i]:
        result[i] = i

        while valueStack and valueStack[-1] < towers[i-1]:
            index = indexStack.pop()
            result[index] = i
            valueStack.pop()

print(" ".join(map(str, result)))