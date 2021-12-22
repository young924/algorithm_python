#
# 1927. 최소 힙
# https://www.acmicpc.net/problem/1927
#

import heapq, sys

heap = []

N = int(sys.stdin.readline())

for _ in range(N):
    input = int(sys.stdin.readline())
    if input == 0:
        if len(heap) == 0: 
            result = 0
        else:
            result = heapq.heappop(heap)
        print(result)
    else:
        heapq.heappush(heap, input)
