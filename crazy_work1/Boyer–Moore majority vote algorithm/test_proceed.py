def findMajority(num_list: list[int]):
    counter = 1
    majority = num_list[0]

    for num in num_list[1:]:
        if counter == 0:
            majority = num

        if num == majority:
            counter += 1
        else:
            counter -= 1

        print("majority=" + str(majority) + " counter=" + str(counter))

    return majority, counter


list1 = [1,2,2,2,1,5]
print(findMajority(list1))
