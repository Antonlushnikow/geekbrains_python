# user_str = input('Введите строку: ')
user_str = 'Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове'
for i, el in enumerate(user_str.split(' '), 1):
    print(f'{i}. {el[:10]}')
