import sys
sys.stdin=open("input.txt", "r")

def DFS(L):
    #이진트리 형태가 아닌 가지가 3개인 트리의 형태 
    global cnt
    
    if L==m: #len(res)=m인 경우 
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt+=1 #counting 
        
    else:
        for i in range(1, n+1):
            res[L]=i #전위순회 (i, x) ... 
            DFS(L+1)

            
if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*n
    cnt=0
    DFS(0)
    print(cnt)

    

<중복 순열 라이브러리 사용>
from itertools import product

for i in product(range(n), repeat=m):
    print(i)

#이진 트리는 값에 대해 넣고, 넣지않고의 선택경우가 있다면 
#지금 문제와 같은 경우는 무조건 넣는 경우밖에 없음 

 
