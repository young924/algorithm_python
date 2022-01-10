#
# 6443. 애너그램
# https://www.acmicpc.net/problem/6443
#

import sys

N = int(sys.stdin.readline())

def dfs(alpha, arr, depth):
    if depth == 0:
        result = "".join(arr)
        sys.stdout.write(result+"\n")
        return

    for idx, cnt in enumerate(alphabet):
        if cnt != 0:
            alpha[idx] -= 1
            arr.append(chr(idx+ord('a')))
            dfs(alpha, arr, depth-1)
            alpha[idx] += 1
            arr.pop()

for _ in range(N):
    alphabet = [ 0 ] * 26
    dictionary = {}
    word = list(sys.stdin.readline().rstrip())
    for letter in word:
        alphabet[ord(letter) - ord('a')] += 1
    
    dfs(alphabet, [], len(word))
