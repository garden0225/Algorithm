import sys

n = int(sys.stdin.readline())
narr = [*map(int, sys.stdin.readline().split())]
m = int(sys.stdin.readline())
marr = [*map(int, sys.stdin.readline().split())]

# 이진탐색: O(log n)


def binary_search(arr, num, left, right):

    while left <= right: # 맨 처음 위치가 맨 마지막 위치랑 같아질 때까지 반복
        mid = int((left + right) /2) #중간값
        
        if arr[mid]==num: # num(i)이랑 == 중간값이면 
            return True # True 반환

        elif arr[mid] < num: # num(i) > 중간값 
            left = mid +1 # 중간값 오른쪽 이동 
        else :
            right = mid -1 # 중간값 왼쪽 이동
    
    return False # 이 외의 경우 False


narr.sort()

for i in marr:
    if binary_search(narr, i, 0,  n-1): # True이면
        print(1, end= ' ')
    else: # Flase이면
        print(0, end= ' ')
