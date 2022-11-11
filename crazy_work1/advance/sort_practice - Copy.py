import numpy as np

scores = [91, 95, 97, 99, 92, 93, 96, 98]

scores_sort = scores.copy()
scores_sort.sort()

print(scores_sort, '\n')

sum = 0
for i in scores:
    sum += i
print('the average is', sum / len(scores), '\n')

print(np.mean(scores), '\n')    # use numpy module for the average value

print('scores below average are ', end='')

for j in scores:
    if j < sum / len(scores):
        print(j, '', end='')

print('\n')

scores_sort_2 = np.array(scores)
print(scores_sort_2)
print('scores below average are {}'
      .format(
          scores_sort_2[
              scores_sort_2<(sum/len(scores))
          ]
      )
      )