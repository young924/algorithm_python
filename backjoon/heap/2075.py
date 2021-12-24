#
# 2075. N번째 큰 수
# https://www.acmicpc.net/problem/2075
#

import sys, heapq

heap = []
N = int(sys.stdin.readline())

for r in range(N):
    input = list(map(int, sys.stdin.readline().split()))
    for c in range(N):
        if len(heap) < N:
            heapq.heappush(heap, input[c])
            continue

        if heap[0] < input[c]:
            heapq.heappop(heap)
            heapq.heappush(heap, input[c])

print(heap[0])