import random

sequence = ['a', 'b', 'c', 'd']

for _ in range(5):
    print(random.choices(population=sequence,
                         k=2)
          )