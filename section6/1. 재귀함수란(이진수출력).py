import sys
sys.stdin=open("input.txt", "r")

def DFS(x):
    if x==0:
        return #종료 
    else:
        DFS(x//2)
        print(x%2, end='') #거꾸로 출력 

n=int(input())
DFS(n)
