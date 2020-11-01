import sys
import heapq as hq
sys.stdin=open("input.txt", "r")

a=[]
while True:
    n=int(input())
    
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a)) #음수를 다시 양수로 바꾼다 
    else:
        hq.heappush(a, -n) #최대힙을 위해 음수로 


