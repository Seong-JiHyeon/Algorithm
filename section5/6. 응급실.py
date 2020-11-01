import sys
from collections import deque
sys.stdin=open("input.txt", "r")
#같은 위험도가 들어가기 때문에 내림차순 정렬로 해서는 안됨 -> 시뮬레이션 필요 

n, m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))] #몇 번째 환자인지 알기 위해 enumerate 사용 

Q=deque(Q)
cnt=0

while True:
    cur=Q.popleft() #가장 앞에 있는 환자 꺼냄 
    
    if any(cur[1]<x[1] for x in Q): #1 index는 위험도를 나타내고, 0 index는 position을 나타냄 
        #현재 환자(cur)보다 큰 위험도를 가진 환자가 Q안에 있다면 cur을 뒤에 append 
        Q.append(cur)
    else:
        cnt+=1 #현재 환자가 진료를 받으므로 count를 +1 
        if cur[0]==m: #m번째 사람이 진료를 받는 순서를 알게 되면 break 
            print(cnt)
            break
