import sys
sys.stdin=open("input.txt", "r")

def Count(len):
    cnt=1
    ep=Line[0]
    for i in range(1, n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt


n, c=map(int, input().split())
Line=[]

for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
    
Line.sort()

lt=1
rt=Line[n-1] #혹은 Line[n-1]-Line[0]

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        #두말의 거리가 최대가 되어야 하기 때문에 c이상의 범위
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)


