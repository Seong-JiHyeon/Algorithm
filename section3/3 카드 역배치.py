#import sys
#sys.stdin = open("input.txt", 'r')

n = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())

    for i in range((e-s+1)//2):
        n[s+i], n[e-i] = n[e-i], n[s+i] #switch

n.pop(0) #첫 번째 원소 제거
for x in n:
    print(x, end= ' ')