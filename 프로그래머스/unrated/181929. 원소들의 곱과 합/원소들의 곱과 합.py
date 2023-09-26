def solution(num_list):
    answer1 = 1
    answer2 = 0
    for i in num_list:
        answer1 *=i
        answer2 +=i
    return int(answer1 < answer2**2)
            
    