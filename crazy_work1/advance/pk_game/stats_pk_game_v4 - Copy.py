# coding=utf-8
# featured with ranged random AP + double damage

import random
#也可合并写成一行：import time,random

def game():

    # 生成随机属性
    player_HP = random.randint(800, 2200)       # “player_HP 代表玩家血量
    player_AP_max = 0                           # initialize player_AP_max
    player_AP_min = 1                           # initialize player_AP_min

    while player_AP_min > player_AP_max:        # make sure the player has minimum AP smaller than maximum AP
        player_AP_min = random.randint(25, 55)  # player's minimum AP
        player_AP_max = random.randint(45, 75)  # player's minimum AP

    enemy_HP = random.randint(800, 2200)        # “enemy_HP 代表敌人 血量
    enemy_AP_max = 0                            # initialize enemy_AP_max
    enemy_AP_min = 1                            # initialize enemy_AP_min

    while enemy_AP_min > enemy_AP_max:          # make sure the enermy has minimum AP smaller than maximum AP
        enemy_AP_min = random.randint(25, 55)   # enemy's minimum AP
        enemy_AP_max = random.randint(45, 75)   # enemy's minimum AP

    def _double_damage_():
        return random.choices(population=[1, 2], weights=[85, 15])[0]
    # 15% chance double damage function

    while player_HP and enemy_HP:

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

    return player_HP, enemy_HP


stats = [0, 0, 0]
for _ in range(100):

    game()

    if player_HP == 0:
        stats[1] += 1
    elif enemy_HP == 0:
        stats[0] += 1
    else:
        stats[2] += 1

print(stats)