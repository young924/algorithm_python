#
# 4659. 비밀번호 발음하기
# https://www.acmicpc.net/problem/4659
#

import sys

result = ""
vowels = ['a', 'e', 'i', 'o', 'u']

def check(str):
    if not 'a' in str and not 'e' in str and not 'i' in str and not 'o' in str and not 'u' in str:
        return f'<{str}> is not acceptable.\n'
    for i in range(len(str)-2):
        if (str[i] in vowels and str[i+1] in vowels and str[i+2] in vowels) or (not str[i] in vowels and not str[i+1] in vowels and not str[i+2] in vowels):
            return f'<{str}> is not acceptable.\n'
    for i in range(len(str)-1):
        if str[i] == str[i+1] and str[i] != 'e' and str[i] != 'o':
            return f'<{str}> is not acceptable.\n'
    else: return f'<{str}> is acceptable.\n'

input = sys.stdin.readline().rstrip()

while (input != 'end'):
    result += check(input)
    input = sys.stdin.readline().rstrip()

print(result)
