from itertools import product

# Вариант 11. Двухбитный сумматор без переноса
# x1 + x2 = x3 (mod 2), причём x1 или x2 равно 1

names = ['x1', 'x2', 'x3']

print('условия:')
print('x1 + x2 ≡ x3 (mod 2)')
print('x1 ∨ x2 = 1')

# КНФ для сложения по модулю 2 и условия x1 ∨ x2
cnf = [
    [1, 2],
    [1, 2, -3],
    [1, -2, 3],
    [-1, 2, 3],
    [-1, -2, -3]
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

# перебор всех 2^3 = 8 наборов
k = 0
total = 0

for values in product([0, 1], repeat=3):
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
        x1, x2, x3 = values
        print('\nПодходящий набор', k)
        print('x1 =', x1)
        print('x2 =', x2)
        print('x3 =', x3)
        print('проверка суммы:', (x1 + x2) % 2 == x3)
        print('хотя бы один вход равен 1:', bool(x1 or x2))

print('\nпроверено:', total)
print('подходящих наборов:', k)

if k > 0:
    print('SAT — формула выполнима')
else:
    print('UNSAT — формула невыполнима')
