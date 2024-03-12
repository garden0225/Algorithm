import sys
input = sys.stdin.readline

arr = [0]*10001

for _ in range((int(input()))):
    n = int(input())
    arr[n] += 1 # arr[n]에 n이 들어온 개수 count 

for i in range(10001): 
	# arr[i]에 숫자가 들어왔다면 
    if arr[i] != 0:
    	# arr[n]에 n이 들어온 개수 만큼 출력 
        for j in range(arr[i]): 
            print(i)