# coding=utf-8

# 工时计算
def estimated_time(size,number):
    time = 80 * size / number
    print(
        'To work out the %.2f size project with %d worker, we need %.2f hours'
        % (size, number, time), '\n'
    )

# 人力计算
def estimated_number(size,time):
    number = 80 * size / time
    print(
        'To work out the %.2f size project in %.2f hours, we need %d workers'
        % (size, time, number), '\n'
    )

# 调用工时计算函数
estimated_time(1.5, 2)
# 调用人力计算函数
estimated_number(0.5, 20)
estimated_number(1,60)