A,B= map(list,input().split())

As=A[::-1]
Bs=B[::-1]

if As<Bs:
    print(''.join(Bs))
elif Bs<As:
    print(''.join(As))