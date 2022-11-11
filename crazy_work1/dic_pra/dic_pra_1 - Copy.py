name = ['tom', 'jack', 'peter']
length_name = len(name)
print(length_name)
print(name)
print(name[:])

scores = {'tom': 95, 'jack': 90, 'peter': 88}
length_score = len(scores)
print(length_score)

print(scores[name[0]])

scores['tom'] = 92
print(scores)