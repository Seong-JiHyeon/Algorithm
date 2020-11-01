import sys
sys.stdin = opne("input.txt", "r")

def DFS(x):
   if x>0:
      print(x) #(3, 2, 1) 역순으로 출력, but 순서대로 출력한 것이다
      DFS(x-1)
      print(x) #(1, 2, 3) 순서대로 출력, but 거꾸로 출력한 
     
 if __name__ == "__main__":
    n = int(input())
    DFS(n)
