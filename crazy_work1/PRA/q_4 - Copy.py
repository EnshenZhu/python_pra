# coding=utf-8

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
# 程序源代码：

year = int(input('year='))
month = int(input('month='))
if (month > 12 or month < 0):
    print('month error, input the month again')
    
    
day = int(input('day='))

sum_all = 0

month_to_day_interval = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]   # present how many days in each months

if year % 400 == 0:
    month_to_day_interval[2] = 29   # if the input year is an leap year, add one day to Feburary
    
for i in range(month):
    if month > i + 1:
        sum_all += month_to_day_interval[i + 1]

print('It is the ' + str(sum_all + day) + ' day of the year ' + str(year))