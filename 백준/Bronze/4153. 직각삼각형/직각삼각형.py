while True:
    a=list(map(int,input().split()))
    if a == [0,0,0]:
        break
    long=max(a)
    a.remove(long)
    if a[0]**2+a[1]**2==long**2:
        print('right')
    else:
        print('wrong')