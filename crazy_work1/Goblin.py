q_1 = input('Wound you need help? Y/N ')
if q_1 == 'Y':
    q_2 = int(input('How can I help you? | deposit = 1; exchange = 2; consult = 3 | Your choice = '))
    if q_2 == 1:
        print()
    elif q_2 == 2:
        money = int(input('the exchange = 1:51.3, by which one SKU equals to 51.3 CNY. How much would you like? | Your depost = '))
        print (money / 51.3)
    else:
        print()
else:
    print('Good bye!')