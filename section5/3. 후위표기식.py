import sys
sys.stdin=open("input.txt", "r")
#숫자는 스택에 넣지 않음
#연산자만 스택에 넣어 우선순위 나타냄

a=input()
stack=[]
res=''

for x in a:
    if x.isdecimal(): #숫자인 경우 string에 누적  
        res+=x
        
    else: #연산자인 경우  
        if x=='(':
            stack.append(x)
            
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'): #stack이 비어있지 않을 때, stack의 상단이 우선순위가 같은 경우 우선 처리 
                #현재 연산자와 우선순위가 같으나 왼쪽에 있으므로 우선 계산함, 따라서 pop후 연산자 처리 
                res+=stack.pop() #stack에서 pop하여 res에 누적 (우선 처리) 
            stack.append(x)
            
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(': #stack이 비어있지 않을 때, 여는 괄호 전까지의 연산자 모두 처리 
                res+=stack.pop()
            stack.append(x)
            
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop() #스택 안의 여는 괄호 '('pop 
            
while stack: #스택에 남은 연산자 모두 pop 
    res+=stack.pop()
    
print(res)






