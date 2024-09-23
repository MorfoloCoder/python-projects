while True:
    choice = input('Добро пожаловать в ридер файлов!\n1.Продолжить\n2.Выйти\n')
    if choice == '1':
        filename = input('Введите название файла(с расширением, предварительно закинув его в папку с reader.py): ')
        print('Содержание файла:')
        with open(filename, 'r') as file:
            text = file.read()
            print(text)
    elif choice == '2':
        break
