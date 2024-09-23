from time import sleep

v_pass = 'qwerty111'
print('Добро пожаловать в установщик RTX4090!\n')
nick = input('Введите логин: ')
u_pass = input('Введите пароль: ')

if u_pass == v_pass:
    with open('log.txt', 'w') as file:
       print(nick, u_pass, file=file, sep='\n')
    print('Верный пароль! Установка начинается...')
    sleep(1)
    for i in range(10, 110, +10):
        print(i, '%')
        sleep(0.5)
    print('Установка завершена! Удачного использования RTX4090!')
else:
    print('Неверный логин или пароль, или такого аккаунта не существует.')
