# ======================================== 2.1
import math
a, b = (int(input()) for _ in range(2))
print(a + b, a - b, a * b, a / b, a // b, a % b, math.sqrt(a ** 10 + b ** 10), sep = '\n')
# ----------------------------------------
m, h = (float(input()) for _ in range(2))
index = m / (h ** 2)
if 18.5 <= index <= 25:
    print('Оптимальная масса')
elif index < 18.5:
    print('Недостаточная масса')
else:
    print('Избыточная масса')
# ----------------------------------------
price = len(input()) * 60
print(f'{price // 100} р. {price % 100} коп.')
# ----------------------------------------
print(len(input().split()))
# ----------------------------------------
print(['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц'][int(input()) % 12 - 8])
# ----------------------------------------
str_ = input()
print(int(str_[::-1]) if len(str_) == 5 else int(str_[0] + str_[1:][::-1]))

s = input()
print(int(s[:-5] + s[-5:][::-1]))
# ----------------------------------------
s = input()
def spl(s):
    split0 = s.split(',')[0]
    if len(split0) > 3:
        return spl(split0[:-3]) + ',' + split0[-3:]
    else:
        return s
print(spl(s))

num = input()
for idx in range(len(num) - 3, 0, -3):
    num = num[:idx] + ',' + num[idx:]
print(num)

num = int(input())
print(f'{num:,}')
# ----------------------------------------
n, k = (int(input()) for _ in range(2))
l = list(range(1, n + 1))
while len(l) > 1:
    if k <= len(l):
        l.pop(k - 1)
        l = l[k - 1:] + l[:k - 1]
    else:
        len_ = len(l)
        l.pop(k % len_ - 1)
        if k % len_ == 0:
            continue
        l = l[k % len_ - 1:] + l[:k % len_ - 1]
print(l[0])

n = int(input())
k = int(input())
res = 0
for i in range(1, n+1):
    res = (res + k) % i
print(res + 1)
# ======================================== 2.2
l = [(input().split()) for _ in range(int(input()))]
p1, p2, p3, p4 = 0, 0, 0, 0
for i in l:
    x = int(i[0])
    y = int(i[1])
    if x > 0 and y > 0:
        p1 += 1
    elif x < 0 and y > 0:
        p2 += 1
    elif x < 0 and y < 0:
        p3 += 1
    elif x > 0 and y < 0:
        p4 += 1
print(f'Первая четверть: {p1}')
print(f'Вторая четверть: {p2}')
print(f'Третья четверть: {p3}')
print(f'Четвертая четверть: {p4}')
# ----------------------------------------
l = [int(i) for i in input().split()]
print(len([i for i in range(len(l) - 1) if l[i + 1] > l[i]]))

a = tuple(map(int, input().split()))
print(sum(a[i - 1] < a[i] for i in range(1, len(a))))
# ----------------------------------------
l = [i for i in input().split()]
for i in range(len(l) // 2):
    l[i * 2], l[i * 2 + 1] = l[i * 2 + 1], l[i * 2]
print(' '.join(l))

print(*list(__import__('itertools').chain(*(lambda a: [(a[i], a[i-1]) for i in range(1, len(a), 2)] + a[len(a)//2*2:])(input().split()))))
# ----------------------------------------
l = [i for i in input().split()]
print(' '.join(l[-1:] + l[:-1]))

a = input().split()
print(*[a[-1]] + a[:-1])

n = input().split()
print(n.pop(), *n)
# ----------------------------------------
print(len(set(input().split())))
# ----------------------------------------
l = [int(input()) for _ in range(int(input()))]
n = int(input())
print('ДА' if any([1 for i in range(len(l)) if (l[i] != 0 and n / l[i] in l[:i] + l[i + 1:])]) else 'НЕТ')
# print('ДА' if     [1 for i in range(len(l)) if (l[i] != 0 and n / l[i] in l[:i] + l[i + 1:])]  else 'НЕТ')

from itertools import combinations
numbers = [int(input()) for _ in range(int(input()))]
target = int(input())
print('ДА' if len([1 for a, b in combinations(numbers, 2) if a * b == target]) else 'НЕТ')
# ----------------------------------------
a, b = (input() for _ in range(2))
if a == 'камень':
    if b == 'ножницы':
        print('Тимур')
    elif b == 'бумага':
        print('Руслан')
    else:
        print('ничья')
elif a == 'ножницы':
    if b == 'бумага':
        print('Тимур')
    elif b == 'камень':
        print('Руслан')
    else:
        print('ничья')
elif a == 'бумага':
    if b == 'камень':
        print('Тимур')
    elif b == 'ножницы':
        print('Руслан')
    else:
        print('ничья')

print(['ничья', 'Тимур', 'Руслан'][input().count('а') - input().count('а')])

a, b = input(), input()
print('ничья' if a == b else 'Тимур' if a + b in ('каменьножницы', 'бумагакамень', 'ножницыбумага') else 'Руслан')
# ----------------------------------------
a, b = (input() for _ in range(2))
options = ['ножницы', 'бумага', 'камень', 'ящерица', 'Спок']
if options.index(b) in ((options.index(a) + 1) % len(options), (options.index(a) + 3) % len(options)):
    print('Тимур')
elif options.index(a) in ((options.index(b) + 1) % len(options), (options.index(b) + 3) % len(options)):
    print('Руслан')
else:
    print('ничья')

g = ('ножницы', 'бумага', 'камень', 'ящерица', 'Спок')
dist = (g.index(input()) - g.index(input())) % len(g)
print(('ничья', 'Тимур', 'Руслан')[dist and dist % 2 + 1])
# ----------------------------------------
print(max([len(i) for i in input().split('О')]))

print(len(max(input().split('О'))))
# ----------------------------------------
import re
pattern = re.compile(r'.*a.*n.*t.*o.*n.*')
l = [input() for _ in range(int(input()))]
print(*[l.index(i) + 1 for i in l if pattern.match(i)])
# ----------------------------------------
import re
ru = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
l = list(f'{input()} запретил букву')
for i in ru:
    if i in l:
        print(re.sub(' +', ' ', ''.join(l).strip()), i)
        while i in l:
            l.remove(i)
# ======================================== 3.1
def func(num1, num2):
    if num1 % num2 == 0:
        return True
    return False

num1, num2 = int(input()), int(input())

if func(num1, num2):
    print('делится')
else:
    print('не делится')
# ======================================== 4.2
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
# ----------------------------------------
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].extend(sub_list)
print(list1)
# ----------------------------------------
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1
for l in list1:
    maximum = max(maximum, max(l))
print(maximum)
# ----------------------------------------
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
for i in range(len(list1)):
    list1[i].reverse()
print(list1)
# ----------------------------------------
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = [item for sublist in list1 for item in sublist]
print(sum(total) / len(total))

from itertools import chain
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = list(chain.from_iterable(list1))
print(sum(total) / len(total))

import numpy as np 
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
print(np.mean(np.array(sum(list1, []))))
# ======================================== 4.3
n = int(input())
for _ in range(n):
    print(list(range(1, n + 1)))

n = int(input())
result = []
for _ in range(n):
    result.append(list(range(1, n + 1)))
print(*result, sep='\n')
# ----------------------------------------
n = int(input())
for i in range(n):
    print(list(range(1, i + 2)))
# ----------------------------------------
num = int(input())
l = [[1], [1, 1]]
for n in range(2, 51):
    l.append([1] + [l[n - 1][i] + l[n - 1][i + 1] for i in range(n - 1)] + [1])
print(l[num])
# ----------------------------------------
num = int(input())
l = [[1], [1, 1]]
for n in range(2, 51):
    l.append([1] + [l[n - 1][i] + l[n - 1][i + 1] for i in range(n - 1)] + [1])
for i in range(num):
    print(*l[i])
# ----------------------------------------
s = input().split()
l = [[0]]
while s:
    l_new = s.pop(0)
    if l[-1][-1] != l_new:
        l.append([l_new])
    else:
        l[-1].extend([l_new])
l.pop(0)
print(l)

res = []
for el in input().split():
    if res and el in res[-1]:
        res[-1].append(el)
    else:
        res.append([el])
print(res)
# ----------------------------------------
s = input().split()
n = int(input())
l = []
while s:
    l.append(s[:n])
    s = s[n:]
print(l)

text, n = input().split(), int(input())
print([text[i:i+n] for i in range(0, len(text), n)])
# ----------------------------------------
# не мой код
input_data = input().split()
output_data = [[]]
for i in range(len(input_data)):
    for j in range(len(input_data) - i):
        output_data.append(input_data[j: j + i + 1])
print(output_data)
# ======================================== 4.4
n, m = int(input()), int(input())
# l = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        print(input(), end=' ')
    print()
# ----------------------------------------
n, m = int(input()), int(input())
l = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        l[i][j] = input()
# n, m = int(input()), int(input())
# matrix = []
# for _ in range(n):
#     row = [input() for j in range(m)]
#     matrix.append(row)
for i in range(n):
    for j in range(m):
        print(l[i][j], end=' ')
    print()
print()
for j in range(m):
    for i in range(n):
        print(l[i][j], end=' ')
    print()

n, m = int(input()), int(input())
arr = [[input() for _ in range(m)] for _ in range(n)]
[print(*row) for row in arr]
print()
[print(*row) for row in zip(*arr)]
# ----------------------------------------
n = int(input())
mx = [[int(i) for i in input().split()] for _ in range(n)]
print(sum([mx[i][i] for i in range(n)]))

print(sum(int(input().split()[i]) for i in range(int(input()))))
# ----------------------------------------
import numpy as np
n = int(input())
mx = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    print(sum([j > sum(mx[i]) / len(mx[i]) for j in mx[i]]))
    # print(sum([j > np.mean(mx[i]) for j in mx[i]]))
# ----------------------------------------
n = int(input())
mx = [[int(i) for i in input().split()] for _ in range(n)]
print(max([mx[i][j] for i in range(n) for j in range(i + 1)]))
# ----------------------------------------
n = int(input())
mx = [[int(i) for i in input().split()] for _ in range(n)]
l = []
for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - j - 1) or (i <= j and i >= n - j - 1):
            l.append(mx[i][j])
print(max(l))

n = int(input())
mx = [[int(i) for i in input().split()] for _ in range(n)]
print(max([mx[i][j] for i in range(n) for j in range(n) if j <= i <= n - j - 1 or n - j - 1 <= i <= j]))
# ----------------------------------------
n = int(input())
mx = [[int(i) for i in input().split()] for _ in range(n)]
print('Верхняя четверть:', sum([mx[i][j] for i in range(n) for j in range(n) if (i < j and i < n - j - 1)]))
print('Правая четверть:', sum([mx[i][j] for i in range(n) for j in range(n) if n - j - 1 < i < j]))
print('Нижняя четверть:', sum([mx[i][j] for i in range(n) for j in range(n) if (i > j and i > n - j - 1)]))
print('Левая четверть:', sum([mx[i][j] for i in range(n) for j in range(n) if j < i < n - j - 1]))
# ======================================== 4.5
n, m = int(input()), int(input())
mx = [[i * j for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        print(str(mx[i][j]).ljust(3), end=' ')
    print()
# ----------------------------------------
n, m = int(input()), int(input())
mx = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0
for i in range(n):
    for j in range(m):
        if mx[i][j] > mx[row][col]:
            row, col = i, j
print(row, col)
# ----------------------------------------
n, m = int(input()), int(input())
mx = [input().split() for _ in range(n)]
# mx = [[int(i) for i in input().split()] for _ in range(n)]
col1, col2 = [int(i) for i in input().split()]
for i in range(n):
    mx[i][col1], mx[i][col2] = mx[i][col2], mx[i][col1]
for i in range(n):
    for j in range(m):
        print(str(mx[i][j]), end=' ')
    print()
# for row in mx:
#     print(*row)
# ----------------------------------------
def is_symmetrical(mx, n):
    for i in range(n):
        for j in range(n):
            if mx[i][j] != mx[j][i]:
                return 'NO'
    return 'YES'

n = int(input())
mx = [input().split() for _ in range(n)]
print(is_symmetrical(mx, n))

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
if all([matrix[i][j] == matrix[j][i] for j in range(n) for i in range(n)]):
    print('YES')
else:
    print('NO')
# ----------------------------------------
n = int(input())
mx = [input().split() for _ in range(n)]
for i in range(n):
    mx[i][i], mx[n - i - 1][i] = mx[n - i - 1][i], mx[i][i]
for row in mx:
    print(*row)
# ----------------------------------------
n = int(input())
mx = [input().split() for _ in range(n)]
for i in range(n):
    print(*mx[n - i - 1])

n = int(input())
mx = [input().split() for _ in range(n)]
mx.reverse()
for row in mx:
    print(*row)
# ----------------------------------------
n = int(input())
mx = [input().split() for _ in range(n)]
mx.reverse()
for i in range(n):
    for j in range(n):
        print(mx[j][i], end=' ')
    print()
# ----------------------------------------
def mark(i, j):
    if i == row and j == col:
        return 'N'
    if 0 <= i <= 7 and 0 <= j <= 7:
        if (row - i) ** 2 + (col - j) ** 2 == 5:
            return '*'
        return '.'

data = input()
row = '87654321'.index(data[1])
col = 'abcdefgh'.index(data[0])
mx = [[mark(i, j) for j in range(8)] for i in range(8)]
for row in mx:
    print(*row)
# ----------------------------------------
def is_magic(mx):
    
    all_d, d1, d2 = [], [], []
    for i in range(n):
        if sum(mx[i]) != sum(mx[0]):
            return 'NO'
        s = []
        for j in range(n):
            s.append(mx[j][i])
            all_d.append(mx[j][i])
        if sum(s) != sum(mx[0]):
            return 'NO'
        d1.append(mx[i][i])
        d2.append(mx[i][n - i - 1])
    if sum(d1) != sum(mx[0]):
            return 'NO'
    if sum(d2) != sum(mx[0]):
            return 'NO'
    all_d.sort()
    for i in range(n ** 2):
        if all_d[i] != i + 1:
            return 'NO'
    return 'YES'

n = int(input())
mx = [[int(i) for i in input().split()] for _ in range(n)]
print(is_magic(mx))

n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]
k = n * (1 + n ** 2) // 2  # магическая константа
print('YES' if all(sum(x) == k for x in (*a, *zip(*a), [a[i][i] for i in range(n)], [a[i][~i] for i in range(n)])) else 'NO')
# ======================================== 4.6
# n, m = [*map(int, input().split())]
n, m = map(int, input().split())
mx = [['.*'[(i + j) % 2] for j in range(m)] for i in range(n)]
for row in mx:
    print(*row)
# ----------------------------------------
n = int(input())
mx = [[0 if i + j < n - 1 else 1 if i + j == n - 1 else 2 for j in range(n)] for i in range(n)]
for row in mx:
    print(*row)
# ----------------------------------------
n, m = map(int, input().split())
mx = [[str(m * i + j + 1).ljust(2) for j in range(m)] for i in range(n)]
for row in mx:
    print(*row)
# ----------------------------------------
n, m = map(int, input().split())
mx = [[str(i + n * j + 1).ljust(2) for j in range(m)] for i in range(n)]
for row in mx:
    print(*row)
# ----------------------------------------
n = int(input())
mx = [['01'[(i + j) == n - 1 or i == j] for j in range(n)] for i in range(n)]
for row in mx:
    print(*row)
# ----------------------------------------
n = int(input())
mx = [['01'[(i <= j  and i <= n - j - 1) or (j <= i and n - j - 1 <= i)] for j in range(n)] for i in range(n)]
for row in mx:
    print(*row)
# ----------------------------------------
n, m = map(int, input().split())
mx = [[str(m * i + j + 1).ljust(2) for j in range(m)] for i in range(n)]
for row in mx:
    print(*row)
# ----------------------------------------
n, m = map(int, input().split())
mx = [[m * i + j + 1 for j in range(m)] for i in range(n)]
for i in range(n):
    print(*sorted(mx[i], reverse = i % 2))   

a, b = map(int, input().split())
for i in range(a):
    print(*sorted(list(range(i*b + 1, i*b + b + 1)), reverse=i%2))
# ----------------------------------------
# не мой код
n, m = map(int, input().split())
mt = [[''] * m for i in '1'* n]
d = 1
for k in range(1, n + m + 1):
    for i in range(n):
        for j in range(m):
            if i + j + 1 == k:
                mt[i][j] = str(d).ljust(3)
                d += 1
[print(*r, sep='') for r in mt]
# ----------------------------------------
# from university
n, m = map(int, input().split())
mx = [[0] * m for _ in range(n)]
i, j = 0, -1
start = 1
while start <= n * m:
    for _ in range(m):
        if j + 1 < m and mx[i][j + 1] == 0:
            mx[i][j + 1] = start
            start += 1
            j += 1
    for _ in range(n):
        if i + 1 < n and mx[i + 1][j] == 0:
            mx[i + 1][j] = start
            start += 1
            i += 1
    for _ in range(m):
        if j > 0 and mx[i][j - 1] == 0:
            mx[i][j - 1] = start
            start += 1
            j -= 1
    for _ in range(n):
        if i > 0 and mx[i - 1][j] == 0:
            mx[i - 1][j] = start
            start += 1
            i -= 1
for row in mx:
    print(*row)
----------
n, m = map(int, input().split())
i = 1; j = 0; c = 0
a = [[0] * (100) for _ in range(100)]

while c < m * n:
    while a[i][j+1] == 0 and j < m: a[i][j+1] = c+1; j += 1; c += 1
    while a[i+1][j] == 0 and i < n: a[i+1][j] = c+1; i += 1; c += 1
    while a[i][j-1] == 0 and j > 1: a[i][j-1] = c+1; j -= 1; c += 1
    while a[i-1][j] == 0 and i > 1: a[i-1][j] = c+1; i -= 1; c += 1

for i in range(1, n+1):
    for j in range(1, m+1):
        print(str(a[i][j]).ljust(3), end=' ')
    print()
# ======================================== 4.7
n, m = map(int, input().split())
mx1 = [[*map(int, input().split())] for _ in range(n)]
input()
mx2 = [[*map(int, input().split())] for _ in range(n)]
for i in range(n):
    for j in range(m):
        mx1[i][j] += mx2[i][j]
for row in mx1:
    print(*row)

n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrixB = [[int(i) for i in input().split()] for _ in range(n)]
matrixC = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrixC[i][j] = matrixA[i][j] + matrixB[i][j]
for row in matrixC:
    print(*row)

n, m = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(n)]
input()
B = [[int(x) for x in input().split()] for _ in range(n)]
C = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]
for row in C:
    print(*row)    

import numpy as np
n, m = map(int, input().split())
a = np.array(list(input().split() for _ in range(n)), int)
input()
b = np.array(list(input().split() for _ in range(n)), int)
c = a + b
for row in c:
    print(*row)
# ----------------------------------------
# не мой код
n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrixB = [[int(i) for i in input().split()] for _ in range(m)]
matrixC = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for q in range(m):
            matrixC[i][j] += matrixA[i][q] * matrixB[q][j]
for row in matrixC:
    print(*row)

import numpy as np
n, m = map(int, input().split())
first = [[int(x) for x in input().split()] for _ in range(n)]
input()
n, m = map(int, input().split())
second = [[int(x) for x in input().split()] for _ in range(n)]
res = np.matmul(first, second)
for row in res:
    print(*row)
# ----------------------------------------
import numpy as np
n = int(input())
mx1 = [[int(x) for x in input().split()] for _ in range(n)]
mx2 = mx1.copy()
power = int(input())
for _ in range(power - 1):
    mx1 = np.matmul(mx1, mx2)
for row in mx1:
    print(*row)
# ======================================== 5 экзамен
s, n = input().split(), int(input())
l = []
for m in range(n):
    l_new = []
    for i in range(m, len(s), n):
        l_new.append(s[i])
    l.append(l_new)
print(l)

s = input().split()
n = int(input())
res = []
for i in range(n):
    res.append(s[i::n])
print(res)

letters, n = input().split(), int(input())
print([letters[i::n] for i in range(n)])
# ----------------------------------------
n = int(input())
mx = [[int(i) for i in input().split()] for _ in range(n)]
print(max([mx[i][j] for i in range(n) for j in range(n) if n - j - 1 <= i <= j or (j <= i and n - j - 1 <= i)]))
# ----------------------------------------
import numpy as np
n = int(input())
mx = np.array([input().split() for _ in range(n)])
# mx = np.array([[int(i) for i in input().split()] for _ in range(n)])
for row in mx.T:
    print(*row)

n = int(input())
matrix = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for row in matrix:
    print(*row)    
# ----------------------------------------
n = int(input())
mx = [['.*'[i == n // 2 or j == n // 2 or i == j or i + j == n - 1] for j in range(n)] for i in range(n)]
for row in mx:
    print(*row)
# ----------------------------------------
def is_symmetrical(mx, n):
    for i in range(n):
        for j in range(n):
            if mx[i][j] != mx[n - j - 1][n - i - 1]:
                return 'NO'
    return 'YES'

n = int(input())
mx = [input().split() for _ in range(n)]
print(is_symmetrical(mx, n))
# ----------------------------------------
def is_latin(mx, n):
    for row in mx:
        if sorted(row) != list(range(1, n + 1)):
            return 'NO'
    for row in mx.T:
        if sorted(row) != list(range(1, n + 1)):
            return 'NO'
    return 'YES'

import numpy as np
n = int(input())
mx = np.array([[int(i) for i in input().split()] for _ in range(n)])
print(is_latin(mx, n))
# ----------------------------------------
def mark(i, j):
    if i == row and j == col:
        return 'Q'
    elif i == row or j == col or abs(row - i) == abs(col - j):
        return '*'
    else:
        return '.'

data = input()
row = '87654321'.index(data[1])
col = 'abcdefgh'.index(data[0])
mx = [[mark(i, j) for j in range(8)] for i in range(8)]
for row in mx:
    print(*row)
# ----------------------------------------
n = int(input())
mx = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(0, i):
        mx[i][j] = i - j
    for j in range(i, n):
        mx[i][j] = j - i
for row in mx:
    print(*row)    

n = int(input())
arr = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in arr:
    print(*row)
# ======================================== 6.2
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
last = countries[-1]
print(last)
# ----------------------------------------
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71) 
print(primes[:6])
# ----------------------------------------
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[2:])
# ----------------------------------------
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[:-3])
# ----------------------------------------
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[3:-2])
# ----------------------------------------
countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
number = len(countries)
print(number)
# ----------------------------------------
numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
print(min(numbers) + max(numbers))
# ----------------------------------------
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
index = countries.index('Slovenia')
print(index)
# ----------------------------------------
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
number = countries.count('Spain')
print(number
# ----------------------------------------
numbers1 = (1, 2, 3)
numbers2 = (6,)
numbers3 = (7, 8, 9, 10, 11, 12, 13)
print(numbers1 * 2 + numbers2 * 9 + numbers3)
# ----------------------------------------
city_name = input()
city_year = int(input())
city = (city_name, city_year)
print(city)
# ----------------------------------------
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if i]
print(non_empty_tuples)
# ----------------------------------------
tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [(lambda x: tuple(list(x)[:-1] + [100]))(i) for i in tuples]
new_tuples = [i[:-1] + (100,) for i in tuples]
print(new_tuples)
# ======================================== 6.3
numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
res = 1
for n in numbers:
    res *= n
print(res)
# ----------------------------------------
data = 'Python для продвинутых!'
print(tuple(data))
# ----------------------------------------
poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
poet_data = list(poet_data)
poet_data[2] = 'Москва'
poet_data = tuple(poet_data)
print(poet_data)

poet_data = ('Пушкин', 1799, 'Санкт-Петербург')[:-1] + ('Москва',)
print(poet_data)
# ----------------------------------------
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
print([sum(n) / len(n) for n in numbers])
# ----------------------------------------
a, b, c = [int(input()) for _ in range(3)]
print((-1 * b / (2 * a), (4 * a * c - b**2) / (4 * a)))
# ----------------------------------------
n = int(input())
t = tuple(input() for _ in range(n))
for row in t:
    print(row)
print()
for row in t:
    if int(row.split()[1]) >= 4:
        print(row)

n = int(input())
pupil = tuple(input().split() for _ in range(n))
[print(*i) for i in pupil]
print()
[print(*i) for i in pupil if int(i[1]) > 3]
# ----------------------------------------
n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end=' ')
    f1, f2, f3 = f2, f3, f1 + f2 + f3
# ======================================== 8.2
n, m, k, x, y, z = [int(input()) for _ in range(6)]
print(n + m - x + k - y + z)
# ----------------------------------------
# не мой код
n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))
i = n + m + k
j = x + y + z
print(3 * (t - i) + 2 * j)
print(2 * i - j - 3 * t)
print(a + i - j - t)
# ======================================== 8.4
numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
print(min(numbers) + max(numbers))
# ----------------------------------------
numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
print(sum(numbers) / len(numbers))
# ----------------------------------------
numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
print(sum(i**2 for i in numbers))
# ----------------------------------------
fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
sortnumbers = sorted(fruits, reverse=True)
print(*sortnumbers, sep='\n')
# ----------------------------------------
print(len(set(input())))
# ----------------------------------------
s = input()
print('YES' if len(set(s)) == len(s) else 'NO')
# ----------------------------------------
s1, s2 = input(), input()
print('YES' if len(set(s1 + s2)) == 10 else 'NO')
# ----------------------------------------
s1, s2 = input(), input()
print('YES' if set(s1) == set(s2) else 'NO')
# ----------------------------------------
s1, s2, s3 = input().split()
print('YES' if set(s1) == set(s2) == set(s3) else 'NO')
# ======================================== 8.5
n = int(input())
print(*[len(set(input().lower())) for _ in range(n)], sep='\n')
# ----------------------------------------
n = int(input())
print(len(set(''.join((input().lower() for _ in range(n))))))
# ----------------------------------------
import re
pattern = re.compile(r'\w+')
print(len(set(re.findall(pattern, input().lower()))))

