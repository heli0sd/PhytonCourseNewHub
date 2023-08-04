# Вводите стороны монеток в формате "0111000"
coins = input("Введите стороны монеток (введите 0 или 1 без пробелов): ")

heads = 0
tails = 0

for coin in coins:
    if coin == '0':
        heads += 1
    else:
        tails += 1

min_flips_needed = min(heads, tails)
print("Минимальное количество монеток для переворота:", min_flips_needed)