import random

# Создаем исходный список для работы
# Пусть будет 20 элементов от -10 до 10
original_list = [random.randint(-10, 10) for _ in range(20)]
print(f"Исходный список: {original_list}")
print("-" * 30)

# ЗАДАНИЕ 1: Вычисления

# 1. Сумма отрицательных чисел
sum_neg = 0
for num in original_list:
    if num < 0:
        sum_neg += num
print(f"Сумма отрицательных: {sum_neg}")

# 2. Сумма четных чисел
sum_even = 0
for num in original_list:
    # Проверяем, делится ли на 2 без остатка
    if num % 2 == 0:
        sum_even += num
print(f"Сумма четных: {sum_even}")

# 3. Сумма нечетных чисел
sum_odd = 0
for num in original_list:
    if num % 2 != 0:
        sum_odd += num
print(f"Сумма нечетных: {sum_odd}")

# 4. Произведение элементов с индексами кратными 3
prod_index_3 = 1
for i in range(len(original_list)):
    # Индекс 0 тоже кратен 3!
    if i % 3 == 0:
        prod_index_3 *= original_list[i]
print(f"Произведение элементов с индексами кратными 3: {prod_index_3}")

# 5. Произведение элементов между минимальным и максимальным
# Сначала ищем индексы min и max
min_val = min(original_list)
max_val = max(original_list)

# Находим первый встреченный индекс
idx_min = original_list.index(min_val)
idx_max = original_list.index(max_val)

# Определяем границы для цикла (важно, чтобы цикл шел от меньшего индекса к большему)
start_idx = min(idx_min, idx_max)
end_idx = max(idx_min, idx_max)

prod_between_min_max = 1
# Идем от индекса, следующего за меньшим, до индекса, ПРЕДШЕСТВУЮЩЕГО большему
for i in range(start_idx + 1, end_idx):
    prod_between_min_max *= original_list[i]

print(f"Произведение между min ({min_val} на {idx_min}) и max ({max_val} на {idx_max}): {prod_between_min_max}")

# 6. Сумма элементов между первым и последним положительными
first_pos_idx = -1
last_pos_idx = -1

# Ищем первый положительный
for i in range(len(original_list)):
    if original_list[i] > 0:
        first_pos_idx = i
        break  # Нашли и выходим

# Ищем последний положительный (идем с конца)
for i in range(len(original_list) - 1, -1, -1):
    if original_list[i] > 0:
        last_pos_idx = i
        break  # Нашли и выходим

sum_between_pos = 0
# Проверяем, что положительные вообще есть и они не совпадают
if first_pos_idx != -1 and first_pos_idx < last_pos_idx:
    # Суммируем элементы между ними
    for i in range(first_pos_idx + 1, last_pos_idx):
        sum_between_pos += original_list[i]

print(f"Сумма между первым ({first_pos_idx}) и последним ({last_pos_idx}) положительными: {sum_between_pos}")
print("-" * 30)

# =================================================================
# ЗАДАНИЕ 2: Создание новых списков
# =================================================================

# Используем обычные циклы и append, чтобы не палиться с list comprehensions

even_list = []
odd_list = []
negative_list = []
positive_list = []

for element in original_list:
    # Четные
    if element % 2 == 0:
        even_list.append(element)
    # Нечетные
    else:
        odd_list.append(element)

    # Отрицательные
    if element < 0:
        negative_list.append(element)
    # Положительные (ноль не включаем)
    elif element > 0:
        positive_list.append(element)

print(f"Список четных: {even_list}")
print(f"Список нечетных: {odd_list}")
print(f"Список отрицательных: {negative_list}")
print(f"Список положительных: {positive_list}")
