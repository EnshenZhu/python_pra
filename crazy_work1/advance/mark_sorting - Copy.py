list1 = [91, 95, 97, 99]
list2 =  [92, 93, 96, 98]

list_sum = list1.copy() + list2.copy()

print('initial list is ' + str(list_sum))

for i in range(len(list_sum)):
    for j in range(i, len(list_sum)):
        if list_sum[i] < list_sum[j]:
            storage = list_sum[i]
            list_sum[i] = list_sum[j]
            list_sum[j] = storage

print('final list is ' + str(list_sum))