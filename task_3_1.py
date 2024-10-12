calls = 0

# Функция count_calls подсчитывает вызовы остальных функций
def count_calls():
    global calls
    calls += 1


# Функция string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(string):
    count_calls()
    return (len(string), str(string).upper(), str(string).lower())


# Функция is_contains принимает два аргумента: строку и список,
# и возвращает True, если строка находится в этом списке, False - если отсутствует.
def is_contains(string, list_to_search):
    count_calls()

    for i in range(len(list_to_search)):
        if (type(string) == type(list_to_search[i]) and
            str(string).lower() == str(list_to_search[i]).lower()):
            return True

    return False


while True:
    user_choice = int(input("\nВведите номер функции ('1' - string_info, '2' - is_contains), для выхода введите '0': "))
    if user_choice == 1:
        print('    ' + str(string_info(input('    Введите строку из произвольных символов: '))))
    elif user_choice == 2:
        _str = str(input('    Введите строку из произвольных символов: '))
        _list = str(input('    Введите элементы списка: ')).split()
        print('    ' + str(is_contains(_str, _list)))
    elif user_choice == 0:
        break
    else:
        print('    Неправильно указан номер функции!')

print(f'\nКоличество вызовов функций: {calls}')
