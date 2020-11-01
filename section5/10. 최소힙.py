import sys
import heapq as hq #list를 heap으로 작동하도록 도와줌
sys.stdin=open("input.txt", "r")

a=[] #heap생성을 위해서는 list가 필요함 
while True:
    n=int(input())
    
    if n==-1:
        break
    if n==0:
        if len(a)==0: #heap에 자료가 없는 경우 
            print(-1)
        else: #heap에 root노드를 꺼내어 프린트 
            print(hq.heappop(a))
    else:
        hq.heappush(a, n) #list a에 자동으로 heap 정렬 


