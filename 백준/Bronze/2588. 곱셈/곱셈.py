A=int(input())
B=input()
B=[int(i) for i in B]

first=A*B[-1]
second=A*B[-2]
third=A*B[-3]

result=A*int(''.join(map(str,B)))

print(first)
print(second)
print(third)
print(result)