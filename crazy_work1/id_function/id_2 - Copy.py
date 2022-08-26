list_ = [1, 2, 3]
list_id = id(list_)

tuple_ = (1, 2, 3)
tuple_id = id(tuple_)

for i in range(5):
    list_ += [i]
    tuple_ += (i, )

print(list_)
print(tuple_)

print(list_id == id(list_))
print(tuple_id==id(tuple_))