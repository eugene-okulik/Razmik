first_result = "результат операции: 42"
second_result = "результат операции: 514"
third_result = "результат работы программы: 9"

first_index = first_result.index(":")
get_first_number_from_string = first_result[first_index::]
get_first_number_from_string = get_first_number_from_string.lstrip(": ")

second_index = second_result.index(":")
get_second_number_from_string = second_result[second_index::]
get_second_number_from_string = get_second_number_from_string.lstrip(": ")

third_index = third_result.index(":")
get_third_number_from_string = third_result[third_index::]
get_third_number_from_string = get_third_number_from_string.lstrip(": ")

print(int(get_first_number_from_string) + 10)
print(int(get_second_number_from_string) + 10)
print(int(get_third_number_from_string) + 10)
