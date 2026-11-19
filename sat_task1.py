from itertools import product

# Вариант 11. Преобразование формулы в КНФ
# F = ((x1 or not x2) and x3) -> x4

names = ['x1', 'x2', 'x3', 'x4', 'y1', 'y2', 'y3', 'y4', 'y5']

print('исходная формула:')
print('F = ((x1 ∨ ¬x2) ∧ x3) → x4')

print('\nвспомогательные переменные:')
print('y1 = ¬x2')
print('y2 = x1 ∨ y1')
print('y3 = y2 ∧ x3')
print('y4 = ¬y3')
print('y5 = y4 ∨ x4')
print('выполнение формулы y5 = 1')

# каждая строка списка — одна скобка КНФ
# положительное число — переменная, отрицательное — её отрицание
cnf = [
    [5, 2], [-5, -2],
    [-6, 1, 5], [6, -1], [6, -5],
    [-7, 6], [-7, 3], [7, -6, -3],
    [8, 7], [-8, -7],
    [-9, 8, 4], [9, -8], [9, -4],
    [9]
]

print('\nКНФ (', len(cnf), 'скобок):', sep='')
for c in cnf:
    s = []
    for n in c:
        if n < 0:
            s.append('¬' + names[-n - 1])
        else:
            s.append(names[n - 1])
    print('(' + ' ∨ '.join(s) + ')')

# перебор всех 2^9 = 512 наборов
k = 0
total = 0

for values in product([0, 1], repeat=9):
    total += 1
    ok = True

    for c in cnf:
        res = False
        for n in c:
            x = values[abs(n) - 1]
            if n < 0:
                x = 1 - x
            if x == 1:
                res = True
                break

        if not res:
            ok = False
            break

    if ok:
        k += 1
        print('\nПодходящий набор', k)
        for i in range(9):
            print(names[i], '=', values[i])

print('\n проверено:', total)
print('подходящих наборов:', k)

if k > 0:
    print('SAT — формула выполнима')
else:
    print('UNSAT — формула невыполнима')
