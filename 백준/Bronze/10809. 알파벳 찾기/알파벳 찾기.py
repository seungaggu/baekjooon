S=str(input())

i=[]
c='abcdefghijklmnopqrstuvwxyz'

for ch in c:
    pos=S.find(ch)
    i.append(pos)
        
print(*i)