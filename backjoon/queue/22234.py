#
# 22234. 가희와 은행
# https://www.acmicpc.net/problem/22234
#

import sys
from collections import deque

N, T, W = map(int, sys.stdin.readline().split(" "))
queue = deque()
waitingList = []
time = 0
result = ""

for i in range(N):
    queue.append(list(map(int, sys.stdin.readline().split(" "))))

M = int(sys.stdin.readline())

for i in range(M):
    waitingList.append(list(map(int, sys.stdin.readline().split(" "))))

waitingQ = deque(sorted(waitingList, key = lambda x:x[2]))

while True:
    customer = queue.popleft()

    for i in range(T):
        customer[1] -= 1
        result += f"{customer[0]}\n"
        time += 1

        if time >= W:
            print(result)
            sys.exit()

        if waitingQ and waitingQ[0][2] == time:
            queue.append([ waitingQ[0][0], waitingQ[0][1]])
            waitingQ.popleft()

        if customer[1] <= 0:
            break
       
    if customer[1] > 0:
        queue.append(customer)
