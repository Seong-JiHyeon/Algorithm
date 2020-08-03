
import sys
#sys.stdin=open("input.txt", "rt")

n, k = map(int, input().split())
c = list(map(int, input().split()))

res = set() #중복 제거
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1,n):
            res.add(c[i]+c[j]+c[m])

res = list(res)
res.sort(reverse=True) #내림차순(역순)
print(res[k-1])