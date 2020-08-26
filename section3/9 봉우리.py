import sys
#sys.stdin = open("input.txt", 'r')
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)




#import sys
#sys.stdin = open("input.txt", 'r')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n) #배열 첫 행
a.append([0]*n) #배열 마지막 행

for x in a:
    x.insert(0,0) #각 행의 첫 열
    x.append(0) #각 행의 마지막 열

cnt=0
for i in range(1, n+1):
    for j in range(1,n+1):
        origin = a[i][j]
        search = [origin, a[i-1][j], a[i+1][j], a[i][j+1], a[i][j-1]]
        search.sort()

        if search[-1]==origin and search[-1]!=search[-2]:
            cnt+=1

print(cnt)
