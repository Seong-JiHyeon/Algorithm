import sys
from collections import deque
sys.stdin=open("input.txt", "r")
#일열의 deque에 왕자들을 넣은 후, k가 아닌 번호를 외친 사람은 pop하여 deque의 뒤에 append 

n, k=map(int, input().split())
q=list(range(1, n+1))

dq=deque(q)

while dq: #dq가 비어있지 않을 때 
    for _ in range(k-1): #k번호를 외치기 전까지 deque뒤에 append 
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft() #k를 외친 사람 pop 
    if len(dq)==1: #왕자가 한 명만 남았을 경우 
        print(dq[0]) 
        dq.popleft() #while문을 끝내기 위해 pop 
