import sys
input = sys.stdin.readline

s=int(input())
for _ in range(s):
    A,B=map(int,input().split())
    print(A+B)