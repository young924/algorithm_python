#
# 9012. 괄호
# https://www.acmicpc.net/problem/9012
#

import sys

def check(string):
    stack = []

    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        elif string[i] == ')':
            if len(stack) > 0: stack.pop()
            else: return 'NO'
    if stack: return 'NO' 
    else: return 'YES'

N = int(sys.stdin.readline())

for n in range(N):
    input = sys.stdin.readline().rstrip()
    print(check(input))