words = [word.lower().strip('.,;:-?!') for word in input().split()]
print(len(set(words)))
# ----------------------------------------
s = set()
for i in input().split():
    if int(i) in s:
        print('YES')
    else:
        s.add(int(i))
        print('NO')

s = set()
for item in input().split():
    print(["NO", "YES"][item in s])
    s.add(item)
# ======================================== 8.6
s1, s2 = (input() for _ in range(2))
print(len(set(s1.split()) & set(s2.split())))
# ----------------------------------------
s1, s2 = (input() for _ in range(2))
print(*sorted([int(i) for i in set(s1.split()) & set(s2.split())]))
# print(*sorted(set(s1.split()) & set(s2.split()), key=int))
# ----------------------------------------
s1, s2 = (input() for _ in range(2))
print(*sorted(set(s1.split()) - set(s2.split()), key=int))
# ----------------------------------------
n = int(input())
l = [set(input()) for _ in range(n)]
for i in range(1, n):
    l[0] &= l[i]
print(*sorted(l[0], key=int))

n = int(input())
numbers = [input() for _ in range(n)]
num_set = set(numbers[0]).intersection(*numbers)
print(*sorted(num_set))

n = int(input())
myset = set(input())
for i in range(n - 1):
    myset.intersection_update(input())
print(*sorted(myset))
# ======================================== 8.7
n1, n2 = (set(input()) for _ in range(2))
print(['YES', 'NO'][n1.isdisjoint(n2)])
# ----------------------------------------
n1, n2 = (set(input()) for _ in range(2))
print(['NO', 'YES'][n1.issuperset(n2)])

