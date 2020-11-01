import sys
sys.stdin=open("input.txt", "r")

a=input()
b=input()

#각각 dictionary를 만든 후 비교 
str1=dict()
str2=dict()

for x in a:
    #dictionary에 생성되지 않은 데이터에 대해 값을 바꿔주려 한다면 에러 발생 (누적해야 하기 때문) 
    str1[x]=str1.get(x, 0)+1 #get함수는 dictionary에 데이터가 있는지 확인후 value return (없으면 0 return) 
for x in b:
    str2[x]=str2.get(x, 0)+1

for i in str1.keys():
    if i in str2.keys(): #str1안의 i값이 str2에 있다면, 
        if str1[i]!=str2[i]: #value값이 같은지 확인 
            print("NO")
            break
    else: #str1안의 i값이 str2에 없다면, 
        print("NO")
        break
else: #value값이 모두 같을 경우 
    print("YES")



<개선된 코드>
import sys
#sys.stdin=open("in1.txt", "r")

a=input()
b=input()

#하나의 dictionary만 생성
sH=dict()

for x in a:
    sH[x]=sH.get(x, 0)+1 #첫 문자열에 대한 누적값
for x in b:
    sH[x]=sH.get(x, 0)-1 #같은 문자에 대한 누적값 제거

for x in a:
    if(sH.get(x)>0): #모든 value값이 0일 때만 아나그램이다! (<0도 포함해야 할 것 같다)
        print("NO")
        break;
else:
    print("YES")



<리스트 해쉬> 
str1=[0]*52 #26자 알파벳이 대문자, 소문자가 있으므로 26*2=52 
str2=[0]*52 #ascii: 대문자(65~90), 소문자(97~122) 

for x in a:
    if x.isupper():
        str1[ord(x)-65] += 1
    else:
        str1[ord(x)-71] += 1
        
for x in b:
    if x.isupper():
        str2[ord(x)-65] += 1
    else:
        str2[ord(x)-71] += 1
        
#if str1==str2: print("YES") else print("NO") 

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")



