T=int(input())

for i in range(T):
    result=''
    R,S=input().split()
    R=int(R)
    for c in S:
        result+=R*c
    print(result)