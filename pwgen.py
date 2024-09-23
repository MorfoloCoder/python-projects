import random

charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*'

while True:
    choice = input('Добро пожаловать в генератор паролей!\n1.Продолжить\n2.Выйти\n')
    if choice == '1':
        nums = int(input('Количество паролей: '))
        length = int(input('Длина паролей: '))
        choice1 = input('Куда вы хотите вывести пароли?\n1.В консоль\n2.В файл\n')
        if choice1 == '1':
            for i in range(nums):
                password =''
                for n in range(length):
                    password += random.choice(charset)
                print(password)
        elif choice1 == '2':
            for i in range(nums):
                password =''
                for n in range(length):
                    password += random.choice(charset)
                with open('password.txt', 'w') as file:
                    print(password, file=file, sep='\n')
        print('Пароли записаны в файл password.txt')
    elif choice == '2':
        break