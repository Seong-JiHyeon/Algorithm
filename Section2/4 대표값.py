
import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
s = list(map(int, input().split()))

ave = round(sum(s)/n +0.5) #반올림 (round half even -> round half up)
min = 2147000000

for idx, x in enumerate(s):
    #번호가 빠른 순
    tmp = abs(x-ave)

    if tmp<min:
        min=tmp
        score=x
        res=idx+1

    elif tmp==min: #점수가 높은 순
        if x>score:
            score=x
            res=idx+1

print(ave, res)