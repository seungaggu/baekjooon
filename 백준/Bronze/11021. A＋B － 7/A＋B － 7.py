T=int(input())
D=[]
for i in range(T):
    A,B=map(int,input().split())
    C=A+B 
    D.append(C)

for i,result in enumerate(D):
    print(f"Case #{i+1}: {result}")