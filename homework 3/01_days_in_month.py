# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if month == int(1):
    print('This is January')
elif month == int(2):
    print('This is February')
elif month == int(3):
    print('This is Marth')
elif month == int(4):
    print('This is April')
elif month == int(5):
    print('This is May')
elif month == int(6):
    print('This is June')
elif month == int(7):
    print('This is July')
elif month == int(8):
    print('This is August')
elif month == int(9):
    print('This is September')
elif month == int(10):
    print('This is October')
elif month == int(11):
    print('This is November')
elif month == int(12):
    print('This is Decamber')
else:
    print('Error!!!\nYear have only 12 months')


# TODO здесь ваш код
