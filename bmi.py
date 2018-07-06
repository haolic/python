height = float(input('height(m):'))
weight = float(input('weight(kg):'))
bmi = weight / (height * height)
print(bmi)
if bmi > 32:
    print('严重过胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过轻')