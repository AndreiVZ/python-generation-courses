# ======================================== 2.2
print('Здравствуй, мир!')
# ----------------------------------------
print(4, 8, 15, 16, 23, 42)
# ----------------------------------------
print(4, 8, 15, 16, 23, 42, sep='\n')
# ----------------------------------------
print('*', '**', '***', '****', '*****', '******', '*******', sep='\n')
# ----------------------------------------
name = input()
print('Привет,', name)
# ----------------------------------------
name = input()
print(name, '- чемпион!')
# ----------------------------------------
str1 = input()
str2 = input()
str3 = input()
print(str1)
print(str2)
print(str3)
# ----------------------------------------
str1 = input()
str2 = input()
str3 = input()
print(str3)
print(str2)
print(str1)

print (*[input() for i in range(3)][::-1], sep='\n')
# ======================================== 2.3
print('I', 'like', 'Python', sep='***')
# ----------------------------------------
sep, a, b, c = input(), input(), input(), input()
print(a, b, c, sep=sep)
# ----------------------------------------
str = input()
print('Привет, ', str, '!', sep='')
# ======================================== 2.4
res = int(input())
print(res)
print(res + 1)
print(res + 2)
# ----------------------------------------
res1, res2, res3 = int(input()), int(input()), int(input())
print(res1 + res2 + res3)
# ----------------------------------------
res = int(input())
print('Объем =', res**3)
print('Площадь полной поверхности =', 6 * res**2)
# ----------------------------------------
a, b = int(input()), int(input())
print(3 * (a + b)**3 + 275 * b**2 - 127 * a - 41)
# ----------------------------------------
res = int(input())
print('Следующее за числом', res, 'число:', res + 1)
print('Для числа', res, 'предыдущее число:', res - 1)
# ----------------------------------------
res1, res2, res3, res4 = int(input()), int(input()), int(input()), int(input())
print(3 * (res1 + res2 + res3 + res4))
# ----------------------------------------
res1, res2 = int(input()), int(input())
print(f'{res1} + {res2} = {res1 + res2}')
print(f'{res1} - {res2} = {res1 - res2}')
print(f'{res1} * {res2} = {res1 * res2}')
# ----------------------------------------
a1, d, n = int(input()), int(input()), int(input())
print(a1 + d * (n - 1))
# ----------------------------------------
a = int(input())
print(a, 2*a, 3*a, 4*a, 5*a, sep='---')
# ======================================== 2.5
b1, q, n = int(input()), int(input()), int(input())
print(b1 * q**(n - 1))
# ----------------------------------------
cm = int(input())
print(cm // 100)
# ----------------------------------------
n, k = int(input()), int(input())
print(k // n)
print(k % n)
# ----------------------------------------
n = int(input())
print(n // 2 if n % 2 == 0 else n // 2 + 1)
# ----------------------------------------
n = int(input())
print(n // 4 + 1 if n % 4 != 0 else n // 4)
# ----------------------------------------
n = int(input())
print(f'{n} мин - это {n // 60} час {n % 60} минут.')
# ----------------------------------------
num = int(input())
a = num // 100
b = (num % 100) // 10
c = num % 10
print(f'Сумма цифр = {a + b + c}')
print(f'Произведение цифр = {a * b * c}')
# ----------------------------------------
num = int(input())
a = num // 100
b = (num % 100) // 10
c = num % 10
print(f'{a}{b}{c}')
print(f'{a}{c}{b}')
print(f'{b}{a}{c}')
print(f'{b}{c}{a}')
print(f'{c}{a}{b}')
print(f'{c}{b}{a}')
# ----------------------------------------
num = int(input())
a = num // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10
print(f'Цифра в позиции тысяч равна {a}')
print(f'Цифра в позиции сотен равна {b}')
print(f'Цифра в позиции десятков равна {c}')
print(f'Цифра в позиции единиц равна {d}')
# ======================================== 3 экзамен
print('*' * 17)
print('*', ' ' * 15, '*', sep='')
print('*', ' ' * 15, '*', sep='')
print('*' * 17)
# ----------------------------------------
a, b = int(input()), int(input())
print(f'Квадрат суммы {a} и {b} равен {(a + b)**2}')
print(f'Сумма квадратов {a} и {b} равна {a**2 + b**2}')
# ----------------------------------------
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(a**b + c**d)
# ----------------------------------------
a = int(input())
print(a*100 + 2*a*10 + 3*a)
# ======================================== 4.1
pass1, pass2 = input(), input()
if pass1 == pass2:
    print('Пароль принят')
else:
    print('Пароль не принят')
# ----------------------------------------
i = int(input())
if i % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
# ----------------------------------------
num = int(input())
a = num // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10
if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')
# ----------------------------------------
num = int(input())
if num >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')
# ----------------------------------------
a, b, c = int(input()), int(input()), int(input())
if b - a == c - b:
    print('YES')
else:
    print('NO')
# ----------------------------------------
a, b = int(input()), int(input())
if a < b:
    print(a)
else:
    print(b)
# ----------------------------------------
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min(a, b, c, d))
# ----------------------------------------
a = int(input())
if a <= 13:
    print('детство')
elif a <= 24:
    print('молодость')
elif a <= 59:
    print('зрелость')
else:
    print('старость')
# ----------------------------------------
a, b, c = int(input()), int(input()), int(input())
sum = 0
if a > 0: sum += a
if b > 0: sum += b
if c > 0: sum += c
print(sum)
# ======================================== 4.2
a = int(input())
if -1 < a < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')
# ----------------------------------------
a = int(input())
if a <= -3 or a >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')
# ----------------------------------------
a = int(input())
if (-30 < a <= -2) or (7 < a <= 25):
    print('Принадлежит')
else:
    print('Не принадлежит')
# ----------------------------------------
a = int(input())
if 1000 <= a <= 9999 and (a % 7 == 0 or a % 17 == 0):
    print('YES')
else:
    print('NO')
# ----------------------------------------
a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')
# ----------------------------------------
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print('YES')
else:
    print('NO')
# ----------------------------------------
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == c or b == d:
    print('YES')
else:
    print('NO')
# ----------------------------------------
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if abs(a - c) <= 1 and abs(b - d) <= 1:
    print('YES')
else:
    print('NO')
# ======================================== 4.3
a, b = int(input()), int(input())
if a > b:
    print('NO')
elif a < b:
    print('YES')
else:  
    print("Don't know")
# ----------------------------------------
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a != b and b != c and a != c:
    print('Разносторонний')
else:  
    print('Равнобедренный')
# ----------------------------------------
a, b, c = int(input()), int(input()), int(input())
if (a < b < c) or (a > b > c):
    print(b)
elif (a < c < b) or (a > c > b):
    print(c)
else:  
    print(a)
# ----------------------------------------
a = int(input())
if a in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif a == 2:
    print(28)
else:  
    print(30)
# ----------------------------------------
a = int(input())
if a < 60:
    print('Легкий вес')
elif a < 64:
    print('Первый полусредний вес')
elif a < 69: 
    print('Полусредний вес')
# ----------------------------------------
a, b, c = int(input()), int(input()), input()
if c in '+-*':
    print(eval(f'{a}{c}{b}'))
elif c == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(eval(f'{a}{c}{b}'))
else:  
    print('Неверная операция')
# ----------------------------------------
a, b = input(), input()
if a not in ('красный', 'синий', 'желтый') or b not in ('красный', 'синий', 'желтый'):
    print('ошибка цвета')
elif a == b:
    print(a)
elif a in ('красный', 'синий') and b in ('красный', 'синий'):
        print('фиолетовый')
elif a in ('красный', 'желтый') and b in ('красный', 'желтый'):
        print('оранжевый')
elif a in ('синий', 'желтый') and b in ('синий', 'желтый'):
        print('зеленый')
# ----------------------------------------
a = int(input())
if not (0 <= a <= 36):
    print('ошибка ввода')
elif a == 0:
    print('зеленый')
elif a <= 10:
    print('черный') if a % 2 == 0 else print('красный')
elif a <= 18:
    print('красный') if a % 2 == 0 else print('черный')
elif a <= 28:
    print('черный') if a % 2 == 0 else print('красный')
elif a <= 36:
    print('красный') if a % 2 == 0 else print('черный')
# ----------------------------------------
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if b < c or d < a:
    print('пустое множество')
elif b == c:
    print(b)
elif d == a:
    print(d)
else:
    print(max(a, c), min(b, d))
# ======================================== 5 экзамен
a = int(input())
if a % 100 == 0:
    print('YES')
else:
    print('NO')
# ----------------------------------------
a, b, c, d = int(input()), int(input()), int(input()), int(input())
color1 = color2 = 0
if (a % 2 == 1 and b % 2 == 1) or (a % 2 == 0 and b % 2 == 0):
    color1 = 1
if (c % 2 == 1 and d % 2 == 1) or (c % 2 == 0 and d % 2 == 0):
    color2 = 1
if color1 == color2:
    print('YES')
else:
    print('NO')
# ----------------------------------------
a = int(input())
if not (0 <= a <= 10):
    print('ошибка')
elif a % 10 == 0:
    print('X')
elif a % 9 == 0:
    print('IX')
elif a // 5 == 1:
    print('V', 'I' * (a % 5), sep='')
elif a % 4 == 0:
    print('IV')
else:
    print('I' * (a % 5), sep='')
# ----------------------------------------
a = int(input())
if a % 2 == 1:
    print('YES')
elif 2 <= a <= 5:
    print('NO')
elif 6 <= a <= 20:
    print('YES')
elif 20 < a:
    print('NO')
# ----------------------------------------
a, b, c, d = (int(input()) for _ in range(4))
if abs(a - c) == abs(b - d):
    print('YES')
else:
    print('NO')
# ----------------------------------------
a, b, c, d = (int(input()) for _ in range(4))
if (abs(a - c) == 1 and abs(b - d) == 2) or (abs(a - c) == 2 and abs(b - d) == 1):
    print('YES')
else:
    print('NO')
# ----------------------------------------
a, b, c, d = (int(input()) for _ in range(4))
if abs(a - c) == abs(b - d) or a == c or b == d:
    print('YES')
else:
    print('NO')
# ======================================== 6.1
a, b = (float(input()) for _ in range(2))
print(0.5 * a * b)
# ----------------------------------------
a, b, c = (float(input()) for _ in range(3))
print(a / (b + c))
# ----------------------------------------
a = float(input())
if a == 0:
    print('Обратного числа не существует')
else:
    print(1 / a)
# ----------------------------------------
a = float(input())
print(5 / 9 * (a - 32))
# ----------------------------------------
a = float(input())
if a <= 2:
    print(10.5 * a)
else:
    print(21 + 4 * (a - 2))
# ----------------------------------------
a = float(input())
print(int(a * 10) % 10)
# ----------------------------------------
a = float(input())
print(a - int(a))
# ----------------------------------------
a = tuple(int(input()) for _ in range(5))
print('Наименьшее число =', min(a))
print('Наибольшее число =', max(a))
# ----------------------------------------
a, b, c  = (int(input()) for _ in range(3))
print(max(a, b, c))
print(a + b + c - max(a, b, c) - min(a, b, c))
print(min(a, b, c))
# ----------------------------------------
num  = input()
num_list = [int(x) for x in list(num)]
if max(num_list) - min(num_list) == sum(num_list) - max(num_list) - min(num_list):
    print('Число интересное')
else:
    print('Число неинтересное')
# ----------------------------------------
a = tuple(abs(float(input())) for _ in range(5))
print(sum(a))
# ----------------------------------------
a, b, c, d = (int(input()) for _ in range(4))
print(abs(a - c) + abs(b - d))
# ======================================== 6.2
print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')
# ----------------------------------------
a, b = ((input()) for _ in range(2))
print(f'Hello {a} {b}! You just delved into Python')
# ----------------------------------------
a = input()
print(f'Футбольная команда {a} имеет длину {len(a)} символов')
# ----------------------------------------
a = ((input()) for _ in range(3))
d = {len(x): x for x in a}
print(d[min(d)], d[max(d)], sep='\n')

a = ((input()) for _ in range(3))
print(min(a, key=len))
print(max(a, key=len))
# ----------------------------------------
a = tuple(len(input()) for _ in range(3))
if (max(a) - min(a)) / 2 == max(a) - (sum(a) - max(a) - min(a)):
    print('YES')
else:
    print('NO')
# ----------------------------------------
a = input()
if 'синий' in a:
    print('YES')
else:
    print('NO')
# ----------------------------------------
a = input()
if 'суббота' in a or 'воскресенье' in a:
    print('YES')
else:
    print('NO')
# ----------------------------------------
a = input()
if '@' in a and '.' in a:
    print('YES')
else:
    print('NO')
# ======================================== 6.3
import math
a, b, c, d  = (float(input()) for _ in range(4))
print(math.sqrt((a - c)**2 + (b - d)**2))
# ----------------------------------------
import math
a = float(input())
print(math.pi * a**2, 2 * math.pi * a, sep='\n')
# ----------------------------------------
import math
a, b  = (float(input()) for _ in range(2))
print((a + b) / 2, math.sqrt(a * b), 2 * a * b / (a + b), math.sqrt((a**2 + b**2) / 2), sep='\n')
# ----------------------------------------
import math
a  = float(input())
print(math.sin(math.radians(a)) + math.cos(math.radians(a)) + math.tan(math.radians(a))**2)
# ----------------------------------------
import math
a  = float(input())
print(math.ceil(a) + math.floor(a))
# ----------------------------------------
import math
a, b, c  = (float(input()) for _ in range(3))
d = b**2 - 4 * a * c
if d < 0:
    print('Нет корней')
elif d == 0:
    print(-1 * b / (2 * a))
else:
    roots = (-1 * b - math.sqrt(d)) / (2 * a), (-1 * b + math.sqrt(d)) / (2 * a)
    print(min(roots), max(roots), sep='\n')
# ----------------------------------------
import math
n, a  = (float(input()) for _ in range(2))
print(n * a**2 / (4 * math.tan(math.pi / n)))
# ======================================== 7.1
for _ in range(10):
    print('Python is awesome!')
# ----------------------------------------
a, b  = (input() for _ in range(2))
for _ in range(int(b)):
    print(a)
# ----------------------------------------
for _ in range(6):
    print('AAA')
for _ in range(5):
    print('BBBB')
print('E')    
for _ in range(9):
    print('TTTTT')
print('G')
# ----------------------------------------
a = int(input())
for _ in range(a):
    print('*' * 19)
# ----------------------------------------
a = input()
for i in range(10):
    print(i, a)
# ----------------------------------------
a = int(input())
for i in range(a + 1):
    print(f'Квадрат числа {i} равен {i**2}')
# ----------------------------------------
a = int(input())
for i in range(a + 1):
    print('*' * (a - i))
# ----------------------------------------
m, p, n  = (float(input()) for _ in range(3))
for i in range(int(n)):
    print(i + 1, m * (1 + p / 100)**(i))
# ======================================== 7.2
m, n  = (int(input()) for _ in range(2))
for i in range(m, n + 1):
    print(i)
# ----------------------------------------
m, n  = (int(input()) for _ in range(2))
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)
# ----------------------------------------
m, n  = (int(input()) for _ in range(2))
for i in range(m, n + 1):
        if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
            print(i)
# ----------------------------------------
n  = int(input())
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
# ======================================== 7.3
a, b  = (int(input()) for _ in range(2))
count = 0
for i in range(a, b + 1):
    if i**3 % 10 in (4, 9):
        count += 1
print(count)        
# ----------------------------------------
a = int(input())
b = (int(input()) for _ in range(a))
print(sum(b)) 
# ----------------------------------------
import math
n = int(input())
for i in range(n + 1):
    b = (1 / i for i in range(1, n + 1))
print(sum(b) - math.log(n))
# ----------------------------------------
n = int(input())
sum = 0
for i in range(1, n + 1):
    if i**2 % 10 in (2, 5, 8):
        sum += i
print(sum)  
# ----------------------------------------
n = int(input())
f = 1
for i in range(1, n + 1):
    f *= i
print(f) 
# ----------------------------------------
t = (int(input()) for _ in range(10))
l = [i for i in t if i != 0]
p = 1
for i in l:
    p *= i
print(p)

n = 1
for _ in range(10):
    k = int(input())
    n *= k if k else 1
print(n)

multi = 1
for i in [int(input()) for j in range(10)]:
    multi *= i if i else 1
print(multi)

print(__import__("numpy").prod([i for i in [int(input()) for __ in range(10)] if i > 0]))
# ----------------------------------------
n, s = int(input()), 0
for i in range(1, n + 1):
    if n % i == 0:
        s += i
print(s)
# ----------------------------------------
n, s = int(input()), 0
for i in range(1, n + 1):
    s += (-1)**(i + 1) * i
print(s)
# ----------------------------------------
n = int(input())
s = set(int(input()) for _ in range(n))
print(max(s))
print(max(s - {max(s)}))
# ----------------------------------------
s = [int(input()) for _ in range(10)]
if len([i for i in s if i % 2 == 1]) > 0:
    print('NO')
else:
    print('YES')

f = 'YES'
for _ in range(10):
    if int(input())%2:
        f = 'NO'
print(f)
# ----------------------------------------
n = int(input())
f = [1, 1]
for i in range(2, 100):
    f.append(f[i - 2] + f[i - 1])
print(*f[:n])

n = int(input())
a, b = 1, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
# ======================================== 7.4
text = input()
while text != 'КОНЕЦ':
    print(text)
    text = input()
# ----------------------------------------
text = input()
while text != 'КОНЕЦ' and text != 'конец':
    print(text)
    text = input()
# ----------------------------------------
text, count = input(), 0
while text not in ('стоп', 'хватит', 'достаточно'):
    count += 1
    text = input()
print(count)

a = 0
while input() not in ("стоп", "хватит", "достаточно"):
    a += 1
print(a)
# ----------------------------------------
text = int(input())
while text % 7 == 0:
    print(text)
    text = int(input())
# ----------------------------------------
text, s = int(input()), 0
while text >= 0:
    s += text
    text = int(input())
print(s)
# ----------------------------------------
text, s = int(input()), 0
while 1 <= text <= 5:
    if text == 5:
        s += 1
    # s += text == 5
    text = int(input())
print(s)
# ----------------------------------------
money, s = int(input()), 0
while money > 0:
    s += money // 25
    money %= 25
    s += money // 10
    money %= 10
    s += money // 5
    money %= 5
    s += money // 1
    money %= 1
print(s)

n = int(input())
k = 0
for i in (25, 10, 5, 1):
    while n // i > 0:
        k += 1
        n -= i
print(k)
# ======================================== 7.5
num = int(input())
while num != 0:
    print(num % 10)
    num = num // 10
# ----------------------------------------
num = int(input())
rev = ''
while num != 0:
    rev += str(num % 10)
    num = num // 10
print(rev)
# ----------------------------------------
num = list(input())
print('Максимальная цифра равна', max(num))
print('Минимальная цифра равна', min(num))

x = str(input())
print('Максимальная цифра равна', max(x))
print('Минимальная цифра равна', min(x))
# ----------------------------------------
import numpy as np
num = [int(i) for i in input()]
# num = list(map(lambda x: int(x), list(input())))
print(sum(num), len(num), np.prod(num), np.mean(nums), num[0], num[0] + num[-1], sep='\n')
# ----------------------------------------
num = [int(i) for i in input()]
print(num[1])

print(input()[1])
# ----------------------------------------
print('YES' if len(set(input())) == 1 else 'NO')

x = input()
print('YES' if max(x) == min(x) else 'NO')
# ----------------------------------------
num = list(input())
print('YES' if num == sorted(num, reverse=True) else 'NO')
# ======================================== 7.6
n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break
# ----------------------------------------
n = int(input())
for i in range(1, n + 1):
    if i in range(5, 10) or i in range(17, 38) or i in range(78, 88):
        continue
    print(i)
# ======================================== 7.7
# 4 errors
count = 0
p = 0
for i in range(1, 10):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)
    print(p)
else:
    print('NO')

# 0 errors
count = 0
p = 1
for i in range(10):
    x = int(input())
    if x >= 0:
        p *= x
        count += 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')
# ----------------------------------------
# 5 errors
mx = 0
s = 0
for i in range(11):
    x = int(input())
    if x < 0:
        s = x
    if x > mx:
        mx = x
print(s)
print(mx)

# 0 errors
mx = -10**6
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        mx = max(mx, x)
if s == 0:
    print('NO')
else:
    print(s)
    print(mx)
# ----------------------------------------
# 4 errors
s = 1
for i in range(1, 7):
    n = input()
    if i % 2 == 0:
        s = s + n
print(s)

# 0 errors
s = 0
for i in range(7):
    n = int(input())
    if n % 2 == 0:
        s += n
print(s)
# ----------------------------------------
# 5 errors
n = int(input())
max_digit = n % 10
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit < max_digit:
            digit = max_digit
    n = n % 10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)

