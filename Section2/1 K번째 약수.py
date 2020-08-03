
import sys
#sys.stdin=open("input.txt", "rt")

#공백이 있는 입력의 경우 string으로 받아 int로 하나씩 mapping
n, k = map(int, input().split())

cnt=0

#for-else 구문
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)