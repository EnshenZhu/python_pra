# coding=utf-8

import random
appetizer = ['话梅花生', '拍黄瓜', '凉拌三丝']

def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 <= money < 10:
        b = random.choice (appetizer)
        return b, '溏心蛋'

coupon_complex = coupon(8)
print(coupon_complex)

dish, egg = coupon_complex
print(dish)
print(egg)