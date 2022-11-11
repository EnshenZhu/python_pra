# coding=utf-8


# 我很喜欢看电影，我回忆了一下，这两年我觉得还不错的国产电影。
# 下面，会将电影的影片名和主演放在字典里，如movie = {'妖猫传':['黄轩','染谷将太']}。
# 需要你补充一些代码，让其他人只要输入演员名，就打印出：××出演了电影××。


movies = {
    '妖猫传': ['黄轩', '染谷将太'],
    '无问西东': ['章子怡', '王力宏', '祖峰'],
    '超时空同居': ['雷佳音', '佟丽娅'],
}

actor = ''   # initial 'actor' variable

while actor != 'end':
    actor = input('你想查询哪个演员？')
    
    for movie_name in movies:
        if actor in movies[movie_name]:   # if the actor name inside the dictionary, print the name of the movie
            print(actor + ' cast the movie ' + movie_name)
            break
        elif actor == 'end' or actor == 'END':  # input 'end' or 'END' to terminate the script
            continue
        elif movie_name == list(movies)[-1]:  # print 'the actor does not exist' when the actor name cannot be found inside the dictionary
            print('the actor does not exist')

print(list(movies))