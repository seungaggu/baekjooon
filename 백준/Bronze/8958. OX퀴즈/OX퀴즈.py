N=int(input())

for _ in range(N):
    test=input()
    count=0
    total=0

    for i in test:
        if i == 'O':
            count+=1
            total+=count
        else :
            count=0
    print(total)