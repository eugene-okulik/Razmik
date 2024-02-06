first_result = "результат операции: 42"
second_result = "результат операции: 514"
third_result = "результат работы программы: 9"

print(int(first_result[first_result.index("42"):]) + 10)
print(int(second_result[second_result.index("514"):]) + 10)
print(int(third_result[third_result.index("9"):]) + 10)
