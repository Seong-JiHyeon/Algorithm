
import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
res=0

for i in range(n):
    tmp = list(map(int, input().split()))
    tmp.sort() #tmp = tmp.sort() X
    a,b,c = tmp[0], tmp[1], tmp[2]

    if a==b and b==c: #눈 3개가 모두 같은 경우
        money=10000 + a*1000

    elif a==b or a==c: #눈 2개가 같은 경우 (a기준)
        money=1000+(a*100)

    elif b==c:          #(b기준)
        money=1000+(b*100)

    else:               #눈 1개가 같은 경우
        money=c*100

    if money>res:
        res=money

print(res)
    