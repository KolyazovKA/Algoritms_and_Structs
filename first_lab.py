import random

# Параметры
M = 53  # Размер хеш-таблицы
N = 5   # Размерность элементов
MAX_ATTEMPTS = 30  # Максимальное количество попыток с квадратичными пробами

# Генерация уникальных элементов
elements = set()
while len(elements) < M:
    element = random.randint(10000, 99999)  # Генерация 5-значного числа
    elements.add(element)

elements = list(elements)

# Хеш-таблица
hash_table = [None] * M

# Хеш-функция
def hash_function(key):
    return key % 1000

total_steps = 0  # Общее количество шагов
successful_insertions = 0  # Количество успешных вставок

for element in elements:
    key = element
    index = hash_function(key) % M
    i = 0
    steps = 0
    
    while i < MAX_ATTEMPTS and hash_table[index] is not None:
        i += 1
        steps += 1
        index = (hash_function(key) + i**2) % M
    
    if i == MAX_ATTEMPTS:
        for j in range(M):
            steps += 1
            index = (hash_function(key) + j) % M
            if hash_table[index] is None:
                break
    
    if hash_table[index] is None:
        hash_table[index] = key
        successful_insertions += 1
    
    total_steps += steps

filled_cells = sum(1 for cell in hash_table if cell is not None)
alpha = filled_cells / M

average_steps = total_steps / successful_insertions if successful_insertions > 0 else 0

print("Хеш-таблица:")
for i, value in enumerate(hash_table):
    print(f"Index {i}: {value}")

print(f"\nКоэффициент заполнения (α): {alpha:.2f}")
print(f"Среднее число шагов для размещения элементов: {average_steps:.2f}")
