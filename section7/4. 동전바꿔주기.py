import sys
sys.stdin=open("input.txt", "r")

#중복 순열 문제
def DFS(L, sum):
    global cnt
    if sum>m: #지폐의 합보다 sum이 더 큰 경우
        return
    if L==n: #모든 동전의 경우를 다 계산한 경우
        if sum==m: #지폐와 값이 같을 때에만 count
            cnt+=1
    else:
        for i in range(cn[L]+1): #동전을 가지고 있는 계수만큼 for loop
            DFS(L+1, sum+(cv[L]*i))
            

m=int(input())
n=int(input())
cv=list()
cn=list()
for i in range(n):
    a, b=map(int, input().split())
    cv.append(a)
    cn.append(b)
cnt=0
DFS(0, 0)
print(cnt)
