x,y  = map(int,input().split())# 종의의 가로, 세로 입력

x_arr = [0, x] 
y_arr = [0, y] 

# 점선 입력 
for _ in range(int(input())): # 점선의 개수 
    xy, dot = map(int,input().split())
    if xy : # 0이면 가로
        x_arr.append(dot)
    else: # 0이 아니면 세로
        y_arr.append(dot)



# 길이 만드는 함수
def length(arr):
    leng =[]
    # 정렬
    arr.sort()
    for i in range(len(arr)-1):
         leng.append(arr[i+1]-arr[i]) 
         
    return max(leng)

print(length(x_arr)*length(y_arr))