print(['NO', 'YES'][set(input()) >= set(input())])
# ----------------------------------------
a, b, c = (set(int(i) for i in input().split()) for _ in range(3))
a -= c
b -= c
a &= b
print(*sorted(a, reverse=True))

a, b, c = [set(map(int, input().split())) for _ in range(3)]
print(*sorted((a & b) - c, reverse=True))
# ----------------------------------------
a, b, c = [set(map(int, input().split())) for _ in range(3)]
print(*sorted((a | b | c) - (a & b & c)))
# ----------------------------------------
a, b, c = [set(map(int, input().split())) for _ in range(3)]
print(*sorted(c - (a | b), reverse=True))

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())
print(*sorted(set3 - set2 - set1, reverse=True))
# ----------------------------------------
a, b, c = [set(map(int, input().split())) for _ in range(3)]
print(*sorted(set(range(11)) - (a | b | c)))
# print(*sorted(set(range(11)) - a - b - c))
# ======================================== 8.8
items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
myset = {int(i) for i in items}
print(*sorted(myset))
# ----------------------------------------
words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
myset = {i[0].lower() for i in words}
print(*sorted(myset))
# ----------------------------------------
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
myset = {i.lower().strip('.,;:-?!()') for i in sentence.split()}
print(*sorted(myset))
# ----------------------------------------
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
myset = {i.lower().strip('.,;:-?!()') for i in sentence.split()}
myset = {i for i in myset if len(i) < 4}
print(*sorted(myset))

