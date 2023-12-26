def solution(numbers):
    answer = 0
    ch = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = ['0','1','2','3','4','5','6','7','8','9']
    num_dict = dict(zip(ch,num))

    for k in num_dict.keys():
        numbers = numbers.replace(k, num_dict[k])

    return int(numbers)
     
