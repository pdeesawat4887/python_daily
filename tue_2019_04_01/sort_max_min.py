def sorted(input_number):
    temp_list = [int(x) for x in input_number.split(',')]
    temp_list.sort(reverse=True)
    return temp_list


print(sorted("2, 3, 4, 5, 6, 7"))
