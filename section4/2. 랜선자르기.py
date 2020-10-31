import sys
sys.stdin=open("input.txt", "r")

#각 랜선에서 len에 따른 작은 랜선이 몇 개 나오는가 계산
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt


k, n=map(int, input().split())

Line=[]
res=0
largest=0

#랜선의 길이는 1~가장 큰 랜선 길이(802) 사이에 있다 -> 이 사이에서 이분탐색
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp) #가장 긴 랜선 길이 구하기

#이분탐색
lt=1
rt=largest

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n: #count값이 주어진 n값보다 크다면 결과값으로 결정한 후, 다시 상위 범위로 이분탐색
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)








