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
        
        #extract <computer_chocie> and <user_choice> 
        computer_chocie=game_basic[1]
        user_choice=game_basic[2]
        
        print('the computer\'s chocie is %s' %computer_chocie)
        
        if computer_chocie=='rock':  #the computer draw the rock
                if user_choice=='rock':
                        print('equal')
                elif user_choice=='scissor':
                        print('computer win')
                else:
                        print('user win')
                        
        elif computer_chocie=='scissor':   #the computer draw the scissor
                if user_choice=='rock':
                        print('user win')
                elif user_choice=='scissor':
                        print('equal')
                else:
                        print('computer win')
                        
        elif computer_chocie=='paper':  #the computer draw the paper
                if user_choice=='rock':
                        print('computer win')
                elif user_choice=='scissor':
                        print('user win')
                else:
                        print('equal')                        
     
def basic(): #settle down the initial punch list, the computer choice and the user choice
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