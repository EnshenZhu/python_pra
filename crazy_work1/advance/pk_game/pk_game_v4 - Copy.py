# coding=utf-8
# featured with ranged random AP + 15% chance of double damage

import time
import random
#也可合并写成一行：import time,random

_round_ = 0   # counting game rounds

# 生成随机属性
player_HP = random.randint(800, 2200)       # “player_HP 代表玩家血量
player_AP_max = 0                           # initialize player_AP_max
player_AP_min = 1                           # initialize player_AP_min

while player_AP_min > player_AP_max:        # make sure the player has minimum AP lower than maximum AP
    player_AP_min = random.randint(25, 55)  # player's minimum AP
    player_AP_max = random.randint(45, 75)  # player's minimum AP

enemy_HP = random.randint(800, 2200)        # “enemy_HP 代表敌人 血量
enemy_AP_max = 0                            # initialize enemy_AP_max
enemy_AP_min = 1                            # initialize enemy_AP_min

while enemy_AP_min > enemy_AP_max:          # make sure the enermy has minimum AP lower than maximum AP
    enemy_AP_min = random.randint(25, 55)   # enemy's minimum AP
    enemy_AP_max = random.randint(45, 75)   # enemy's minimum AP

# 展示双方角色的属性
print('【玩家】'
      +'\n血量：'+str(player_HP)
      +'\n攻击：'+str(player_AP_min) + ' to '+str(player_AP_max))
# player_HP和player_AP(min or max)的数据类型都是整数，所以拼接时需要先用str()转换

print('------------------------')
time.sleep(1)
# 暂停一秒再执行后续代码

print('【敌人】'
      + '\n血量：' + str(enemy_HP)
      + '\n攻击：' + str(enemy_AP_min) + ' to ' + str(enemy_AP_max))
print('------------------------')
time.sleep(1)

def _double_damage_():
    return random.choices(population=[1, 2], weights=[85, 15])[0]
    # 15% chance double damage function

while player_HP and enemy_HP:

    _round_ += 1


    enemy_double_damage = _double_damage_()
    # enemy attacks while triggering double damage by 15% chance
    
    enemy_stage_AP = random.randint(enemy_AP_min, enemy_AP_max) * enemy_double_damage
    # enemy attacks the player enemy AP is randomly ranged between enemy_AP_min and enemy_AP_max with the multiplication of the double damage

    player_HP = player_HP - enemy_stage_AP

    ####################我是华丽的分界线########################

    player_double_damage = _double_damage_()
    player_stage_AP = random.randint(player_AP_min, player_AP_max) * player_double_damage
    enemy_HP = enemy_HP - player_stage_AP
    # same as above

    if player_HP < 0:
        player_HP = 0

    if enemy_HP < 0:
        enemy_HP = 0

    print('Round ' + str(_round_))

    if enemy_double_damage == 1:
        print('【敌人】向你发起了攻击，造成' + str(enemy_stage_AP) + '伤害，【玩家】剩余血量' + str(player_HP))
    else:
        print('【敌人】向你发起了攻击，造成' + str(enemy_stage_AP) + '伤害，【玩家】剩余血量' + str(player_HP) + ', get double damaged!!!')

    if player_double_damage == 1:
        print('【玩家】向【敌人】发起了攻击，造成' + str(player_stage_AP) + '伤害，【敌人】剩余血量' + str(enemy_HP))
    else:
        print('【玩家】向【敌人】发起了攻击，造成' + str(player_stage_AP) + '伤害，【敌人】剩余血量' + str(enemy_HP) + ', get double damaged!!!')

    print('------------------------')
    time.sleep(1)

if player_HP == 0:
    print('you are dead')

if enemy_HP == 0:
    print('enemy eliminated')