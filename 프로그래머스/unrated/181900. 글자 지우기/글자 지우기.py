def solution(my_string, indices):
    answer = ''
    for i,string in enumerate(my_string):
        if i not in indices:
            answer+=string
    return answer