# 0 errors
n = [int(i) for i in input() if int(i) % 3 == 0]
print(max(n) if len(n) > 0 else 'NO')
# ----------------------------------------
# 2 errors
n = int(input())
while n > 0:
    n %= 10
print(n)

# 0 errors
n = int(input())
while n >= 10:
    n //= 10
print(n)

print(input()[0])
# ----------------------------------------
# 3 errors
n = input()
product = n % 10
while n >= 10:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)

# 0 errors
n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
# ======================================== 7.8
n = int(input())
for i in range(n):
    print(f'{n} ' * 3)
# ----------------------------------------
n = int(input())
for i in range(1, n + 1):
    print(f'{i} ' * 5)

[print(f'{i} ' * 5) for i in range(1, int(input()) + 1)]
# ----------------------------------------
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        print(f'{i} + {j} = {i + j}')
    print()
# ----------------------------------------
n = int(input())
for i in range(1, n + 1):
    print('*' * i) if i <= n // 2 + 1 else print('*' * (n - i + 1))

n = int(input())
for i in range(1, n + 1):
    print('*' * min(i, n - i + 1))
# ----------------------------------------
n = int(input())
for i in range(1, n + 1):
    print(f'{i}' * i)
# ----------------------------------------
total = 0
for x in range(1, 45):
    for y in range(1, 45):
        for z in range(1, 45):
            if x ** 2 + y ** 2 + z ** 2 == 2020:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
