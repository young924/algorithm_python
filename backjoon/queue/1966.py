#
# 1966. 프린터 큐
# https://www.acmicpc.net/problem/1966
#

import sys
from collections import deque

T = int(sys.stdin.readline())

for test in range(T):
    N, M = map(int, sys.stdin.readline().split(" "))
    queue = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 1

    while (len(queue) > 0):
        maxValue = max(queue)
        doc = queue.popleft()
        M -= 1
        if doc != maxValue:   # 중요도가 더 큰 게 있다면
            queue.append(doc)
            if M < 0:
                M += len(queue)
        elif M < 0:     # 뺀 것이 찾고자 하는 값
            break
        else:   # 그냥 프린트
            cnt += 1
    
    print(cnt)