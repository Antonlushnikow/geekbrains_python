# products = []
# num_products = int(input('Введите количество товаров: '))
# for i in range(num_products):
#     name = input(f'Введите название товара {i+1}: ')
#     price = float(input(f'Введите цену товара {i+1}: '))
#     amount = int(input(f'Введите количество товара {i+1}: '))
#     measure = input(f'Введите единицу измерения товара {i+1}: ')
#     product = (i+1, {'название': name, 'цена': price, 'количество': amount, 'eд': measure})
#     products.append(product)

products = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

product_keys = list(products[0][1].keys())  # не придумал, как изящнее получить ключи
product_val = []
for num, product in products:
    product_val.append(list(product.values()))

product_val = list(zip(*product_val))  # транспонируем
an_dict = {product_keys[i]: list(set(product_val[i])) for i in range(len(product_keys))}
print(an_dict)

