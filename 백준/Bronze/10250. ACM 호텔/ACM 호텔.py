T=int(input())
for _ in range(T):
    H,W,N=map(int,input().split())
    if N%H==0:    
        ch=H
        ho=N//H
    else:
        ho= N//H+1
        ch= N%H
    print(f'{ch}{ho:02}')