import re
print(*sorted(set(re.findall(r'\b\w{,3}\b', sentence.lower()))))
# ----------------------------------------
files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
myset = {i.lower() for i in files if i.lower().split('.')[1] == 'png'}
print(*sorted(myset))
# ======================================== 9.1 экзамен
set1 = {'p', 'a', 't', 'f'}
set2 = {'a', 't', 'f'}
print(set1 - set2)
# ======================================== 9.2 экзамен
n, m, k, p = (int(input()) for _ in range(4))
print(n - (m - p) - (k - p) - p)
# ----------------------------------------
l = input().split()
print(len(l) - len(set(l)))
# ----------------------------------------
s = set(input() for _ in range(int(input())))
# s = {input() for _ in range(int(input()))}
print(('OK', 'REPEAT')[input() in s])
# ----------------------------------------
m, n = (int(input()) for _ in range(2))
s = {input() for _ in range(m)}
print(*(('NO', 'YES')[input() in s] for _ in range(n)), sep='\n')
# ----------------------------------------
n1, n2 = (set(int(i) for i in input().split()) for _ in range(2))
print('BAD DAY') if n1.intersection(n2) == set() else print(*sorted(n1.intersection(n2), reverse=True))

set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}
if set1.isdisjoint(set2):
    print('BAD DAY')
else:
    print(*sorted(set1 & set2, reverse=True))
# ----------------------------------------
n1, n2 = (set(int(i) for i in input().split()) for _ in range(2))
print(('NO', 'YES')[n1 == n2])

print(('NO', 'YES')[set(input().split()) == set(input().split())])
# ----------------------------------------
m, n = (int(input()) for _ in range(2))
s1 = {input() for _ in range(m)}
s2 = {input() for _ in range(n)}
print(len(s1 - s2))
# ----------------------------------------
m, n = (int(input()) for _ in range(2))
s1 = {input() for _ in range(m)}
s2 = {input() for _ in range(n)}
print(len(s1 ^ s2) if len(s1 ^ s2) else 'NO')
# ----------------------------------------
s1, s2 = (set(input().split()) for _ in range(2))
print(*sorted((s1 | s2)))
# ----------------------------------------
# не мой код
m, n = int(input()), int(input())
set_all = {input() for _ in range(m + n)}
print(['NO', 2 * len(set_all) - (m + n)][2 * len(set_all) != m + n])
# ----------------------------------------
# не мой код
n = int(input())
result = {input() for _ in range(int(input()))}
for _ in range(n - 1):
    result &= {input() for _ in range(int(input()))}
print(*sorted(result), sep='\n')
# ======================================== 10.2
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
print(min(my_dict) + max(my_dict))
# ----------------------------------------
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
print(*sorted([user['name'] for user in users if user['phone'].endswith('8')]))
# ----------------------------------------
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
print(*sorted([user['name'] for user in users if not 'email' in user or not user['email']]))
# ----------------------------------------
digits = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
             '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
print(*[digits[i] for i in input()])
# ----------------------------------------
d = {'CS101': 'CS101: 3004, Хайнс, 8:00',
     'CS102': 'CS102: 4501, Альварадо, 9:00',
     'CS103': 'CS103: 6755, Рич, 10:00',
     'NT110': 'NT110: 1244, Берк, 11:00',
     'CM241': 'CM241: 1411, Ли, 13:00'}
print(d[input()])

courses = {
    "CS101": (3004, 'Хайнс', '8:00'),
    "CS102": (4501, 'Альварадо', '9:00'),
    "CS103": (6755, 'Рич', '10:00'),
    "NT110": (1244, 'Берк', '11:00'),
    "CM241": (1411, 'Ли', '13:00')
}
s = input()
print('{}: {}, {}, {}'.format(s, *courses[s]))

d = {
    "CS101": "3004, Хайнс, 8:00",
    "CS102": "4501, Альварадо, 9:00",
    "CS103": "6755, Рич, 10:00",
    "NT110": "1244, Берк, 11:00",
    "CM241": "1411, Ли, 13:00"
}
s = input()
print(f'{s}: {d[s]}')
# ----------------------------------------
keyboard = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
for letter in input().upper():
    for key, value in keyboard.items():
        if letter in value:
            print(key * (value.index(letter) + 1), end="")

num = {'.,?!:': '1', 'ABC': '2', 'DEF': '3',
       'GHI': '4', 'JKL': '5', 'MNO': '6',
       'PQRS': '7', 'TUV': '8', 'WXYZ': '9',
       ' ': '0'}
for l in input().upper():
    [print(num[i] * (i.index(l) + 1), end='') for i in num if l in i]            
# ----------------------------------------
letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
d = dict(zip(letters, morse))
for c in input().upper():
    if c in d:
    # if c in d.keys():
        print(d[c], end=' ')
# ======================================== 10.3
result = {i: i**2 for i in range(1, 16)}
# ----------------------------------------
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = dict1.copy()
result.update(dict2)
for k, v in dict2.items():
    if k in dict1:
        result[k] += dict1[k]

result = dict1.copy()
for key, value in dict2.items():
    result[key] = result.get(key, 0) + value

result = dict1.copy()
for key in dict2:
    result[key] = result.get(key, 0) + dict2[key]

result = {i: dict1.get(i, 0) + dict2.get(i, 0) for i in set(dict1.keys() | dict2.keys())}
# ----------------------------------------
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for c in text:
    result[c] = result.get(c, 0) + 1
# ----------------------------------------
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
d = {}
for w in s.split():
    d[w] = d.get(w, 0) + 1
d_max = max(v for v in d.values())
print(sorted([key for key, value in d.items() if value == d_max])[0])

print(sorted({s.count(i): i for i in sorted(set(s.split()), reverse=True)}.items())[-1][1])

result = {l: s.split().count(l) for l in set(s.split())}
print(min(l for l in result if result[l]==max(result.values())))
# ----------------------------------------
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]
result = {}
for i in pets:
    result.setdefault(i[1:], []).append(i[0])
