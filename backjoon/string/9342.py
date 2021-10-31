#
# 9342. 염색체
# https://www.acmicpc.net/problem/9342
#

import sys
import re

def check(str):
    reg = re.compile('\A[A-F]?A+F+C+[A-F]?$\Z')
    if reg.match(str):
        return "Infected!\n"
    else: 
        return "Good\n"

T = int(sys.stdin.readline())
result = ""

for i in range(T):
    input = sys.stdin.readline().rstrip()
    result += check(input)

print(result)