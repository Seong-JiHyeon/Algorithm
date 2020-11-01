import sys
from collections import deque
sys.stdin=open("input.txt", "r")

need=input() #필수 과목
n=int(input())

for i in range(n):
    plan=input()
    dq=deque(need)
    
    for x in plan:
        if x in dq: #x가 dq에 있는 경우 중,
            if x!=dq.popleft(): #필수 과목 순서에 맞는지 가장 앞을 꺼내 체크 
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else: #필수 과목을 아예 수강하지 않은 경우 
            print("#%d NO" %(i+1))
