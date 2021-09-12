#
# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
#

import math

def solution(s):
    answer = len(s)

    for i in range(1, math.floor(len(s)/2)+1):
        length = len(s)
        cnt = 1

        for j in range(0, len(s)-i , i):
            if s[j:j+i] == s[j+i:j+i*2]:
                cnt += 1
                length -= i
                if cnt == 2 or cnt == 10 or cnt == 100 or cnt == 1000:
                    length += 1
            else:
                cnt = 1

        if length < answer:
            answer = length

    return answer