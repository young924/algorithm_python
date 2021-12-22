#
# 11279. 최대 힙
# https://www.acmicpc.net/problem/11279
#

import heapq, sys

maxheap = []

N = int(sys.stdin.readline())

for _ in range(N):
    input = int(sys.stdin.readline())
    if input == 0:
        if len(maxheap) == 0: 
            result = 0
        else:
            result = heapq.heappop(maxheap)[1]
        print(result)
    else:
        heapq.heappush(maxheap, (-input, input))
