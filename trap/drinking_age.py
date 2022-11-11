import math

age =float(input('你今年几岁了？'))
age=int(math.floor(age))

print(age)
if age < 18:
    print('不可以喝酒噢')