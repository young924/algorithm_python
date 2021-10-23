#
# 5464. 주차장
# https://www.acmicpc.net/problem/5464
#

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))
R = []
W = []
parkingLot = [ False for i in range(N) ]
parkedCar = [ -1 for i in range(M) ]
queue = deque()
result = 0

for i in range(N):
    R.append(int(sys.stdin.readline()))

for i in range(M):
    W.append(int(sys.stdin.readline()))

for i in range(2*M):
    input = int(sys.stdin.readline())

    if (input > 0):             # in
        if False in parkingLot:      # not full
            minIdx = parkingLot.index(False)

            result += R[minIdx] * W[input-1]
            parkedCar[input-1] = minIdx
            parkingLot[minIdx] = True
        else:                           # full
            queue.append(input)
    else:                       # out
        parkedIdx = parkedCar[abs(input)-1]
        parkingLot[parkedIdx] = False

        # queue check
        if len(queue) > 0:
            qIdx = queue.popleft()

            result += R[parkedIdx] * W[qIdx-1]
            parkedCar[qIdx-1] = parkedIdx
            parkingLot[parkedIdx] = True

print(result)