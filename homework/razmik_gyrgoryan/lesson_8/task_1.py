import random

list_bool = [True, False]
salary = int(input())
bonus = random.choice(list_bool)

if bonus:
    salary += random.randint(1, 1000)

print(f'${salary}')
