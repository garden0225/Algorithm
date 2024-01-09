def solution(age):
    answer = ""
    alphabet = 'abcdefghij'
    
    for num in str(age):
        for n, i in enumerate(alphabet):
            if str(n) == num:
                answer += i

    return answer
