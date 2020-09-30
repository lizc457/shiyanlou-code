b=7
c=7
for a in range(101):
    if a % 10==7:
        continue
    if a % 7==0:
        continue
    if a >= 70 and a %70<=9:
        continue
    print(a)

