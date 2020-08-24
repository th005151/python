import random
num=random.randint(1,10)
print(num)
ans=int(input("你的答案? "))

if ans==num:
    print("right")
else:
    print("wrong")