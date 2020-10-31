import sys
sys.stdin=open("input.txt", "r")

n=int(input())
meeting=[]

for i in range(n):
    a, b=map(int, input().split())
    meeting.append((a, b))
    
meeting.sort(key=lambda x : (x[1], x[0])) #끝시간부터 정렬 후 시작시간으로 

et=0
cnt=0
for x, y in meeting:
    if x>=et:
        et=y
        cnt+=1
        
print(cnt)


#다음과 같은 코드도 
all = sorted(a, key = lambda x: (x[1], x[0]))
end=all[0][1]

for i in range(1,n):
    start=all[i][0]
    if start>=end:
        cnt+=1
        end=all[i][1]
