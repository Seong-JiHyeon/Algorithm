import sys
sys.stdin=open("input.txt", "r")

L=int(input())
a=list(map(int, input().split()))
m=int(input())

a.sort()
for _ in range(m): #한 번에 1씩 옮김 -> 총 m번 옮김
    a[0]+=1
    a[L-1]-=1 #매번 최소값, 최대값에서 1씩 옮긴 후
    a.sort() #다시 정렬하여 최소값, 최대값을 

print(a[L-1]-a[0])
