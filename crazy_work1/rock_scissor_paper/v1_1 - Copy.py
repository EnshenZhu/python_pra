#Version 1.1 improve coding logic and running efficiency of the <game funtion>

import random

def is_true(general_basic):
        #extract <punches> and <user choice> from the <general_basic> list
        is_true_punches=general_basic[0]
        is_true_user_choice=general_basic[2]
        
        #figure out whether the <user_choice> is inside the <punches>
        while is_true_user_choice not in is_true_punches: 
                is_true_user_choice=input('your punch is invalid, input your punch again (rock/scissor/paper) // your punch is ')
                
        return is_true_user_choice

def game(game_basic):
        
        #extract <computer_choice> and <user_choice> 
        computer_choice=game_basic[1]
        user_choice=game_basic[2]
        
        print('the computer\'s chocie is %s' %computer_choice)
                
        if computer_choice==user_choice: #the computer and the user hasve the same punch
                print('equal')
        elif computer_choice==game_basic[0][game_basic[0].index(user_choice)-1]: 
                #game_basic[0][0] is rock; game_basic[0][1] is scissor; game_basic[0][2] is paper
                #<game_basic[0].index(user_choice)-1> is to make a shift of the index for comparing between computer choice and the user choice
                #by which game_basic[0][-1] is paper; game_basic[0][0] is rock; game_basic[0][1] is scissor
                #computer may win the game as long as having the value of game_basic[0][x-1], when the user has the value of game_basic[0][x]
                print('computer win')
        else:
                print('user win')
                
                                    
def basic():  #settle down the initial punch list, the computer choice and the user choice
        basic_punches = ['rock','scissor','paper']
        basic_computer_choice = random.choice(basic_punches)
        basic_user_choice = input('your punch is ')
        return basic_punches,basic_computer_choice,basic_user_choice
        
def main():
        general_basic=list(basic()) #the return of the <basic function> was a tuple, we need to list it
        
        game_basic=general_basic
        game_basic[2]=is_true(general_basic)
        #The <user choice> value --game_basic[2]-- from the <basic function>, which may contain invalid value from the input. 
        #We need to overcover it with the valid value from the <is_true function>        
        
        game(game_basic)

main()