total=int(input())
n=int(input())
sum=0

for i in range(n+1):
    a, b = map(int, input().split())
    c=a*b
    sum+=c

if total==sum:
    print("Yes")
else:
    print("No")