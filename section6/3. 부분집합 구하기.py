import sys
sys.stdin=open("input.txt", "r")

def DFS(v):
    if v==n+1: #이미 노드 DFS(4)가 생성되어서 n+1로 함수 종료 (3에서 종료되면 3이 부분집합에 포함X) 
        for i in range(1, n+1): #index를 1부터 사용하였음 
            if ch[i]==1: #1인 경우 부분집합에 포함된다는 뜻이므로 프린트 한다 
                print(i, end=' ')
        print()
    else:
        #전위 순회 
        ch[v]=1 #원소가 부분집합에 포함된다 
        DFS(v+1)
        
        ch[v]=0 #원소가 부분집합에 포함되지 않는다 
        DFS(v+1)

if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1)
    DFS(1)
    


<itertools의 combination으로 부분집합 구하기>
from itertools import combinations

a=[1,2,3]
result=[]

for i in range(0,len(a)+1):
    c=combinations(a,i)
    result.extend(c)

print(result)
#[(),(1),(2),(3),(1,2),(1,3),(2,3),(1,2,3)]
