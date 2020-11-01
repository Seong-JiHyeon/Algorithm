import sys
sys.stdin=open("input.txt", "r")

def DFS(L, sum): #L=level, a의 index의 원소를 사용하겠다/사용하지 않겠다 
    if sum>total//2: #sum이 total의 반값보다 크면 더 이상의 탐색은 의미가 없음 (이미 부분집합의 합이 같지 않기 때문) 
        return
    
    if L==n:
        if sum==(total-sum): #전체의 합에서 부분집합의 합을 뺀 것은 또 다른 부분집합의 합이다 
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L]) #부분집합을 만들면서 sum을 바로 계산한다 
        DFS(L+1, sum) #부분집합에 원소를 포함하지 않는 경우 

        
if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    
    total=sum(a) #전체 집합 원소의 합 
    DFS(0, 0)
    print("NO") #DFS에서 sys.exit이 실행되지 않았을 경우 
