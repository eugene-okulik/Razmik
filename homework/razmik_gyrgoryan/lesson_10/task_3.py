def decorator(func):

    def wrapper(first_number, second_number):
        if first_number == second_number:
            return func(first_number, second_number, '+')
        if first_number < 0 or second_number < 0:
            return func(first_number, second_number, '*')
        elif first_number > second_number:
            return func(first_number, second_number, '-')
        elif first_number < second_number:
            return func(first_number, second_number, '/')

    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == "-":
        return second - first
    elif operation == "/":
        return first / second
    elif operation == "*":
        return first * second


number_one = int(input("Введите первое число: "))
number_two = int(input("Введите второе число: "))
print("Результат:", calc(number_one, number_two))