print('Общее количество натуральных решений =', total)
# ----------------------------------------
27 + 84 + 110 + 133 + 144 = 498
# ======================================== 7.9
n = int(input())
p = 1
for i in range(n):
    for j in range(i + 1):
        print(p, end=' ')
        p += 1
    print()
# ----------------------------------------
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(j + 1, end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()

n = int(input())
for i in range(1, n + 1):
    for j in range(1, 2 * i):
        print(min(j, 2 * i - j), end='')
    print()

for i in range(1, int(input())+1):
       print(*list(range(1, i + 1)) + list(range(i - 1, 0, -1)), sep = '')
# ----------------------------------------
a, b = (int(input()) for _ in range(2))
sum_ = 0
max_sum = 0
max_digit = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            sum_ += j
    if max_sum <= sum_:
        max_sum = sum_
        max_digit = i
    sum_ = 0
print(max_digit, max_sum)
# ----------------------------------------
a = int(input())
for i in range(1, a + 1):
    sum_ = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sum_ += 1
    print(i, '+' * sum_, sep='')
# ----------------------------------------
n = [int(i) for i in input()]
n_sum = sum(n)
while n_sum > 10:
    n = [int(i) for i in str(n_sum)]
    n_sum = sum(n)
print(n_sum)

n = int(input())
while n // 10 > 0:
    n = n // 10 + n % 10
print(n)

print(int(input()) % 9 or 9)
# ----------------------------------------
import math
sum_ = 0
for i in range(1, int(input()) + 1):
    sum_ += math.factorial(i)
print(sum_)

from math import factorial as f
print(sum([f(i) for i in range(1, int(input())+1)]))
# ----------------------------------------
a, b = (int(input()) for _ in range(2))
for i in range(max(a, 2), b + 1):
    sum_ = 0
    for j in range(2, i + 1):
        if i % j == 0:
            sum_ += 1
    if sum_ == 1:
        print(i)

from sympy import isprime
num_1, num_2 = int(input()), int(input())
for i in range(num_1, num_2 + 1):
    if isprime(i):
        print(i)
# ======================================== 8.2
n = input()
s = 0
while n > 10:
    if n % 2 == 1:
        s = n % 10
    n //= 10
print(s)

# 0 errors
n = int(input())
s = 0
while n > 0:
    d = n % 10
    if d % 2 == 0:
        s += d
    n //= 10
print(s)
# ----------------------------------------
n = 7
count = 0
maximum = 1000
for i in range(1, n + 1):
    x = int(input())
    if x // 4 == 0:
        count += 1
        if x < maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# 0 errors
n = 8
count = 0
maximum = -10**12
for i in range(n):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
# ----------------------------------------
n = 4
count = 0
maximum = 999
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = i
            break
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# 0 errors
n = 4
count = 0
maximum = -10**8
for i in range(n):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
# ----------------------------------------
a = int(input())
print('*' * 19)
for _ in range(a - 2):
    print('*', ' ' * 17, '*', sep='')
print('*' * 19) 
# ----------------------------------------
print(input()[2])
# ----------------------------------------
import numpy as np
n = [int(i) for i in input()]
print(n.count(3))
print(n.count(n[-1]))
print(len([i for i in n if i % 2 == 0]))
print(sum([i for i in n if i > 5]))
print(int(np.prod([i for i in n if i > 7]) or 1))
print(len([i for i in n if i in (0, 5)]))
# ----------------------------------------
1729 4104 13832 20683 32832
# ======================================== 9.1
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])
# ----------------------------------------
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-10])
# ----------------------------------------
s = input()
for i in range(0, len(s), 2):
    print(s[i])

