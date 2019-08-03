import random


def foo(number, digit, position, ex_00, ex_11, ex_xx00, ex_xx11, counter):
    str_num = str(number)

    print("Lastest: {}{}".format(ex_00, ex_11))

    if str_num.__len__() == 1:
        num0 = 0
        num1 = int(str_num)
    else:
        num0 = int(str_num[0])
        num1 = int(str_num[1])

    if digit == 0 and position == 0:
        if ex_00 == 1 and ex_11 == 0:
            # print("00/10")
            num1 = ex_xx00
            restrict0.append(ex_xx11)
            num0 = random.choice([x for x in nnn0 if x not in restrict0])
            return True, num0, num1
        elif ex_00 == 2 and ex_11 == 1:
            num0 = num1 = ex_xx00
            return True, num0, num1
        else:
            restrict0.append(num0)
            restrict0.append(num1)
            restrict1.append(num0)
            restrict1.append(num1)
            return True, random.choice([x for x in nnn0 if x not in restrict0]), random.choice(
                [x for x in nnn1 if x not in restrict1])
    elif digit == 2 and position == 2:
        print("Solve this puzzle in {cnt} turn.".format(cnt=counter))
        return False, num0, num1

    elif digit == 2 and position == 0:
        temp_n = num0
        num0 = num1
        num1 = temp_n
        return True, num0, num1
    elif digit == 2 and position == 1:
        num0 = num1
        return True, num0, num1
    elif digit == 1:
        if position == 0:
            # nnn.remove(num1)
            # restrict1.append(num1)
            num1 = num0
            num0 = random.choice([x for x in nnn1 if x not in restrict1])
            return True, num0, num1
        elif position == 1:
            # restrict1.append(num1)
            # nnn.remove(num1)
            if ex_00 == 1 and ex_11 == 1:
                # print("11/11")
                num1 = ex_xx11
                # restrict0.append(ex_xx00)
                num0 = random.choice([x for x in nnn1 if x not in restrict1])
                return True, num0, num1
            else:
                num1 = random.choice([x for x in nnn1 if x not in restrict1])
                return True, num0, num1
    else:
        return True, random.randint(0, 9), random.randint(0, 9)

    print("num0", num0)
    print("num1", num1)
    # print("nnn0: {}\nres0: {}\nnnn1: {}\nres1: {}".format(nnn0, restrict0, nnn1, restrict1))


if __name__ == '__main__':

    user_number = input("Enter your number: ")
    flag = True
    temp = random.randint(10, int(user_number))
    xx1 = str(temp)[0]
    xx2 = str(temp)[1]
    print("random", temp)

    nnn0 = nnn1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    restrict0 = []
    restrict1 = []
    ex_status0 = 9
    ex_status1 = 9
    ex_val0 = 0
    ex_val1 = 0

    counter = 0

    while flag:
        user_ans = input("Enter correct [digit][position]: ")

        digit = int(str(user_ans)[0])
        position = int(str(user_ans)[1])

        flag, xx1, xx2 = foo(''.join(map(str, [int(xx1), int(xx2)])), digit, position, ex_status0, ex_status1, ex_val0, ex_val1,
                             counter)
        print("random: {}{}".format(xx1, xx2))
        ex_val0 = xx1
        ex_val1 = xx2
        ex_status0 = digit
        ex_status1 = position
        counter += 1
        # print("nnn0: {}\nres0: {}\nnnn1: {}\nres1: {}".format(list(nnn0), restrict0, list(nnn1), restrict1))
