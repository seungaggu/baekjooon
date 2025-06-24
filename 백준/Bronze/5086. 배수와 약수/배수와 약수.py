while True:
    A,B=map(int,input().split())
    if A==0 and B==0:
        break
    if A//B==0:
        a='factor'
    elif A%B==0:
        a='multiple'
    else:
        a='neither'
    print(a)