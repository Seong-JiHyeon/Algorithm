import sys
sys.stdin=open("input.txt", "r")

def DFS(L, sum):
    global res
    #L값 자체가 동전을 몇 개 사용하였는가를 나타냄 (트리의 레벨이 동전 사용 개수) 
    if L>=res: #현재의 최소값보다 크다면 더이상 탐색할 필요 없음 
        return
    
    if sum>m: #거슬러 줘야 하는 금액보다 현재 동전의 합이 더 크다면 더이상 탐색할 필요 없음 
        return
    
    if sum==m: 
        if L<res:
            res=L #최소값 구함 
    else:
        for i in range(n):
            DFS(L+1, sum+a[i]) #거스름 돈의 합을 계속 구함 (한 동전을 여러번 넣을 수도 있으므로 중복순열) 

            
if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    m=int(input())
    
    res=2147000000 #최소값을 구하므로 양의 무한대 
    a.sort(reverse=True)
    
    DFS(0, 0)
    print(res)
