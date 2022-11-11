# coding=utf-8

students = ['小明', '小红', '小刚']

k = int(input('which student? '))

if k <= len(students):
    k = k - 1
    print (students[k])
else:
    print('input out of list')