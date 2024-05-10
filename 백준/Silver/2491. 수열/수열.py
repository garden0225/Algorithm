n = int(input())
li = list(map(int, input().split()))
inc = 1
dec = 1
len = []
for i in range(1,n):
     if li[i] >= li[i-1]: inc +=1 
     else: 
        len.append(inc) 
        inc = 1
     if li[i] <= li[i-1]: dec +=1 
     else: 
        len.append(dec) 
        dec = 1
len.append(dec)
len.append(inc)
print(max(len))