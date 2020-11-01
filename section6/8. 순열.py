import sys
sys.stdin=open("input.txt", "r")

#중복순열 문제에서 중복을 제외하는 checklist를 만듦  
def DFS(L):
    global cnt
    if L==m: 
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i]==0: #checklist에서 중복 아닌 경우에만 (!= 1)  
                ch[i]=1 #1로 값을 바꿈으로서 순열에 사용되었다고 체크  
                res[L]=i #순열에 포함 
                DFS(L+1)
                ch[i]=0 #checklist의 값을 다시 풀어주어야 부모노드로 돌아가서 다시 check 가능 

                
if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*n
    ch=[0]*(n+1)
    cnt=0
    
    DFS(0)
    print(cnt)


<파이썬 순열 라이브러리>
from itertools import permutations

for i in permutations([1,2,3,4], 2):
    print(i, end=" ")

 
