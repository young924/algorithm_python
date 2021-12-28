#
# 11725. 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
#

import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
tree = [ [] for _ in range(N+1) ]
result = [ 0 for _ in range(N+1) ]

def dfs(index):
    for node_num in tree[index]:
        if result[node_num] == 0:
            result[node_num] = index
            dfs(node_num)

for _ in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

result[1] = 1
dfs(1)

for i in range(2, N+1):
    print(result[i])
