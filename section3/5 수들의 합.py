#import sys
#sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt=0
rt=1
tot=a[0]
cnt=0

while True:
    if tot<m: #rt를 증가하며 수를 더해줌
        if rt<n: 
            tot += a[rt]
            rt+=1
        else: #list 범위에서 벗어난 경우
            break;
    elif tot==m: #lt를 증가하여 다음 경우로 넘어감
        cnt+=1
        tot-=a[lt]
        lt+=1
    else: #lt를 증가시켜 m 값과 같거나 작게 만듦
        tot -=a[lt]
        lt+=1

print(cnt)