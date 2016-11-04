print('Здравствуйте! Вас приветствует программа-анкета!')
name = input('Укажите Ваше имя:')
lastname = input('Ваша фамилия:')
age = int(input('Ваш возраст:'))
programmer = input('Вы умеете программировать? (да/нет)')
if programmer == 'да':
    programmer = True
else:
    programmer = False

print('А я думал, что Вам', age + 1, 'лет,', name, lastname)
if programmer:
    print('Я рад, что Вы - программист!')
else:
    print('Ну ничего, скоро научишься!')
