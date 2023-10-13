Hour, Minute = map(int, input().split())
Time = int(input())

Hour = (Minute + Time) // 60 + Hour
Minute = (Minute + Time) % 60

if(Hour >= 24):
    Hour -=24

print(Hour, Minute)