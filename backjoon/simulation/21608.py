#
# 21608. 상어 초등학교
# https://www.acmicpc.net/problem/21608
#

import sys

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(sys.stdin.readline())

order = []      # 학생 순서
favDict = {}    # 좋아하는 학생 list를 dictionary로 저장
seats = {}

for i in range(N*N):
    inputLine = list(map(int, sys.stdin.readline().split()))
    order.append(inputLine[0])
    favDict[inputLine[0]] = inputLine[1:5]

board = [ [0] * N for _ in range(N) ]

for studentNo in order:
    likeMaxCnt = -1
    likeMaxSeats = []

    # 1. 비어 있는 칸 중 주변에 좋아하는 학생이 많은 칸 정하기
    for i in range(N):
        for j in range(N):

            if board[i][j] == 0:
                cnt = 0

                for d in range(4):
                    nX = i+dx[d]
                    nY = j+dy[d]

                    if nX >= 0 and nY >= 0 and nX < N and nY < N:
                        if board[nX][nY] in favDict[studentNo]:
                            cnt += 1
                
                if cnt > likeMaxCnt:
                    likeMaxCnt = cnt
                    likeMaxSeats = [[i, j]]
                elif cnt == likeMaxCnt:
                    likeMaxSeats.append([i, j])

    # 2. 1번을 만족하는 경우가 여러 개 -> 비어있는 칸이 가장 많은 칸
    if len(likeMaxSeats) == 1:
        x = likeMaxSeats[0][0]
        y = likeMaxSeats[0][1]
        board[x][y] = studentNo
        continue
    else:
        emptyMaxCnt = -1
        emptyMaxSeats = []

        for seat in likeMaxSeats:
            cnt = 0

            for d in range(4):
                nX = seat[0]+dx[d]
                nY = seat[1]+dy[d]

                if nX >= 0 and nY >= 0 and nX < N and nY < N:
                    if board[nX][nY] == 0:
                        cnt += 1

            if cnt > emptyMaxCnt:
                emptyMaxCnt = cnt
                emptyMaxSeats = [ [seat[0], seat[1]] ]
            elif cnt == emptyMaxCnt:
                emptyMaxSeats.append([seat[0], seat[1]])

    # 3-1. 2번을 만족하는 경우가 여러 개면, 행 번호 최대  
    if len(emptyMaxSeats) == 1:
        x = emptyMaxSeats[0][0]
        y = emptyMaxSeats[0][1]
        board[x][y] = studentNo
        continue
    else:
        maxRowSeats = []
        maxRow = 0

        for seat in emptyMaxSeats:
            if seat[0] > maxRow:
                maxRowSeats = [ [seat[0], seat[1]] ]
            elif seat[0] == maxRow:
                maxRowSeats.append([seat[0], seat[1]])
        
    # 3-2. 3-1번을 만족하는 경우가 여러 개면, 열 번호 최대
    if len(maxRowSeats) == 1:
        x = maxRowSeats[0][0]
        y = maxRowSeats[0][1]
        board[x][y] = studentNo
        continue
    else:
        maxColSeat = []
        maxCol = -1

        for seat in maxRowSeats:
            if seat[1] > maxCol:
                maxColSeat = [seat[0], seat[1]]
        
        x = maxColSeat[0]
        y = maxColSeat[1]
        board[x][y] = studentNo

# 만족도 계산        
sum = 0

for i in range(N):
    for j in range(N):
        studentNo = board[i][j]
        cnt = 0

        for d in range(4):
            nX = i+dx[d]
            nY = j+dy[d]

            if nX >= 0 and nY >= 0 and nX < N and nY < N:
                if board[nX][nY] in favDict[studentNo]:
                    cnt += 1
        
        if cnt == 4: sum += 1000
        elif cnt == 3: sum += 100
        elif cnt == 2: sum += 10
        elif cnt == 1: sum += 1

print(sum)


