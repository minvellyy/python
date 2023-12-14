#주사위 4개일 때
#1. 다 같을 때 200
#2. 제일 큰 수 곱하기 100
#3. 하나만 다를 때 300
#4. 두개만 같을 때 400

d1,d2,d3,d4=map(int.input().split())

if d1 == d2 == d3==d4:
    print(d1*200)
elif d1==d3 or d1==d2:
    print(1000+d1*100)
elif d2==d3:
    print(1000+d2*100)

else:
    print(max(d1, d2, d3,d4)*100)
