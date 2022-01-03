#
# 5639. 이진 검색 트리
# https://www.acmicpc.net/problem/5639
#

import sys
sys.setrecursionlimit(10000000)

############ 시간 초과 ############
# class Node:
#     def __init__(self, data, parent):
#         self.data = data
#         self.parent = parent
#         self.left = None
#         self.right = None

# val = int(input())
# root = Node(val, None)
# curr = root

# # Preorder Traversal
# def pre_order(curr, val):
#     if val < curr.data:
#         if curr.left:
#             pre_order(curr.left, val)
#         else: curr.left = Node(val, curr)
#     else:
#         if curr.right:
#             pre_order(curr.right, val)
#         else: curr.right = Node(val, curr)

# while True:
#     try:
#         val = int(input())
#     except:
#         break

#     pre_order(root, val)

# # Postorder Traversal
# def post_order(curr):
#     if curr.left:
#         post_order(curr.left)

#     if curr.right:
#         post_order(curr.right)

#     print(curr.data)

# post_order(root)

pre_order = []

while True:
    try:
        val = int(sys.stdin.readline())
    except:
        break
    pre_order.append(val)

def post_order(start, end):
    if start >= end:
        return

    mid = end
    for i in range(start+1, end):
        if pre_order[i] > pre_order[start]:
            mid = i
            break

    post_order(start+1, mid)
    post_order(mid, end)
    print(pre_order[start])

post_order(0, len(pre_order))