#import sys
#sys.stdin = open("input.txt", 'r')

n = int(input())
a=[list(map(int, input().split())) for _ in range(n)] #2차원 배열

res=0
s=e=n//2

for i in range(n):
    for j in range(s,e+1):
        res += a[i][j]

    if i<n//2: #더하는 원소 수 증가
        s -=1 
        e +=1 
    else: #더하는 원소 수 감소
        s+=1 
        e-=1 

print(res)