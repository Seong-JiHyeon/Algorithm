import sys
sys.stdin=open("input.txt", "r")

a=input()
stack=[]

for x in a:
    if x.isdecimal(): #숫자면 스택에 삽입 
        stack.append(int(x))
        
    else: #연산자일 경우, 스택 내의 가장 위에 있는 두 숫자로 연산 수행 
        if x=='+': 
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2+n1)
            
        elif x=='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
            
        elif x=='*':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)
            
        elif x=='/':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)
            
print(stack[0]) #가장 마지막에는 결과값 하나만 스택에 남아있음 
