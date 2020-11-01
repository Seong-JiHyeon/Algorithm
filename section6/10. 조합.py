import sys
sys.stdin=open("input.txt", "r")

def DFS(L, s): #s는 start 변수 
    global cnt
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(s, n+1): #한 번 뽑은 수는 다시 뽑을 필요가 없음 (뒷 리스트 인덱스를 넘겨주는 것과 같음) 
            res[L]=i
            DFS(L+1, i+1)
           

        
n, m=map(int, input().split())
res=[0]*(n+1)
cnt=0

DFS(0, 1)
print(cnt)


<파이썬 조합 라이브러리>
from itertools import combinations

for i in combinations([1,2,3,4], 2):
    print(i, end=" ")
#(1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)

 
 