print('\n'.join(input()[::2]))
# ----------------------------------------
s = input()
for i in range(len(s) - 1, -1, -1):
    print(s[i])
# ----------------------------------------
i, f, o = (input() for _ in range(3))
print(f[0], i[0], o[0], sep='')
# ----------------------------------------
print(sum([int(i) for i in input()]))
# ----------------------------------------
for c in input():
    if c.isdigit():
        print('Цифра')
        break
else:
    print('Цифр нет')

print('Цифра' if [i for i in input() if i.isdigit()] else 'Цифр нет')
# ----------------------------------------
s = list(input())
print(f'''Символ + встречается {s.count('+')} раз''')
print(f'''Символ * встречается {s.count('*')} раз''')
# ----------------------------------------
s = input()
coumter = 0
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        coumter += 1
print(coumter)

s = input()
print(sum(1 for i in range(len(s) - 1) if s[i] == s[i + 1]))

s = input()
print(sum(s[i]==s[i-1] for i in range(1, len(s)))) 

import re
print(len(re.findall(r'(.)(?=\1)', input())))
# ----------------------------------------
s = input()
print('Количество гласных букв равно',
    sum(1 for i in range(len(s) - 1) if s[i].lower() in 'ауоыиэяюёе'))
print('Количество согласных букв равно',
    sum(1 for i in range(len(s) - 1) if s[i].lower() in 'бвгджзйклмнпрстфхцчшщ'))

