#import sys
#sys.stdin = open("input.txt", 'r')

n = int(input())
a =[list(map(int, input().split())) for _ in range(n)] #2차원 배열

m = int(input())
b =[list(map(int, input().split())) for _ in range(m)]

res=0

for i in b:
    row = i[0]-1
    move = i[2]

    if i[1]==0:
        for _ in range(move):
            a[row].append(a[row].pop(0)) #행의 가장 앞 원소 pop 후 가장 뒤에 연결
    else:
        for _ in range(move):
            a[row].insert(0, a[row].pop()) #행의 가장 뒤 원소 pop 후 가장 앞에 연결

s=0
e=n
for i in range(n):
    for j in range(s,e):
        res += a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(res)
