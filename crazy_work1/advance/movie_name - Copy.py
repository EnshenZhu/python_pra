# coding=utf-8


# 我很喜欢看电影，我回忆了一下，这两年我觉得还不错的国产电影。
# 下面，会将电影的影片名和主演放在字典里，如movie = {'妖猫传':['黄轩','染谷将太']}。
# 需要你补充一些代码，让其他人只要输入演员名，就打印出：××出演了电影××。


movies = {
    '妖猫传': ['黄轩', '染谷将太'],
    '无问西东': ['章子怡', '王力宏', '祖峰'],
    '超时空同居': ['雷佳音', '佟丽娅'],
}

actor = input('你想查询哪个演员？')

for movie_name in movies:
    if actor in movies[movie_name]:
        print(actor + ' cast the movie ' + movie_name)