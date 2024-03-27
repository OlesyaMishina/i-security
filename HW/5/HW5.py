# Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
# — не менее 8 символов
# — наличие прописных и строчных букв
# — наличие цифр
# и переводит его в хэш-значение.

import hashlib
def is_valid_password(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])

password = input('Введите ваш пароль: ')
while not is_valid_password(password):
    password= input('Пароль некорректен. Введите ваш пароль: ')
    is_valid_password(password)
print(f'Хэш-значение пароля: {hashlib.sha256(password.encode()).hexdigest()}')