# coding=utf-8

import numpy as np

scores = [91, 95, 97, 99, 92, 93, 96, 98]

average = np.average(scores)
scores_no_copy = scores
scores_array = np.array(scores)

scores.append(99)

print('scores_no_copy={}'.format(scores_no_copy))
print('scores_array={}'.format(scores_array))

print(scores_array<average)

print('低于平均成绩的有：{}'.format(scores_array[scores_array <average]))
