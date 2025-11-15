# Задание 1

def find_min_index(data_list):
    """
    Находит индекс наименьшего элемента в заданном списке.
    Предполагается, что список не пустой.
    """
    if not data_list:
        # Это для защиты от ошибок, если вдруг список пустой
        return -1

    min_val = data_list[0]
    min_idx = 0

    # Перебираем список, начиная со второго элемента (индекс 1)
    for i in range(1, len(data_list)):
        if data_list[i] < min_val:
            min_val = data_list[i]
            min_idx = i

    return min_idx


# Пример использования:
# numbers = [5, 1, 9, 3, 7]
# print(find_min_index(numbers)) # Выведет: 1


# Задание 2

def sort_numbers_in_string(input_string):
    """
    Принимает строку чисел, разделенных пробелами,
    сортирует их и возвращает отсортированную строку.
    """

    # 1. Разбиваем строку на отдельные строковые числа
    str_numbers = input_string.split()

    # 2. Преобразуем строковые числа в целые числа (int)
    # Используем генератор списка, чтобы было "красиво"
    try:
        int_numbers = [int(num) for num in str_numbers]
    except ValueError:
        # Если в строке мусор, возвращаем пустую строку, чтобы не упасть
        return "Ошибка: в строке должны быть только числа."

    # 3. Сортируем список чисел
    # Используем встроенный метод sort(), это стандартный подход
    int_numbers.sort()

    # 4. Преобразуем отсортированные числа обратно в строки
    sorted_str_numbers = [str(num) for num in int_numbers]

    # 5. Объединяем их обратно в одну строку через пробел
    result_string = " ".join(sorted_str_numbers)

    return result_string

# Пример использования:
# data = "45 12 9 100 3"
# print(sort_numbers_in_string(data)) # Выведет: 3 9 12 45 100