s = input().lower()
print('Количество гласных букв равно', sum(1 for _ in s if _ in 'ауоыиэяюёе'))
print('Количество согласных букв равно', sum(1 for _ in s if _ in 'бвгджзйклмнпрстфхцчшщ'))
# ----------------------------------------
print(str(bin(int(input())))[2:])

print(format(int(input()), 'b'))

n = int(input())
print (f'{n:b}')
# ======================================== 9.2
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])
# ----------------------------------------
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])
# ----------------------------------------
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])
# ----------------------------------------
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])
# ----------------------------------------
import math
s = input()
print('YES' if s[:math.ceil(len(s) / 2):] == s[:-len(s) // 2 - 1: -1] else 'NO')

n = input()
print('YES' if n == n[::-1] else 'NO')
# ----------------------------------------
s = input()
print(len(s))
print(s * 3)
print(s[0])
print(s[:3])
print(s[-3:])
print(s[::-1])
print(s[1:-1])
# ----------------------------------------
s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
# ----------------------------------------
import math
s = input()
print(s[math.ceil(len(s) / 2):] + s[:math.ceil(len(s) / 2)])
# ======================================== 9.3
s = input()
print('YES' if s == s.title() else 'NO')
# ----------------------------------------
print(input().swapcase())
# ----------------------------------------
print('YES' if 'хорош' in input().lower() else 'NO')
# ----------------------------------------
print(sum(1 for c in input() if c.islower()))

print(sum(s.islower() for s in input()))
# ======================================== 9.4
print(input().count(' ') + 1)

print(len(input().split()))
# ----------------------------------------
s = input().lower()
print('Аденин:', s.count('а'))
print('Гуанин:', s.count('г'))
print('Цитозин:', s.count('ц'))
print('Тимин:', s.count('т'))

s = input().upper()
for c in ('Аденин:', 'Гуанин:', 'Цитозин:', 'Тимин:'):
    print(c, s.count(c[0]))
# ----------------------------------------
n = int(input())
print(sum(input().count('11') >= 3 for _ in range(n)))

print(sum(input().count('11') > 2 for _ in range(int(input()))))
# ----------------------------------------
print(sum(c.isdigit() for c in input()))
# ----------------------------------------
s = input()
print('YES' if s.endswith('.com') or s.endswith('.ru') else 'NO')

print('YES' if input().endswith(('.com','.ru')) else 'NO')
# ----------------------------------------
s = input()
max_count = 0
for c in s:
  if s.count(c) >= max_count:
    max_count = s.count(c)
    max_el = c
print(max_el)

a = input()[::-1]
z = max(a, key = a.count)
print(z)

from collections import Counter as c
print(c(input()[::-1]).most_common(1)[0][0])
# ----------------------------------------
s = input()
if s.count('f') == 0:
    print('NO')
elif s.count('f') == 1:
    print(s.find('f'))
else:
    print(s.find('f'), s.rfind('f'))

s = input()
if s.find('f') == -1:
    print('NO')
elif s.find('f') == s.rfind('f'):
    print(s.find('f'))
else:
    print(s.find('f'), s.rfind('f'))

s = input()
print('NO' if s.count('f') == 0 else s.find('f'), s.rfind('f') if s.count('f') > 1 else '')
# ----------------------------------------
s = input()
print(s[:s.find('h')] + s[s.rfind('h') + 1:])
# ======================================== 9.5
s = 'In {0}, someone paid {1} {2} for two pizzas.'
print(s.format(2010, '10k', 'Bitcoin'))
# ----------------------------------------
year = 2010
amount = '10K'
currency = 'Bitcoin'
print(f'In {year}, someone paid {amount} {currency} for two pizzas.')
# ======================================== 9.6
a, b = (int(input()) for _ in range(2))
print(*[chr(i) for i in range(a, b + 1)])

print(*[chr(i) for i in range(int(input()), int(input())+1)])

for i in range(int(input()), int(input()) + 1):
    print(chr(i), end = ' ')
# ----------------------------------------
print(*[ord(i) for i in input()])
# ----------------------------------------
n, s = int(input()), input()
print(*[chr(ord(c) - n) if ord(c) - n >= ord('a') else chr(ord(c) - n + 26) for c in s], sep='')
# ======================================== 10.2
s = 'Python rocks!'
print(len(s))
# ----------------------------------------
s = 'Python rocks!'
print(s[3])
# ----------------------------------------
s = 'Python rocks!'
print(s[1:5])
# ----------------------------------------
s = '    Python rocks!     '
print(s.strip())
# ----------------------------------------
s = 'Python rocks!'
print(s.upper())
# ----------------------------------------
s = 'Python rocks!'
print(s.replace('o', '@'))
# ----------------------------------------
s = input()
print(*[s[i] for i in range(len(s)) if i % 3 != 0], sep='')

# del s[i:j] same as s[i:j] = []
s = list(input())
del s[0::3]  
print(*s, sep='')
# ----------------------------------------
print(input().replace('1', 'one'))
# ----------------------------------------
print(input().replace('@', ''))
# ----------------------------------------
s = input()
if s.count('f') == 0:
    print(-2)
elif s.count('f') == 1:
    print(-1)
else:
    print(s.find('f', s.find('f') + 1))

s = input()
print('-2' if s.count('f') == 0 else s.find('f', s.find('f') + 1))
# ----------------------------------------
s = input()
print(s[:s.find('h')] + s[s.rfind('h'):s.find('h'):-1] + s[s.rfind('h'):])
# ======================================== 11.1
print(list(range(1, int(input()) + 1)))
# ----------------------------------------
import string
print(list(string.ascii_lowercase[:int(input())]))

print(list(__import__('string').ascii_lowercase[:int(input())]))
# ======================================== 11.2
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[16])
# ----------------------------------------
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[-1])
# ----------------------------------------
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[:6])
# ----------------------------------------
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
print(min(numbers) + max(numbers))
# ----------------------------------------
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)
print(average)
# ----------------------------------------
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3] = 'Зеленый'
rainbow[6] = 'Фиолетовый'
print(rainbow)
# ----------------------------------------
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])
# ----------------------------------------
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]
print(numbers1 * 2 + numbers2 * 9 + numbers3)
# ======================================== 11.3
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
print('YES' if 5 in numbers and 17 in numbers else 'NO')
# 'YES' if {5, 17} in set(numbers) else 'NO'
# 'YES' if (5 and 17) in numbers else 'NO'
del numbers[0]
del numbers[-1]
print(numbers)
# numbers[1:-1]
# del numbers[::len(numbers) - 1]
# ----------------------------------------
n = int(input())
s = []
for _ in range(n):
    s.append(input())
