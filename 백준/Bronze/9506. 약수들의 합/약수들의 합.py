while True:
    n = int(input())
    if n == -1: break
    else:
        ans = [i for i in range(1,n) if n%i == 0]
        if sum(ans) == n: 
            print(n,"=", 1 , end = " " )
            for i in ans[1:]:
                print("+", i, end = " ")
        else: print( n ,"is NOT perfect.")