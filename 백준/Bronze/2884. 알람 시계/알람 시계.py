from datetime import datetime, timedelta
H,M=map(int,input().split())

time=datetime(1999,1,1,H,M)

result=time-timedelta(minutes=45)

print(result.hour, result.minute)