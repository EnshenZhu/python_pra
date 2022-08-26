#coding=utf-8

movie = {
    '妖猫传':['黄轩','染谷将太'],
    '无问西东':['章子怡','王力宏','祖峰'],
    '超时空同居':['雷佳音','佟丽娅']
}

name=input('你查询的演员是？')
for i in movie:
    actors=movie[i]
    if name in actors:        
        print(name+'出演了'+i)
        verify=True #Prove that the actor name has been found inside the movie name list
        
if (name not in movie[i]) and verify!=True:
    print('This actor is not in the list')  
    #When the previous "for i" loop finished, the i value should be the last key in the movie dictionary.
    #Thus if the input actor name cannot be found at last key indsie the movie dictionary, 
    #and the variable 'verify's value is not True, the input actor name can be regarded as not existed inside the movie name list.
    