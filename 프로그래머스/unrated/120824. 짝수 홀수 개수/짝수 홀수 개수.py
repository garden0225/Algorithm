def solution(num_list):
    answer = len( [i for i in num_list if i%2==0])
    return [answer,len(num_list)-answer]