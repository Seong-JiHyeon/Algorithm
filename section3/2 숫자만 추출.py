#import sys
#sys.stdin = open("input.txt", 'r')

s = input()

res=0
for i in s:
    if i.isdecimal():
        res=res*10+int(i)

print(res)

cnt=0
for i in range(1,res +1): #약수는 자신 포함 / 서로소는 1과 자신 제외
    if res%i==0:
         cnt+=1
print(cnt)