# ----------------------------------------
d = {}
for w in input().split():
    w = w.lower().strip('.,;:-?!')
    d[w] = d.get(w, 0) + 1
d_min = min(v for v in d.values())
print(sorted([key for key, value in d.items() if value == d_min])[0])

d = {}
for w in input().split():
    w = w.lower().strip('.,!?:;-')
    d[w] = d.get(w, 0) + 1  
print(min(d.items(), key=lambda x: (x[1], x[0]))[0])

st = [i.strip('.,!?:;-') for i in input().lower().split()]
print(min(st, key=lambda x: (st.count(x), x)))
# lst = [word.strip('.,!?:;-') for word in input().lower().split()]
# ----------------------------------------
# не мой код
lst = input().split()
res = {}
for c in lst:
    if c in res:
        print(f'{c}_{res[c]}', end=' ')
    else:
        print(c, end=' ')
    res[c] = res.get(c, 0) + 1

n = input().split()
d = {}
for i in n:
    d[i] = d.get(i, -1) + 1
    print(i if d[i] == 0 else f"{i}_{d[i]}", end=" ")
# ======================================== 10.4
l = [tuple(input().split(': ')) for _ in range(int(input()))]
d = {i[0].lower(): i[1] for i in l}
print(*[d.get(input().lower(), 'Не найдено') for _ in range(int(input()))], sep='\n')

mydict = {}
for _ in range(int(input())):
    key, value = input().split(': ')
    mydict[key.lower()] = value
for _ in range(int(input())):
    print(mydict.get(input().lower(), 'Не найдено'))
# ----------------------------------------
d1, d2 = {}, {}
for c in input():
    d1[c] = d1.get(c, 0) + 1
for c in input():
    d2[c] = d2.get(c, 0) + 1
print('YES' if d1 == d2 else 'NO')

d = {}
for c in input().lower():
    d[c] = d.get(c, 0) + 1
for c in input().lower():
    d[c] = d.get(c, 0) - 1    
print(('NO', 'YES')[set(d.values()) == {0}])

print('YES' if sorted(input()) == sorted(input()) else 'NO')

# d1 = dict.fromkeys(input())
# d2 = dict.fromkeys(input())
# print('YES' if d1 == d2 else 'NO')
# ----------------------------------------
d1, d2 = {}, {}
for c in input().lower():
    if c.isalpha():
        d1[c] = d1.get(c, 0) + 1
for c in input().lower():
    if c.isalpha():
        d2[c] = d2.get(c, 0) + 1
print('YES' if d1 == d2 else 'NO')

def s(word):
    res = {}
    for i in word.lower():
        if i.isalpha():
            res[i] = res.get(i, 0) + 1
    return res
print(("NO", "YES")[s(input()) == s(input())])

s1 = [i for i in input().lower() if i.isalpha()]
s2 = [i for i in input().lower() if i.isalpha()]
print('YES' if sorted(s1) == sorted(s2) else 'NO')
# ----------------------------------------
d1, d2 = {}, {}
for _ in range(int(input())):
    key, value = input().split()
    d1[key] = value
    d2[value] = key
w = input()
print(d1[w] if w in d1.keys() else d2[w])

words = {}
for _ in range(int(input())):
    a, b = input().split()
    words[a], words[b] = b, a
print(words[input()])
# ----------------------------------------
d = {}
for _ in range(int(input())):
    s = input().split()
    d.update(dict.fromkeys(s[1:], s[0]))
    # country, *cities = input().split()
    # d.update(dict.fromkeys(cities, country))
for _ in range(int(input())):
    print(d[input()])
# ----------------------------------------
d = {}
for _ in range(int(input())):
    phone, name = input().lower().split()
    d.setdefault(name, []).append(phone)
for _ in range(int(input())):
    print(*d.get(input().lower(), ['абонент не найден']))
# ----------------------------------------
d1, d2 = {}, {}
s = input()
for c in s:
    d1[c] = d1.get(c, 0) + 1
for _ in range(int(input())):
    v, k = input().split(': ')
    d2[int(k)] = v
print(*[d2[d1[c]] for c in s], sep='')
# ======================================== 10.5
numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
result = {i: numbers[i]**2 for i in range(len(numbers))}
# ----------------------------------------
colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
result = {k: v for k, v in colors.items() if v is not None}
# ----------------------------------------
favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
result = {k: v for k, v in favorite_numbers.items() if 10 <= v <= 99}
# ----------------------------------------
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
result = {v: k for k, v in months.items()}
# ----------------------------------------
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(w.split(':')[0]): w.split(':')[1] for w in s.split()}

result = {int(k):v for k, v in [l.split(':') for l in s.split()]}
# ----------------------------------------
numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
result = {n: [i for i in range(1, n + 1) if n % i == 0] for n in numbers}
# ----------------------------------------
words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
result = {w: [ord(c) for c in w] for w in words}
# ----------------------------------------
letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
result = {k: v for k, v in letters.items() if k not in remove_keys}
# ----------------------------------------
students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
result = {k: v for k, v in students.items() if v[0] > 167 and v[1] < 75}
# ----------------------------------------
tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
result = {t[0]: t[1:] for t in tuples}
# ----------------------------------------
student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013'] 
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy'] 
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
result = [{i[0]: {i[1]: i[2]}} for i in zip(student_ids, student_names, student_grades)]
# ======================================== 11.1 экзамен
my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
my_dict = {k: [i for i in v if i <= 20 ] for k, v in my_dict.items()}
# ----------------------------------------
emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'], 
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'], 
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'], 
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
print(*sorted([f'{i}@{k}' for k, v in emails.items() for i in v]), sep='\n')
# ======================================== 11.2 экзамен
d = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
print(*[d[c] for c in input()], sep='')
# ----------------------------------------
d = {}
for c in input().split():
    d[c] = d.get(c, 0) + 1
    print(d[c], end=' ')
# ----------------------------------------
d = {
    1: 'AEILNORSTU',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ'
}
print(sum([k for c in input() for k, v in d.items() if c in v]))
# ----------------------------------------
def build_query_string(params):
    return '&'.join([f'{k}={v}' for k, v in sorted(params.items())])
# ----------------------------------------
# не мой код
def merge(values):
    res = {}
    for d in values:
        for k, v in d.items():
            res.setdefault(k, set()).add(v)
    return res
# ----------------------------------------
t = {'write': 'W', 'read': 'R', 'execute': 'X'}
d = {}
for _ in range(int(input())):
    l = input().split()
    d[l[0]] = l[1:]
for _ in range(int(input())):
    l = input().split()
    print('OK' if t[l[0]] in d[l[1]] else 'Access denied')

for _ in range(int(input())):
    name, *oper = input().split()
    d[name] = oper
for _ in range(int(input())):
    oper, name = input().split()
    print('OK' if t[oper] in d[name] else 'Access denied')
# ----------------------------------------
# не мой код
data = {}
for _ in range(int(input())):
    name, product, count = input().split()
    data.setdefault(name, {})
    data[name][product] = data[name].get(product, 0) + int(count)
for person, products in sorted(data.items()):
    print(f'{person}:')
    for product, count in sorted(products.items()):
        print(product, count)
# ======================================== 12.1
import random
for _ in range(int(input())):
    print(random.choice(['Орел', 'Решка'])) 
# ----------------------------------------
import random
for _ in range(int(input())):
    print(random.randint(1, 6))
# ----------------------------------------
import random
for _ in range(int(input())):
    print(chr(random.choice([i for i in range(65, 90 + 1)] + [i for i in range(97, 122 + 1)])), end='')
# ----------------------------------------
import random
print(*sorted(random.sample(range(1, 50), k=7)))
# ======================================== 12.2
import random
def generate_ip():
    return '.'.join([str(random.choice(range(256))) for _ in range(4)])

from random import randrange as r
def generate_ip():
    return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'
# ----------------------------------------
import random
import string
def generate_index():
    return f'{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randrange(100)}_{random.randrange(100)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}'

from random import choice, randrange
from string import ascii_uppercase as letter
def generate_index():
    return f'{choice(letter)}{choice(letter)}{randrange(100)}_{randrange(100)}{choice(letter)}{choice(letter)}'
# ----------------------------------------
import random
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
random.shuffle(matrix)
# ----------------------------------------
import random
import string
for _ in range(100):
    print(random.choice(string.digits[1:]) + ''.join([random.choice(string.digits) for _ in range(6)]))

import random
print(*random.sample(range(int(1e6), int(1e7)), 100), sep='\n')

import random
for i in range(100):
    print(random.randint(1000000, 9999999))
# ----------------------------------------
import random
l = list(input())
random.shuffle(l)
print(*l, sep='')
# ----------------------------------------
import random
l = [i for i in random.sample(range(1, 76), 24)]
for i in range(5):
    for j in range(5):
        print('0'.ljust(3) if i == j == 2 else str(l.pop()).ljust(3), end='')
    print()

