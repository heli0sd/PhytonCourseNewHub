# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по 
# номеру строки и столбца. Аргументы num_rows и num_columns указывают 
# число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой 
# ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    print("    ", end="")
    for col in range(1, num_columns + 1):
        print(f"{col:8}", end="")
    print()
    
    print("  " + "-" * (num_columns * 8))
    
    for row in range(1, num_rows + 1):
        print(f"{row}| ", end="")
        for col in range(1, num_columns + 1):
            result = operation(row, col)
            print(f"{result:8}", end="")
        print()

# Вызов функции 
print_operation_table(lambda x, y: x * y)