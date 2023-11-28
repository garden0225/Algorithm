def solution(my_string):
    op = my_string.split()
    answer=int(op[0])
    for i in range(len(op)):
        if op[i]=="+":
            answer+=int(op[i+1])
        elif op[i]=="-":
            answer-=int(op[i+1])
    return answer