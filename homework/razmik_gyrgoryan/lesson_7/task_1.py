def guessing_game():
    number = 7
    guess_number = int(input("Угадайте цифру: "))
    while True:
        if number == guess_number:
            print("Поздравляю! Вы угадали!")
            break
        elif number != guess_number:
            guess_number = int(input("попробуйте снова: "))
            continue


guessing_game()
