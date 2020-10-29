# user_list = input('Введите список через пробел: ').split(' ')
user_list = ['1', 2, '3', 4, '5', 6, '7']
for i in range(len(user_list) // 2):
    user_list[2 * i + 1], user_list[2 * i] = user_list[2 * i], user_list[2 * i + 1]
print(user_list)
