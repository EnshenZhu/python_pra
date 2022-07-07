def FindMissingNum(arr):
    result = []

    if len(arr) > 1:
        # create the hash table for the input arr
        hash_table = {}
        for unit_num in arr:
            hash_table[unit_num] = True

        # check the missing number
        num_is_missing = False  # default setting the passed array have no missing numbers
        for target_num in range(min(arr), max(arr) + 1):
            if target_num not in hash_table:
                num_is_missing = True
                result.append(target_num)

        if not num_is_missing:
            result.append(0)
    else:
        result.append(0)

    return result
