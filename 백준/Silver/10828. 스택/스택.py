#10828 스택
import sys

n=int(sys.stdin.readline())

stack=[]
for i in range(n):
    say=sys.stdin.readline().split()
    if say[0] == 'push':
        stack.append(say[1])
    elif say[0] =='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif say[0]=='size':
        print(len(stack))
    elif say[0] =='empty':
         if len(stack)==0:
            print(1)
         else:
            print(0)
    elif say[0] == 'top':
        if len(stack)==0:
            print(-1)
        else :
            print(stack[-1])
