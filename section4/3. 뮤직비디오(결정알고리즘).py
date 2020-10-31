import sys
sys.stdin=open("input.txt", "r")

def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m=map(int, input().split())
Music=list(map(int, input().split()))

maxx=max(Music)

lt=1
rt=sum(Music)

res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m: #최대 곡 길이보다는 dvd용량이 커야 한다(maxx)
        #앞의 문제와 달리 m개 이상을 만드는 것도 m개 포함되지 않기 때문에 res값은 <=m안에서 정의되어야 한다
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)

