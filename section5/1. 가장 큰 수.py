import sys
sys.stdin=open("input.txt", "rt")

num, m=map(int, input().split())
num=list(map(int, str(num))) #전체 숫자를 각 자리별 분리하기 위해 string처리 후, 각각 정수화
stack=[] #리스트를 스택으로 사용

for x in num:
    while stack and m>0 and stack[-1]<x: #스택이 비어있지 않을 때, 숫자를 더 꺼낼 수 있을 때(m), stack 가장 상단의 숫자가 현 숫자x보다 작을 때 
        stack.pop() #스택에서 가장 끝 값 제거 
        m-=1
    stack.append(x) #현 숫자x 스택에 삽입 
    
if m!=0: #m값이 남아서 더 숫자를 꺼내야 하는 경우, 가장 끝자리의 m개 숫자 제거 (끝에 있는 수가 가장 작은 수이기 때문) 
    stack=stack[:-m]
    
res=''.join(map(str, stack))
print(res)





