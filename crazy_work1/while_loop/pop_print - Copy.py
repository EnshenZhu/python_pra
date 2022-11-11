# coding=utf-8

students = ['小明', '小红', '小刚']

for i in range(3):
    print(students)
    students.append(students.pop(0))

print(students)