import sys
sys.stdin=open("input.txt", "r")

def check(a):
    for i in range(9):
        ch1=[0]*10 #check list 행 
        ch2=[0]*10 #check list 열
        for j in range(9):
            ch1[a[i][j]]=1 #a[i][j]값을 인덱스로 하여 해당 ch1인덱스에 1표시 -> 후에 sum=9로 확인
            ch2[a[j][i]]=1 #n행과 열 동시 체크 (ex. 0행과 0열 동시)
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3): #그룹탐색을 위한 4중 for loop
        for j in range(3): #3x3으로 9개 그룹
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

a=[list(map(int, input().split())) for _ in range(9)] #2차원 리스트
if check(a):
    print("YES")
else:
    print("NO")
