def check_enter_value():
    while True:
        try:
            number = int(input("Введите число от 1 до 5: "))

            if number > 5 or number < 1:
                print("Ошибка! Число должно быть в диапазона от 1 до 5!")

                continue

            return number

        except ValueError:
            print("Ошибка! Необходимо ввести целое число!")

def get_number_text(number):
    match number:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case 4:
            return "Four"
        case 5:
            return "Five"
    return "Ошибка при попытке преобразовать число в текст!"

print("Соответсвуюшее слово:", get_number_text(check_enter_value()))
