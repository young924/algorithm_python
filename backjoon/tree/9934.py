#
# 9934. 완전 이진 트리
# https://www.acmicpc.net/problem/9934
#

import sys

def traversal(tree, depth, result):
    mid = len(tree) // 2
    result[depth].append(tree[mid])

    if depth + 1 >= K:
        return

    left = tree[:mid]
    right = tree[mid+1:]
    traversal(left, depth+1, result)
    traversal(right, depth+1, result)
    
K = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
result = [ ]

for _ in range(K):
    result.append([])

traversal(tree, 0, result)

for i in range(K):
    print(" ".join(map(str, result[i])))