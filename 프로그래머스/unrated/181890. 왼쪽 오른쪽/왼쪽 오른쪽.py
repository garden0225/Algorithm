def solution(str_list):
    if  "l" not in str_list and "r" not in str_list:    
        return []
    for n, i in enumerate(str_list):
        if i =="l":
            return str_list[:n]
        elif i == "r":
            return str_list[n+1:] 
   
            