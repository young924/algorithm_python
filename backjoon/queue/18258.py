#
# 18258. 큐 2
# https://www.acmicpc.net/problem/18258
#

import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
result = ""

for i in range(N):
    input = sys.stdin.readline().rstrip()

    if input.startswith('push'):
        queue.append(input.split(" ")[1])
    elif input == 'pop':
        if len(queue) > 0:
            result += f"{queue.popleft()}\n"
        else:
            result += "-1\n"
    elif input == 'size':
        result += f"{len(queue)}\n"
    elif input == 'empty':
        if len(queue) > 0:
            result += "0\n"
        else:
            result += "1\n"
    elif input == 'front':
        if len(queue) > 0:
            result += f"{queue[0]}\n"
        else:
            result += "-1\n"
    elif input == 'back':
        if len(queue) > 0:
            result += f"{queue[len(queue)-1]}\n"
        else:
            result += "-1\n"

print(result)