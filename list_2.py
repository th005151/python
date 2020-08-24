n=int(input("how many students?"))
stu=[]
for i in range(n):
    score=int(input("score? "))
    stu.append(score)
s=0
for i in range(n):
    s=s+stu[i]
print(s/n)