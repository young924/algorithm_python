#
# 1260. DFS와 BFS
# https://www.acmicpc.net/problem/1260
#

import sys
from collections import deque

def dfs(v):
    visited.append(v)

    for node in sorted(graph[v]):
        if not node in visited:
            dfs(node)

def bfs(v):
    visited = [v]
    queue = deque([v])

    while queue:
        node = queue.popleft()

        for n in sorted(graph[node]):
            if not n in visited:
                queue.append(n)
                visited.append(n)


    return " ".join(map(str, visited))

N, M, V = map(int, sys.stdin.readline().split())
visited = []
graph = dict()

for i in range(N):
    graph[i+1] = []

for m in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    
    graph[node1].append(node2)
    graph[node2].append(node1)


dfs(V)
print(" ".join(map(str, visited)))

print(bfs(V))