print(s)

n = int(input())
print([input() for _ in range(n)])
# ----------------------------------------
import string
print([string.ascii_lowercase[i] * (i + 1) for i in range(26)])
# ----------------------------------------
n = int(input())
print([int(input())**3 for _ in range(n)])
# ----------------------------------------
n = int(input())
print([i for i in range(1, n + 1) if n % i == 0])
# ----------------------------------------
n = int(input())
l = [int(input()) for _ in range(n)]
print([sum(l[i:i + 2]) for i in range(n - 1)])
# ----------------------------------------
n = int(input())
print([int(input()) for _ in range(n)][::2])
# ----------------------------------------
n = int(input())
l = [input() for _ in range(n)]
k = int(input())
print(''.join([i[k - 1] for i in l if len(i) >= k]))
# print(*[i[k - 1] for i in l if len(i) >= k], sep='')
# ----------------------------------------
n = int(input())
s = []
for _ in range(n):
    s.extend(input())
print(s)

print(list(''.join([input() for _ in range(int(input()))])))

print([c for _ in range(int(input())) for c in input()])  # !!!
# ----------------------------------------
print([c for c in '123' for _ in '456'])  # ['1', '1', '1', '2', '2', '2', '3', '3', '3']
print([c for _ in '123' for c in '456'])  # ['4', '5', '6', '4', '5', '6', '4', '5', '6']
print([(i, j) for i in '123' for j in '456'])
# [('1', '4'), ('1', '5'), ('1', '6'), ('2', '4'), ('2', '5'), ('2', '6'), ('3', '4'), ('3', '5'), ('3', '6')]
# ======================================== 11.4
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
print(sum([i**2 for i in numbers]))
# ----------------------------------------
n = int(input())
l = [int(input()) for _ in range(n)]
print(*l, sep='\n')
print()
print(*[c**2 + 2*c + 1 for c in l], sep='\n')

numbers = [int(input()) for _ in range(int(input()))]
print(*numbers, '', *[(x + 1) ** 2 for x in numbers], sep='\n')

# n = int(input())
# print(*[(lambda x: x**2 + 2*x + 1)(int(input())) for _ in range(n)], sep='\n')

# n = int(input())
# f = lambda x: x**2 + 2*x + 1
# print(*[f(int(input())) for _ in range(n)], sep='\n')
# ----------------------------------------
numbers = [int(input()) for _ in range(int(input()))]
numbers.remove(min(numbers))
numbers.remove(max(numbers))
print(*numbers, sep='\n')

numbers = [int(input()) for _ in range(int(input()))]
del numbers[numbers.index(min(numbers))]
del numbers[numbers.index(max(numbers))]
print(*numbers, sep='\n')

ls = [int(input()) for _ in range(int(input()))]
[print(i) for i in ls if i not in (max(ls), min(ls))]
# ----------------------------------------
l = [input() for _ in range(int(input()))]
l2 = []
for s in l:
    if s not in l2:
        l2.append(s)
print(*l2, sep='\n')

s = [input() for _ in range(int(input()))]
print(*[s[i] for i in range(len(s)) if s[:i].count(s[i]) == 0], sep="\n")

print(*{input(): 0 for _ in range(int(input()))}, sep='\n')
# ----------------------------------------
l = [input() for _ in range(int(input()))]
search = input().lower()
[print(s) for s in l if search in s.lower()]
# ----------------------------------------
l1 = [input() for _ in range(int(input()))]
l2 = [input() for _ in range(int(input()))]
tf = [s2.lower() in s1.lower() for s1 in l1 for s2 in l2]
final = []
for i in range(len(l1)):
    final.append(sum(tf[i * len(l2):i * len(l2) + len(l2)]) == len(l2))
print(*[l1[i] for i in range(len(l1)) if final[i]], sep='\n')

s = [input() for _ in range(int(input()))]
d = [input() for _ in range(int(input()))]
for i in s:
    for j in d:
        if j.lower() not in i.lower():
            break
    else:
        print(i)

lst = [input() for _ in range(int(input()))]
searches = [input() for _ in range(int(input()))]
for text in lst:
    if all(search.lower() in text.lower() for search in searches):
        print(text)
# ----------------------------------------
numbers = [int(input()) for _ in range(int(input()))]
print(*[n for n in numbers if n < 0],
      *[n for n in numbers if n == 0],
      *[n for n in numbers if n > 0], sep='\n')
# ======================================== 11.5
B**E**E**G**E**E**K
# ----------------------------------------
s = input().split()
print(*[w for w in s], sep='\n')
# ----------------------------------------
s = input().split()
print('.'.join([w[0] for w in s]) + '.')

s = input().split()
print(*[w[0] for w in s], '', sep='.')

s = input().split()
for i in (s):
    print(i[0], end=".")
# ----------------------------------------
print(*input().split('\\'), sep='\n')
# ----------------------------------------
print(*['+' * int(i) for i in input().split()], sep='\n')
# ----------------------------------------
print('ДА' if all([0 <= int(i) <= 255 for i in input().split('.')]) else 'НЕТ')
# ----------------------------------------
s = input()
sep = input()
print(sep.join(list(s)))

print(*list(input()), sep=input())

st = input()
print (input().join(st))
# ----------------------------------------
s = input().split()
print(sum([s[c + 1:].count(el) for c, el in enumerate(s)]))
# ======================================== 11.6
numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)
# ----------------------------------------
numbers = [int(i) for i in input().split()]
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
numbers.insert(max_index, numbers.pop(numbers.index(min(numbers))))
numbers.insert(min_index, numbers.pop(numbers.index(max(numbers))))
print(*numbers)

