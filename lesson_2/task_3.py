# Решение через list
month = 12
seasons = ['зима', 'весна', 'лето', 'осень']
if month == 12:
    month = 0
season_index = month // 3
print(seasons[season_index])

# Решение через dict
month = 12
seasons = {
    (1, 2, 12): 'зима',
    (3, 4, 5): 'весна',
    (6, 7, 8): 'лето',
    (9, 10, 11): 'осень',
}

for key, value in seasons.items():
    if month in key:
        print(value)
