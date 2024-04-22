import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    x = sys.stdin.readline().split()
    if x[0] == '1':stack.append(x[1])
    if x[0] == '2' :
        if stack:print(stack.pop())
        else: print(-1) 
    if x[0] == '3': print(len(stack))
    if x[0] == '4':
        if len(stack) == 0: print(1) 
        else: print(0)
    if x[0] == '5':
        if stack: print(stack[-1])
        else:  print(-1)  
