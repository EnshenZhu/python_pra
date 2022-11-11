numbers = [[], (0, ), None, '0']

filtered = filter(None, numbers)

print(filtered)

for i in filtered:
    print(i, end='')