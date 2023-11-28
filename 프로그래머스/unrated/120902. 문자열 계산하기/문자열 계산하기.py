def solution(my_string):
    op = my_string.split()
    answer=int(op[0])
    for i in range(len(op)):
        if op[i]=="+":
            answer+=int(op[i+1])
        elif op[i]=="-":
            answer-=int(op[i+1])
    return answer

#def solution(my_string):
#    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
#미친사람,,, 5-8를 5 +(-8)로 변환