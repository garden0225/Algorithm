def solution(str_list, ex):
    answer=[i for i in str_list[:] if ex not in i]
    return ''.join(answer)