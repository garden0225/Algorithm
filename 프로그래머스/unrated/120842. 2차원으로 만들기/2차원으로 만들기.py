def solution(num_list, n):
    answer = [num_list[num : num + n] for num in range(0,len(num_list),n)]
    return answer