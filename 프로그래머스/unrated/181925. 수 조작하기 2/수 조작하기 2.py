def solution(numLog):
    answer = []
    string =""
    for i in range(1,len(numLog)):
        answer.append(numLog[i]-numLog[i-1])
    for i in answer:
        if i == 1:
            string +="w"
        elif i == -1:
            string += "s"
        elif i == 10:
            string += "d"
        elif i == -10:
            string += "a"
    return string