# Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
# — не менее 8 символов
# — наличие прописных и строчных букв
# — наличие цифр
# и переводит его в хэш-значение.

import hashlib
def is_valid_password(password):
    flag1=False
    flag2 = False
    flag3 = False
    for c in password:
        if c.isdigit():
            flag1=True
        elif c==c.upper():
            flag2=True
        elif c == c.lower():
            flag3=True
    if len(password) >=8 and flag1 and flag3 and flag2:
        return True
    else: return False

password = input('Введите ваш пароль: ')
while not is_valid_password(password):
    password= input('Пароль некорректен. Введите ваш пароль: ')
    is_valid_password(password)
print(f'Хэш-значение пароля: {hashlib.sha256(password.encode()).hexdigest()}')

