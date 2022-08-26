# coding=utf-8

students = ['小明', '小红', '小刚']

for i in range(3):
    print(students)
    students.append(students[0])
    del students[0]