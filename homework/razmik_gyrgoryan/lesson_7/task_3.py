def some_program(first_result, second_result, third_result, last_result):
    return (
        int(first_result.split()[-1]) + 10,
        int(second_result.split()[-1]) + 10,
        int(third_result.split()[-1]) + 10,
        int(last_result.split()[-1]) + 10
    )


print(*some_program(
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
))
