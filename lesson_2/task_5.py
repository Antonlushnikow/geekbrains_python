my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите новый элемент: '))
# new_el = 1
index = 0
for i in range(len(my_list)):
    if new_el <= my_list[i]:
        index = i + 1
my_list.insert(index, new_el)
print(my_list)
