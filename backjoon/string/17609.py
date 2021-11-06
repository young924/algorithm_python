#
# 17609. 회문
# https://www.acmicpc.net/problem/17609
#

import sys

def psuedo_palindrome(left, right, str):
    is_palindrome = True

    while left < right:
        if str[left] != str[right]:
            is_palindrome = False
            break

        left += 1
        right -= 1
    
    return is_palindrome

def palindrome(left, right, str):
    is_palindrome = True

    while left < right:
        if str[left] != str[right]:
            is_palindrome = False
            
            if psuedo_palindrome(left+1, right, str):
                return 1
            if psuedo_palindrome(left, right-1, str):
                return 1
            
            break

        left += 1
        right -= 1
    
    if is_palindrome: return 0
    else: return 2

T = int(sys.stdin.readline())
result = ""

for i in range(T):
    input = sys.stdin.readline().rstrip()
    result += f"{palindrome(0, len(input) - 1, input)}\n"

print(result)