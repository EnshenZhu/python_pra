import random
import time

#���Խ���
print('��ã����ǻ�����С������������������С��Ϸ��')
time.sleep(2)


print('С�����ʵ������1��10֮��Ŷ��')
time.sleep(2)


print('��������ֻ��5�λ���Ŷ��')
time.sleep(2)


print('���棬������С�������ɣ�')


#��0��10����һ���������������ֵ������age
age = random.randint(1,10)


#���ô���
for guess in range(1,6):
   
   #������Ҳ²������
    choice=int(input())
    
    #�ж��������������Ƿ������ȷ������
    if choice<age:
        print('С�����ʾ�����С��')
                
    elif choice>age:
        print('С�����ʾ���˲´�����')
            
    else: 
        print('����'+str(guess)+'�Σ���Ͳ¶���')
        break   
                
#�жϲ²���� 
if choice  == age:
    time.sleep(5)
    print('�Ѹ�����ôС�������ˡ��ݰ�')
    
else:
    print('��ѽ���㻹��ľ�в¶԰���������ֻ��5�λ���������ô�찡��')
    print('�Ǻðɡ������С��ֻ�ø����㣬�Ҳ�'+str(age)+'��Ŷ')