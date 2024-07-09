#모음 받아오기 
lst = ['a','e','i','o','u']
#모음이 연속되면 안되지만 예외경우 처리 
accept = ['e','o']

while True:
    word  = input()
    if word == "end": break
    count = 0
    if len([1 for i in word if i in lst]) == 0:
        count +=1
            
    for i in range(len(word) - 2):
        if (word[i] in lst and word[i + 1] in lst and word[i + 2] in lst) or \
           (word[i] not in lst and word[i + 1] not in lst and word[i + 2] not in lst):
            count += 1
            
    for i in range(len(word)-1) :
        if word[i]==word[i+1] and word[i] not in accept:
            count+=1
               
    if count > 0: print(f'<{word}> is not acceptable.')
    else:  print(f"<{word}> is acceptable.")