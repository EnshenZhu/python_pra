# coding=utf-8

# 发放奖金的要求如下：

# 工作时长不满六个月，发放固定奖金500元。
# 工作时长在六个月和一年之间(含一年)，发放奖金120元*月数（如8个月为960元）
# 工作时长在一年以上，发放奖金180元*月数 （如20个月为3600元）


# 定义两个函数：第一个函数功能为根据工作月数返回奖金额，第二个函数功能为打印出'该员工来了XX个月，获得奖金XXX元'。
# 最后传入参数('大聪'，14)调用第二个函数，打印结果'大聪来了14个月，获得奖金2520元'

def bonus_calculation(month):
     if month < 6:
          bonus = 500
     elif 6 <= month <= 12:
          bonus = 120 * month
     else:
          bonus = 180 * month
     return bonus

def main(name, month):
     print('{} has worked for {} monthes, the bonus payment is {}'
           .format(name, month, bonus_calculation(month))
           )

main('大聪', 14)