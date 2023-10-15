def solution(my_string):
    answer = [chr(i) for i in range(ord('A'),ord('Z')+1)]+[chr(i) for i in range(ord('a'),ord('z')+1)]
    li = [0] * 52
    for i in my_string:
        i = answer.index(i)
        li[i]+=1
    return li