def solution(todo_list, finished):
    answer=[]
    for n,i in enumerate(finished):
        if i==0:
            answer.append(todo_list[n])
    return answer
            