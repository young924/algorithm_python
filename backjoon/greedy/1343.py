#
# 1343. 폴리오미노
# https://www.acmicpc.net/problem/1343
#

import sys

board = sys.stdin.readline().rstrip()
result = ""
idx = 0

while (idx < len(board)):
    if idx + 4 <= len(board) and board[idx:idx+4] == 'XXXX':
        result += "AAAA"
        idx += 4
    elif idx + 2 <= len(board) and board[idx:idx+2] == 'XX':
        result += "BB"
        idx += 2
    elif board[idx] == '.':
        result += '.'
        idx += 1
    else:
        result = -1
        break

print(result)
    