#
# num=int(input())
#
# for i in range(1,10):
#     result =num*i
#     print(f"{num} * {i} = {result}")


#10950
# j = int(input())
# for i in range(j):
#     n1,n2 = map(int, input().split())
#     print(n1+n2)

#8393
# i= int(input())
# sum=0
# for j in range(1,i+1):
#     sum+=j
# print(sum)

#15552
import sys
n = int(sys.stdin.readline())

for i in range(n):
    n1, n2 = map(int, sys.stdin.readline().split())
    n3 = n1+n2
    print(f"Case #{i+1}: {n1} + {n2} = {n3}")
