import random

m = 53  # Размер хеш-таблицы
n = 5   # Размерность элементов
max_attempts = 30  # Максимальное количество попыток с квадратичными пробами

# Генерация уникальных элементов
elements = set()
while len(elements) < m:
    element = random.randint(10000, 99999)  
    elements.add(element)

elements = list(elements)

# Хеш-таблица
hash_table = [None] * m

# Хеш-функция
def hash_function(key):
    return key % 1000

total_steps = 0  # Общее количество шагов
successful_insertions = 0  # Количество успешных вставок

for element in elements:
    key = element
    index = hash_function(key) % m
    i = 0
    steps = 0
    
    while i < max_attempts and hash_table[index] is not None:
        i += 1
        steps += 1
        index = (hash_function(key) + i**2) % m
    
    if i == max_attempts:
        # Линейные пробы
        for j in range(m):
            steps += 1
            index = (hash_function(key) + j) % m
            if hash_table[index] is None:
                break
    
    if hash_table[index] is None:
        hash_table[index] = key
        successful_insertions += 1
    
    total_steps += steps

# Вычисление коэффициента заполнения
filled_cells = sum(1 for cell in hash_table if cell is not None)
alpha = filled_cells / m

# Среднее число шагов для размещения элементов
average_steps = total_steps / successful_insertions if successful_insertions > 0 else 0

# Вывод результатов
print("Сгенерированные ключи:")
print(elements)
print("\nХеш-таблица:")
for i, value in enumerate(hash_table):
    print(f"Index {i}: {value}")

print(f"\nКоэффициент заполнения (α): {alpha:.2f}")
print(f"Среднее число шагов для размещения элементов: {average_steps:.2f}")
