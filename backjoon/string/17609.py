#
# 17609. 회문
# https://www.acmicpc.net/problem/17609
#

############# Time out #############

import sys

def psuedo_palindrome(str):

    for i in range(len(str)):   # exclude ith char
        left = 0
        right = len(str) - 1

        is_palindrome = True
        
        while (left < right):
            if str[left] != str[right]:
                is_palindrome = False
                break

            left += 1
            right -= 1

            if left == i: left += 1
            elif right == i: right -= 1
        
        if is_palindrome: return True

    return False

def palindrome(str):
    is_palindrome = True
    half_len = len(str) // 2

    for i in range(half_len):
        if str[i] != str[-i-1]:
            is_palindrome = False
            break
    
    if is_palindrome: return 0
    elif psuedo_palindrome(str): return 1
    else: return 2

T = int(sys.stdin.readline())
result = ""

for i in range(T):
    input = sys.stdin.readline().rstrip()
    result += f"{palindrome(input)}\n"

print(result)