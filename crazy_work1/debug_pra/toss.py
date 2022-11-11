#coding=utf-8

import random

guess = ''

while guess not in ['head','tail']:
    print('------猜硬币游戏------')
    print('猜一猜硬币是head还是tail？')
    guess = input('请输入“head”或“tail”：')

# 随机抛硬币，0代表正面，1代表反面
toss = random.randint(0,1)
if toss==0:
    toss='head'
else:
    toss='tail'

if toss == guess:
    print('猜对了！你真棒')
else:
    print('没猜对，你还有一次机会。')
    guess = input('再输一次“head”或“tail”：')
    if toss == guess:
        print('你终于猜对了！')
    else:
        print('大失败！')