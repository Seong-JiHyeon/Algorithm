import sys
sys.stdin=open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))

seq=[0]*n

for i in range(n): 
    for j in range(n):
        if(a[i]==0 and seq[j]==0): #a[i]=0 앞 자리에 있는 숫자들 가져오기
            seq[j]=i+1 
            break
        elif seq[j]==0: #seq만 0인 경우, 아직 할당받지 못함 -> i값이 증가하는 대신 a에서 1을 
            a[i]-=1

for x in seq:
    print(x, end=' ')
