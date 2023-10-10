def solution(n, control):
    
    answer = int(n)
    for i in range(len(control)):
        print(control[0])
        if control[i] == "w":
            answer +=1
        elif control[i] == "s":
            answer -=1
        elif control[i] == "d":
            answer +=10
        elif control[i] == 'a':
            answer -=10
    return answer

