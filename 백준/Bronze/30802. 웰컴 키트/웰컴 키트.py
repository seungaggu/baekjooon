import math

N=int(input())
s=list(map(int,input().split()))
T,P=map(int,input().split())

T_result=0
for i in s:
    T_result+=math.ceil(i/T)
    
P_m=N//P
P_n=N%P

print(T_result)
print(P_m , P_n)