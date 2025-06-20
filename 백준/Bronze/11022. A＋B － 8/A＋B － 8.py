T=int(input())
D=[]
Al=[]
Bl=[]
for i in range(T):
    A,B=map(int,input().split())
    C=A+B
    D.append(C)
    Al.append(A)
    Bl.append(B)
for i,(A,B,result) in enumerate(zip(Al,Bl,D)):
    print(f'Case #{i+1}: {A} + {B} = {result}')