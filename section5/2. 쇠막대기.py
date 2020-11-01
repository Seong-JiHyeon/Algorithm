import sys
sys.stdin=open("input.txt", "r")
#()열림괄호와 닫힘괄호가 연속적으로 나올 때, 레이저 
#((으로 나올 때, 쇠막대기 시작점 
#))으로 나올 때, 쇠막대기 끝점 

s=input()
stack=[] #스택 사용 
cnt=0

for i in range(len(s)):
    if s[i]=='(': #쇠막대기의 시적점 혹은 레이저일 수 있음, 일단 stack에 삽입 
        stack.append(s[i])
    else: #)의 경우, 스택의 가장 끝 값을 팝하여 확인함 
        stack.pop()
        #stack이 아닌 기존 배열 s에서 앞의 괄호가 무엇인지 확인을 통해 레이저와 쇠막대기 구분 
        if s[i-1]=='(': #레이저인 경우 
            cnt+=len(stack) #레이저에 의해 잘려진 쇠막대기 count (스택 내에 있는 쇠막대기 모두가 잘려짐으로 stack내의 모든 '('값 count) 
        else: #쇠막대기의 끝점인 경우 
            cnt+=1 #쇠막대기의 마지막 조각 count 
            
print(cnt)
