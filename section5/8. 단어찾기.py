import sys
sys.stdin=open("input.txt", "r")

n=int(input())
p=dict() #dictionary 자료형 사용 

for i in range(n):
    word=input()
    p[word]=1 #전체 word에 대해 dictionary 생성 
    
for i in range(n-1):
    word=input()
    p[word]=0 #시에 쓰인 word에 대해 dictionary 값 1->0으로 변경 
    
for key, val in p.items():
    if val==1: #value값이 0으로 변경되지 않은 것만 찾음 
        print(key)
        break

       
    
#파이썬 라이브러리 collection을 사용하여 문제 해결 
n=int(input())
word = []
poem = []

for _ in range(n):
    w=input()
    word.append(w)

for _ in range(n-1):
    w=input()
    poem.append(w)

answer = collections.Counter(word) - collections.Counter(poem)
print(list(answer.keys())[0])

