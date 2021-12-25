#
# 1655. 가운데를 말해요
# https://www.acmicpc.net/problem/1655
#

# 1. 최대 힙과 최소 힙을 준비한다.
# 2. 첫 번째 수를 중앙값으로 한다.
# 3. 두 번째부터 입력받은 수를 중앙값과 비교해서 작으면 최대 힙, 크면 최소 힙에 push한다.
# 4. 홀수 번째라면 최대 힙과 최소 힙 중에 사이즈가 작은 힙에 중앙값을 push 하고 그리고 힙 중에 사이즈가 큰 힙의 top을 중앙값으로 한다.

import sys, heapq

minheap = []
maxheap = []
N = int(sys.stdin.readline())
mid = int(sys.stdin.readline())
print(mid)

for i in range(1, N):
    input = int(sys.stdin.readline())
    
    if input > mid:
        heapq.heappush(minheap, input)
    else:
        heapq.heappush(maxheap, (-input, input))  

    if len(maxheap) - len(minheap) > 1 or i % 2 == 1 and len(maxheap) > len(minheap):
        heapq.heappush(minheap, mid)
        mid = heapq.heappop(maxheap)[1]
    if len(minheap) - len(maxheap) > 1:
        heapq.heappush(maxheap, (-mid, mid))
        mid = heapq.heappop(minheap)

    print(mid)