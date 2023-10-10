def solution(arr, queries):
    for n in range(len(queries)):
        i = queries[n][0]
        j = queries[n][1]
        arr[i],arr[j] = arr[j],arr[i]
    return arr