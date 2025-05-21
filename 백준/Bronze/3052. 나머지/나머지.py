A=[int(input()) for _ in range(10)]
B=42

def abc(A,B):
    C=set()
    for a in A:
        C.add(a%B)
    print(len(C))
        
abc(A,B)