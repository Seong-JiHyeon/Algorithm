#import sys
#sys.stdin = open("input.txt", 'r')

a = int(input())
a1 = list(map(int, input().split()))

b = int(input())
b1 = list(map(int, input().split()))

c = a1+b1
c.sort()

for x in c:
    print(x, end= ' ')