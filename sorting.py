import random

# 10000 случайных чисел от -100 до 100
random.seed(45)
a = [random.randint(-100, 100) for i in range(10000)]


# 1 cортировка пузырьком
def bubble(a):
    count = 0

    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            count += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return count


# 2 cортировка вставками с  insert
def insertion(a):
    count = 0

    for i in range(1, len(a)):
        key = a.pop(i)
        j = i - 1

        while j >= 0:
            count += 1
            if a[j] > key:
                j -= 1
            else:
                break

        a.insert(j + 1, key)
    return count


# 3 Хоара с двумя кортежами
def hoare(a):
    if len(a) <= 1:
        return tuple(a), 0

    x = a[len(a) // 2]

    # 2 кортежа: элементы меньше и больше опорного
    left = tuple(value for value in a if value < x)
    right = tuple(value for value in a if value > x)

    # количество элементов, равных опорному
    equal_count = len(a) - len(left) - len(right)

    count = 2 * len(a)

    # рекурсивная сортировка левого и правого кортежа
    left, count_left = hoare(left)
    right, count_right = hoare(right)

    # отсортированный кортеж
    result = left + (x,) * equal_count + right
  
    return result, count + count_left + count_right

# копии исходного массива
b = a.copy()
c = a.copy()
d = a.copy()

# сортировка и подсчёт сравнений
count_bubble = bubble(b)
count_insertion = insertion(c)

d, count_hoare = hoare(d)
d = list(d)

# вывод количества сравнений
print("пузырёк:", count_bubble, "сравнений")
print("вставки:", count_insertion, "сравнений")
print("хоара:", count_hoare, "сравнений")

# проверка правильности сортировки
print("все массивы правильно отсортированы:",
      b == c == d == sorted(a))
print("первые 10 чисел:", d[:10])

# сравнение количества сравнений
print("пузырёк / хоара:", round(count_bubble / count_hoare, 2))
print("вставки / хоара:", round(count_insertion / count_hoare, 2))