import random
nums = iter(random.sample(list(range(1, 75)), 24))
[print(*('0  ' if i == j == 2 else str(next(nums)).ljust(3) for j in range(5))) for i in range(5)]
# ----------------------------------------
# не мой код
from random import shuffle
l = [input() for _ in range(int(input()))]
shuffle(l)
for i in range(len(l)):
    print(f'{l[i - 1]} - {l[i]}')
# ----------------------------------------
import random
def generate_password(length):
    s = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    print(''.join([random.choice(s) for _ in range(length)]))
def generate_passwords(count, length):
    for _ in range(count):
        generate_password(length)
n, m = int(input()), int(input())
generate_passwords(n, m)

import string
s = ''.join((set(string.ascii_letters) | set(string.digits)) - set('lI1oO0'))
# ----------------------------------------
# не мой код
import string
from random import sample, shuffle

set1 = set('23456789')
set2 = set(string.ascii_uppercase) - set('IO')
set3 = set(string.ascii_lowercase) - set('lo')
n, m = int(input()), int(input())
for _ in range(n):
    password = sample(set1, 1) + sample(set2, 1) + sample(set3, 1) + sample(set1|set2|set3, m-3)
    shuffle(password)
    print(''.join(password))
# ======================================== 12.3
import random
n = 10 ** 6
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if -2 - x ** 3 <= y**4 and y**2 <= 2 - 3 * x:
        k += 1
print((k / n) * s0)
# ----------------------------------------
import random
n = 10 ** 6
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y**2 <= 1:
        k += 1
print((k / n) * s0)
# ======================================== 13.1
from decimal import *
s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
numbers = [Decimal(i) for i in s.split()]
maximum = max(numbers)
minimum = min(numbers)
print(maximum + minimum)
# ----------------------------------------
from decimal import *
s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
numbers = [Decimal(i) for i in s.split()]
print(sum(numbers))
print(*[i for i in sorted(numbers, reverse=True)[:5]])
# ----------------------------------------
from decimal import *
num = input()
s = set(num) - set(['.', '-'])
print(int(max(s)) + int(min(s)))

from decimal import *
num = Decimal(input())
cyphers = num.as_tuple().digits
print(max(cyphers) + min(cyphers) * (abs(num) >= 1))

d = [int(i) for i in input() if i.isdigit()]
print(max(d) + min(d))
# ----------------------------------------
from decimal import *
num = Decimal(input())
print(num.exp() + num.ln() + num.log10() + num.sqrt())

