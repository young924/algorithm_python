#
# 10815. 숫자 카드
# https://www.acmicpc.net/problem/10815
#

import sys

def binary_search(arr, num):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return True
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    
    return False

res = ""

N = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split(" "))))

M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))

for num in arr:
    found = binary_search(cards, num)
    if (found): res += "1 "
    else: res += "0 "

print(res)
