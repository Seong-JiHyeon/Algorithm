
import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

# string으로 치환하여 reverse
def reverse(x):
    y=str(x)
    y=y[::-1] #string reverse 공식
    x=int(y) 

    return x

def isPrime(x):
    if x==1:
        return False

    for i in range(2,x//2+1):
        if x%i==0:
            return False
    else:
        return True

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end = ' ')