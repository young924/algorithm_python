#
# 1874. 스택 수열
# https://www.acmicpc.net/problem/1874
#

import sys

n = int(sys.stdin.readline())
stack = []
idx = 1
result = ''

for i in range(n):
    num = int(sys.stdin.readline())
    
    if len(stack) == 0 or stack[-1] < num:    # 아직 해당 숫자 안 넣은 경우
        while not stack or num != stack[-1]:
            stack.append(idx)
            idx += 1
            result += "+\n"
        stack.pop()
        result += "-\n"
    elif stack[-1] == num:       # 해당 숫자 이미 넣은 경우
        stack.pop()
        result += "-\n"
    else:
        result = "NO"
        break

print(result)
