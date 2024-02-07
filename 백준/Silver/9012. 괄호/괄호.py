# 9012 괄호

T = int(input())


for i in range(T):
    stack = []
    vps = input()
    for x in vps:
        if x == "(":
            stack.append("(")
        elif x == ")":
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을경우 NO
                print("NO")
                break
    else: # break문으로 끊기지 않고 수행됬을 경우 
        if not stack: # break문으로 안끊기고 스택이 비어있다면
            print("YES")
        else: # break안 걸렸더라도 스택에 괄호가 들어있다면
            print("NO")
