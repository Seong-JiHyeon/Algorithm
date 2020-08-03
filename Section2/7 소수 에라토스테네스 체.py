
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
ch=[0]*(n+1)
cnt=0

for i in range(2,n+1): #소수 찾기
    if ch[i]==0: #소수
        cnt +=1
        
        for j in range(i, n+1, i): #소수의 배수들 제거
            ch[j]=1

print(cnt)