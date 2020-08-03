
import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
s = list(map(int, input().split()))
res=0
cnt=0

for i in s:
    if i==0:
        res+=0
        cnt=0

    elif i==1:
        cnt+=1
        res+=cnt

print(res)