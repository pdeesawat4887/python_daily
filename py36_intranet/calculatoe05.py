def verifyInput(num):
    list_num = [0, 1, 2, 3, 4, 5]

    for chk in str(num):
        if int(chk) not in list_num:
            raise ValueError("Number out of bound, please use only 0, 1, 2, 3, 4, 5")
    return int(num)


def plus(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiple(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calculator():
    dict_operation = {
        '+': plus,
        '-': minus,
        'x': multiple,
        '/': divide,
    }
    while True:
        try:
            num1 = verifyInput(input("Enter your first number: "))
            operation_input = input("Enter your operation: ")

            if operation_input not in dict_operation.keys():
                raise ValueError("Operation Error, please use only +, -, x, /")

            num2 = verifyInput(input("Enter your second number: "))
        except Exception as error:
            print('Error: {err}'.format(err=error))
            continue
        else:
            print("Answer is: {ans}".format(ans=dict_operation[operation_input](num1, num2)))
            break


if __name__ == '__main__':
    calculator()
