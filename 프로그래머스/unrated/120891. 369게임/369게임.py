def solution(order):
    answer=0
    for i in ["3","6","9"]:
        answer+= str(order).count(i)
    return answer