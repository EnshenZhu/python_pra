# coding=utf-8

import time
import random
#也可合并写成一行：import time,random

# 生成随机属性
player_life = random.randint(100,150) # “player_life” 代表玩家血量
player_attack = random.randint(30,50) # “player_attack” 代表玩家攻击
enemy_life = random.randint(100,150) # “enemy_life” 代表敌人血量
enemy_attack = random.randint(30,50) # “enemy_attack” 代表敌人攻击

# 展示双方角色的属性
print('【玩家】\n'+'血量：'+str(player_life)+'\n攻击：'+str(player_attack))
#player_life和player_attack的数据类型都是整数，所以拼接时需要先用str()转换
print('------------------------')
time.sleep(1)
# 暂停一秒再执行后续代码

print('【敌人】\n'+'血量：'+str(enemy_life)+'\n攻击：'+str(enemy_attack))
print('------------------------')
time.sleep(1)

while (player_life
        and
        enemy_life):
    
    player_life = player_life - enemy_attack
    enemy_life = enemy_life - player_attack

    if player_life < 0:
        player_life = 0

    if enemy_life < 0:
        enemy_life = 0

    print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))
    print('敌人向你发起了攻击，【玩家】剩余血量' + str(player_life))
    print('------------------------')
    time.sleep(1)

if player_life == 0:
    print('you are dead')

if enemy_life == 0:
    print('enemy eliminated')