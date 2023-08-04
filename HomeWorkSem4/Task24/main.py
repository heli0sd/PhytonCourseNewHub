def max_collected_berries(berries):
    n = len(berries)

    # Обработка кустов на круглой грядке
    max_collected = 0
    for i in range(n):
        collected = berries[i] + berries[(i - 1) % n] + berries[(i + 1) % n]
        max_collected = max(max_collected, collected)

    return max_collected

# Чтение данных из файла berries.txt
try:
    with open('berries.txt', 'r') as file:
        n = int(file.readline())
        berries = list(map(int, file.readline().split()))

    result = max_collected_berries(berries)
    print("Максимальное число ягод, которое может собрать собирающий модуль за один заход:", result)

except FileNotFoundError:
    print("Файл 'berries.txt' не найден. Убедитесь, что файл существует в той же папке, что и программа.")