
import sys
#sys.stdin=open("input.txt", "rt")

#int형으로 읽어오기 / input()=string type
t=int(input())

for i in range(1,t+1):
    n, s, e, k = map(int, input().split())
    #list형태로 입력 받아오기
    A = list(map(int, input().split()))
    A = A[s-1:e]
    A.sort() #sort(A) x
    print("#%d %d" %(i, A[k-1]))