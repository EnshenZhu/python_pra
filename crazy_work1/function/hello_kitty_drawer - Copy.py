# coding=utf-8

import random
import time

# 提示：将以下部分封装进函数

def drawer(*namelist):
    a = random.choice(namelist)
    print('开奖倒计时', 3)
    time.sleep(1)
    print('开奖倒计时', 2)
    time.sleep(1)
    print('开奖倒计时', 1)
    time.sleep(1)
    image = '''
     /\_)o<
    |      \\
    | O . O|
     \_____/
    '''
    print(image)
    print('恭喜' + a + '中奖！')
    return namelist

print(drawer('a', 'b', 'c'))   # recall that the namelist is a tuple