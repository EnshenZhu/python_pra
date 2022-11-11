# coding=utf-8

rent = 3000
# rent is a global variable (全局变量)
 
def cost():
    utilities = int(input('请输入本月的水电费用'))
    food_cost = int(input('请输入本月的食材费用'))
    variable_cost = utilities + food_cost     # recall that that variable_cost is a local variable (局部变量)
    print('本月的变动成本费用是' + str(variable_cost))
    return variable_cost

def sum_cost():
    sum = rent + cost()
    print('本月的总成本是' + str(sum))

sum_cost()