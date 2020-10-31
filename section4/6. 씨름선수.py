import sys
sys.stdin=open("input.txt", "r")

n=int(input())
body=[]

for i in range(n):
    a, b=map(int, input().split())
    body.append((a, b))
    
body.sort(reverse=True) #키로 먼저 정렬

largest=0 #몸무게 비교 -> 몸무게 최대값을 찾는 방법으로 선수 뽑음
cnt=0

for x, y in body: #body가 튜플이기 때문에 x,y로 받을 수 있음
    if y>largest: #자신보다 키가 큰 사람 중 한명이라도 몸무게를 넘지 못하면 선발될 수 없음으로 최댓값을 뽑는 논리를 가져옴
        largest=y 
        cnt+=1
        
print(cnt)
