A=[]
for i in range(9):
    i=int(input())
    A.append(i)
m=max(A)
b=A.index(m)+1
print(m,b)