#
# 20055. 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055
#

import sys

def process(N, K):
    belt = list(map(int, sys.stdin.readline().split()))
    robot = [ False for _ in range(N) ]

    step = 0
    numOfZero = 0
    
    while True:
        step += 1

        # 1. 회전 & 내리기
        belt.insert(0, belt[2*N-1])
        belt.pop()
        robot.insert(0, False)
        robot.pop()

        robot[N-1] = False

        # 2. 로봇 움직이기
        for i in range(N-2, 0, -1):
            if robot[i] and not robot[i+1] and belt[i+1] > 0:
                robot[i+1] = True
                robot[i] = False
                belt[i+1] -= 1
                if (belt[i+1] == 0): numOfZero += 1

        # 3. 로봇 올리기
        if belt[0] > 0:
            robot[0] = True
            belt[0] -= 1
            if (belt[0] == 0): numOfZero += 1

        # 4. 내구도 체크
        if numOfZero >= K: return step

N, K = map(int, sys.stdin.readline().split())

print(process(N, K))
