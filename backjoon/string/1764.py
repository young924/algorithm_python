#
# 1764. 듣보잡
# https://www.acmicpc.net/problem/1764
#

import sys 

N, M = map(int, sys.stdin.readline().split())
hear = {}
cnt = 0
result = []

for i in range(N):
    hear[sys.stdin.readline().rstrip()] = 1

for i in range(M):
    see = sys.stdin.readline().rstrip()
    if hear.get(see, 0) == 1:
        cnt += 1
        result.append(see)

result.sort(reverse=False)

print(str(cnt)+"\n"+"\n".join(result))

