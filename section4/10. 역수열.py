import sys
sys.stdin=open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))

seq=[0]*n

for i in range(n): 
    for j in range(n):
        if(a[i]==0 and seq[j]==0): #a[i]=0 앞 자리에 있는 숫자들 가져오기 -> seq가 빈자리가 아닐 경우 j값이 증가되면서 다음 칸에 들어감 
            seq[j]=i+1 
            break
        elif seq[j]==0: #seq만 0인 경우, a값을 1씩 빼주면서 적절한 j값을 찾아 위의 if문에서 seq에 할당
            a[i]-=1

for x in seq:
    print(x, end=' ')
