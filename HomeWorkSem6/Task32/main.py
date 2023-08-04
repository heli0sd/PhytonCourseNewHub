def find_indexes_in_range(arr, minimum, maximum):
    indexes = []
    for i, num in enumerate(arr):
        if minimum <= num <= maximum:
            indexes.append(i)
    return indexes

# Пример использования
my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_value = 5
max_value = 15

result = find_indexes_in_range(my_list, min_value, max_value)
print("Индексы элементов, которые принадлежат заданному диапазону:")
print(result)