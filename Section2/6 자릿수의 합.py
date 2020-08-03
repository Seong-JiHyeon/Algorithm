
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

#list 전체를 함수로 받아오기
def digit_sum(x):
    max=0
    max_sum=0
    for i in x:
        sum=0
        tmp=i

        while tmp>0:
            sum+=tmp%10
            tmp=tmp//10

        if sum > max_sum:
            max_sum=sum
            max=i

    print(max)

def digit_sum2(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum

#digit_sum(a)

max=0
for x in a:
    tot=digit_sum2(x)
    if tot>max:
        max=tot
        res=x

print(res)