import sys
sys.stdin = opne("input.txt", "r")

def DFS(x):
   if x>0:
      print(x) #(3, 2, 1) 역순으로 출력
      DFS(x-1)
      print(x) #(1, 2, 3) 순서대로 출력 
     
 if __name__ == "__main__":
    n = int(input())
    DFS(n)
