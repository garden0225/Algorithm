n = input()
arr = [0]*10 

for i in n:
    if i == '6' or i == '9':
        if arr[6] <= arr[9]:
            arr[6]+=1
        else: 
            arr[9]+=1 
    else:
        arr[int(i)]+=1 

print(max(arr)) 