#
# 1935. 후위 표기식2
# https://www.acmicpc.net/problem/1935
#

import sys

N = int(sys.stdin.readline())
exp = sys.stdin.readline().rstrip()
nums = []
stack = []

for i in range(N):
    nums.append(int(sys.stdin.readline()))

for i in range(len(exp)):
    if exp[i].isalpha():
        stack.append(nums[ord(exp[i]) - ord('A')])
    else:
        val2 = stack.pop()
        val1 = stack.pop()
        if exp[i] == '+':
            stack.append(val1 + val2)
        elif exp[i] == '-':
            stack.append(val1 - val2)
        elif exp[i] == '*':
            stack.append(val1 * val2)
        elif exp[i] == '/':
            stack.append(val1 / val2)

print("{:.2f}".format(stack[0]))
