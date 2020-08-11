#import sys
#sys.stdin = open("input.txt", 'r')

n = int(input())

for i in range(n):
    string = input()
    string = string.upper()
    rev_string = string[::-1]

    if string!=rev_string: #list끼리의 비교도 가능
        print("#%d NO" %(i+1))
    else:
        print("#%d YES" %(i+1))