def solution(myStr):
    myStr=myStr.replace("a"," ")
    myStr=myStr.replace("b"," ")
    myStr=myStr.replace("c"," ")
    if myStr.split() == []:
        return ["EMPTY"]
    else: return myStr.split()