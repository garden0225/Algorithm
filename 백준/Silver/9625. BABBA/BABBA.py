n = int(input())
a = [0] *45
a[1] = 1
b = [1] *45

for i in range(2,n):
    b[i] = b[i-1] + b[i-2]
    a[i] = a[i-1] + a[i-2]

print(a[n-1],b[n-1])