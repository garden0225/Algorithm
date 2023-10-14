def solution(start, end_num):
    answer = [i for i in range(end_num,start+1)]
    
    return sorted(answer,reverse=True)

#def solution(start, end):   return list(range(start,end-1,-1))