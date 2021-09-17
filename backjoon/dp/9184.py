#
# 9184. 신나는 함수 실행
# https://www.acmicpc.net/problem/9184
#

import sys

w = [ [ [0] * 21 for _ in range(22) ] for _ in range(22) ]
w[0][0][0] = 1

def dp(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: return 1
    if a > 20 or b > 20 or c > 20:
        if not w[20][20][20]:
            w[20][20][20] = dp(20, 20, 20)
        return w[20][20][20]
    
    if w[a][b][c] != 0: return w[a][b][c]

    if a < b and b < c:
        w[a][b][c] = dp(a, b, c-1) + dp(a, b-1, c-1) - dp(a, b-1, c)
        return w[a][b][c]
    
    w[a][b][c] = dp(a-1, b, c) + dp(a-1, b-1, c) + dp(a-1, b, c-1) - dp(a-1, b-1, c-1)
    return w[a][b][c]


while True:
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == -1 and b == -1 and c == -1:
        break

    print('w({0}, {1}, {2}) = {3}'.format(a, b, c, dp(a, b, c)))