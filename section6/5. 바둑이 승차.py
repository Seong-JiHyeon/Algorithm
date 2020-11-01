import sys
sys.stdin=open("input.txt", "r")

def DFS(L, sum, tsum):
    global result
    if sum+(total-tsum)<result: #앞으로 구할 최대 sum의 값이 현재 최대값을 넘지 않는 경우 가지치기 
        return
    
    if sum>c: #sum이 무게제한을 넘으면 않됨 (가지치기) 
        return
    
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L]) #tsum은 현재까지 판단한 모든 바둑이들의 무게 
        DFS(L+1, sum, tsum+a[L])


        
if __name__=="__main__":
    c, n=map(int, input().split())
    a=[0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input()) #바둑이 무게
        
    total=sum(a)
    DFS(0, 0, 0)
    print(result)