from decimal import Decimal as D
d = D(input())
print(sum(func() for func in (d.exp, d.ln, d.log10, d.sqrt)))
# ======================================== 13.2
from fractions import Fraction
numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
numbers = [f'{i} = {Fraction(i)}' for i in numbers]
print(*[i for i in numbers], sep='\n')
# ----------------------------------------
from fractions import Fraction
s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
numbers = [Fraction(i) for i in s.split()]
maximum = max(numbers)
minimum = min(numbers)
print(maximum + minimum)
# ----------------------------------------
from fractions import Fraction
print(Fraction(int(input()), int(input())))
# ----------------------------------------
from fractions import Fraction
num1 = input()
num2 = input()
print(f'{num1} + {num2} = {Fraction(num1) + Fraction(num2)}')
print(f'{num1} - {num2} = {Fraction(num1) - Fraction(num2)}')
print(f'{num1} * {num2} = {Fraction(num1) * Fraction(num2)}')
print(f'{num1} / {num2} = {Fraction(num1) / Fraction(num2)}')
# ----------------------------------------
from fractions import Fraction
print(sum([Fraction(1, i ** 2) for i in range(1, int(input()) + 1)]))
# ----------------------------------------
from fractions import Fraction
from math import factorial
print(sum([Fraction(1, factorial(i)) for i in range(1, int(input()) + 1)]))
# ----------------------------------------
from fractions import Fraction as F
n = int(input())
print(max([F(i, n - i) for i in range(1, n // 2 + 1) if F(i, n - i).numerator + F(i, n - i).denominator == n]))
# ----------------------------------------
from fractions import Fraction as F
n = int(input())
print(*sorted(set([F(j, i) for i in range(1, n + 1) for j in range(1, i)])), sep='\n')
# ======================================== 13.3
z1 = complex(input())
z2 = complex(input())
print(f'{z1} + {z2} = {z1 + z2}')
print(f'{z1} - {z2} = {z1 - z2}')
print(f'{z1} * {z2} = {z1 * z2}')
# ----------------------------------------
numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
res = 0
for num in numbers:
    if abs(num) > abs(res):
        res = num
print(res, abs(res), sep='\n')

numbers = [3+4j, 3+1j, -7+3j, 4+8j, -8+10j, -3+2j, 3-2j, -9+9j, -1-1j, -1-10j, -20+15j, -21+1j, 1j, -3+8j, 4-6j, 8+2j, 2+3j]
print(max(numbers, key=abs))
print(abs(max(numbers, key=abs)))
# ----------------------------------------
n = int(input())
z1 = complex(input())
z2 = complex(input())
print(z1 ** n + z2 ** n + z1.conjugate() ** n + z2.conjugate() ** (n + 1))
# ======================================== 15.1
# wrong
def append(element, seq=[]):
    seq.append(element)
    return seq
# correct
def append(element, seq=None):
    if seq is None:
        seq = []
    seq.append(element)
    return seq
# ----------------------------------------
def matrix(n=1, m=None, value=0):
    if m is None:  # это уже выполняется во время вызова функции
        m = n
    return [[value] * m for _ in range(n)]
    
print(matrix())                   # матрица 1 × 1 из 0
print(matrix(3))                  # матрица 3 × 3 из 0
print(matrix(2, 5))               # матрица 2 × 5 из 0
print(matrix(3, 4, 9))            # матрица 3 × 4 из 9
# ======================================== 15.2
# correct
def my_func(a, b, *args, name='Gvido', age=17, **kwargs):
    print(a, b)
    print(args)
    print(name, age)
    print(kwargs)
# ----------------------------------------
def count_args(*args):
    return len(args)
# ----------------------------------------
def sq_sum(*args):
    return sum(i**2 for i in args)
# ----------------------------------------
def mean(*args):
    l = [i for i in args if type(i) in (int, float)]
    # l = [i for i in args if not isinstance(i, (bool)) and isinstance(i, (int, float))]
    return sum(l) / len(l) if l else 0
# ----------------------------------------
def greet(name, *args):
    return f'''Hello, {name}{' and ' if args else ''}{' and '.join(args)}!'''

def greet(name, *args):
    return f'Hello, {" and ".join((name,) + args)}!'
# ----------------------------------------
def print_products(*args):
    l = [i for i in args if type(i) is str and i]
    print(*[f'{c}) {el}' for c, el in enumerate(l, 1)], sep='\n') if l else print('Нет продуктов')

def print_products(*args):
    lst = [i for i in args if type(i) is str and i]
    [print(f'{n}) {p}') for n, p in enumerate(lst, 1)] or print('Нет продуктов')
# ----------------------------------------
def info_kwargs(**kwargs):
    print(*[f'{k}: {v}' for k, v in sorted(kwargs.items())], sep='\n')

def info_kwargs(**kwargs):
    for k, v in sorted(kwargs.items()):
        print(f'{k}: {v}')
# ======================================== 15.4
import numpy as np 
numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
print(min(numbers, key=np.mean))
print(max(numbers, key=np.mean))
# ----------------------------------------
points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
points.sort(key=lambda x: (x[0]**2 + x[1]**2)**0.5)
print(points)
# ----------------------------------------
numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
numbers.sort(key=lambda x: min(x) + max(x))
print(numbers)
# ----------------------------------------
athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
n = int(input())
athletes.sort(key=lambda x: x[n - 1])
[print(*i) for i in athletes]    

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
n = int(input())
[print(*i) for i in sorted(athletes, key=lambda x: x[n - 1])]
# int(input()) can't be embedded in lambda
# ----------------------------------------
import math
commands = {
    'квадрат': lambda x: math.pow(x, 2),
    'куб': lambda x: math.pow(x, 3),
    'корень': math.sqrt,
    'модуль': abs,
    'синус': math.sin}
n = int(input())
command = input()
print(commands[command](n)) 

import math
def pwr(p):
  def numpower(n):
    return n**p
  return numpower
commands = {
    'квадрат': pwr(2),
    'куб': pwr(3),
    'корень': pwr(0.5),
    'модуль': abs,
    'синус': math.sin}
n = int(input())
command = input()
print(commands[command](n))
# ----------------------------------------
s = input().split()
s.sort(key=lambda x: sum([int(i) for i in x]))
print(*s)

print(*sorted(input().split(), key=lambda x: sum([int(i) for i in x])))
print(*sorted(input().split(), key=lambda x: sum(map(int, x))))
# ----------------------------------------
print(*sorted(sorted(input().split(), key=int), key=lambda x: sum([int(i) for i in x])))
print(*sorted(sorted(input().split(), key=int), key=lambda x: sum(map(int, x))))
# ======================================== 15.5
def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result
def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result
def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc
# ----------------------------------------
numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
print(*map(lambda x: round(x, ndigits=2), numbers), sep='\n')
# ----------------------------------------
numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
print(*map(lambda x: x**3, filter(lambda x: 100 <= x <= 999 and x % 5 == 2, numbers)), sep='\n')
# ----------------------------------------
numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
print(sum(map(lambda x: x ** 2, numbers)))

def add(x, y):
    return x + y**2
print(reduce(add, numbers, 0))

print(reduce(lambda x, y: x + y**2, numbers, 0))
# ----------------------------------------
numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
print(sum(map(lambda x: x ** 2, filter(lambda x: 10 <= abs(x) <= 99 and x % 7 == 0, numbers))))
# ----------------------------------------
def func_apply(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def func_apply(function, items):
    return [function(i) for i in items]
# ======================================== 15.7
from functools import reduce 

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

map_result = list(map(lambda num: round(num**2, 1), floats))
filter_result = list(filter(lambda name: name == name[::-1] and len(name) > 4, words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)
# ----------------------------------------
from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

data = filter(lambda x: x[1] > 10_000_000 and x[2] == 'primary', data)
data = map(lambda x: x[0], data)
data = sorted(data)
data = reduce(lambda x, y: x + ', ' + y, data)
print('Cities:', data)

print('Cities:', reduce(lambda x, y: x + ', ' + y, sorted(map(lambda x: x[0], filter(lambda x: x[1] > 10_000_000 and x[2] == 'primary', data)))))
# ======================================== 15.8
func = lambda x: x % 19 == 0 or x % 13 == 0
# ----------------------------------------
func = lambda x: x[0].lower() == x[-1].lower() == 'a'

func = lambda x: x.lower().startswith('a') and x.lower().endswith('a')
# ----------------------------------------
is_non_negative_num = lambda x: len(x.split('.')) <= 2 and all([i.isdigit() for i in x.split('.')]) and float(x) >= 0

is_non_negative_num = lambda q: q.replace('.', '', 1).isdigit()
# ----------------------------------------
import re
pattern = re.compile(r'^[-]?\d*[.]?\d*$')
# pattern = re.compile(r'^[-]?[0-9]*[.]?[0-9]*$')
is_num = lambda x: True if pattern.match(x) else False

is_non_negative_num = lambda q: q.replace('.', '', 1).isdigit()
is_num = lambda q: is_non_negative_num(q[1:]) if q[0] == '-' else is_non_negative_num(q)
# ----------------------------------------
words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
print(*sorted(filter(lambda x: len(x) == 6, words)), sep=' ')
# ----------------------------------------
numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
print(*map(lambda x: x // 2 if x % 2 == 0 else x, filter(lambda x: not (x % 2 == 1 and x > 47), numbers)), sep=' ')
# ----------------------------------------
data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
print(*[f'{y}: {x}' for x, y in sorted(data, key=lambda x: x[1][-1], reverse=True)], sep='\n')

for pop, city in sorted(data, key=lambda x: x[1][-1], reverse=True):
    print(f'{city}: {pop}')
# ----------------------------------------
data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
print(*sorted(sorted(data), key=len))
# ----------------------------------------
mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
print(max(filter(lambda x: type(x) is int, mixed_list)))

print(max(mixed_list, key=lambda x: 0 if type(x) is str else x))
# ----------------------------------------
mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
print(*sorted(mixed_list, key=lambda x: x if type(x) is str else str(x)), sep=' ')
# ----------------------------------------
print(*map(lambda x: 255 - int(x), input().split()))
# ----------------------------------------
# не мой код
def evaluate(l, x):
    ch = list(map(lambda y, z: y * x**z, l, list(range(len(l)-1, -1, -1))))
    return sum(ch)
a = list(map(int, input().split()))
x = int(input())
print(evaluate(a, x))
# ======================================== 15.9
def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(i in command for i in ignore)

    return any(map(lambda x: x in command, ignore))
# ----------------------------------------
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
print(*[f'{x} is the capital of {y}, population equal {z} people.' for x, y, z in zip(capitals, countries, population)], sep='\n')

for country, capital, people in zip(countries, capitals, population):
    print(f'{capital} is the capital of {country}, population equal {people} people.')
# ----------------------------------------
abscissas = map(float, input().split())
ordinates = map(float, input().split())
applicates = map(float, input().split())
print(all([x ** 2 + y ** 2 + z ** 2 <= 4 for x, y, z in zip(abscissas, ordinates, applicates)]))

abscissas, ordinates, applicates = (map(float, input().split()) for _ in range(3))
print(all([x ** 2 + y ** 2 + z ** 2 <= 4 for x, y, z in zip(abscissas, ordinates, applicates)]))
# ----------------------------------------
print(all([i.isdigit() and int(i) <= 255 for i in input().split('.')]))
# ----------------------------------------
a, b = int(input()), int(input())
print(*[i for i in range(a, b + 1) if all([int(j) != 0 and i % int(j) == 0 for j in str(i)])])
# ----------------------------------------
import string
s = input()
print('YES' if all((any(i in string.digits for i in s),
                    any(i in string.ascii_lowercase for i in s),
                    any(i in string.ascii_uppercase for i in s),
                    len(s) >= 7))
                    else 'NO')

print('YES' if all((any(i.isupper() for i in s), 
                    any(i.islower() for i in s), 
                    any(i.isdigit() for i in s), 
                    len(s) >= 7)) else 'NO')
# ----------------------------------------
n = int(input())
print('YES' if all(any([int(input().split()[1]) == 5 for i in range(int(input()))]) for j in range(n)) else 'NO')

n = int(input())
l = [[int(input().split()[1]) for i in range(int(input()))] for i in range(n)]
print('YES' if all(map(lambda x: 5 in x, l)) else 'NO')
# ======================================== 16.1
def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    return f'''To: {mail}\
        \nПриветствую, {name}!\
        \nВам назначен экзамен, который пройдет {date}, в {time}.\
        \nПо адресу: {place}.\
        \nЭкзамен будет проводить {teacher} в кабинете {number}.\
        \nЖелаем удачи на экзамене!'''
# ----------------------------------------
def pretty_print(data, side='-', delimiter='|'):
    side_size = (3 * len(data) - 1) + len(''.join(map(str, data)))
    print(' ' + side * side_size + ' ')
    print(f'{delimiter} ' + f' {delimiter} '.join(map(str, data)) + f' {delimiter}')
    print(' ' + side * side_size + ' ')
# ======================================== 16.3
def concat(*args, sep=' '):
    return sep.join(map(str, args))
# ----------------------------------------
from functools import reduce
def product_of_odds(data):
    return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)

from functools import reduce
from operator import mul
def product_of_odds(data):
    return reduce(mul, filter(lambda x: x % 2 == 1, data), 1)
# ----------------------------------------
words = 'the world is mine take a look what you have started'.split()
print(*map(lambda x: '"' + x + '"', words))
# ----------------------------------------
numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
print(*filter(lambda x: str(x) != str(x)[::-1], numbers))
# ----------------------------------------
import numpy as np
numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
sorted_numbers = sorted(numbers, key=np.mean, reverse=True)
print(sorted_numbers)
# ----------------------------------------
def call(f, *args):
    return f(*args)

def mul7(x):
    return x * 7
def add2(x, y):
    return x + y
def add3(x, y, z):
    return x + y + z
print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))
70
9
80
False
# ----------------------------------------
def compose(f, g):
    return lambda x: f(g(x))

def add3(x):
    return x + 3
def mul7(x):
    return x * 7
print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))
28
17
3333333
35
# ----------------------------------------
import operator
def arithmetic_operation(operation):
    d = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    return d[operation]

def arithmetic_operation(op):
    return lambda x, y: eval(f'{x}{op}{y}')
# ----------------------------------------
print(*sorted(input().split(), key=lambda x: x.lower()))
# ----------------------------------------
l = []
for _ in range(int(input())):
    s = input()
    gem = sum(ord(i) - ord('A') for i in s.upper())
    l.append((gem, s))
print(*map(lambda x: x[1], sorted(l)), sep='\n')
# ----------------------------------------
print(*sorted([input() for _ in range(int(input()))], key=lambda x: int(x.split('.')[0]) * 256**3 + int(x.split('.')[1]) * 256**2 + int(x.split('.')[2]) * 256 + int(x.split('.')[3])), sep='\n')

print(*sorted([input() for _ in range(int(input()))], key=lambda x: [*map(int, x.split('.'))]), sep='\n')

import ipaddress
l = [input() for _ in range(int(input()))]
print(*sorted(l, key = ipaddress.ip_address), sep='\n')
# ======================================== 17.2
file = open(fr'{input()}', 'r', encoding='utf-8')
for line in file:
    print(line.strip())
file.close()

file = open(input())
print(file.read())
file.close()
# ----------------------------------------
file = open(input(), 'r', encoding='utf-8')
print(file.readlines()[-2])
file.close()()

with open(input()) as f:
    print(f.readlines()[-2])
# ----------------------------------------
import random
with open('lines.txt', 'r', encoding='utf-8') as f:
    print(random.choice(f.readlines()))
# ----------------------------------------
with open('numbers.txt', 'r', encoding='utf-8') as f:
    print(sum(map(int, f.readlines())))
# ----------------------------------------
with open('nums.txt', 'r', encoding='utf-8') as f:
    print(sum(map(int, filter(lambda x: x.strip(), f.readlines()))))

with open('nums.txt', 'r', encoding='utf-8') as f:
    print(sum(map(int, f.read().split())))
# ----------------------------------------
with open('prices.txt', 'r', encoding='utf-8') as f:
    print(sum(int(x[1]) * int(x[2]) for x in [line.split() for line in f]))

with open('prices.txt', 'r', encoding='utf-8') as f:
    print(sum(int(x[1]) * int(x[2]) for x in map(str.split, f)))

with open('prices.txt', 'r', encoding='utf-8') as f:
    print(sum(map(lambda x: int(x[1]) * int(x[2]), map(str.split, f.readlines()))))
# ======================================== 17.3
with open('text.txt', 'r', encoding='utf-8') as f:
    print(f.readline()[::-1])
# ----------------------------------------
with open('data.txt', 'r', encoding='utf-8') as f:
    print(*f.readlines()[::-1], sep='')
# ----------------------------------------
with open('lines.txt', 'r', encoding='utf-8') as f:
    l = f.readlines()
    print(*filter(lambda x: len(x) == max(map(len, l)), l), sep='')
# ----------------------------------------
with open('numbers.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(sum(map(int, line.split())))
# ----------------------------------------
with open('nums.txt', 'r', encoding='utf-8') as f:
    print(sum(map(int, ''.join([i if i.isdigit() else ' ' for i in f.read()]).split())))

with open('nums.txt', 'r', encoding='utf-8') as f:
    line = ''.join(i if i.isdigit() else ' ' for i in f.read())
    print(sum(map(int, line.split())))

import re
print(sum(map(int, re.findall(r'\d+', open('numbers.txt').read()))))
# ----------------------------------------
with open('file.txt', 'r', encoding='utf-8') as f:
    line = f.read()
    print('Input line contains:', f'{sum(map(str.isalpha, line))} letters', f'{len(line.split())} words', str(line.count('\n') + 1) + ' lines', sep='\n')
# ----------------------------------------
import random
with open('first_names.txt', 'r', encoding='utf-8') as fn, open('last_names.txt', 'r', encoding='utf-8') as ln:
    l_fn = list(map(str.strip, fn.readlines()))
    l_ln = list(map(str.strip, ln.readlines()))
    print(*[f'{random.choice(l_fn)} {random.choice(l_ln)}' for _ in range(3)], sep='\n')
# ----------------------------------------
with open('population.txt', 'r', encoding='utf-8') as f:
    print(*[line.split('\t')[0] for line in f if line.split('\t')[0].startswith('G') and int(line.split('\t')[1]) > 500_000], sep='\n')

with open('population.txt') as f:
    for line in f:
        n, p = line.split('\t')
        if n.startswith('G') and int(p) > 500000:
            print(n)
# ----------------------------------------
def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as f:
        l = []
        k = f.readline().strip().split(',')
        for line in f:
            v = line.strip().split(',')
            l.append(dict(zip(k, v)))
    return l

def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as f:
        keys = f.readline().strip().split(',')
        return [dict(zip(keys, line.strip().split(','))) for line in f]
# ======================================== 17.4
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(input())
# ----------------------------------------
import random
with open('random.txt', 'w', encoding='utf-8') as f:
    f.writelines([str(random.randint(111, 777)) + '\n' for _ in range(25)])

from random import randrange
with open('random.txt','w') as out:
    print(*[randrange(111, 778) for _ in range(25)], sep='\n', file=out)
# ----------------------------------------
with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:
    f_out.writelines([f'{str(n)}) {s}' for n, s in enumerate(f_in.readlines(), 1)])

with open('input.txt') as fin, open('output.txt', 'w') as fout:
    [fout.write(f'{i}) {line}') for i, line in enumerate(fin, 1)]

with open('input.txt') as inp, open('output.txt', 'w') as out:
    for i, j in enumerate(inp, start=1):
        print(f'{i}) {j}', end='', file=out)
# ----------------------------------------
with open('class_scores.txt', 'r') as f_in, open('new_scores.txt', 'w') as f_out:
    f_out.writelines([f'{line.split()[0]} {min(int(line.split()[1]) + 5, 100)}\n' for line in f_in.readlines()])

with open('class_scores.txt', 'r') as f_in, open('new_scores.txt', 'w') as f_out:
    [f_out.write(f'{name} {min(int(score) + 5, 100)}\n') for line in f_in for name, score in [line.split()]]

with open('class_scores.txt') as i, open('new_scores.txt', 'w') as o:
    for line in i.readlines():
        n, s = line.split()
        print(f'{n} {min(int(s) + 5, 100)}', file=o)
# ----------------------------------------
# не мой код
with open('goats.txt') as f1, open('answer.txt', 'w') as f2:
    cont = f1.read().split('\n')
    colors, goats = cont[1:cont.index('GOATS')], cont[cont.index('GOATS')+1:]
    print(*sorted(filter(lambda x: goats.count(x) / len(goats) > 0.07, colors)), sep='\n', file=f2)
# ----------------------------------------
# не мой код
with open('output.txt', 'w') as out:
    for i in range(int(input())):
        with open(input()) as f:
            out.write(f.read())
# ----------------------------------------
# не мой код
with open('logfile.txt',encoding='utf-8') as fr, open('output.txt','a',encoding='utf-8') as fw:
    for line in fr:
         name, st, en = line.split(', ')
         if int(en.replace(':','')) - int(st.replace(':','')) >= 100:
            print(name,file = fw)

def get_diff_mins(time2, time1):
    t2 = list(map(int, time2.split(':')))
    t1 = list(map(int, time1.split(':')))
    return (t2[0]*60 + t2[1]) - (t1[0]*60 + t1[1])
with open('logfile.txt', encoding='utf-8') as inputf, open('output.txt', 'w') as outputf:
    for fn in inputf:
        name, time1, time2 = fn.strip().split(', ')
        if get_diff_mins(time2, time1) >= 60:
            print(name, file=outputf)            
# ======================================== 18 экзамен
with open(input(), 'r') as f:
    print(len(f.readlines()))
# ----------------------------------------
with open('ledger.txt', 'r') as f:
    print('$', sum(map(lambda x: int(x[1:]), f.readlines())), sep='')

with open('ledger.txt', 'r') as f:
    print('$', sum(map(lambda x: int(x[1:]), f)), sep='')
# ----------------------------------------
with open('grades.txt', 'r') as f:
    print(sum(map(lambda x: int(x.split()[1]) >= 65 and int(x.split()[2]) >= 65 and int(x.split()[3]) >= 65, f)))

with open('grades.txt', 'r') as f:
    print(sum(map(lambda x: all([int(y) >= 65 for y in x.split()[1:]]), f)))
# ----------------------------------------
with open('words.txt', 'r', encoding='utf-8') as f:
    l = f.read().split()
    print(*filter(lambda x: len(x) == max(map(len, l)), l), sep='\n')
# ----------------------------------------
with open(input(), 'r', encoding='utf-8') as f:
    print(*f.readlines()[-10:], sep='')
# ----------------------------------------
# не мой код
with open('forbidden_words.txt') as f:
    forbidden_words = {word: '*' * len(word) for word in f.read().split()}
with open(input()) as f:
    s = f.read()
    s_lower = s.lower()
for forbidden_word in forbidden_words:
    s_lower = s_lower.replace(forbidden_word, forbidden_words[forbidden_word])
print(*map((lambda c1, c2: '*' if c2 == '*' else c1), s, s_lower), sep='')
# ----------------------------------------
# не мой код
with open('transliteration.txt', 'w') as out, open('cyrillic.txt') as inp:
    d = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }
    for s in inp.read():
        res = d.get(s.lower(), s)
        out.write(res if s.islower() else res.capitalize())
# ----------------------------------------
# не мой код
with open(input(), encoding='utf-8') as inf:
    not_commented_funcs, preline = [], ''
    for line in inf:
        if not preline.startswith('#') and line.startswith('def '):
            not_commented_funcs.append(line[4:line.find('(')])
        preline = line
    print('\n'.join(not_commented_funcs) if not_commented_funcs else 'Best Programming Team')
# ========================================
