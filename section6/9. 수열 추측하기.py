import sys
sys.stdin=open("input.txt", "rt")

#순열 
def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0) #여러 가지 경우 중 최초로 발견되는 경우 선택 
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0

                
if __name__ == "__main__":
    n, f=map(int, input().split())
    
    p=[0]*n #순열 
    b=[1]*n #이항계수 
    ch=[0]*(n+1)
    
    #파스칼 정리 -> (a+b)**n의 계수를 binary 리스트에 저장하여 계산을 빠르게 함 
    for i in range(1, n): #가장 앞 계수는 1로 정해져 있음 -> 제외 
        b[i]=b[i-1]*(n-i)//i #각 계수는 combination nCm과 같음 -> combination 식을 이용하여 앞 계수에 index를 곱하고 나눔  
        
    DFS(0, 0)





    
