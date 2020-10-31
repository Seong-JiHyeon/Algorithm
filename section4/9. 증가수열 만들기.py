import sys
sys.stdin=open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))

lt=0 #각 LR 포인터
rt=n-1
last=0 #수열의 가장 마지막 값
res="" #LR 기록
tmp=[]

while lt<=rt:
    #증가 수열을 위해서는 수열의 가장 끝 값인 last보다 다음 받아올 값이 커야한다
    if a[lt]>last:
        tmp.append((a[lt], 'L'))
    if a[rt]>last:
        tmp.append((a[rt], 'R'))
    #LR값을 받아놓고 둘 중 더 작은 값을 찾기 위해 정렬
    tmp.sort()
    #tmp에 값이 받아지지 않았다면 더 이상 수열을 만들 수 없음
    if len(tmp)==0:
        break;
    else:
        res=res+tmp[0][1] #LR중 작은 값 문자 이어 붙이기
        last=tmp[0][0] #LR중 작은 값 숫자 수열에 포함
        if tmp[0][1]=='L': #L일 때 lt포인터 이동
            lt=lt+1
        else: #R일 때 rt포인터 이동
            rt=rt-1
    tmp.clear() #tmp를 비워줘야 다음 최대 2개를 받아 다시 정렬

print(len(res))
print(res)
