# def print_params(a, b, c):
#     print(a, b, c)
#     print(a + c) #ошибка
#
# print_params('True', True, 1)


# def print_params(a, b, c):
#     print(a, b, c)
#     print(a + c)
#
# print_params(2, True, 1) # должны передать 3 параметра (< или >, ошибка)


# def print_params(a=1, b=2, c=3):
#     print(a, b, c)
#
# print_params()


# def print_params(a=1, b=2, c=3):
#     print(a, b, c)
#
# print_params(3, 1, 2)

#
# def print_params(a=1, b=2, c=3):
#     print(a, b, c)
#
# print_params(1, 2, c = 'Str') #сначала позиционные параметры, потом именованные, наоборот нельзя

# def print_params(a=1, b=2, c=3):
#     print(a, b, c)
#
# print_params(b = 5, a = 1, c = 'Str')


# def print_params(a, *, b, c): #полсе звездочки парметры указываются явно
#     print(a, b, c)
#
# print_params(5, b = 4, c = 8)


 # Домашняя работа по уроку "Способы вызова функции"

# Задача "Рассылка писем":
# Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же пользователя(администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.
# Попробуем реализовать функцию с подробной логикой.
#
# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.
# Пункты задачи:
# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.

def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if ('@' not in recipient and '@' not in sender or
            (not recipient.endswith('.com') and not recipient.endswith('.ru') and not recipient.endswith('.net')) or
            (not sender.endswith('.com') and not sender.endswith('.ru') and not sender.endswith('.net'))):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе')
        return
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return
    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')