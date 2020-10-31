import sys
from collections import deque 
#list는 원소를 제거하면 다른 원소들이 빈 자리에 한 칸씩 이동
#하지만 deque는 원소를 제거하더라도 움직이지 않음 (포인터로 표시) -> 훨씬 효율적
sys.stdin=open("input.txt", "r")

n, limit=map(int, input().split())
p=list(map(int, input().split()))

p.sort()
p=deque(p)
cnt=0

while p: #p가 비어있을 때 멈춤
    if len(p)==1: #마지막 한 명인 경우
        cnt+=1
        break
    if p[0]+p[-1]>limit: #최소값과 최대값이 함께 탈 수 없을 때
        p.pop() #최대값만 제거
        cnt+=1
    else: #함께 탈 수 있을 때
        p.popleft() #deque의 앞 뒤로 모두 제거
        p.pop()
        cnt+=1
        
print(cnt)

