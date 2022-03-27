def convert_dec_hexa(dec_num):
    hex_list = []

    if dec_num == 0:
        hex_list = [0]

    while dec_num != 0:
        unit = dec_num % 16

        if unit <= 9:
            hex_list.append(str(unit))
        elif unit == 10:
            hex_list.append('a')
        elif unit == 11:
            hex_list.append('b')
        elif unit == 12:
            hex_list.append('c')
        elif unit == 13:
            hex_list.append('d')
        elif unit == 14:
            hex_list.append('e')
        elif unit == 15:
            hex_list.append('f')

        dec_num = dec_num // 16

    hex_list.reverse()
    hex_result = ''.join(hex_list)

    return hex_list


print(convert_dec_hexa(725))
