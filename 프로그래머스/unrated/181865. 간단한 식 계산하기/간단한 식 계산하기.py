def solution(binomial):
    a = binomial.split()
    if a[1]=="+":
        return int(a[0])+int(a[2])
    elif a[1]=="-":
        return int(a[0])-int(a[2])
    else:
        return int(a[0])*int(a[2])
    
    #eval 함수는 expression 인자에 string 값을 넣으면 해당 값을 그대로 실행하여 결과를 출력