l = [int(i) for i in input().split()]
x = l.index(min(l))
y = l.index(max(l))
l[x], l[y] = max(l), min(l)
print(*l)
# ----------------------------------------
s = input().lower().split()
print('Общее количество артиклей:', s.count('a') + s.count('an') + s.count('the'))
# ----------------------------------------
text = [input() for _ in range(int(input()[1:]))]
print(*[line.split('#')[0].rstrip() for line in text], sep='\n')
# ----------------------------------------
numbers = [int(i) for i in input().split()]
numbers.sort()
print(*numbers)
numbers.sort(reverse=True)
# numbers.reverse()
print(*numbers)

s = sorted(int(i) for i in input().split())
print(*s)
print(*s[::-1])

n = input().split()
n.sort(key=int)
print(*n)
n.sort(reverse=True, key=int)
print(*n)

lst = [int(i) for i in input().split()]
print(*sorted(lst))
print(*sorted(lst, reverse=True))
# ======================================== 11.7
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [i[1:] for i in keywords]
print(new_keywords)
# ----------------------------------------
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(i) for i in keywords]
print(lengths)
# ----------------------------------------
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(i) for i in keywords]
print(lengths)
# ----------------------------------------
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [i for i in keywords if len(i) >= 5]
print(new_keywords)
# ----------------------------------------
palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
print(palindromes)
# ----------------------------------------
print(*[i**2 for i in range(1, int(input()) + 1)], sep='\n')
# ----------------------------------------
print(*[int(i)**3 for i in input().split()])
# ----------------------------------------
print(*[i for i in input().split()], sep='\n')
# ----------------------------------------
print(*[i for i in input() if i.isdigit()], sep='')
# ----------------------------------------
print(*[i**2 for i in list(map(int, input().split())) if i % 2 == 0 and i**2 % 10 != 4])
# ======================================== 11.8
'''Сортировка пузырьком с прерыванием'''
a = [17, 24, 91, 96, 67]
for i in range(n - 1):
    f = True  # new
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            f = False  # new
    if f:  # new
        break  # new
print(a)
# ----------------------------------------
'''Сортировка выбором'''
a = [78, -32, 5, 39, 58]
for i in range(len(a), 0, -1):
    a.insert(i, max(a[:i]))
    a.remove(max(a[:i]))
print(a)
# ======================================== 12 экзамен
print([i for i in range(2, int(input()) + 1, 2)])
# ----------------------------------------
l = [int(i) for i in input().split()]
m = [int(i) for i in input().split()]
print(*[l[i] + m[i] for i in range(len(l))])

print(*[int(i) + int(j) for i, j in zip(input().split(), input().split())])
# ----------------------------------------
l = [int(i) for i in input().split()]
print(*l, sep='+', end=f'={sum(l)}')
# ----------------------------------------
# 'abc-def-hijk' or '7-abc-def-hijk'
import re
pattern = re.compile(r'^(7-)?[0-9]{3}-[0-9]{3}-[0-9]{4}$')
print('YES' if pattern.match(input()) else 'NO')
# pattern = re.compile(r'^(7-)?\d{3}-\d{3}-\d{4}$')
# pattern = re.compile(r'(7-[0-9]{3}-...)|([0-9]{3}...)')
# ----------------------------------------
print(max([len(i) for i in input().split()]))
# ----------------------------------------
print(*[i[1:] + i[0] + 'ки' for i in input().split()])
# ======================================== 13.1
def draw_box():
    print('*' * 10)
    for i in range(12):
        print('*', ' ' * 8, '*', sep='')
    print('*' * 10)

draw_box()
# ----------------------------------------
def draw_triangle():
    for i in range(1, 11):
        print('*' *i)

draw_triangle()
# ======================================== 13.2
def draw_triangle(fill, base):
    for i in range(1, base // 2 + 1):
        print(fill * i)
    for i in range(base // 2 + 1, 0, -1):
        print(fill * i)
    # for i in range(1, base + 1):
    #     print(fill * min(i, base - i + 1))

fill = input()
base = int(input())
draw_triangle(fill, base)
# ----------------------------------------
def print_fio(name, surname, patronymic):
    print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')
    # print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())

name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)
# ----------------------------------------
def print_digit_sum(num):
    print(sum([int(i) for i in str(num)]))
    # print(sum(int(i) for i in str(num)))

n = int(input())
print_digit_sum(n)
# ======================================== 13.4
def convert_to_miles(km):
    return km * 0.6214

num = int(input())
print(convert_to_miles(num))
# ----------------------------------------
def get_days(month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (2,):
        return 28
    else:
        return 30

num = int(input())
print(get_days(num))


from calendar import monthrange
def get_days(month):
    return monthrange(2021, month)[1]

num = int(input())
print(get_days(num))
# ----------------------------------------
def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

n = int(input())
print(get_factors(n))
# ----------------------------------------
def number_of_factors(num):
    return sum([1 for i in range(1, num + 1) if num % i == 0])

n = int(input())
print(number_of_factors(n))
# ----------------------------------------
def find_all(target, symbol):
    return [i for i, c in enumerate(target) if c == symbol]

s = input()
char = input()
print(find_all(s, char))
# ----------------------------------------
def merge(list1, list2):
    return sorted(list1 + list2)

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]
print(merge(numbers1, numbers2))
# ----------------------------------------
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


n = int(input())
sl  = [input().split() for _ in range(n)]
while len(sl) > 1:
    l1 = [int(c) for c in sl.pop()]
    l2 = [int(c) for c in sl.pop()]
    sl.append(quick_merge(l1, l2))
print(*sl[0])
# ======================================== 13.5
def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))
# ----------------------------------------
def is_prime(num):
    return True if sum([1 for i in range(2, num + 1) if num % i == 0]) == 1 else False

n = int(input())
print(is_prime(n))
# ----------------------------------------
def get_next_prime(num):
    num += 1
    while True:
        if sum([1 for i in range(1, num + 1) if num % i == 0]) > 2:
            num += 1
        else:
            break
    return num
# def get_next_prime(num):    
#     num += 1
#     while len([i for i in range(1, num + 1) if num % i == 0]) != 2:
#         num += 1
#     return num

n = int(input())
print(get_next_prime(n))
# ----------------------------------------
def is_password_good(password):
    d, u, l = 0, 0, 0
    for c in password:
        if c.isdigit(): d += 1
        if c.isupper(): u += 1
        if c.islower(): l += 1
    return all([d, u, l, len(password) >= 8])
# def is_password_good(password):
#     upp = [i for i in password if i.isupper()]
#     low = [i for i in password if i.islower()]
#     dig = [i for i in password if i.isdigit()]
#     return all([len(password) >= 8, upp, low, dig])

txt = input()
print(is_password_good(txt))
# ----------------------------------------
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    if sum(1 for i in range(len(word1)) if word1[i] != word2[i]) == 1:
        return True
    else:
        return False
# def is_one_away(word1, word2):
#     return len([i for i in word1 if i not in word2]) == 1 and len(word1) == len(word2)

txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))
# ----------------------------------------
def is_palindrome(text):
    l = [c for c in text.lower() if c.isalpha()]
    for i in range(len(l) // 2):
        if l[i] != l[-1 - i]:
            return False
    return True
# def is_palindrome(text):
#     l = [c for c in text.lower() if c.isalpha()]
#         return l == l[::-1]

txt = input()
print(is_palindrome(txt))
# ----------------------------------------
def is_palindrome(text):
    return text == text[::-1]


def is_prime(num):
    return True if sum([1 for i in range(2, num + 1) if num % i == 0]) == 1 else False


def is_even(num):
    return num % 2 == 0


def is_valid_password(password):
    import re
    l = password.split(':')
    pattern = re.compile(r'^[0-9]*:[0-9]*:[0-9]*$')
    return all([pattern.match(password), is_palindrome(l[0]), is_prime(int(l[1])), is_even(int(l[2]))])


psw = input()
print(is_valid_password(psw))
# ----------------------------------------
def is_correct_bracket(text):
    sum_ = 0
    for i in [1 if c == '(' else -1 for c in text]:
        sum_ += i
        if sum_ < 0:
            return False
    if sum_ != 0:
        return False
    return True
# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#     return not text
#     return text == ''

txt = input()
print(is_correct_bracket(txt))
# ----------------------------------------
def convert_to_python_case(text):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in text])[1:]

txt = input()
print(convert_to_python_case(txt))
# ======================================== 13.6
def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)
# ----------------------------------------
def get_circle(radius):
    import math
    return 2 * math.pi * radius, math.pi * radius**2

r = float(input())
length, square = get_circle(r)
print(length, square)
# ----------------------------------------
def solve(a, b, c):
    import math
    d = b**2 - 4 * a * c
    if d < 0:
        print('Нет корней')
    else:
        roots = (-1 * b - math.sqrt(d)) / (2 * a), (-1 * b + math.sqrt(d)) / (2 * a)
        return min(roots), max(roots)

a, b, c = int(input()), int(input()), int(input())
x1, x2 = solve(a, b, c)
print(x1, x2)
# ======================================== 14 экзамен
def draw_triangle():
    print(*[' ' * int((15 - i) / 2) + '*' * i for i in range(1, 16, 2)], sep='\n')

draw_triangle()
# ----------------------------------------
def get_shipping_cost(quantity):
    return 1000 + 120 * (quantity - 1)

n = int(input())
print(get_shipping_cost(n))
# ----------------------------------------
def compute_binom(n, k):
    import math
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))

n = int(input())
k = int(input())
print(compute_binom(n, k))
# ----------------------------------------
def number_to_words(num):
    if num == 0: return ''
    if num == 1: return 'один'
    if num == 2: return 'два'
    if num == 3: return 'три'
    if num == 4: return 'четыре'
    if num == 5: return 'пять'
    if num == 6: return 'шесть'
    if num == 7: return 'семь'
    if num == 8: return 'восемь'
    if num == 9: return 'девять'
    if num == 10: return 'десять'
    if num == 11: return 'одиннадцать'
    if num == 12: return 'двенадцать'
    if num == 13: return 'тринадцать'
    if num == 14: return 'четырнадцать'
    if num == 15: return 'пятнадцать'
    if num == 16: return 'шестнадцать'
    if num == 17: return 'семнадцать'
    if num == 18: return 'восемнадцать'
    if num == 19: return 'девятнадцать'
    if num // 10 == 2: return ' '.join(['двадцать', number_to_words(num % 10)])
    if num // 10 == 3: return ' '.join(['тридцать', number_to_words(num % 10)])
    if num // 10 == 4: return ' '.join(['сорок', number_to_words(num % 10)])
    if num // 10 == 5: return ' '.join(['пятьдесят', number_to_words(num % 10)])
    if num // 10 == 6: return ' '.join(['шестьдесят', number_to_words(num % 10)])
    if num // 10 == 7: return ' '.join(['семьдесят', number_to_words(num % 10)])
    if num // 10 == 8: return ' '.join(['восемьдесят', number_to_words(num % 10)])
    if num // 10 == 9: return ' '.join(['девяносто', number_to_words(num % 10)])

n = int(input())
print(number_to_words(n))
# ----------------------------------------
def get_month(language, number):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return lng_ru[number - 1]
    if language == 'en':
        return lng_en[number - 1]

lan = input()
num = int(input())
print(get_month(lan, num))
# ----------------------------------------
def is_magic(date):
    l = [int(i) for i in date.split('.')]
    return True if l[0] * l[1] == l[2] % 100 else False

date = input()
print(is_magic(date))
# ----------------------------------------
def is_pangram(text):
    return set(__import__('string').ascii_lowercase) == set(c for c in text.lower() if c.isalpha())

text = input()
print(is_pangram(text))
# ======================================== 15.2
import math
print(math.ceil(math.log2(int(input()))))
# ======================================== 15.5
import string

def caesar(text, shift, lang='en'):
    alphabet = string.ascii_lowercase if lang == 'en' else 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    result = []
    for c in text:
        if not c.isalpha():
            result.append(c)
        else:
            c_shift = alphabet[(alphabet.find(c.lower()) + shift) % len(alphabet)]
            result.append(c_shift.upper() if c.isupper() else c_shift)
    return ''.join(result)

print(caesar('Блажен, кто верует, тепло ему на свете!', 10, 'ru'))
# Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп!
# ----------------------------------------
print(caesar('To be, or not to be, that is the question!', 17, 'en'))
# Kf sv, fi efk kf sv, kyrk zj kyv hlvjkzfe!
# ----------------------------------------
print(caesar('Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.', -7, 'ru'))
# Скупой теряет все, желая все достать.
# ----------------------------------------
print(caesar('Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.', -25, 'en'))
# The grass is always greener on the other side of the fence.
# ----------------------------------------
# Hawnj pk swhg xabkna ukq nqj.
# Learn to walk before you run.
# ----------------------------------------
import string

def caesar(text):
    alphabet = string.ascii_lowercase
    result = []
    for word in text.split():
        shift = sum(1 for i in word if i.isalpha())
        for char in word:
            if not char.isalpha():
                result.append(char)
            else:
                c_shift = alphabet[(alphabet.find(char.lower()) + shift) % len(alphabet)]
                result.append(c_shift.upper() if char.isupper() else c_shift)
        result.append(' ')
    return ''.join(result)

txt = input()
print(caesar(txt))
# Day, mice. "Year" is a mistake!
# Gdb, qmgi. "Ciev" ku b tpzahrl! 
# ======================================== 15.6
txt = int(input())
print(bin(txt)[2:], oct(txt)[2:], hex(txt)[2:].upper(), sep='\n')
# ========================================
